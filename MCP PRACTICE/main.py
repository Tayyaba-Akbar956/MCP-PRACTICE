from mcp.server.fastmcp import FastMCP

mcp = FastMCP("Demo Server",stateless_http = True)

@mcp.tool("Divide")

def divide(a: float, b: float) -> float:
    """Divides two numbers."""
    return a / b

app = mcp.streamable_http_app()
