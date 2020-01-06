About longpolling
==================

**What is HTTP Long Polling?**


Web applications were originally developed around a client/server model, where the client is always the initiator of transactions, requesting data from the server. Thus, there was no mechanism for the server to independently send, or push, data to the client without the client first making a request. 

**In a Nutshell: HTTP Long Polling**


To overcome this deficiency, Web app developers can implement a technique called HTTP long polling, where the client polls the server requesting new information.  The server holds the request open until new data is available. Once available, the server responds and sends the new information. When the client receives the new information, it immediately sends another request, and the operation is repeated. This effectively emulates a server push feature.

Thus, each data packet means new connection which will remain open until the server sends the information.

In practice the connection usually reinstalls once per 20-30 seconds to get rid of possible problems (mistakes) , e.g. problems connected with HTTP-proxy.

In contradiction to usual polling, such notice appears faster.

``Delay = connection installing + data transfer``

**Advantages of longpolling**


+ The loading to the server is reduced unlike usual polling
+ Reduced traffic
+ Supporting in all modern browsers

Thus, longpolling helps the client to receive data as soon as they appear in the server in contrast to periodic, which send requests according to interval specified.

