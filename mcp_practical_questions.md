# MCP Advanced Practical Questions - Code Analysis

## Tools with Transport Complexity

### Question 1
```python
mcp = FastMCP("Server", stateless_http=True, json_response=True)

@mcp.tool()
async def process_large_file(file_path: str, ctx: Context) -> dict:
    await ctx.info("Starting file processing")
    
    total_lines = 10000
    processed = 0
    
    for chunk in read_file_chunks(file_path):
        await ctx.report_progress(processed, total_lines)
        await ctx.debug(f"Processing chunk at line {processed}")
        process_chunk(chunk)
        processed += 1000
        await asyncio.sleep(0.5)
    
    await ctx.info("Processing complete")
    return {"status": "success", "processed_lines": total_lines}
```
**Request:** User calls this tool with a 10,000 line file

**Question:** What will the user experience be? What will they see and when? How would you modify the configuration to improve user experience during this long operation?

---

### Question 2
```python
mcp_server_1 = FastMCP("Server1", stateless_http=True, json_response=False)
mcp_server_2 = FastMCP("Server2", stateless_http=True, json_response=True)

@mcp_server_1.tool()
async def tool_a(ctx: Context) -> str:
    await ctx.report_progress(50, 100)
    return "Result A"

@mcp_server_2.tool()
async def tool_b(ctx: Context) -> str:
    await ctx.report_progress(50, 100)
    return "Result B"
```

**Question:** Compare what happens when calling `tool_a` vs `tool_b`. If both tools take 10 seconds to complete, describe the user experience for each. Which configuration is better for which scenario?

---

### Question 3
```python
mcp = FastMCP("Server", stateless_http=True, json_response=False)

@mcp.tool()
async def parallel_tasks(task_count: int, ctx: Context) -> dict:
    tasks = []
    for i in range(task_count):
        await ctx.info(f"Starting task {i+1}")
        tasks.append(asyncio.create_task(long_running_task(i)))
    
    results = await asyncio.gather(*tasks)
    await ctx.info("All tasks complete")
    return {"completed": len(results)}
```

**Question:** What's the problem with progress reporting in this parallel execution? How would you properly track and report progress for parallel tasks? Provide a corrected implementation approach.

---

### Question 4
```python
@mcp.tool()
async def retry_operation(url: str, ctx: Context, max_retries: int = 3) -> str:
    for attempt in range(1, max_retries + 1):
        try:
            await ctx.info(f"Attempt {attempt}/{max_retries}")
            result = await fetch_data(url)
            await ctx.info("Success!")
            return result
        except Exception as e:
            await ctx.warning(f"Attempt {attempt} failed: {e}")
            if attempt == max_retries:
                await ctx.error("All retries exhausted")
                raise
            await asyncio.sleep(2 ** attempt)
```
**Server Config:** stdio transport

**Question:** This tool works perfectly on stdio. You're asked to deploy it as HTTP with `json_response=True`. What functionality will be lost? How would you restructure it to work well with both transports?

---

## Resources with Transport Edge Cases

### Question 5
```python
mcp = FastMCP("Server", stateless_http=True, json_response=False)

@mcp.resource("stream://{source}/data")
async def stream_data(source: str, ctx: Context) -> str:
    await ctx.info(f"Starting stream from {source}")
    data_chunks = []
    
    for i, chunk in enumerate(fetch_stream(source)):
        await ctx.report_progress(i * 100, 1000)
        await ctx.debug(f"Received chunk {i}")
        data_chunks.append(chunk)
    
    await ctx.info("Stream complete")
    return "".join(data_chunks)
```
**Request:** Client requests `stream://api/data`

**Question:** Resources are typically read operations. Is using progress/notifications appropriate here? What happens if the client is using `json_response=True` config? Should resources behave differently based on transport?

---

