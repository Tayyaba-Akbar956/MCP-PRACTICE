from mcp.server.fastmcp import FastMCP
import asyncio
from mcp.server.fastmcp.server import Context


mcp = FastMCP("First MCP server")

print("Connecting Server")
print("Example Messages")
print("-"*50)
print("""{"jsonrpc":"2.0","id":1,"method":"initialize","params":{"protocolVersion":"2025-06-18","capabilities":{},"clientInfo":{"name":"Example Client","version":"0.1.0"}}}""")
print("-"*50)
print("""{"jsonrpc":"2.0","method":"notifications/initialized"}""")
print("-"*50)
print("""{"jsonrpc":"2.0","id":2,"method":"tools/call","params":{"name":"greet","arguments":{"name":"Alice"}}}""")
print("-"*50)
print("""{"jsonrpc":"2.0","id":3,"method":"resources/list","params":{}}""")
print("-"*50)
print("""{"jsonrpc":"2.0","id":4,"method":"tools/call","params":{"name":"divide","arguments":{"a":10,"b":2}}}""")


@mcp.tool()
def greet(name: str) -> str:
    """Greet someone by name"""
    return f"Hello, {name}!"

# @mcp.tool(description="takes two number and divide them")
# async def divide(ctx:Context, a: float, b: float) -> float:
#     await ctx.info("preparing to divide")
#     await ctx.report_progress(20, 100)
#     await asyncio.sleep(2)  
#     await ctx.debug(f"dividing {a} by {b}")
#     await ctx.report_progress(80, 100)
#     await asyncio.sleep(2)  
#     return a / b


docs = {
    "plan.md": "The plan outlines the steps for the project's implementation.",
    "spec.txt": "These specifications define the technical requirements for the equipment.",
}

@mcp.resource(
    "xyz:/abc",
    mime_type="application/json"
)
def list_docs() -> list[str]:
    return list(docs.keys())

@mcp.resource(
    "docs://{doc_id}",
    mime_type="text/plain"
)
def get_doc(doc_id: str) -> str:
    return docs[doc_id]


if __name__ == "__main__":
    mcp.run()