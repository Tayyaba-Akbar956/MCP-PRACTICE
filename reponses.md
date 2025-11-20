# Responses to All Requests

## Response 1 (main.py):
### HTTP : 200 OK
### JSON 
{
    "jsonrpc": "2.0",
    "id": 1,
    "result": {
        "tools": [
            {
                "name": "Divide",
                "description": "Divides two numbers.",
                "inputSchema": {
                    "properties": {
                        "a": {
                            "title": "A",
                            "type": "number"
                        },
                        "b": {
                            "title": "B",
                            "type": "number"
                        }
                    },
                    "required": [
                        "a",
                        "b"
                    ],
                    "title": "divideArguments",
                    "type": "object"
                },
                "outputSchema": {
                    "properties": {
                        "result": {
                            "title": "Result",
                            "type": "number"
                        }
                    },
                    "required": [
                        "result"
                    ],
                    "title": "divideOutput",
                    "type": "object"
                }
            }
        ]
    }
}

## Response 2 (main.py):
### HTTP : 200 OK
### JSON 
{
    "jsonrpc": "2.0",
    "id": 2,
    "result": {
        "content": [
            {
                "type": "text",
                "text": "5.0"
            }
        ],
        "structuredContent": {
            "result": 5.0
        },
        "isError": false
    }
}

## Response 3 and 4 (main.py):
### HTTP : 400 Bad Request
### JSON 
{
    "jsonrpc": "2.0",
    "id": "server-error",
    "error": {
        "code": -32602,
        "message": "Validation error: 6 validation errors for JSONRPCMessage\nJSONRPCRequest.jsonrpc\n  Field required [type=missing, input_value={'method': 'tools/call', ...ts': {'a': 10, 'b': 2}}, input_type=dict]\n    For further information visit https://errors.pydantic.dev/2.12/v/missing\nJSONRPCNotification.jsonrpc\n  Field required [type=missing, input_value={'method': 'tools/call', ...ts': {'a': 10, 'b': 2}}, input_type=dict]\n    For further information visit https://errors.pydantic.dev/2.12/v/missing\nJSONRPCResponse.jsonrpc\n  Field required [type=missing, input_value={'method': 'tools/call', ...ts': {'a': 10, 'b': 2}}, input_type=dict]\n    For further information visit https://errors.pydantic.dev/2.12/v/missing\nJSONRPCResponse.result\n  Field required [type=missing, input_value={'method': 'tools/call', ...ts': {'a': 10, 'b': 2}}, input_type=dict]\n    For further information visit https://errors.pydantic.dev/2.12/v/missing\nJSONRPCError.jsonrpc\n  Field required [type=missing, input_value={'method': 'tools/call', ...ts': {'a': 10, 'b': 2}}, input_type=dict]\n    For further information visit https://errors.pydantic.dev/2.12/v/missing\nJSONRPCError.error\n  Field required [type=missing, input_value={'method': 'tools/call', ...ts': {'a': 10, 'b': 2}}, input_type=dict]\n    For further information visit https://errors.pydantic.dev/2.12/v/missing"
    }
}

## Response 5 (main.py):
### HTTP : 202 Accepted 
### JSON : No response 

## Response 6, 7, 8, 9 (main.py):
### HTTP : 200 OK 
### JSON : 
{
    "jsonrpc": "2.0",
    "id": 6,
    "error": {
        "code": -32602,
        "message": "Invalid request parameters",
        "data": ""
    }
}

## Response 10 (main.py):
### HTTP : 200 OK 
### JSON : 
{
    "jsonrpc": "2.0",
    "id": 10,
    "result": {
        "content": [
            {
                "type": "text",
                "text": "Unknown tool: Add"
            }
        ],
        "isError": true
    }
}

## Response 11 (main.py):
### HTTP : 200 OK 
### JSON : 

{
    "jsonrpc": "2.0",
    "id": 11,
    "result": {
        "content": [
            {
                "type": "text",
                "text": "Error executing tool Divide: float division by zero"
            }
        ],
        "isError": true
    }
}

## Response 12 (Resources.py):
### HTTP : 200 OK 
### JSON : 
{
    "jsonrpc": "2.0",
    "id": 12,
    "result": {
        "resources": [
            {
                "name": "list_docs",
                "uri": "docs://documents",
                "description": "",
                "mimeType": "application/json"
            },
            {
                "name": "get_openai_agents_docs",
                "uri": "web://openai-agents-docs",
                "description": "Fetch OpenAI Agents documentation",
                "mimeType": "text/html"
            },
            {
                "name": "get_formula",
                "uri": "file://formula.py/",
                "description": "",
                "mimeType": "text/plain"
            }
        ]
    }
}

