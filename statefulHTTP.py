from mcp.server.fastmcp import FastMCP
mcp = FastMCP("Demo Server", stateless_http=False, json_response=True)

print("Connecting Server")
print ("-"*50)
print("Example Messages")
print("-"*50)
print("""{"jsonrpc":"2.0","id":1,"method":"initialize","params":{"protocolVersion":"2025-06-18","capabilities":{},"clientInfo":{"name":"Example Client","version":"0.1.0"}}}""")
print("-"*50)
print("""{"jsonrpc":"2.0","method":"notifications/initialized"}""")
print("-"*50)
print("""{"jsonrpc":"2.0","id":2,"method":"tools/call","params":{"name":"greet","arguments":{"name":"Tayyaba"}}}""")
print("-"*50)
print("""{"jsonrpc":"2.0","id":3,"method":"tools/list","params":{}}""")
print("-"*50)
print("""{"jsonrpc":"2.0","id":4,"method":"tools/call","params":{"name":"Divide","arguments":{"a":10,"b":2}}}""")
print("-"*50)

@mcp.tool("Greet")
def greet(name: str) -> str:
    """Greets a person by name."""
    return f"Hello, {name}!"

@mcp.tool("Divide")
def divide(a: float, b: float) -> float:
    """Divides two numbers."""
    return a / b

app = mcp.streamable_http_app()