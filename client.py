from xmlrpc.client import ServerProxy, MultiCall, Error

server = ServerProxy("http://localhost:8000")
print(server)
print(server.multiply(10, 5))
multi = MultiCall(server)
multi.pow(2, 9)
multi.add(5, 1)
multi.add(24, 11)
multi.multiply(2, 5)
try:
    for response in multi():
        print(response)
except Error as v:
    var = "ERROR", v
    print(var)
