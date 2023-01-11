# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: io/raw/project.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
from io.common import distribution_pb2 as io_dot_common_dot_distribution__pb2
from io.common import localization_pb2 as io_dot_common_dot_localization__pb2
from io.common import project_pb2 as io_dot_common_dot_project__pb2
from io.common import billing_pb2 as io_dot_common_dot_billing__pb2
from protoc_gen_openapiv2.options import annotations_pb2 as protoc__gen__openapiv2_dot_options_dot_annotations__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x14io/raw/project.proto\x12\x03raw\x1a\x1fgoogle/protobuf/timestamp.proto\x1a\x1cio/common/distribution.proto\x1a\x1cio/common/localization.proto\x1a\x17io/common/project.proto\x1a\x17io/common/billing.proto\x1a.protoc-gen-openapiv2/options/annotations.proto\"\xfe\x03\n\x0bPassProject\x12\n\n\x02id\x18\x01 \x01(\t\x12\x0c\n\x04name\x18\x02 \x01(\t\x12*\n\rlocalizedName\x18\x03 \x01(\x0b\x32\x13.io.LocalizedString\x12!\n\x06status\x18\x04 \x03(\x0e\x32\x11.io.ProjectStatus\x12\x18\n\x05quota\x18\x05 \x01(\x0b\x32\t.io.Quota\x12\x1a\n\x12passTypeIdentifier\x18\x06 \x01(\t\x12\x36\n\x14\x64istributionSettings\x18\x07 \x01(\x0b\x32\x18.io.DistributionSettings\x12+\n\x07\x63reated\x18\x08 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12+\n\x07updated\x18\t \x01(\x0b\x32\x1a.google.protobuf.Timestamp:\xbd\x01\x92\x41\xb9\x01\n\xb6\x01*\x0cPass Project2\x95\x01Pass Project holds the basic business logic. Pass Project holds details on pass distribution, quotas, Apple certificate, integrations & hooks to use.\xd2\x01\x04name\xd2\x01\x06status\"q\n\x16PassProjectCopyRequest\x12\n\n\x02id\x18\x01 \x01(\t\x12\x0c\n\x04name\x18\x02 \x01(\t\x12!\n\x06status\x18\x03 \x03(\x0e\x32\x11.io.ProjectStatus\x12\x1a\n\x12passTypeIdentifier\x18\x04 \x01(\tBS\n\x14\x63om.passkit.grpc.RawZ(stash.passkit.com/io/model/sdk/go/io/raw\xaa\x02\x10PassKit.Grpc.Rawb\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'io.raw.project_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\024com.passkit.grpc.RawZ(stash.passkit.com/io/model/sdk/go/io/raw\252\002\020PassKit.Grpc.Raw'
  _PASSPROJECT._options = None
  _PASSPROJECT._serialized_options = b'\222A\271\001\n\266\001*\014Pass Project2\225\001Pass Project holds the basic business logic. Pass Project holds details on pass distribution, quotas, Apple certificate, integrations & hooks to use.\322\001\004name\322\001\006status'
  _PASSPROJECT._serialized_start=221
  _PASSPROJECT._serialized_end=731
  _PASSPROJECTCOPYREQUEST._serialized_start=733
  _PASSPROJECTCOPYREQUEST._serialized_end=846
# @@protoc_insertion_point(module_scope)