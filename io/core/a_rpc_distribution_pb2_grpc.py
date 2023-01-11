# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2
from io.common import common_objects_pb2 as io_dot_common_dot_common__objects__pb2
from io.common import distribution_pb2 as io_dot_common_dot_distribution__pb2


class DistributionStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.sendWelcomeEmail = channel.unary_unary(
                '/io.Distribution/sendWelcomeEmail',
                request_serializer=io_dot_common_dot_distribution__pb2.EmailDistributionRequest.SerializeToString,
                response_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
                )
        self.getSmartPassLink = channel.unary_unary(
                '/io.Distribution/getSmartPassLink',
                request_serializer=io_dot_common_dot_distribution__pb2.SmartPassLinkRequest.SerializeToString,
                response_deserializer=io_dot_common_dot_common__objects__pb2.Url.FromString,
                )
        self.getDataCollectionPageFields = channel.unary_unary(
                '/io.Distribution/getDataCollectionPageFields',
                request_serializer=io_dot_common_dot_common__objects__pb2.ClassObjectInput.SerializeToString,
                response_deserializer=io_dot_common_dot_distribution__pb2.DataCollectionFields.FromString,
                )
        self.uploadSmartPassCsv = channel.unary_unary(
                '/io.Distribution/uploadSmartPassCsv',
                request_serializer=io_dot_common_dot_distribution__pb2.SmartPassCsvUploadRequest.SerializeToString,
                response_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
                )
        self.importProtocolCsv = channel.unary_unary(
                '/io.Distribution/importProtocolCsv',
                request_serializer=io_dot_common_dot_distribution__pb2.ImportProtocolRequest.SerializeToString,
                response_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
                )
        self.validateBarcode = channel.unary_unary(
                '/io.Distribution/validateBarcode',
                request_serializer=io_dot_common_dot_common__objects__pb2.Payload.SerializeToString,
                response_deserializer=io_dot_common_dot_common__objects__pb2.Payload.FromString,
                )


class DistributionServicer(object):
    """Missing associated documentation comment in .proto file."""

    def sendWelcomeEmail(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def getSmartPassLink(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def getDataCollectionPageFields(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def uploadSmartPassCsv(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def importProtocolCsv(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def validateBarcode(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_DistributionServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'sendWelcomeEmail': grpc.unary_unary_rpc_method_handler(
                    servicer.sendWelcomeEmail,
                    request_deserializer=io_dot_common_dot_distribution__pb2.EmailDistributionRequest.FromString,
                    response_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
            ),
            'getSmartPassLink': grpc.unary_unary_rpc_method_handler(
                    servicer.getSmartPassLink,
                    request_deserializer=io_dot_common_dot_distribution__pb2.SmartPassLinkRequest.FromString,
                    response_serializer=io_dot_common_dot_common__objects__pb2.Url.SerializeToString,
            ),
            'getDataCollectionPageFields': grpc.unary_unary_rpc_method_handler(
                    servicer.getDataCollectionPageFields,
                    request_deserializer=io_dot_common_dot_common__objects__pb2.ClassObjectInput.FromString,
                    response_serializer=io_dot_common_dot_distribution__pb2.DataCollectionFields.SerializeToString,
            ),
            'uploadSmartPassCsv': grpc.unary_unary_rpc_method_handler(
                    servicer.uploadSmartPassCsv,
                    request_deserializer=io_dot_common_dot_distribution__pb2.SmartPassCsvUploadRequest.FromString,
                    response_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
            ),
            'importProtocolCsv': grpc.unary_unary_rpc_method_handler(
                    servicer.importProtocolCsv,
                    request_deserializer=io_dot_common_dot_distribution__pb2.ImportProtocolRequest.FromString,
                    response_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
            ),
            'validateBarcode': grpc.unary_unary_rpc_method_handler(
                    servicer.validateBarcode,
                    request_deserializer=io_dot_common_dot_common__objects__pb2.Payload.FromString,
                    response_serializer=io_dot_common_dot_common__objects__pb2.Payload.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'io.Distribution', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class Distribution(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def sendWelcomeEmail(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/io.Distribution/sendWelcomeEmail',
            io_dot_common_dot_distribution__pb2.EmailDistributionRequest.SerializeToString,
            google_dot_protobuf_dot_empty__pb2.Empty.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def getSmartPassLink(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/io.Distribution/getSmartPassLink',
            io_dot_common_dot_distribution__pb2.SmartPassLinkRequest.SerializeToString,
            io_dot_common_dot_common__objects__pb2.Url.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def getDataCollectionPageFields(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/io.Distribution/getDataCollectionPageFields',
            io_dot_common_dot_common__objects__pb2.ClassObjectInput.SerializeToString,
            io_dot_common_dot_distribution__pb2.DataCollectionFields.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def uploadSmartPassCsv(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/io.Distribution/uploadSmartPassCsv',
            io_dot_common_dot_distribution__pb2.SmartPassCsvUploadRequest.SerializeToString,
            google_dot_protobuf_dot_empty__pb2.Empty.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def importProtocolCsv(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/io.Distribution/importProtocolCsv',
            io_dot_common_dot_distribution__pb2.ImportProtocolRequest.SerializeToString,
            google_dot_protobuf_dot_empty__pb2.Empty.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def validateBarcode(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/io.Distribution/validateBarcode',
            io_dot_common_dot_common__objects__pb2.Payload.SerializeToString,
            io_dot_common_dot_common__objects__pb2.Payload.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
