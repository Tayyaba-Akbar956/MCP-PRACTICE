from mcp.server.fastmcp import FastMCP

mcp = FastMCP("First MCP server",stateless_http = True)

@mcp.tool("Add")
def add(a: int, b: int) -> int:
    return a + b

@mcp.tool("division","takes two number and divide them")
def divide(a: float, b: float) -> float:
    return a / b

app = mcp.streamable_http_app()