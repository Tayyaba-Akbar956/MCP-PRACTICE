import requests 

url = "http://localhost:8000/mcp/"

headers = {"Accept": "application/json,text/event-stream"}


print ("Correct Code Execution:")   

body1 = {
    "jsonrpc": "2.0",
    "method": "tools/list",
    "id": 1
}

response1 = requests.post(url, json=body1, headers=headers)
print("Tools List Response:")
print(response1.json())
print ("\n_"*50)


body2 = {
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

response2 = requests.post(url, json=body2, headers=headers)
print("Divide Tool Response:")
print(response2.json())
print ("\n_"*50)

print ("problematic Code Execution")

#No jsonrpc filed is given 
body3 = {
    # "jsonrpc": "2.0",
    "method": "tools/call",
    "id": 3,
    "params": {
        "name": "Divide",
        "arguments": {
            "a": 10,
            "b": 2
        }
    }
}

response3 = requests.post(url, json=body3, headers=headers)
print("Response for missing jsonrpc field:")
print(response3.json())

#wrong version of json_rpc
body4 = {
    "jsonrpc": "1.0",
    "method": "tools/call",
    "id": 4,
    "params": {
        "name": "Divide",
        "arguments": {
            "a": 10,
            "b": 2
        }
    }
}

response4 = requests.post(url, json=body4, headers=headers)
print("Response for wrong jsonrpc version:")
print(response4.json())

#missing id field
body5 = {
    "jsonrpc": "2.0",
    "method": "tools/call",
    # "id": 5,
    "params": {
        "name": "Divide",
        "arguments": {
            "a": 10,
            "b": 2
        }
    }
}
response5 = requests.post(url, json=body5, headers=headers)
print("Response for missing id field:")
print(response5.json())

#wrong method name
body6 = {
    "jsonrpc": "2.0",
    "method": "tools/unknown_method",
    "id": 6,
    "params": {
        "name": "Divide",
        "arguments": {
            "a": 10,
            "b": 2
        }
    }
}

response6 = requests.post(url, json=body6, headers=headers)
print("Response for wrong method name:")
print(response6.json())

#missing params field
body7 = {
    "jsonrpc": "2.0",
    "method": "tools/call",
    "id": 7,
    # "params": {
    #     "name": "Divide",
    #     "arguments": {
    #         "a": 10,
    #         "b": 2
    #     }
    # }
}

response7 = requests.post(url, json=body7, headers=headers)
print("Response for missing params field:")
print(response7.json())

# #missing name in params
body8 = {
    "jsonrpc": "2.0",
    "method": "tools/call",
    "id": 8,
    "params": {
        # "name": "Divide",
        "arguments": {
            "a": 10,
            "b": 2
        }
    }
}

response8 = requests.post(url, json=body8, headers=headers)
print("Response for missing name in params:")
print(response8.json())

#missing args in params
body9 = {
    "jsonrpc": "2.0",
    "method": "tools/call",
    "id": 9,
    "params": {
        "name": "Divide",
        # "arguments": {
        #     "a": 10,
        #     "b": 2
        # }
    }
}

response9 = requests.post(url, json=body9, headers=headers)
print("Response for missing args in params:")
print(response9.json())


#wrong tool name
body10 = {
    "jsonrpc": "2.0",
    "method": "tools/call",
    "id": 10,
    "params": {
        "name": "Add",
        "arguments": {
            "a": 10,
            "b": 2
        }
    }
}

response10 = requests.post(url, json=body10, headers=headers)
print("Response for wrong tool name:")
print(response10.json())
print ("\n_"*50)

#division by zero
body11 = {
    "jsonrpc": "2.0",
    "method": "tools/call",
    "id": 11,
    "params": {
        "name": "Divide",
        "arguments": {
            "a": 10,
            "b": 0
        }
    }
}

response11 = requests.post(url, json=body11, headers=headers)
print("Response for division by zero:")
print(response11.json())
print ("\n_"*50)