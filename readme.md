# SAP Order-to-Cash (O2C) Agent

> **Automate SAP sales order workflows** with a multi-agent system built on [Google ADK](https://google.github.io/adk-docs/) and the [Model Context Protocol (MCP)](https://modelcontextprotocol.io/).

---

## Overview

This project implements an **Order-to-Cash automation agent team** that interacts with the SAP `API_SALES_ORDER_SRV` OData API.
A supervisor agent classifies incoming requests and delegates to specialised sub-agents — one for reading data, one for creating orders.
The SAP API is exposed to the agents through a generated TypeScript **MCP server**.

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="docs/diagrams/architecture-dark.png">
  <img src="docs/diagrams/architecture-light.png" alt="System architecture diagram" width="700">
</picture>

---

## Repository Structure

| Path | Description |
|------|-------------|
| `adk/O2C/` | Python ADK agent package (`pyproject.toml` + source) |
| `adk/O2C/o2c_agent/agent.py` | Agent definitions (supervisor + sub-agents) |
| `adk/O2C/o2c_agent/prompts.py` | System prompts for each agent |
| `generated/API_SALES_ORDER_SRV/` | Auto-generated TypeScript MCP server |
| `sap_api/` | OpenAPI / JSON specs for SAP OData services |

---

## Tech Stack

| Layer | Technology |
|-------|-----------|
| Agent framework | [Google ADK](https://google.github.io/adk-docs/) (`google-adk`) |
| Agent models | `gemini-2.5-pro` (supervisor), `gemini-flash-latest` (sub-agents) |
| Tool protocol | [Model Context Protocol](https://modelcontextprotocol.io/) (`mcp[cli]`) |
| MCP server runtime | Node.js / TypeScript |
| MCP server generator | [`openapi-mcp-generator`](https://www.npmjs.com/package/openapi-mcp-generator) |
| SAP backend | SAP S/4HANA – `API_SALES_ORDER_SRV` (OData v2) |
| Python env | `python-dotenv`, `hatchling` |

---

## Agent Team

| Agent | Model | Access | Responsibility |
|-------|-------|--------|----------------|
| `sales_supervisor_agent` | `gemini-2.5-pro` | — | Classifies intent and routes to the right sub-agent |
| `sales_reviewer_agent` | `gemini-flash-latest` | GET only | Retrieves and summarises sales orders and related data |
| `sales_order_creator_agent` | `gemini-flash-latest` | POST only | Creates sales order headers, line items, and pricing conditions |

### Request routing

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="docs/diagrams/routing-dark.png">
  <img src="docs/diagrams/routing-light.png" alt="Request routing diagram" width="700">
</picture>

---

## Quick Start

### Prerequisites

- Python ≥ 3.9 and Node.js ≥ 18
- A Google AI API key (set `GOOGLE_API_KEY`)
- Access to a SAP S/4HANA system with `API_SALES_ORDER_SRV` enabled

### 1 — Install Python dependencies

```bash
cd adk/O2C
python -m venv .venv && source .venv/bin/activate
pip install -e .
```

### 2 — Configure environment

```bash
cp .env.example .env   # then fill in your values
```

| Variable | Description |
|----------|-------------|
| `GOOGLE_API_KEY` | Google AI (Gemini) API key |
| `BASIC_USERNAME_BASICAUTH` | SAP basic-auth username |
| `BASIC_PASSWORD_BASICAUTH` | SAP basic-auth password |
| `API_BASE_URL` | Full URL of the SAP OData service root |
| `MCP_SERVER_JS` | Absolute path to `generated/API_SALES_ORDER_SRV/build/index.js` |

### 3 — Build the MCP server

```bash
cd generated/API_SALES_ORDER_SRV
npm install && npm run build
```

### 4 — Run the agent

```bash
cd adk/O2C
adk run o2c_agent
```

---

## MCP Server

The TypeScript MCP server is generated from the SAP OpenAPI spec using [`openapi-mcp-generator`](https://www.npmjs.com/package/openapi-mcp-generator).

### Regenerating from spec

```bash
openapi-mcp-generator \
  --input  ./sap_api/API_SALES_ORDER_SRV.json \
  --output ./generated/API_SALES_ORDER_SRV \
  --server-name API_SALES_ORDER_SRV \
  --base-url http://<host>:50000/sap/opu/odata/sap/API_SALES_ORDER_SRV/
```

### Tools exposed per agent

Each sub-agent receives an isolated MCP stdio process with a `tool_filter` applied:

| Entity | Reviewer (GET) | Creator (POST) |
|--------|:--------------:|:--------------:|
| Sales Order header | `GetASalesorder` | `PostASalesorder` |
| Line items (`ToItem`) | ✅ | ✅ |
| Partners (`ToPartner`) | ✅ | ✅ |
| Pricing elements (`ToPricingelement`) | ✅ | ✅ |
| Header texts (`ToText`) | ✅ | ✅ |
| Billing plan (`ToBillingplan`) | ✅ | ✅ |
| Payment plan details (`ToPaymentplanitemdetails`) | ✅ | ✅ |
| Preceding proc. flow doc | ✅ | ✅ |
| Related objects | ✅ | ✅ |
| Subsequent proc. flow doc | ✅ | ✅ |

### Full tool list

<details>
<summary>Click to expand all <code>API_SALES_ORDER_SRV</code> tools</summary>

```
GetASalesorder
PostASalesorder
GetASalesorder___salesorder___
DeleteASalesorder___salesorder___
PatchASalesorder___salesorder___
GetASalesorder___salesorder___ToBillingplan
GetASalesorder___salesorder___ToItem
PostASalesorder___salesorder___ToItem
GetASalesorder___salesorder___ToPartner
PostASalesorder___salesorder___ToPartner
GetASalesorder___salesorder___ToPaymentplanitemdetails
PostASalesorder___salesorder___ToPaymentplanitemdetails
GetASalesorder___salesorder___ToPrecedingprocflowdoc
GetASalesorder___salesorder___ToPricingelement
PostASalesorder___salesorder___ToPricingelement
GetASalesorder___salesorder___ToRelatedobject
PostASalesorder___salesorder___ToRelatedobject
GetASalesorder___salesorder___ToSubsequentprocflowdoc
GetASalesorder___salesorder___ToText
PostASalesorder___salesorder___ToText
GetASalesorderbillingplan
GetASalesorderbillingplan_salesorder___salesorder___billingplan___billingplan___
PatchASalesorderbillingplan_salesorder___salesorder___billingplan___billingplan___
GetASalesorderbillingplan_salesorder___salesorder___billingplan___billingplan___ToBillingplanitem
PostASalesorderbillingplan_salesorder___salesorder___billingplan___billingplan___ToBillingplanitem
GetASalesorderbillingplan_salesorder___salesorder___billingplan___billingplan___ToSalesorder
GetASalesorderbillingplanitem
PostASalesorderbillingplanitem
GetASalesorderbillingplanitem_salesorder___salesorder___billingplan___billingplan___billingplanitem___billingplanitem___
DeleteASalesorderbillingplanitem_salesorder___salesorder___billingplan___billingplan___billingplanitem___billingplanitem___
PatchASalesorderbillingplanitem_salesorder___salesorder___billingplan___billingplan___billingplanitem___billingplanitem___
GetASalesorderbillingplanitem_salesorder___salesorder___billingplan___billingplan___billingplanitem___billingplanitem___ToBillingplan
GetASalesorderbillingplanitem_salesorder___salesorder___billingplan___billingplan___billingplanitem___billingplanitem___ToSalesorder
GetASalesorderheaderpartner
PostASalesorderheaderpartner
GetASalesorderheaderpartner_salesorder___salesorder___partnerfunction___partnerfunction___
DeleteASalesorderheaderpartner_salesorder___salesorder___partnerfunction___partnerfunction___
PatchASalesorderheaderpartner_salesorder___salesorder___partnerfunction___partnerfunction___
GetASalesorderheaderpartner_salesorder___salesorder___partnerfunction___partnerfunction___ToAddress
GetASalesorderheaderpartner_salesorder___salesorder___partnerfunction___partnerfunction___ToSalesorder
GetASalesorderheaderprelement
PostASalesorderheaderprelement
GetASalesorderheaderprelement_salesorder___salesorder___pricingprocedurestep___pricingprocedurestep___pricingprocedurecounter___pricingprocedurecounter___
DeleteASalesorderheaderprelement_salesorder___salesorder___pricingprocedurestep___pricingprocedurestep___pricingprocedurecounter___pricingprocedurecounter___
PatchASalesorderheaderprelement_salesorder___salesorder___pricingprocedurestep___pricingprocedurestep___pricingprocedurecounter___pricingprocedurecounter___
GetASalesorderheaderprelement_salesorder___salesorder___pricingprocedurestep___pricingprocedurestep___pricingprocedurecounter___pricingprocedurecounter___ToSalesorder
GetASalesorderitem
PostASalesorderitem
GetASalesorderitem_salesorder___salesorder___salesorderitem___salesorderitem___
DeleteASalesorderitem_salesorder___salesorder___salesorderitem___salesorderitem___
PatchASalesorderitem_salesorder___salesorder___salesorderitem___salesorderitem___
GetASalesorderitem_salesorder___salesorder___salesorderitem___salesorderitem___ToBillingplan
GetASalesorderitem_salesorder___salesorder___salesorderitem___salesorderitem___ToPartner
PostASalesorderitem_salesorder___salesorder___salesorderitem___salesorderitem___ToPartner
GetASalesorderitem_salesorder___salesorder___salesorderitem___salesorderitem___ToPrecedingprocflowdocitem
GetASalesorderitem_salesorder___salesorder___salesorderitem___salesorderitem___ToPricingelement
PostASalesorderitem_salesorder___salesorder___salesorderitem___salesorderitem___ToPricingelement
GetASalesorderitem_salesorder___salesorder___salesorderitem___salesorderitem___ToRelatedobject
PostASalesorderitem_salesorder___salesorder___salesorderitem___salesorderitem___ToRelatedobject
GetASalesorderitem_salesorder___salesorder___salesorderitem___salesorderitem___ToSalesorder
GetASalesorderitem_salesorder___salesorder___salesorderitem___salesorderitem___ToScheduleline
PostASalesorderitem_salesorder___salesorder___salesorderitem___salesorderitem___ToScheduleline
GetASalesorderitem_salesorder___salesorder___salesorderitem___salesorderitem___ToSubsequentprocflowdocitem
GetASalesorderitem_salesorder___salesorder___salesorderitem___salesorderitem___ToText
PostASalesorderitem_salesorder___salesorder___salesorderitem___salesorderitem___ToText
GetASalesorderitembillingplan
GetASalesorderitembillingplan_salesorder___salesorder___salesorderitem___salesorderitem___billingplan___billingplan___
PatchASalesorderitembillingplan_salesorder___salesorder___salesorderitem___salesorderitem___billingplan___billingplan___
GetASalesorderitembillingplan_salesorder___salesorder___salesorderitem___salesorderitem___billingplan___billingplan___ToBillingplanitem
PostASalesorderitembillingplan_salesorder___salesorder___salesorderitem___salesorderitem___billingplan___billingplan___ToBillingplanitem
GetASalesorderitembillingplan_salesorder___salesorder___salesorderitem___salesorderitem___billingplan___billingplan___ToSalesorder
GetASalesorderitembillingplan_salesorder___salesorder___salesorderitem___salesorderitem___billingplan___billingplan___ToSalesorderitem
GetASalesorderitempartner
PostASalesorderitempartner
GetASalesorderitempartner_salesorder___salesorder___salesorderitem___salesorderitem___partnerfunction___partnerfunction___
DeleteASalesorderitempartner_salesorder___salesorder___salesorderitem___salesorderitem___partnerfunction___partnerfunction___
PatchASalesorderitempartner_salesorder___salesorder___salesorderitem___salesorderitem___partnerfunction___partnerfunction___
GetASalesorderitempartner_salesorder___salesorder___salesorderitem___salesorderitem___partnerfunction___partnerfunction___ToAddress
GetASalesorderitempartner_salesorder___salesorder___salesorderitem___salesorderitem___partnerfunction___partnerfunction___ToSalesorder
GetASalesorderitempartner_salesorder___salesorder___salesorderitem___salesorderitem___partnerfunction___partnerfunction___ToSalesorderitem
GetASalesorderitempartneraddress
GetASalesorderitempartneraddress_salesorder___salesorder___salesorderitem___salesorderitem___partnerfunction___partnerfunction___addressrepresentationcode___addressrepresentationcode___
PatchASalesorderitempartneraddress_salesorder___salesorder___salesorderitem___salesorderitem___partnerfunction___partnerfunction___addressrepresentationcode___addressrepresentationcode___
GetASalesorderitempartneraddress_salesorder___salesorder___salesorderitem___salesorderitem___partnerfunction___partnerfunction___addressrepresentationcode___addressrepresentationcode___ToPartner
GetASalesorderitempartneraddress_salesorder___salesorder___salesorderitem___salesorderitem___partnerfunction___partnerfunction___addressrepresentationcode___addressrepresentationcode___ToSalesorder
GetASalesorderitempartneraddress_salesorder___salesorder___salesorderitem___salesorderitem___partnerfunction___partnerfunction___addressrepresentationcode___addressrepresentationcode___ToSalesorderitem
GetASalesorderitemprelement
PostASalesorderitemprelement
GetASalesorderitemprelement_salesorder___salesorder___salesorderitem___salesorderitem___pricingprocedurestep___pricingprocedurestep___pricingprocedurecounter___pricingprocedurecounter___
DeleteASalesorderitemprelement_salesorder___salesorder___salesorderitem___salesorderitem___pricingprocedurestep___pricingprocedurestep___pricingprocedurecounter___pricingprocedurecounter___
PatchASalesorderitemprelement_salesorder___salesorder___salesorderitem___salesorderitem___pricingprocedurestep___pricingprocedurestep___pricingprocedurecounter___pricingprocedurecounter___
GetASalesorderitemprelement_salesorder___salesorder___salesorderitem___salesorderitem___pricingprocedurestep___pricingprocedurestep___pricingprocedurecounter___pricingprocedurecounter___ToSalesorder
GetASalesorderitemprelement_salesorder___salesorder___salesorderitem___salesorderitem___pricingprocedurestep___pricingprocedurestep___pricingprocedurecounter___pricingprocedurecounter___ToSalesorderitem
GetASalesorderitemrelatedobject
PostASalesorderitemrelatedobject
GetASalesorderitemrelatedobject_salesorder___salesorder___salesorderitem___salesorderitem___sddocrelatedobjectsequencenmbr___sddocrelatedobjectsequencenmbr___
DeleteASalesorderitemrelatedobject_salesorder___salesorder___salesorderitem___salesorderitem___sddocrelatedobjectsequencenmbr___sddocrelatedobjectsequencenmbr___
GetASalesorderitemrelatedobject_salesorder___salesorder___salesorderitem___salesorderitem___sddocrelatedobjectsequencenmbr___sddocrelatedobjectsequencenmbr___ToSalesorder
GetASalesorderitemrelatedobject_salesorder___salesorder___salesorderitem___salesorderitem___sddocrelatedobjectsequencenmbr___sddocrelatedobjectsequencenmbr___ToSalesorderitem
GetASalesorderitemtext
PostASalesorderitemtext
GetASalesorderitemtext_salesorder___salesorder___salesorderitem___salesorderitem___language___language___longtextid___longtextid___
DeleteASalesorderitemtext_salesorder___salesorder___salesorderitem___salesorderitem___language___language___longtextid___longtextid___
PatchASalesorderitemtext_salesorder___salesorder___salesorderitem___salesorderitem___language___language___longtextid___longtextid___
GetASalesorderitemtext_salesorder___salesorder___salesorderitem___salesorderitem___language___language___longtextid___longtextid___ToSalesorder
GetASalesorderitemtext_salesorder___salesorder___salesorderitem___salesorderitem___language___language___longtextid___longtextid___ToSalesorderitem
GetASalesorderitmprecdgprocflow
GetASalesorderitmprecdgprocflow_salesorder___salesorder___salesorderitem___salesorderitem___docrelationshipuuid_guid__docrelationshipuuid___
GetASalesorderitmprecdgprocflow_salesorder___salesorder___salesorderitem___salesorderitem___docrelationshipuuid_guid__docrelationshipuuid___ToSalesorder
GetASalesorderitmprecdgprocflow_salesorder___salesorder___salesorderitem___salesorderitem___docrelationshipuuid_guid__docrelationshipuuid___ToSalesorderitem
GetASalesorderitmsubsqntprocflow
GetASalesorderitmsubsqntprocflow_salesorder___salesorder___salesorderitem___salesorderitem___docrelationshipuuid_guid__docrelationshipuuid___
GetASalesorderitmsubsqntprocflow_salesorder___salesorder___salesorderitem___salesorderitem___docrelationshipuuid_guid__docrelationshipuuid___ToSalesorder
GetASalesorderitmsubsqntprocflow_salesorder___salesorder___salesorderitem___salesorderitem___docrelationshipuuid_guid__docrelationshipuuid___ToSalesorderitem
GetASalesorderpartneraddress
GetASalesorderpartneraddress_salesorder___salesorder___partnerfunction___partnerfunction___addressrepresentationcode___addressrepresentationcode___
PatchASalesorderpartneraddress_salesorder___salesorder___partnerfunction___partnerfunction___addressrepresentationcode___addressrepresentationcode___
GetASalesorderpartneraddress_salesorder___salesorder___partnerfunction___partnerfunction___addressrepresentationcode___addressrepresentationcode___ToPartner
GetASalesorderpartneraddress_salesorder___salesorder___partnerfunction___partnerfunction___addressrepresentationcode___addressrepresentationcode___ToSalesorder
GetASalesorderprecdgprocflow
GetASalesorderprecdgprocflow_salesorder___salesorder___docrelationshipuuid_guid__docrelationshipuuid___
GetASalesorderprecdgprocflow_salesorder___salesorder___docrelationshipuuid_guid__docrelationshipuuid___ToSalesorder
GetASalesorderrelatedobject
PostASalesorderrelatedobject
GetASalesorderrelatedobject_salesorder___salesorder___sddocrelatedobjectsequencenmbr___sddocrelatedobjectsequencenmbr___
DeleteASalesorderrelatedobject_salesorder___salesorder___sddocrelatedobjectsequencenmbr___sddocrelatedobjectsequencenmbr___
GetASalesorderrelatedobject_salesorder___salesorder___sddocrelatedobjectsequencenmbr___sddocrelatedobjectsequencenmbr___ToSalesorder
GetASalesorderscheduleline
PostASalesorderscheduleline
GetASalesorderscheduleline_salesorder___salesorder___salesorderitem___salesorderitem___scheduleline___scheduleline___
DeleteASalesorderscheduleline_salesorder___salesorder___salesorderitem___salesorderitem___scheduleline___scheduleline___
PatchASalesorderscheduleline_salesorder___salesorder___salesorderitem___salesorderitem___scheduleline___scheduleline___
GetASalesordersubsqntprocflow
GetASalesordersubsqntprocflow_salesorder___salesorder___docrelationshipuuid_guid__docrelationshipuuid___
GetASalesordersubsqntprocflow_salesorder___salesorder___docrelationshipuuid_guid__docrelationshipuuid___ToSalesorder
GetASalesordertext
PostASalesordertext
GetASalesordertext_salesorder___salesorder___language___language___longtextid___longtextid___
DeleteASalesordertext_salesorder___salesorder___language___language___longtextid___longtextid___
PatchASalesordertext_salesorder___salesorder___language___language___longtextid___longtextid___
GetASalesordertext_salesorder___salesorder___language___language___longtextid___longtextid___ToSalesorder
GetASlsorderitembillingplanitem
PostASlsorderitembillingplanitem
GetASlsorderitembillingplanitem_salesorder___salesorder___salesorderitem___salesorderitem___billingplan___billingplan___billingplanitem___billingplanitem___
DeleteASlsorderitembillingplanitem_salesorder___salesorder___salesorderitem___salesorderitem___billingplan___billingplan___billingplanitem___billingplanitem___
PatchASlsorderitembillingplanitem_salesorder___salesorder___salesorderitem___salesorderitem___billingplan___billingplan___billingplanitem___billingplanitem___
GetASlsorderitembillingplanitem_salesorder___salesorder___salesorderitem___salesorderitem___billingplan___billingplan___billingplanitem___billingplanitem___ToBillingplan
GetASlsorderitembillingplanitem_salesorder___salesorder___salesorderitem___salesorderitem___billingplan___billingplan___billingplanitem___billingplanitem___ToSalesorder
GetASlsorderitembillingplanitem_salesorder___salesorder___salesorderitem___salesorderitem___billingplan___billingplan___billingplanitem___billingplanitem___ToSalesorderitem
GetASlsordpaymentplanitemdetails
PostASlsordpaymentplanitemdetails
GetASlsordpaymentplanitemdetails_salesorder___salesorder___paymentplanitem___paymentplanitem___
DeleteASlsordpaymentplanitemdetails_salesorder___salesorder___paymentplanitem___paymentplanitem___
PatchASlsordpaymentplanitemdetails_salesorder___salesorder___paymentplanitem___paymentplanitem___
GetASlsordpaymentplanitemdetails_salesorder___salesorder___paymentplanitem___paymentplanitem___ToSalesorder
PostRejectapprovalrequest
PostReleaseapprovalrequest
```

</details>

---

## Example Walkthrough

The steps below demonstrate creating and enriching a sales order through the agent.

### Step 1 — Create the order header

The creator agent calls `PostASalesorder` with the minimum required fields:

```json
{
  "SalesOrganization": "1710",
  "DistributionChannel": "10",
  "OrganizationDivision": "00",
  "SoldToParty": "17100003"
}
```

SAP returns a new sales order number (e.g. **6319**).

### Step 2 — Add a line item

```json
{
  "Material": "PUMP_MOTOR_KE",
  "RequestedQuantity": "2",
  "RequestedQuantityUnit": "PC",
  "Plant": "1710"
}
```

`PUMP_MOTOR_KE` has a unit price of **835 USD** → total net amount **1,670 USD**.

### Step 3 — Apply pricing conditions

| Condition | Type | Value |
|-----------|------|-------|
| Customer discount | `K007` | −5 % |
| Freight surcharge | `KF00` | +25 USD |

Call `PostASalesorder___salesorder___ToPricingelement` once per condition row.

### Step 4 — Review the order

Ask the supervisor: *"Review sales order 6319"*  
The reviewer agent fetches the header, items, and pricing elements and returns a structured summary.

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="docs/diagrams/sequence-dark.png">
  <img src="docs/diagrams/sequence-light.png" alt="Example walkthrough sequence diagram" width="700">
</picture>

---

## Design Decisions

| Decision | Rationale |
|----------|-----------|
| Supervisor uses `gemini-2.5-pro` | Higher reasoning for intent classification and multi-step orchestration |
| Sub-agents use `gemini-flash-latest` | Faster, cheaper model sufficient for structured tool-calling tasks |
| Each sub-agent gets its own MCP process | Isolated stdio connections; `tool_filter` enforces read/write separation |
| Reviewer is strictly read-only | Prevents accidental mutations; only `GET` tools are exposed |
| Creator is strictly write-only | Prevents acting on stale state without the supervisor's knowledge |

---

> See [adk/O2C/readme.md](adk/O2C/readme.md) for detailed agent prompts and inner architecture notes.
