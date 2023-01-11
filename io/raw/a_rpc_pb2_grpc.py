# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2
from io.common import common_objects_pb2 as io_dot_common_dot_common__objects__pb2
from io.raw import pass_pb2 as io_dot_raw_dot_pass__pb2
from io.raw import project_pb2 as io_dot_raw_dot_project__pb2


class RawStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.createPassProject = channel.unary_unary(
                '/raw.Raw/createPassProject',
                request_serializer=io_dot_raw_dot_project__pb2.PassProject.SerializeToString,
                response_deserializer=io_dot_common_dot_common__objects__pb2.Id.FromString,
                )
        self.updatePassProject = channel.unary_unary(
                '/raw.Raw/updatePassProject',
                request_serializer=io_dot_raw_dot_project__pb2.PassProject.SerializeToString,
                response_deserializer=io_dot_raw_dot_project__pb2.PassProject.FromString,
                )
        self.getPassProject = channel.unary_unary(
                '/raw.Raw/getPassProject',
                request_serializer=io_dot_common_dot_common__objects__pb2.Id.SerializeToString,
                response_deserializer=io_dot_raw_dot_project__pb2.PassProject.FromString,
                )
        self.copyPassProject = channel.unary_unary(
                '/raw.Raw/copyPassProject',
                request_serializer=io_dot_raw_dot_project__pb2.PassProjectCopyRequest.SerializeToString,
                response_deserializer=io_dot_common_dot_common__objects__pb2.Id.FromString,
                )
        self.deletePassProject = channel.unary_unary(
                '/raw.Raw/deletePassProject',
                request_serializer=io_dot_common_dot_common__objects__pb2.Id.SerializeToString,
                response_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
                )
        self.createPass = channel.unary_unary(
                '/raw.Raw/createPass',
                request_serializer=io_dot_raw_dot_pass__pb2.Pass.SerializeToString,
                response_deserializer=io_dot_common_dot_common__objects__pb2.Id.FromString,
                )
        self.updatePass = channel.unary_unary(
                '/raw.Raw/updatePass',
                request_serializer=io_dot_raw_dot_pass__pb2.Pass.SerializeToString,
                response_deserializer=io_dot_common_dot_common__objects__pb2.Id.FromString,
                )
        self.streamPassUpdates = channel.stream_stream(
                '/raw.Raw/streamPassUpdates',
                request_serializer=io_dot_raw_dot_pass__pb2.Pass.SerializeToString,
                response_deserializer=io_dot_common_dot_common__objects__pb2.Id.FromString,
                )
        self.getPassById = channel.unary_unary(
                '/raw.Raw/getPassById',
                request_serializer=io_dot_common_dot_common__objects__pb2.Id.SerializeToString,
                response_deserializer=io_dot_raw_dot_pass__pb2.Pass.FromString,
                )
        self.getPassByExternalId = channel.unary_unary(
                '/raw.Raw/getPassByExternalId',
                request_serializer=io_dot_raw_dot_pass__pb2.PassRecordByExternalIdRequest.SerializeToString,
                response_deserializer=io_dot_raw_dot_pass__pb2.Pass.FromString,
                )
        self.deletePass = channel.unary_unary(
                '/raw.Raw/deletePass',
                request_serializer=io_dot_raw_dot_pass__pb2.Pass.SerializeToString,
                response_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
                )
        self.listPassesByPassProject = channel.unary_stream(
                '/raw.Raw/listPassesByPassProject',
                request_serializer=io_dot_raw_dot_pass__pb2.ListPassesByPassProjectRequest.SerializeToString,
                response_deserializer=io_dot_raw_dot_pass__pb2.Pass.FromString,
                )
        self.listPassesByPassTemplate = channel.unary_stream(
                '/raw.Raw/listPassesByPassTemplate',
                request_serializer=io_dot_raw_dot_pass__pb2.ListPassesByPassTemplateRequest.SerializeToString,
                response_deserializer=io_dot_raw_dot_pass__pb2.Pass.FromString,
                )


