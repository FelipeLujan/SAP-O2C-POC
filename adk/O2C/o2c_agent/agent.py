"""
O2C Agent Team – SAP Order-to-Cash automation with Google ADK + MCP.

Architecture
------------
root_agent  (sales_supervisor)     gemini-3.1-pro
  ├── sales_reviewer_agent          gemini-3.1-flash   (GET tools only)
  └── sales_order_creator_agent     gemini-3.1-flash   (POST tools only)

Both sub-agents share the same MCP toolbox that is launched as a stdio child process:

  node <MCP_SERVER_JS>

The SAP credentials and API base URL are forwarded to the node process via environment
variables (see .env.example).
"""

import os

from dotenv import load_dotenv
from google.adk.agents import Agent
from google.adk.tools.mcp_tool import McpToolset
from google.adk.tools.mcp_tool.mcp_session_manager import StdioConnectionParams
from mcp import StdioServerParameters

from o2c_agent.prompts import (
    SALES_ORDER_CREATOR_PROMPT,
    SALES_REVIEWER_PROMPT,
    SALES_SUPERVISOR_PROMPT,
)

# ---------------------------------------------------------------------------
# Environment
# ---------------------------------------------------------------------------
load_dotenv()  # loads .env from the current working directory

MCP_SERVER_JS = os.environ.get(
    "MCP_SERVER_JS",
    "/Users/felipe/Documents/coding/O2C-ADK-next/generated/API_SALES_ORDER_SRV/build/index.js",
)

# Environment variables forwarded to the MCP node process
_MCP_ENV = {
    "BASIC_USERNAME_BASICAUTH": os.environ.get("BASIC_USERNAME_BASICAUTH", "bpinst"),
    "BASIC_PASSWORD_BASICAUTH": os.environ.get("BASIC_PASSWORD_BASICAUTH", "Welcome1"),
    "API_BASE_URL": os.environ.get(
        "API_BASE_URL",
        "http://34.19.215.140:50000/sap/opu/odata/sap/API_SALES_ORDER_SRV/",
    ),
}

# ---------------------------------------------------------------------------
# MCP toolset factory
# ---------------------------------------------------------------------------
# ADK starts a *separate* MCP child process for every McpToolset instance.
# We define a factory so each sub-agent gets its own isolated connection and
# can apply its own tool_filter.


def _make_mcp_toolset(tool_filter: list[str] | None = None) -> McpToolset:
    """Return an McpToolset connected to the SAP MCP server via stdio."""
    return McpToolset(
        connection_params=StdioConnectionParams(
            server_params=StdioServerParameters(
                command="node",
                args=[MCP_SERVER_JS],
                env=_MCP_ENV,
            ),
            timeout=60,
        ),
        tool_filter=tool_filter,
    )


# ---------------------------------------------------------------------------
# Sub-agent: Sales Reviewer  (read-only – GET tools)
# ---------------------------------------------------------------------------
_REVIEWER_TOOLS = [
    "GetASalesorder",
    "GetASalesorder___salesorder___ToItem",
    "GetASalesorder___salesorder___ToPartner",
    "GetASalesorder___salesorder___ToPricingelement",
    "GetASalesorder___salesorder___ToText",
    "GetASalesorder___salesorder___ToBillingplan",
    "GetASalesorder___salesorder___ToPaymentplanitemdetails",
    "GetASalesorder___salesorder___ToPrecedingprocflowdoc",
    "GetASalesorder___salesorder___ToRelatedobject",
    "GetASalesorder___salesorder___ToSubsequentprocflowdoc",
]

sales_reviewer_agent = Agent(
    name="sales_reviewer_agent",
    model="gemini-flash-latest",
    description=(
        "Read-only agent that retrieves and summarises SAP sales orders, "
        "line items, partners, pricing elements, billing plans, and process flows."
    ),
    instruction=SALES_REVIEWER_PROMPT,
    tools=[_make_mcp_toolset(tool_filter=_REVIEWER_TOOLS)],
)

# ---------------------------------------------------------------------------
# Sub-agent: Sales Order Creator  (write – POST tools)
# ---------------------------------------------------------------------------
_CREATOR_TOOLS = [
    "PostASalesorder",
    "PostASalesorder___salesorder___ToItem",
    "PostASalesorder___salesorder___ToPartner",
    "PostASalesorder___salesorder___ToPricingelement",
    "PostASalesorder___salesorder___ToText",
    "PostASalesorder___salesorder___ToBillingplan",
    "PostASalesorder___salesorder___ToPaymentplanitemdetails",
    "PostASalesorder___salesorder___ToPrecedingprocflowdoc",
    "PostASalesorder___salesorder___ToRelatedobject",
    "PostASalesorder___salesorder___ToSubsequentprocflowdoc",
]

sales_order_creator_agent = Agent(
    name="sales_order_creator_agent",
    model="gemini-flash-latest",
    description=(
        "Write agent that creates SAP sales order headers, line items, partners, "
        "pricing conditions, billing plans, and header texts."
    ),
    instruction=SALES_ORDER_CREATOR_PROMPT,
    tools=[_make_mcp_toolset(tool_filter=_CREATOR_TOOLS)],
)

# ---------------------------------------------------------------------------
# Root agent: Sales Supervisor
# ---------------------------------------------------------------------------
root_agent = Agent(
    name="sales_supervisor_agent",
    model="gemini-2.5-pro",
    description="Supervisor that routes O2C requests to the appropriate sub-agent.",
    instruction=SALES_SUPERVISOR_PROMPT,
    # Sub-agents are delegated to via the sub_agents list (ADK multi-agent pattern)
    sub_agents=[sales_reviewer_agent, sales_order_creator_agent],
)
