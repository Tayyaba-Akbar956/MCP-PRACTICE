1. What is the main purpose of the “2xx” class of status codes? How does 200 OK differ from 201 Created?

2. When are “3xx” redirection codes used, and what is the difference between 301 Moved Permanently and 302 Found?

3. What defines a “4xx” class error, and how is it different from a “5xx” class error?

4. What do “5xx” status codes represent?


5. If an API frequently returns 429 Too Many Requests, what does it mean, and how should clients respond?

6. In REST API design, what are the best practices for assigning and evaluating HTTP status codes?

6. Discuss two major performance limitations of HTTP/1.1 (specifically concerning TCP connection usage), and explain how HTTP/2 addresses both of these issues through features like multiplexing and header compression.

7. Describe the performance function of the Connection: keep-alive header in HTTP/1.1.

8. what is the common factors in all HTTP versions (0.9 to 3)?

9. What is meant by context in terms of MCP?

10. If you get  200 HTTP code but error in jsonrpc, what could be the possible reason?

11. What problem does the Model Context Protocol (MCP) solve in AI applications?

12. How does MCP differ from traditional REST APIs when connecting AI models to external data sources?

13. Explain the client-server architecture in MCP. Which component is the AI model, and which provides the data?

14. What are the three main primitives (building blocks) that MCP uses to enable AI-data integration?

15. What is a "tool" in the context of MCP, and how does it differ from a traditional function call?

16. How does an MCP server expose tools to AI clients? What information must be provided?

17. Explain the concept of tool "discovery" in MCP. How does the client know what tools are available?

18. How does resource URI structure work in MCP? What makes a good resource identifier?

19. Explain the concept of resource "templates" in MCP. Why are they useful?

20. When would you expose data as a resource versus creating a tool to fetch that data?

21. What are resources in MCP, and how are they identified?

22. Explain the purpose of prompts in MCP and why they are described as "user-controlled" rather than automatically invoked?

23. Give an example scenario where a combination of a prompt (template), multiple resources (context data), and a tool (action) would be used together in an MCP-powered AI application (e.g., code assistant or agent workflow).

24. What is the fundamental difference between stateful and stateless and stateful transports in MCP?

25. Why is STDIO considered a stateful transport while Streamable HTTP can be either?

26. What are "roots" in MCP, and who exposes them?

27. how are roots different from resources?

28. Name the four standard log levels defined in the MCP spec.

29. In FastMCP, what is the difference between setting stateless_http=True versus setting both stateless_http=True and json_response=True? What capability does each configuration remove?

30. If a JSON-RPC request has the method name without double quotes ke bina, like this:
{
  "jsonrpc": "2.0",
  "method": "tools/call",
  "params": 
        {"name": Divide, "arguments": {"a": 10, "b": 2}},
  "id": 1
}
What error will the server return and why?

31. If the client sends this request:
JSON{
  "jsonrpc": "2.0",
  "method": "tools/call",
  "params": 
        {"name": "Multiply", "arguments": {"a": 10, "b": 2}},
  "id": 2
}
What will be the correct JSON-RPC response? What value should be in the result field?

32. Wha are the optional keys in mcp response?

33. The client sent this message:
JSON{
  "jsonrpc": "2.0",
  "method": "resources/read"
  "params": {"uri": "file://test.txt"},
  "id": 5
}
What is the syntax error in this message?

34. {
  "method": "prompts/list",
  "params": {},
  "id": 10
}
Is this a valid request? If not, what should the error response contain?

35. What are three keys in error  response and which of them is optional?

36. {
  "jsonrpc": "2.0",
  "method": "tool/execute",
  "params": {
    "name": "calculator"
  },
  "id": 7
}
what will be the reponse of this request?

37. In MCP, which method does the client call to initialize the connection?

38. what is meant by batch request in jsonrpc?

39. Which HTTP methods are inherently idempotent?

40. Name one big difference between GET and POST.

41. Which HTTP method is used to delete a resource (like deleting a user)?

42. Which HTTP method is used when you want to update only some fields of a resource?

43. If you submit a web form to sign up, which HTTP method is usually used?

44. What does the HEAD method do? How is it different from GET?

45. Explain the Client-Server constraint in simple words. Why is separation of concerns important in REST?

46. The Uniform Interface constraint has 4 sub-rules. Name all 4 of them.

47. Explain HATEOAS (Hypermedia as the Engine of Application State).

48. What is the Layered System constraint? Why can a client not tell if it is connected directly to the end server or to an intermediary (like a load balancer)?

49. What is the Cacheability constraint? How does it affect the performance of a REST API?

50. The Code on Demand constraint is the only optional one in REST. What does it mean and give one real-world example of when it is used?





## Answers 