### Question 6
```python
@mcp.resource("config://{env}/{key}")
async def get_config(env: str, key: str, ctx: Context) -> str:
    if env not in ["dev", "staging", "prod"]:
        await ctx.error(f"Invalid environment: {env}")
        raise ValueError("Invalid environment")
    
    await ctx.info(f"Fetching {key} from {env}")
    return fetch_config(env, key)
```
**Request 1:** `config://dev/database_url`  
**Request 2:** `config://invalid/some_key`

**Question:** With stdio transport, what happens on request 2? With HTTP `json_response=True`, what changes? How should error handling differ across transports?

---

### Question 7
```python
mcp = FastMCP("Server", stateless_http=True, json_response=False)

@mcp.resource("file://{path}")
async def read_file(path: str, ctx: Context) -> str:
    file_size = os.path.getsize(path)
    await ctx.info(f"Reading file: {file_size} bytes")
    
    chunks = []
    bytes_read = 0
    
    with open(path, 'r') as f:
        while chunk := f.read(1024):
            chunks.append(chunk)
            bytes_read += len(chunk)
            await ctx.report_progress(bytes_read, file_size)
    
    return "".join(chunks)
```

**Question:** You're reading a 50MB file. With SSE transport, what's the user experience? What if there are 100 concurrent requests for different files? What are the performance and resource implications? How would you optimize this?

---

## Prompts with Sampling and Transport

### Question 8
```python
@mcp.prompt()
async def dynamic_prompt(context: str, style: str, ctx: Context) -> str:
    await ctx.info("Generating dynamic prompt")
    
    # Use sampling to generate a better prompt
    enhanced = await ctx.sample(
        f"Improve this context for a {style} style: {context}",
        max_tokens=200
    )
    
    await ctx.info("Prompt generated")
    return enhanced
```

**Question:** What happens when a prompt uses sampling? Does this create nested MCP calls? With `json_response=False`, will notifications from both the prompt and the sampling appear? Explain the execution flow.

---

### Question 9
```python
@mcp.prompt("analyze")
async def analyze_code(code: str, ctx: Context) -> list[dict]:
    await ctx.info("Analyzing code structure")
    
    return [
        {"role": "system", "content": "You are a code analyzer"},
        {"role": "user", "content": f"Analyze:\n{code}"}
    ]
```
**Config:** `stateless_http=True, json_response=True`

**Question:** When this prompt is called, what does the client receive? Can prompts send notifications? Do prompts have different transport behavior than tools?

---

### Question 10
```python
@mcp.prompt()
async def multi_step_prompt(topic: str, ctx: Context) -> str:
    await ctx.info("Step 1: Researching")
    research = await ctx.sample(f"Research {topic}", max_tokens=500)
    
    await ctx.info("Step 2: Analyzing")
    analysis = await ctx.sample(f"Analyze: {research}", max_tokens=300)
    
    await ctx.info("Step 3: Formatting")
    return f"Research: {research}\nAnalysis: {analysis}"
```
**Transport:** WebSocket

**Question:** This prompt makes multiple sampling calls. Describe the complete message flow between client and server. What gets sent when? How does WebSocket's bidirectionality affect this?

---

## Sampling with Complex Scenarios

### Question 11
```python
@mcp.tool()
async def intelligent_search(query: str, ctx: Context) -> dict:
    await ctx.info("Enhancing query")
    enhanced_query = await ctx.sample(
        f"Improve search query: {query}",
        temperature=0.3,
        max_tokens=50
    )
    
    await ctx.info(f"Searching with: {enhanced_query}")
    results = search_database(enhanced_query)
    
    await ctx.info("Summarizing results")
    summary = await ctx.sample(
        f"Summarize: {results}",
        temperature=0.7,
        max_tokens=200
    )
    
    return {"query": enhanced_query, "summary": summary}
```
**Config:** stdio transport

**Question:** This tool makes 2 sampling calls with different temperatures. How many round-trips happen? What's the latency impact? Would HTTP `json_response=False` change anything? Compare stdio vs SSE for this use case.

---
