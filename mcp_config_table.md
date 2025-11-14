# MCP Server Configuration Comparison

| Configuration | Transport Type | Notifications? |
|--------------|---------------|----------------|
| `stateless_http=True, json_response=True` | Single HTTP request/response with JSON | ❌ No notifications (single response only) |
| `stateless_http=True, json_response=False` | **SSE (Server-Sent Events) streaming** | ✅ **Yes! Notifications stream in real-time** |
| `stateless_http=False` | WebSocket (stateful) | ✅ Yes, bidirectional |

## Key Points:

- **`json_response=True`**: Returns a single JSON response, no streaming
- **`json_response=False`**: Enables SSE streaming, allows notifications
- **`stateless_http=True`**: Server doesn't maintain session state between requests
- **`stateless_http=False`**: Maintains persistent WebSocket connection

## Explanation:

When `stateless_http=True` and `json_response=False`, FastMCP uses Server-Sent Events (SSE) streaming. This allows the server to stream notifications, progress updates, and the final result while remaining stateless (no persistent connection state needed).
