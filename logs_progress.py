from mcp.server.fastmcp import FastMCP, Context
import asyncio

mcp = FastMCP(name="Demo Server")

@mcp.tool("Web search with logs")
async def web_search(query: str, ctx: Context) -> str:
    await ctx.info(f"Starting web search for query: {query}")
    await asyncio.sleep(1)  # Simulate initial delay
    await ctx.report_progress(20, 100)

    await ctx.debug("Fetching results from search engine...")
    await asyncio.sleep(2)  # Simulate fetching results
    await ctx.report_progress(40, 100)

    await ctx.warning("Processing results from non-ideal sources...")
    await asyncio.sleep(1)  # Simulate processing
    await ctx.report_progress(70, 100)

    await ctx.error("Encountered an error with one of the sources, but continuing...")
    await asyncio.sleep(1)  # Simulate error handling
    await ctx.report_progress(90, 100)

    await ctx.info("Continuing with remaining results...")
    await asyncio.sleep(1)  # Simulate continuation
    await ctx.report_progress(100, 100)
    
    await ctx.info("Web search completed.")
    return f"Results for '{query}': [Result 1, Result 2, Result 3]"

app = mcp.streamable_http_app()
