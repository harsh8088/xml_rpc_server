from xmlrpc.server import SimpleXMLRPCServer
from xmlrpc.server import SimpleXMLRPCRequestHandler


# Restrict to a particular path.
class RequestHandler(SimpleXMLRPCRequestHandler):
    rpc_paths = ('/RPC2',)


# Create server
server = SimpleXMLRPCServer(("localhost", 8000),
                            requestHandler=RequestHandler)
server.register_introspection_functions()

# Register pow() function; this will use the value of
# pow.__name__ as the name, which is just 'pow'.
server.register_function(pow)


# Register a function under a different name
def adder_function(x, y):
    return x + y


# Register a function under a different name
def multi_function(x, y):
    return x * y


server.register_function(adder_function, 'add')
server.register_function(multi_function, 'multiply')


# Register an instance; all the methods of the instance are
# published as XML-RPC methods (in this case, just 'div').
class MyFuncs:
    def div(self, x, y):
        return x // y


server.register_instance(MyFuncs())
server.register_multicall_functions()

# Run the server's main loop
server.serve_forever()
