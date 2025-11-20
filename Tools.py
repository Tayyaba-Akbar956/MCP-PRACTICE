from mcp.server.fastmcp import FastMCP
import httpx

mcp = FastMCP("Demo Server",stateless_http = True)

@mcp.tool("Quiz")
def quiz_format(topic: str, type: str, questions: int, level: str):
    return f"Generating a {type} based quiz on {topic} with {questions} questions at {level} level."

@mcp.tool("Summarize")
def summarize_web_content(url:str) -> str:
    """Fetch OpenAI Agents documentation"""
    response = httpx.get(url)
    print ("summarizing web content from ", url)
    return response.text

app = mcp.streamable_http_app()
