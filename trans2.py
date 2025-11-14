from mcp.server.fastmcp import FastMCP
import asyncio
from mcp.server.fastmcp.server import Context

mcp = FastMCP("First MCP server",stateless_http = True,json_response = True)

@mcp.tool("divide",description="takes two number and divide them")
async def divide(ctx:Context, a: float, b: float) -> float:
    await ctx.info("preparing to divide")
    await asyncio.sleep(2)  
    await ctx.debug(f"dividing {a} by {b}")
    await ctx.warning (f"may be an error arise")
    await ctx.error ("division by zero error")
    await asyncio.sleep(2)  
    return a / b

app = mcp.streamable_http_app()

