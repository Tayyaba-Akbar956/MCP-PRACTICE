# To Test The server Using Custom Client and Postman

# Instructions To Test Server Using Client.py

## Phase 1: Testing Tools (Requests 1-11)

### Step 1 : Run Main Server
Run **main.py** file using command:
```bash
uv run uvicorn main:app --reload
```

### Step 2 : Run Client
Run **client.py** file using following command:
```bash
uv run client.py
```

**Scope**: Requests 1 through 11 in `client.py` will execute automatically. These test the `Divide` tool and various error handling scenarios.

## Phase 2: Testing Resources (Requests 12-15)

### Step 1 : Run Resources Server
Stop the previous server (Ctrl+C) and run **Resources.py**:
```bash
uv run uvicorn Resources:app --reload
```

### Step 2 : Run Client
Run **client.py** file using following command:
```bash
uv run client.py
```

**Scope**: Requests 12 through 15 in `client.py` will execute automatically. These test resource listing and reading capabilities.

> [!NOTE]
> **Initialization Process**: For Phases 4, 5, and 6, `client.py` has been updated to automatically send the required `initialize` request (ID: 1) and `notifications/initialized` notification before performing tool calls. This ensures the server is properly initialized according to the MCP protocol.

## Phase 3: Testing Prompts (Requests 16-19)

### Step 1 : Run Prompts Server
```bash
uv run uvicorn prompts:app --reload
```

### Step 2 : Run Client
Run `client.py` and use requests 16-19.

## Phase 4: Testing Sampling (Requests 20-21)

### Step 1 : Run Sampling Server
```bash
uv run uvicorn sampling:app --reload
```

### Step 2 : Run Client
Run `client.py` and use requests 20-21.

## Phase 5: Testing Logs (Request 22)

### Step 1 : Run Logs Server
```bash
uv run uvicorn logs_progress:app --reload
```

### Step 2 : Run Client
Run `client.py` and use request 22.

## Phase 6: Testing Roots (Request 23)

### Step 1 : Run Roots Server
```bash
uv run uvicorn roots:app --reload
```

### Step 2 : Run Client
Run `client.py` and use request 23.

***Important:***   
1. Send all requests one by one 
2. Send one request at a time, comment all others and analyze the response 

# Instructions To Test Server In Postman

## Step 1 : Run Your Server
Run **main.py** file using command   
```uv run uvicorn main:app --reload```

## Step 2 : Initialize postman

## Step 3 : Set parameters
1. ### Request : Post
2. ### URL : http://localhost:8000/mcp/

3. ### In heaaders Section    

Key         | value      |
------------|------------|
Accept      |application/json,text/event-stream
 |

## Step 3 : Write Body  

1. Go in body section
2. Choose **raw**

3. Send one request at a time from client.py in following format 

```
{
    "jsonrpc": "2.0",
    "method": "tools/call",
    "id": 2,
    "params": {
        "name": "Divide",
        "arguments": {
            "a": 10,
            "b": 2
        }
    }
} 
```