## Response 13 (Resources.py):
### HTTP : 200 OK 
### JSON : 
{
    "jsonrpc": "2.0",
    "id": 13,
    "result": {
        "contents": [
            {
                "uri": "file://formula.py/",
                "mimeType": "text/plain",
                "text": "area_of_circle = \"3.14 * radius * radius\"\narea_of_square = \"side * side\"\narea_of_rectangle = \"length * breadth\"\narea_of_triangle = \"0.5 * base * height\"\narea_of_trapezium = \"0.5 * (a + b) * h\"\narea_of_parallelogram = \"base * height\"\narea_of_ellipse = \"3.14 * a * b\"\narea_of_rhombus = \"0.5 * d1 * d2\"\narea_of_kite = \"0.5 * d1 * d2\""
            }
        ]
    }
}

## Response 14 (Resources.py):
### HTTP : 200 OK 
### JSON : 
{
    "jsonrpc": "2.0",
    "id": 14,
    "result": {
        "contents": [
            {
                "uri": "docs://spec.txt",
                "mimeType": "text/plain",
                "text": "These specifications define the technical requirements for the equipment."
            }
        ]
    }
}

## Response 15 (Resources.py):
### HTTP : 200 OK 
### JSON :
{
    "jsonrpc": "2.0",
    "id": 15,
    "result": {
        "contents": [
            {
                "uri": "web://openai-agents-docs",
                "mimeType": "text/html",
                "text": "<!doctype html>\n<html lang=\"en\"class=\"no-js\">\n..."
            }
        ]
    }
}

## Response 16 (prompts.py):
### HTTP : 200 OK
### JSON :
{
    "jsonrpc": "2.0",
    "id": 16,
    "result": {
        "prompts": [
            {
                "name": "Github Profile",
                "description": "",
                "arguments": [
                    {
                        "name": "username",
                        "required": true
                    }
                ]
            },
            {
                "name": "to_divide_numbers",
                "description": "A prompt that divides two numbers",
                "arguments": []
            },
            {
                "name": "format",
                "description": "Rewrites the contents of the document in Markdown format.",
                "arguments": [
                    {
                        "name": "doc_content",
                        "required": true
                    }
                ]
            }
        ]
    }
}

## Response 17 (prompts.py):
### HTTP : 200 OK
### JSON :
{
    "jsonrpc": "2.0",
    "id": 17,
    "result": {
        "description": "Github Profile",
        "messages": [
            {
                "role": "user",
                "content": {
                    "type": "text",
                    "text": "Fetch the github profile information for the username: Tayyaba-Akbar956 and summarize the details."
                }
            }
        ]
    }
}

## Response 18 (prompts.py):
### HTTP : 200 OK
### JSON :
{
    "jsonrpc": "2.0",
    "id": 18,
    "result": {
        "description": "to_divide_numbers",
        "messages": [
            {
                "role": "user",
                "content": {
                    "type": "text",
                    "text": "You are a helpful assistant that divides two numbers.\n    Use the following format:\n    Input: <number1>, <number2>\n    Output: <result>\n    "
                }
            }
        ]
    }
}

## Response 19 (prompts.py):
### HTTP : 200 OK
### JSON :
{
    "jsonrpc": "2.0",
    "id": 19,
    "result": {
        "description": "format",
        "messages": [
            {
                "role": "user",
                "content": {
                    "type": "text",
                    "text": "Rewrites the contents of the document in Markdown format.\nDocument Content:\nThis is a test document."
                }
            }
        ]
    }
}

## Initialization Response (for Sampling, Logs,Progress, Roots):
### HTTP : 200 OK
### JSON :
{
    "jsonrpc": "2.0",
    "id": 1,
    "result": {
        "protocolVersion": "2024-11-05",
        "capabilities": {
            "logging": {},
            "prompts": {
                "listChanged": true
            },
            "resources": {
                "listChanged": true,
                "subscribe": true
            },
            "tools": {
                "listChanged": true
            }
        },
        "serverInfo": {
            "name": "mcp-server",
            "version": "0.1.0"
        }
    }
}

## Response 20 & 21 (sampling.py):
### HTTP : 200 OK
### JSON :
{
    "jsonrpc": "2.0",
    "id": 20,
    "error": {
        "code": -32603,
        "message": "Sampling not supported by client"
    }
}
> **Note:** These requests fail because the client declares no sampling capabilities in the initialization handshake (Request ID 1). The server attempts to use sampling, but aborts or fails when it detects the client does not support it.

## Response 22 (Logs_progress.py):
### HTTP : 200 OK
### JSON :
{
    "jsonrpc": "2.0",
    "id": 22,
    "result": {
        "content": [
            {
                "type": "text",
                "text": "Results for 'MCP protocol': [Result 1, Result 2, Result 3]"
            }
        ],
        "isError": false
    }
}

## Response 23 (roots.py):
### HTTP : 200 OK
### JSON :
{
    "jsonrpc": "2.0",
    "id": 23,
    "result": {
        "content": [
            {
                "type": "text",
                "text": "No project roots found"
            }
        ],
        "isError": false
    }
}