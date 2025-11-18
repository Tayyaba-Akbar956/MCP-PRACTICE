# To Understand difference in HTTP and JSON Response

# Instructions To Test Server Using Client.py

## Step 1 : Run Your Server
Run **main.py** file using command   
```uv run uvicorn main:app --reload```

## Step 2 : Run your Client
Run **client.py** file using folllowing command   
```uv run client.py```

***Important:***   
1. Send all reuqests one by one 
2. Send one request at a time, comment and all others and analyze the response 

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
        "args": {
            "a": 10,
            "b": 2
        }
    }
} 
```

