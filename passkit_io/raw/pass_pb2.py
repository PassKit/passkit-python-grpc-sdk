# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: io/raw/pass.proto
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
    'io/raw/pass.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
from passkit_io.common import metrics_pb2 as io_dot_common_dot_metrics__pb2
from passkit_io.common import filter_pb2 as io_dot_common_dot_filter__pb2
from passkit_io.common import pass_pb2 as io_dot_common_dot_pass__pb2
from passkit_io.common import personal_pb2 as io_dot_common_dot_personal__pb2
from protoc_gen_openapiv2.options import annotations_pb2 as protoc__gen__openapiv2_dot_options_dot_annotations__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x11io/raw/pass.proto\x12\x03raw\x1a\x1fgoogle/protobuf/timestamp.proto\x1a\x17io/common/metrics.proto\x1a\x16io/common/filter.proto\x1a\x14io/common/pass.proto\x1a\x18io/common/personal.proto\x1a.protoc-gen-openapiv2/options/annotations.proto\"\xc7\x05\n\x04Pass\x12\n\n\x02id\x18\x01 \x01(\t\x12\x12\n\nexternalId\x18\x02 \x01(\t\x12\x15\n\rpassProjectId\x18\x03 \x01(\t\x12\x16\n\x0epassTemplateId\x18\x04 \x01(\t\x12#\n\x0fpersonalDetails\x18\x05 \x01(\x0b\x32\n.io.Person\x12/\n\x0b\x64ynamicData\x18\x06 \x03(\x0b\x32\x1a.raw.Pass.DynamicDataEntry\x12\x0e\n\x06optOut\x18\x08 \x01(\x08\x12\x10\n\x08isVoided\x18\t \x01(\x08\x12\x32\n\x0einvalidateDate\x18\n \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12.\n\nexpiryDate\x18\x0b \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12$\n\x0bpassOptions\x18\x0c \x01(\x0b\x32\x0f.io.PassOptions\x12(\n\rpassOverrides\x18\r \x01(\x0b\x32\x11.io.PassOverrides\x12\"\n\x0cpassMetaData\x18\x0e \x01(\x0b\x32\x0c.io.Metadata\x12+\n\x07\x63reated\x18\x0f \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12+\n\x07updated\x18\x10 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x1a\x32\n\x10\x44ynamicDataEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01:\x91\x01\x92\x41\x8d\x01\n\x8a\x01*\x04Pass2aPass contains dynamic information that combined with a Pass Project & Template results in a pass.\xd2\x01\rpassProjectId\xd2\x01\x0epassTemplateId\"J\n\x1dPassRecordByExternalIdRequest\x12\x15\n\rpassProjectId\x18\x01 \x01(\t\x12\x12\n\nexternalId\x18\x02 \x01(\t\"U\n\x1eListPassesByPassProjectRequest\x12\x15\n\rpassProjectId\x18\x01 \x01(\t\x12\x1c\n\x07\x66ilters\x18\x02 \x01(\x0b\x32\x0b.io.Filters\"V\n\x1fListPassesByPassTemplateRequest\x12\x15\n\rpassProjectId\x18\x01 \x01(\t\x12\x1c\n\x07\x66ilters\x18\x02 \x01(\x0b\x32\x0b.io.FiltersBS\n\x14\x63om.passkit.grpc.RawZ(stash.passkit.com/io/model/sdk/go/io/raw\xaa\x02\x10PassKit.Grpc.Rawb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'io.raw.pass_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n\024com.passkit.grpc.RawZ(stash.passkit.com/io/model/sdk/go/io/raw\252\002\020PassKit.Grpc.Raw'
  _globals['_PASS_DYNAMICDATAENTRY']._loaded_options = None
  _globals['_PASS_DYNAMICDATAENTRY']._serialized_options = b'8\001'
  _globals['_PASS']._loaded_options = None
  _globals['_PASS']._serialized_options = b'\222A\215\001\n\212\001*\004Pass2aPass contains dynamic information that combined with a Pass Project & Template results in a pass.\322\001\rpassProjectId\322\001\016passTemplateId'
  _globals['_PASS']._serialized_start=205
  _globals['_PASS']._serialized_end=916
  _globals['_PASS_DYNAMICDATAENTRY']._serialized_start=718
  _globals['_PASS_DYNAMICDATAENTRY']._serialized_end=768
  _globals['_PASSRECORDBYEXTERNALIDREQUEST']._serialized_start=918
  _globals['_PASSRECORDBYEXTERNALIDREQUEST']._serialized_end=992
  _globals['_LISTPASSESBYPASSPROJECTREQUEST']._serialized_start=994
  _globals['_LISTPASSESBYPASSPROJECTREQUEST']._serialized_end=1079
  _globals['_LISTPASSESBYPASSTEMPLATEREQUEST']._serialized_start=1081
  _globals['_LISTPASSESBYPASSTEMPLATEREQUEST']._serialized_end=1167
# @@protoc_insertion_point(module_scope)