class RawServicer(object):
    """Missing associated documentation comment in .proto file."""

    def createPassProject(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def updatePassProject(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def getPassProject(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def copyPassProject(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def deletePassProject(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def createPass(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def updatePass(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def streamPassUpdates(self, request_iterator, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def getPassById(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def getPassByExternalId(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def deletePass(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def listPassesByPassProject(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def listPassesByPassTemplate(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_RawServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'createPassProject': grpc.unary_unary_rpc_method_handler(
                    servicer.createPassProject,
                    request_deserializer=io_dot_raw_dot_project__pb2.PassProject.FromString,
                    response_serializer=io_dot_common_dot_common__objects__pb2.Id.SerializeToString,
            ),
            'updatePassProject': grpc.unary_unary_rpc_method_handler(
                    servicer.updatePassProject,
                    request_deserializer=io_dot_raw_dot_project__pb2.PassProject.FromString,
                    response_serializer=io_dot_raw_dot_project__pb2.PassProject.SerializeToString,
            ),
            'getPassProject': grpc.unary_unary_rpc_method_handler(
                    servicer.getPassProject,
                    request_deserializer=io_dot_common_dot_common__objects__pb2.Id.FromString,
                    response_serializer=io_dot_raw_dot_project__pb2.PassProject.SerializeToString,
            ),
            'copyPassProject': grpc.unary_unary_rpc_method_handler(
                    servicer.copyPassProject,
                    request_deserializer=io_dot_raw_dot_project__pb2.PassProjectCopyRequest.FromString,
                    response_serializer=io_dot_common_dot_common__objects__pb2.Id.SerializeToString,
            ),
            'deletePassProject': grpc.unary_unary_rpc_method_handler(
                    servicer.deletePassProject,
                    request_deserializer=io_dot_common_dot_common__objects__pb2.Id.FromString,
                    response_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
            ),
            'createPass': grpc.unary_unary_rpc_method_handler(
                    servicer.createPass,
                    request_deserializer=io_dot_raw_dot_pass__pb2.Pass.FromString,
                    response_serializer=io_dot_common_dot_common__objects__pb2.Id.SerializeToString,
            ),
            'updatePass': grpc.unary_unary_rpc_method_handler(
                    servicer.updatePass,
                    request_deserializer=io_dot_raw_dot_pass__pb2.Pass.FromString,
                    response_serializer=io_dot_common_dot_common__objects__pb2.Id.SerializeToString,
            ),
            'streamPassUpdates': grpc.stream_stream_rpc_method_handler(
                    servicer.streamPassUpdates,
                    request_deserializer=io_dot_raw_dot_pass__pb2.Pass.FromString,
                    response_serializer=io_dot_common_dot_common__objects__pb2.Id.SerializeToString,
            ),
            'getPassById': grpc.unary_unary_rpc_method_handler(
                    servicer.getPassById,
                    request_deserializer=io_dot_common_dot_common__objects__pb2.Id.FromString,
                    response_serializer=io_dot_raw_dot_pass__pb2.Pass.SerializeToString,
            ),
            'getPassByExternalId': grpc.unary_unary_rpc_method_handler(
                    servicer.getPassByExternalId,
                    request_deserializer=io_dot_raw_dot_pass__pb2.PassRecordByExternalIdRequest.FromString,
                    response_serializer=io_dot_raw_dot_pass__pb2.Pass.SerializeToString,
            ),
            'deletePass': grpc.unary_unary_rpc_method_handler(
                    servicer.deletePass,
                    request_deserializer=io_dot_raw_dot_pass__pb2.Pass.FromString,
                    response_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
            ),
            'listPassesByPassProject': grpc.unary_stream_rpc_method_handler(
                    servicer.listPassesByPassProject,
                    request_deserializer=io_dot_raw_dot_pass__pb2.ListPassesByPassProjectRequest.FromString,
                    response_serializer=io_dot_raw_dot_pass__pb2.Pass.SerializeToString,
            ),
            'listPassesByPassTemplate': grpc.unary_stream_rpc_method_handler(
                    servicer.listPassesByPassTemplate,
                    request_deserializer=io_dot_raw_dot_pass__pb2.ListPassesByPassTemplateRequest.FromString,
                    response_serializer=io_dot_raw_dot_pass__pb2.Pass.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'raw.Raw', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class Raw(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def createPassProject(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/raw.Raw/createPassProject',
            io_dot_raw_dot_project__pb2.PassProject.SerializeToString,
            io_dot_common_dot_common__objects__pb2.Id.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def updatePassProject(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/raw.Raw/updatePassProject',
            io_dot_raw_dot_project__pb2.PassProject.SerializeToString,
            io_dot_raw_dot_project__pb2.PassProject.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def getPassProject(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/raw.Raw/getPassProject',
            io_dot_common_dot_common__objects__pb2.Id.SerializeToString,
            io_dot_raw_dot_project__pb2.PassProject.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def copyPassProject(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/raw.Raw/copyPassProject',
            io_dot_raw_dot_project__pb2.PassProjectCopyRequest.SerializeToString,
            io_dot_common_dot_common__objects__pb2.Id.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def deletePassProject(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/raw.Raw/deletePassProject',
            io_dot_common_dot_common__objects__pb2.Id.SerializeToString,
            google_dot_protobuf_dot_empty__pb2.Empty.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def createPass(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/raw.Raw/createPass',
            io_dot_raw_dot_pass__pb2.Pass.SerializeToString,
            io_dot_common_dot_common__objects__pb2.Id.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def updatePass(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/raw.Raw/updatePass',
            io_dot_raw_dot_pass__pb2.Pass.SerializeToString,
            io_dot_common_dot_common__objects__pb2.Id.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def streamPassUpdates(request_iterator,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.stream_stream(request_iterator, target, '/raw.Raw/streamPassUpdates',
            io_dot_raw_dot_pass__pb2.Pass.SerializeToString,
            io_dot_common_dot_common__objects__pb2.Id.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def getPassById(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/raw.Raw/getPassById',
            io_dot_common_dot_common__objects__pb2.Id.SerializeToString,
            io_dot_raw_dot_pass__pb2.Pass.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def getPassByExternalId(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/raw.Raw/getPassByExternalId',
            io_dot_raw_dot_pass__pb2.PassRecordByExternalIdRequest.SerializeToString,
            io_dot_raw_dot_pass__pb2.Pass.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def deletePass(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/raw.Raw/deletePass',
            io_dot_raw_dot_pass__pb2.Pass.SerializeToString,
            google_dot_protobuf_dot_empty__pb2.Empty.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def listPassesByPassProject(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_stream(request, target, '/raw.Raw/listPassesByPassProject',
            io_dot_raw_dot_pass__pb2.ListPassesByPassProjectRequest.SerializeToString,
            io_dot_raw_dot_pass__pb2.Pass.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def listPassesByPassTemplate(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_stream(request, target, '/raw.Raw/listPassesByPassTemplate',
            io_dot_raw_dot_pass__pb2.ListPassesByPassTemplateRequest.SerializeToString,
            io_dot_raw_dot_pass__pb2.Pass.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)