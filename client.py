# import grpc

# # import the generated classes
# import calculator_pb2
# import calculator_pb2_grpc

# # open a gRPC channel
# channel = grpc.insecure_channel('172.16.66.43:50051')

# # create a stub (client)
# stub = calculator_pb2_grpc.CalculatorStub(channel)

# # create a valid request message
# number = calculator_pb2.Number(value=25)

# # make the call
# response = stub.SquareRoot(number)

# # et voilà
# print(response.value)

import grpc
import os

# import the generated classes
import monitor_pb2
import monitor_pb2_grpc

# open a gRPC channel
channel = grpc.insecure_channel("localhost"+':50051')

# create a stub (client)
stub = monitor_pb2_grpc.MachineMonitorStub(channel)

# create a valid request message
number = monitor_pb2.CpuLoad(value=os.getloadavg()[0])
# make the call
response = stub.checkCpu(number)

# et voilà
print(response.answer)
