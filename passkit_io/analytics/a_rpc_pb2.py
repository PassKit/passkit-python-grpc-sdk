# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: io/analytics/a_rpc.proto
# Protobuf Python Version: 5.27.2
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(
    _runtime_version.Domain.PUBLIC,
    5,
    27,
    2,
    '',
    'io/analytics/a_rpc.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from protoc_gen_openapiv2.options import annotations_pb2 as protoc__gen__openapiv2_dot_options_dot_annotations__pb2
from passkit_io.common import reporting_pb2 as io_dot_common_dot_reporting__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x18io/analytics/a_rpc.proto\x12\tanalytics\x1a\x1cgoogle/api/annotations.proto\x1a.protoc-gen-openapiv2/options/annotations.proto\x1a\x19io/common/reporting.proto2\xe6\x01\n\tAnalytics\x12\xd8\x01\n\x0cgetAnalytics\x12\x14.io.AnalyticsRequest\x1a\x15.io.AnalyticsResponse\"\x9a\x01\x92\x41{\n\tAnalytics\x12\rGet Analytics\x1a\x1bRetrieves an analytics dataJ\"\n\x03\x34\x30\x33\x12\x1b\n\x19User lacks authorization.J\x1e\n\x03\x34\x30\x34\x12\x17\n\x15Record was not found.\x82\xd3\xe4\x93\x02\x16\x12\x14/analytics/{classId}B\xa1\x07\n\x1a\x63om.passkit.grpc.AnalyticsZ.stash.passkit.com/io/model/sdk/go/io/analytics\xaa\x02\x16PassKit.Grpc.Analytics\x92\x41\xb8\x06\x12\xf3\x01\n\x15PassKit Analytics API\x12_The PassKit Analytics API lets you track the performance of Apple Wallet and Google Pay passes.\x1a\x38https://passkit.com/legal/terms-of-subscription-service/\"?\n\x0fPassKit Support\x12\x17https://docs.passkit.io\x1a\x13support@passkit.com*\x01\x02\x32\x10\x61pplication/json:\x10\x61pplication/jsonR9\n\x03\x32\x30\x30\x12\x32\n(Returned when the request is successful.\x12\x06\n\x04\x9a\x02\x01\x07R4\n\x03\x34\x30\x30\x12-\n+Returned when wrong user input is provided.R0\n\x03\x34\x30\x31\x12)\n\'Returned when the user is unauthorized.RP\n\x03\x34\x30\x33\x12I\nGReturned when the user does not have permission to access the resource.R;\n\x03\x34\x30\x34\x12\x34\n*Returned when the resource does not exist.\x12\x06\n\x04\x9a\x02\x01\x07R<\n\x03\x35\x30\x30\x12\x35\n+Returned when there is an unexpected error.\x12\x06\n\x04\x9a\x02\x01\x07RW\n\x03\x35\x30\x33\x12P\nNServer is unavailable. Back off for 250ms and repeat request until successful.Z>\n<\n\napiKeyAuth\x12.\x08\x02\x12\x19JWT Authentication token.\x1a\rAuthorization \x02\x62\x10\n\x0e\n\napiKeyAuth\x12\x00\x62\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'io.analytics.a_rpc_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n\032com.passkit.grpc.AnalyticsZ.stash.passkit.com/io/model/sdk/go/io/analytics\252\002\026PassKit.Grpc.Analytics\222A\270\006\022\363\001\n\025PassKit Analytics API\022_The PassKit Analytics API lets you track the performance of Apple Wallet and Google Pay passes.\0328https://passkit.com/legal/terms-of-subscription-service/\"?\n\017PassKit Support\022\027https://docs.passkit.io\032\023support@passkit.com*\001\0022\020application/json:\020application/jsonR9\n\003200\0222\n(Returned when the request is successful.\022\006\n\004\232\002\001\007R4\n\003400\022-\n+Returned when wrong user input is provided.R0\n\003401\022)\n\'Returned when the user is unauthorized.RP\n\003403\022I\nGReturned when the user does not have permission to access the resource.R;\n\003404\0224\n*Returned when the resource does not exist.\022\006\n\004\232\002\001\007R<\n\003500\0225\n+Returned when there is an unexpected error.\022\006\n\004\232\002\001\007RW\n\003503\022P\nNServer is unavailable. Back off for 250ms and repeat request until successful.Z>\n<\n\napiKeyAuth\022.\010\002\022\031JWT Authentication token.\032\rAuthorization \002b\020\n\016\n\napiKeyAuth\022\000'
  _globals['_ANALYTICS'].methods_by_name['getAnalytics']._loaded_options = None
  _globals['_ANALYTICS'].methods_by_name['getAnalytics']._serialized_options = b'\222A{\n\tAnalytics\022\rGet Analytics\032\033Retrieves an analytics dataJ\"\n\003403\022\033\n\031User lacks authorization.J\036\n\003404\022\027\n\025Record was not found.\202\323\344\223\002\026\022\024/analytics/{classId}'
  _globals['_ANALYTICS']._serialized_start=145
  _globals['_ANALYTICS']._serialized_end=375
# @@protoc_insertion_point(module_scope)