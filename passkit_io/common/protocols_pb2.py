# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: io/common/protocols.proto
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
    'io/common/protocols.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x19io/common/protocols.proto\x12\x02io*\xa0\x01\n\x0cPassProtocol\x12\x1c\n\x18PASS_PROTOCOL_DO_NOT_USE\x10\x00\x12\x10\n\x0cRAW_PROTOCOL\x10\x01\x12\x0f\n\x0bV1_PROTOCOL\x10\x02\x12\x13\n\x0f\x46LIGHT_PROTOCOL\x10\x03\x12\x0e\n\nMEMBERSHIP\x10\x64\x12\x15\n\x11SINGLE_USE_COUPON\x10\x65\x12\x13\n\x0f\x45VENT_TICKETING\x10\x66*\x8e\x02\n\x14ProtocolCommonEvents\x12%\n!PROTOCOL_COMMON_EVENTS_DO_NOT_USE\x10\x00\x12\x18\n\x14\x45VENT_OBJECT_CREATED\x10\x01\x12\x18\n\x14\x45VENT_OBJECT_UPDATED\x10\x02\x12\x18\n\x14\x45VENT_OBJECT_EXPIRED\x10\x03\x12\x18\n\x14\x45VENT_OBJECT_DELETED\x10\x04\x12\x15\n\x11\x45VENT_PASS_ISSUED\x10\x05\x12\x18\n\x14\x45VENT_PASS_INSTALLED\x10\x06\x12\x1a\n\x16\x45VENT_PASS_UNINSTALLED\x10\x07\x12\x1a\n\x16\x45VENT_PASS_INVALIDATED\x10\x08\x42G\n\x10\x63om.passkit.grpcZ$stash.passkit.com/io/model/sdk/go/io\xaa\x02\x0cPassKit.Grpcb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'io.common.protocols_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n\020com.passkit.grpcZ$stash.passkit.com/io/model/sdk/go/io\252\002\014PassKit.Grpc'
  _globals['_PASSPROTOCOL']._serialized_start=34
  _globals['_PASSPROTOCOL']._serialized_end=194
  _globals['_PROTOCOLCOMMONEVENTS']._serialized_start=197
  _globals['_PROTOCOLCOMMONEVENTS']._serialized_end=467
# @@protoc_insertion_point(module_scope)