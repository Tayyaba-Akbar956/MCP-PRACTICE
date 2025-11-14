from mcp.server.fastmcp import FastMCP
import httpx

mcp = FastMCP("First MCP server",stateless_http = True)

@mcp.tool("Add")
def add(a: int, b: int) -> int:
    return a + b

@mcp.tool("division","takes two number and divide them")
def divide(a: float, b: float) -> float:
    return a / b

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

@mcp.resource(
    "web://openai-agents-docs",
    mime_type="text/html"
)
def get_openai_agents_docs() -> str:
    """Fetch OpenAI Agents documentation"""
    response = httpx.get("https://openai.github.io/openai-agents-python/")
    return response.text

@mcp.resource(
    "file://formula.py",
    mime_type="text/plain"
)
def get_formula() -> str:
    with open("formula.py", "r") as f:
        return f.read()
    

app = mcp.streamable_http_app()
