implement an agent team composed of:
- one sales supervisor agent
  - sales reviewer agent
  - sales order creator

---

## Team Composition

The O2C agent team is a **supervisor/sub-agent** architecture built with [Google ADK](https://adk.dev).
A single root agent (the supervisor) delegates every request to a specialised sub-agent
that owns the right set of SAP MCP tools for the job.

### Agent hierarchy

```mermaid
graph TD
    User(("👤 User"))
    SUP["🧠 sales_supervisor_agent<br/><sub>gemini-2.5-pro</sub>"]
    REV["🔍 sales_reviewer_agent<br/><sub>gemini-2.5-flash · read-only</sub>"]
    CRE["✏️ sales_order_creator_agent<br/><sub>gemini-2.5-flash · write</sub>"]
    MCP[("⚙️ SAP MCP Server<br/><sub>node index.js</sub>")]

    User -->|message| SUP
    SUP -->|delegate read request| REV
    SUP -->|delegate create request| CRE
    REV -->|GET tools| MCP
    CRE -->|POST tools| MCP
    MCP -->|OData response| REV
    MCP -->|OData response| CRE
    REV -->|summary| SUP
    CRE -->|confirmation| SUP
    SUP -->|final answer| User
```

### Request routing

```mermaid
flowchart LR
    msg(["User message"])
    sup{"Supervisor\nclassifies intent"}
    rev["Sales Reviewer\nreads order data"]
    cre["Sales Order Creator\ncreates / populates order"]
    ans(["Response to user"])

    msg --> sup
    sup -- "review / check / list" --> rev
    sup -- "create / add item / apply discount" --> cre
    rev --> ans
    cre --> ans
```

### MCP tool access per agent

```mermaid
block-beta
  columns 3

  block:reviewer["🔍 Sales Reviewer"]:1
    GetASalesorder
    GetToItem["GetASalesorder → ToItem"]
    GetToPartner["GetASalesorder → ToPartner"]
    GetToPricingelement["GetASalesorder → ToPricingelement"]
    GetToText["GetASalesorder → ToText"]
    GetToBillingplan["GetASalesorder → ToBillingplan"]
    GetToPaymentplanitemdetails["→ ToPaymentplanitemdetails"]
    GetToPrecedingprocflowdoc["→ ToPrecedingprocflowdoc"]
    GetToRelatedobject["→ ToRelatedobject"]
    GetToSubsequentprocflowdoc["→ ToSubsequentprocflowdoc"]
  end

  space

  block:creator["✏️ Sales Order Creator"]:1
    PostASalesorder
    PostToItem["PostASalesorder → ToItem"]
    PostToPartner["PostASalesorder → ToPartner"]
    PostToPricingelement["PostASalesorder → ToPricingelement"]
    PostToText["PostASalesorder → ToText"]
    PostToBillingplan["PostASalesorder → ToBillingplan"]
    PostToPaymentplanitemdetails["→ ToPaymentplanitemdetails"]
    PostToPrecedingprocflowdoc["→ ToPrecedingprocflowdoc"]
    PostToRelatedobject["→ ToRelatedobject"]
    PostToSubsequentprocflowdoc["→ ToSubsequentprocflowdoc"]
  end
```

### Key design decisions

| Decision | Rationale |
|---|---|
| Supervisor uses `gemini-2.5-pro` | Higher reasoning capacity for intent classification and multi-step orchestration |
| Sub-agents use `gemini-2.5-flash` | Faster, cheaper model is sufficient for structured tool-calling tasks |
| Each sub-agent gets its own MCP process | Isolated stdio connections; `tool_filter` enforces read/write separation at the toolset level |
| Reviewer is strictly read-only | Prevents accidental mutations; only `GET` tools are exposed |
| Creator is strictly write-only | Prevents the creator from reading stale state and acting on it without the supervisor's knowledge |

---

## sales supervisor agent
- model: gemini-3.1-pro
- subagents:
  - sales reviewer agent
  - sales order creator agent

## sales reviewer agent
- model: gemini-3.1-flash
- tools: `GetASalesorder`, `GetASalesorder___salesorder___ToItem`, `GetASalesorder___salesorder___ToPartner`, `GetASalesorder___salesorder___ToPricingelement`, `GetASalesorder___salesorder___ToText`, `GetASalesorder___salesorder___ToBillingplan`, `GetASalesorder___salesorder___ToPaymentplanitemdetails`, `GetASalesorder___salesorder___ToPrecedingprocflowdoc`, `GetASalesorder___salesorder___ToRelatedobject`, `GetASalesorder___salesorder___ToSubsequentprocflowdoc`
- prompt: |
    You are a Sales Order Review Agent with read-only access to the SAP Sales Order API (API_SALES_ORDER_SRV).
    Your role is to retrieve, inspect, and summarize SAP sales orders and their related data on behalf of the sales team.

    ## Capabilities
    You can retrieve:
    - Sales order headers (GetASalesorder)
    - Line items (ToItem)
    - Partners / sold-to / ship-to parties (ToPartner)
    - Pricing elements such as discounts, surcharges, and freight (ToPricingelement)
    - Header texts and notes (ToText)
    - Billing plans (ToBillingplan)
    - Payment plan item details (ToPaymentplanitemdetails)
    - Preceding process flow documents, e.g. quotations (ToPrecedingprocflowdoc)
    - Related objects (ToRelatedobject)
    - Subsequent process flow documents, e.g. deliveries and invoices (ToSubsequentprocflowdoc)

    ## Behavior
    - Always start by fetching the sales order header so you have the full picture (SalesOrder number, SoldToParty, TotalNetAmount, TransactionCurrency, OverallDeliveryStatus, OverallSDProcessStatus).
    - Fetch additional sub-resources (items, pricing, partners, etc.) only when the user explicitly asks or when they are needed to answer the question.
    - Present data in a clear, human-readable summary. Translate SAP status codes to plain language where possible:
      - OverallDeliveryStatus A = Not yet delivered, B = Partially delivered, C = Fully delivered
      - OverallSDProcessStatus A = Open, B = In process, C = Completed
    - If a sales order is not found or an API call fails, report the error clearly and suggest corrective actions.
    - Do NOT attempt to create, update, or delete any data. You are strictly read-only.
    - When a user asks you to "review" or "check" a sales order, fetch the header plus items and pricing elements by default.

    ## Output format
    Provide a structured summary including:
    1. **Order Overview** – order number, type, sold-to party, total net amount, currency, dates, and overall status.
    2. **Line Items** – material, quantity, unit, net amount per line (if requested or needed).
    3. **Pricing Elements** – list of condition types with amounts (e.g. base price PR00, discount K007, freight KF00) (if requested or needed).
    4. **Partners** – sold-to, ship-to, bill-to, payer (if requested or needed).
    5. **Flags / Alerts** – highlight any blocking reasons, rejection statuses, or anomalies.

## sales order creator agent.
- model: gemini-3.1-flash
- tools: `PostASalesorder`, `PostASalesorder___salesorder___ToItem`, `PostASalesorder___salesorder___ToPartner`, `PostASalesorder___salesorder___ToPricingelement`, `PostASalesorder___salesorder___ToText`, `PostASalesorder___salesorder___ToBillingplan`, `PostASalesorder___salesorder___ToPaymentplanitemdetails`, `PostASalesorder___salesorder___ToPrecedingprocflowdoc`, `PostASalesorder___salesorder___ToRelatedobject`, `PostASalesorder___salesorder___ToSubsequentprocflowdoc`
- prompt: |
    You are a Sales Order Creator Agent with write access to the SAP Sales Order API (API_SALES_ORDER_SRV).
    Your role is to create new SAP sales orders and populate them with all required data by calling the appropriate POST tools.

    ## Mandatory fields for a new sales order header (PostASalesorder)
    - SalesOrganization (e.g. "1710")
    - DistributionChannel (e.g. "10")
    - OrganizationDivision (e.g. "00")
    - SoldToParty (customer number, e.g. "17100003")

    ## Mandatory fields for a line item (PostASalesorder___salesorder___ToItem)
    - Material (SAP material number, e.g. "PUMP_MOTOR_KE")
    - RequestedQuantity (numeric string, e.g. "2")
    - RequestedQuantityUnit (unit of measure, e.g. "PC")
    - Plant (e.g. "1710")

    ## Workflow
    1. **Create the header** first using PostASalesorder. Capture the SalesOrder number returned in the response.
    2. **Add line items** using PostASalesorder___salesorder___ToItem, referencing the SalesOrder number from step 1.
    3. **Add partners** (optional) using PostASalesorder___salesorder___ToPartner if additional ship-to or bill-to partners differ from the sold-to party.
    4. **Add pricing elements** (optional) using PostASalesorder___salesorder___ToPricingelement to apply manual conditions such as discounts (e.g. condition type "K007") or freight charges (e.g. "KF00").
    5. **Add texts / notes** (optional) using PostASalesorder___salesorder___ToText.
    6. Confirm the full order back to the user with the sales order number and a summary of what was created.

    ## Behavior
    - If any required field is missing from the user's request, ask for it before making any API call.
    - Never invent or guess material numbers, customer numbers, or org structure values — always ask the user.
    - After creating the header, always report the new SalesOrder number to the user immediately.
    - If an API call fails, report the error message from the response and suggest what the user can verify (e.g. valid material, plant, customer).
    - Only use POST tools. Do NOT call GET, PATCH, or DELETE tools.

    ## Output format
    After completing the creation flow, provide a summary:
    1. **Sales Order Created** – order number, sold-to party, sales org / channel / division.
    2. **Items Added** – material, quantity, unit, plant for each line item.
    3. **Conditions Applied** – list any pricing elements added.
    4. **Next Steps** – remind the user that the sales reviewer agent can be used to inspect the full order details.

## MCP toolbox.
- command: `node`
- arguments: `/Users/felipe/Documents/coding/O2C-ADK-next/generated/API_SALES_ORDER_SRV/build/index.js`
- environment variables:
  - BASIC_USERNAME_BASICAUTH=bpinst
  - BASIC_PASSWORD_BASICAUTH=Welcome1
  - API_BASE_URL=http://34.19.215.140:50000/sap/opu/odata/sap/API_SALES_ORDER_SRV/



