from mcp.server.fastmcp import FastMCP, Context
from mcp.types import SamplingMessage, TextContent
from mcp.server.fastmcp.prompts import base


mcp = FastMCP(name="Demo Server")


@mcp.tool()
async def summarize(text_to_summarize: str, ctx: Context):
    prompt = f"""
        Please summarize the following text:
        {text_to_summarize}
    """
    await ctx.info("Sending prompt to language model")
    result = await ctx.session.create_message(
        messages=[
            SamplingMessage(
                role="user", content=TextContent(type="text", text=prompt)
            )
        ],
        max_tokens=4000,
        system_prompt="You are a helpful research assistant.",
    )
    await ctx.info("Waiting for  response from language model")

    if result.content.type == "text":
        return result.content.text
    else:
        raise ValueError("Sampling failed")
    
@mcp.tool("Story Writer")
async def story_writer(topic: str, ctx: Context) -> str:
    prompt = f"Write a short story about {topic}."

    await ctx.info("Sending prompt to language model")
    result = await ctx.session.create_message(
        messages=[
            SamplingMessage([base.UserMessage(prompt)])
                # role="user", content=TextContent(type="text", text=prompt)
            
        ],
        max_tokens=2000,
        system_prompt="You are a creative story writer.",
    )
    await ctx.info("Waiting for response from language model")

    if result.content.type == "text":
        return result.content.text
    else:
        raise ValueError("Sampling failed")


app = mcp.streamable_http_app()
