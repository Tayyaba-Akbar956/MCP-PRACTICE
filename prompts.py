from mcp.server.fastmcp import FastMCP


mcp = FastMCP("Demo Server",stateless_http = True)

from mcp.server.fastmcp import FastMCP
from mcp.server.fastmcp.prompts import base
# from pydantic import Field
from mcp.types import PromptMessage,TextContent

mcp = FastMCP("First MCP server",stateless_http = True)

@mcp.prompt("Github Profile")
def get_github_profile(username: str) -> str:
    return f"Fetch the github profile information for the username: {username} and summarize the details."

@mcp.prompt ("to_divide_numbers","A prompt that divides two numbers")
def to_divide_numbers():
    prompt = """You are a helpful assistant that divides two numbers.
    Use the following format:
    Input: <number1>, <number2>
    Output: <result>
    """
    return [base.UserMessage(prompt)]

@mcp.prompt(
    name="format",
    description="Rewrites the contents of the document in Markdown format.",
)
def format_document(
    doc_content: str ) -> list[base.Message]:
    prompt = f"""
    Your goal is to reformat a document to be written with markdown syntax.

    The contents of the document you need to reformat is:
    <document_content>
    {doc_content}
    </document_content>

    Add in headers, bullet points, tables, etc as necessary. Feel free to add in extra text, but don't change the meaning of the report.
    After the document has been edited, respond with the final version of the doc. Don't explain your changes.
    """

    
    return [PromptMessage(role="user", content=TextContent (type = "text",text = prompt))]


app = mcp.streamable_http_app()
