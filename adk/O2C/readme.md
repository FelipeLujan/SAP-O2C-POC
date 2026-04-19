implement an agent team composed of:
- one sales supervisor agent
  - sales reviewer agent
  - sales order creator

## sales supervisor agent
- model: Gemini 3.1 Pro
- subagents:
  - sales reviewer agent
  - sales order creator agent

## sales reviewer agent
- model: Gemini 3.1 flash
- tools: `GetASalesorder`, `GetASalesorder___salesorder___ToItem`, `GetASalesorder___salesorder___ToPartner`, `GetASalesorder___salesorder___ToPricingelement`, `GetASalesorder___salesorder___ToText`, `GetASalesorder___salesorder___ToBillingplan`, `GetASalesorder___salesorder___ToPaymentplanitemdetails`, `GetASalesorder___salesorder___ToPrecedingprocflowdoc`, `GetASalesorder___salesorder___ToRelatedobject`, `GetASalesorder___salesorder___ToSubsequentprocflowdoc`
- prompt: ""

## sales order creator agent.
- model: Gemini 3.1 flash
- tools: `PostASalesorder`, `PostASalesorder___salesorder___ToItem`, `PostASalesorder___salesorder___ToPartner`, `PostASalesorder___salesorder___ToPricingelement`, `PostASalesorder___salesorder___ToText`, `PostASalesorder___salesorder___ToBillingplan`, `PostASalesorder___salesorder___ToPaymentplanitemdetails`, `PostASalesorder___salesorder___ToPrecedingprocflowdoc`, `PostASalesorder___salesorder___ToRelatedobject`, `PostASalesorder___salesorder___ToSubsequentprocflowdoc`
- prompt: ""

## MCP toolbox.
- command: `node`
- arguments: `/Users/felipe/Documents/coding/O2C-ADK-next/generated/API_SALES_ORDER_SRV/build/index.js`
- environment variables:
  - BASIC_USERNAME_BASICAUTH=bpinst
  - BASIC_PASSWORD_BASICAUTH=Welcome1
  - API_BASE_URL=http://34.19.215.140:50000/sap/opu/odata/sap/API_SALES_ORDER_SRV/



