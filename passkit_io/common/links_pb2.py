# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: passkit/io/common/links.proto
# Protobuf Python Version: 6.31.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(
    _runtime_version.Domain.PUBLIC,
    6,
    31,
    1,
    '',
    'passkit/io/common/links.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from passkit.io.common import common_objects_pb2 as passkit_dot_io_dot_common_dot_common__objects__pb2
from passkit.io.common import localization_pb2 as passkit_dot_io_dot_common_dot_localization__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1dpasskit/io/common/links.proto\x12\x02io\x1a&passkit/io/common/common_objects.proto\x1a$passkit/io/common/localization.proto\"\xd3\x01\n\x04Link\x12\n\n\x02id\x18\x01 \x01(\t\x12\x0b\n\x03url\x18\x02 \x01(\t\x12\r\n\x05title\x18\x03 \x01(\t\x12\x1a\n\x04type\x18\x04 \x01(\x0e\x32\x0c.io.LinkType\x12*\n\rlocalizedLink\x18\x05 \x01(\x0b\x32\x13.io.LocalizedString\x12+\n\x0elocalizedTitle\x18\x06 \x01(\x0b\x32\x13.io.LocalizedString\x12\x1c\n\x05usage\x18\x07 \x03(\x0e\x32\r.io.UsageType\x12\x10\n\x08position\x18\x08 \x01(\r\"!\n\x06\x44\x62Link\x12\x17\n\x05links\x18\x01 \x03(\x0b\x32\x08.io.Link*k\n\x08LinkType\x12\x12\n\x0eURI_DO_NOT_USE\x10\x00\x12\x0b\n\x07URI_WEB\x10\x01\x12\x0b\n\x07URI_TEL\x10\x02\x12\r\n\tURI_EMAIL\x10\x03\x12\x10\n\x0cURI_LOCATION\x10\x04\x12\x10\n\x0cURI_CALENDAR\x10\x05\x42G\n\x10\x63om.passkit.grpcZ$stash.passkit.com/io/model/sdk/go/io\xaa\x02\x0cPassKit.Grpcb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'passkit.io.common.links_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n\020com.passkit.grpcZ$stash.passkit.com/io/model/sdk/go/io\252\002\014PassKit.Grpc'
  _globals['_LINKTYPE']._serialized_start=364
  _globals['_LINKTYPE']._serialized_end=471
  _globals['_LINK']._serialized_start=116
  _globals['_LINK']._serialized_end=327
  _globals['_DBLINK']._serialized_start=329
  _globals['_DBLINK']._serialized_end=362
# @@protoc_insertion_point(module_scope)
