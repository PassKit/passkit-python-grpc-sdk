# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from io.common import reporting_pb2 as io_dot_common_dot_reporting__pb2


class AnalyticsStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.getAnalytics = channel.unary_unary(
                '/analytics.Analytics/getAnalytics',
                request_serializer=io_dot_common_dot_reporting__pb2.AnalyticsRequest.SerializeToString,
                response_deserializer=io_dot_common_dot_reporting__pb2.AnalyticsResponse.FromString,
                )


class AnalyticsServicer(object):
    """Missing associated documentation comment in .proto file."""

    def getAnalytics(self, request, context):
        """Retrieve a daily, monthly or yearly record.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_AnalyticsServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'getAnalytics': grpc.unary_unary_rpc_method_handler(
                    servicer.getAnalytics,
                    request_deserializer=io_dot_common_dot_reporting__pb2.AnalyticsRequest.FromString,
                    response_serializer=io_dot_common_dot_reporting__pb2.AnalyticsResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'analytics.Analytics', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class Analytics(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def getAnalytics(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/analytics.Analytics/getAnalytics',
            io_dot_common_dot_reporting__pb2.AnalyticsRequest.SerializeToString,
            io_dot_common_dot_reporting__pb2.AnalyticsResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
