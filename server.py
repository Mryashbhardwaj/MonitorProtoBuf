import grpc
from concurrent import futures
import time

# import the generated classes
import monitor_pb2
import monitor_pb2_grpc

# import the original calculator.py
import cpulib

# create a class to define the server functions, derived from
# calculator_pb2_grpc.CalculatorServicer
class MachineMonitorServicer( monitor_pb2_grpc.MachineMonitorServicer):

    # calculator.square_root is exposed here
    # the request and response are of the data type
    # calculator_pb2.Number
    def checkCpu(self, request, context):
        response = monitor_pb2.Response()
        response.answer = cpulib.checkCpu(request.value)
        return response


# create a gRPC server
server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))

# use the generated function `add_CalculatorServicer_to_server`
# to add the defined class to the server
monitor_pb2_grpc.add_MachineMonitorServicer_to_server(
        MachineMonitorServicer(), server)

# listen on port 50051
print('Starting server. Listening on port 50051.')
server.add_insecure_port('[::]:50051')
server.start()

# since server.start() will not block,
# a sleep-loop is added to keep alive
try:
    while True:
        time.sleep(86400)
except KeyboardInterrupt:
    server.stop(0)
