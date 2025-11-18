# Responses of All Requests

## Response 1:
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

## Response 2:
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

## Response 3 and 4:
### HTTP : 400 Bad Request
### JSON 
{
    "jsonrpc": "2.0",
    "id": "server-error",
    "error": {
        "code": -32602,
        "message": "Validation error: 6 validation errors for JSONRPCMessage\nJSONRPCRequest.jsonrpc\n  Field required [type=missing, input_value={'method': 'tools/call', ...ts': {'a': 10, 'b': 2}}}, input_type=dict]\n    For further information visit https://errors.pydantic.dev/2.12/v/missing\nJSONRPCNotification.jsonrpc\n  Field required [type=missing, input_value={'method': 'tools/call', ...ts': {'a': 10, 'b': 2}}}, input_type=dict]\n    For further information visit https://errors.pydantic.dev/2.12/v/missing\nJSONRPCResponse.jsonrpc\n  Field required [type=missing, input_value={'method': 'tools/call', ...ts': {'a': 10, 'b': 2}}}, input_type=dict]\n    For further information visit https://errors.pydantic.dev/2.12/v/missing\nJSONRPCResponse.result\n  Field required [type=missing, input_value={'method': 'tools/call', ...ts': {'a': 10, 'b': 2}}}, input_type=dict]\n    For further information visit https://errors.pydantic.dev/2.12/v/missing\nJSONRPCError.jsonrpc\n  Field required [type=missing, input_value={'method': 'tools/call', ...ts': {'a': 10, 'b': 2}}}, input_type=dict]\n    For further information visit https://errors.pydantic.dev/2.12/v/missing\nJSONRPCError.error\n  Field required [type=missing, input_value={'method': 'tools/call', ...ts': {'a': 10, 'b': 2}}}, input_type=dict]\n    For further information visit https://errors.pydantic.dev/2.12/v/missing"
    }
}

## Response 5:
### HTTP : 202 Accepted 
### JSON : No reponse 

## Response 6 , 7, 8, 9:
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

## Response 10:
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

## Response 11:
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



