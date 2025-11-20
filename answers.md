1. 2xx means success; 200 OK = request succeeded (general), 201 Created = request succeeded and a new resource was created.
2. 3xx is for redirection; 301 = resource moved permanently (cacheable), 302 = temporary redirect (not cacheable by default).
3. 4xx = client-side error (client is wrong), 5xx = server-side error (server failed even if request was valid).
4. 5xx status codes indicate the server failed to fulfill a valid request.
5. 429 means rate-limited; client should stop, wait, and retry after the time given in Retry-After header.
6. Best practice: use accurate semantics – 200/201/204 for success, 400/401/403/404/409 for client errors, 500/503 for server errors, never hide errors behind 200.
7. HTTP/1.1 limitations: head-of-line blocking & multiple TCP connections; HTTP/2 fixes both with multiplexing (many requests on one connection) and HPACK header compression.
8. Connection: keep-alive reuses the same TCP connection for multiple requests/responses instead of closing it after each one.
9. All HTTP versions share: request-response model, methods, status codes, headers, and text-based protocol (until HTTP/3 QUIC).
10. In MCP, context is the set of resources, prompts, and tools the client makes available to the AI model.
11. 200 OK with JSON-RPC error inside means the HTTP/REST layer succeeded, but the JSON-RPC protocol layer rejected the request (e.g., invalid params or method not found).
12. MCP solves secure, standardized, two-way access between LLMs and external tools/files without giving away API keys or full filesystem access.
13. MCP reverses traditional REST: the AI model is the server, the data/tools provider (IDE, app) is the client.
14. The three main primitives are: Tools (actions), Resources (data), Prompts (templates).
15. An MCP tool is a remotely callable function exposed by the client to the AI (server), unlike traditional calls where the app calls external APIs.
16. Tools are exposed via tools/list and tools/call JSON-RPC methods with name, description, and JSON schema.
17. Tool discovery happens via the tools/list method during or after initialization.
18. Resources use URIs (file://, http://, memory://, etc.); a good URI is unique, stable, and scoped.
19. Resource templates are parameterized URIs (e.g., file://{path}) that the AI can fill in.
20. Expose static/frequent data as resources (fast & cacheable); use tools for actions or expensive computations.
21. Resources are readable pieces of data identified by URIs that the client exposes to the AI.
22. Prompts are reusable, user-controlled message templates the AI can invoke via prompts/list and are not auto-triggered.
23. Code assistant: user prompt → AI selects code-explain prompt template + current file resource + run-code tool → executes and explains.
24. Stateful transport maintains session state and allows server → client calls; stateless does not.
25. STDIO is always stateful (single pipe), Streamable HTTP can be stateful (with session cookies) or stateless.
26. Roots are client-exposed filesystem directories that the server (AI) can request access to.
27. Roots are access boundaries (folders); resources are individual files/data reachable via URIs.
28. The four log levels: error, warn, info, debug.
29. stateless_http=True removes session & server → client calls; adding json_response=True also removes streaming (only single JSON replies).
30. Parse error (-32700) because all JSON string values must be in double quotes; the tool name 'Divide' is not quoted, making it invalid JSON.
31. Error response: {"jsonrpc":"2.0","id":2,"error":{"code":-32601,"message":"Unknown tool: Multiply"}} — The 'Multiply' tool doesn't exist in the server (only 'Divide' is registered).
32. Optional keys in MCP tool call response: structuredContent, progressToken, and metadata fields (usage, etc.) — required keys are content and isError.
33. Missing comma after "resources/read" line → invalid JSON syntax → Parse error (-32700).
34. Not valid (missing jsonrpc field) → error -32600 Invalid Request.
35. code, message, data → data is optional.
36. Method not found (-32601) because correct method is tools/call, not tool/execute.
37. The client calls the initialize method to start an MCP session.
38. Batch request is an array of multiple JSON-RPC requests/notifications sent together.
39. GET, PUT, DELETE, HEAD, OPTIONS, TRACE are inherently idempotent.
40. GET is safe and should not change state; POST can change server state and is not safe.
41. DELETE.
42. PATCH.
43. POST.
44. HEAD returns only headers (no body), used for metadata/checks; GET returns full response.
45. Client-Server separates UI from data/storage; improves portability and scalability.
46. The four sub-rules: Resource identification, Manipulation through representations, Self-descriptive messages, HATEOAS.
47. HATEOAS means responses contain links so clients can discover next actions dynamically.
48. Layered System allows proxies, gateways, load balancers; client cannot tell because each layer behaves identically.
49. Cacheable responses can be stored and reused → reduces latency and server load.
50. Code on Demand = server can send executable code (e.g., JavaScript) to client; example: browser loading JS from CDN.