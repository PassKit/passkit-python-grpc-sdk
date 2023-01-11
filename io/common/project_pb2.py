# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: io/common/project.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
from io.common import protocols_pb2 as io_dot_common_dot_protocols__pb2
from io.common import template_pb2 as io_dot_common_dot_template__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x17io/common/project.proto\x12\x02io\x1a\x1fgoogle/protobuf/timestamp.proto\x1a\x19io/common/protocols.proto\x1a\x18io/common/template.proto\"\xc3\x01\n\x07Project\x12\"\n\x08protocol\x18\x01 \x01(\x0e\x32\x10.io.PassProtocol\x12\x0f\n\x07\x63lassId\x18\x02 \x01(\t\x12\x0c\n\x04name\x18\x03 \x01(\t\x12\x11\n\tshortCode\x18\x04 \x01(\t\x12+\n\x07\x63reated\x18\x05 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x0e\n\x06secret\x18\x06 \x01(\t\x12\x0b\n\x03key\x18\x07 \x01(\t\x12\x18\n\x10\x65ncryptedClassId\x18\t \x01(\t\"\\\n\x18ProjectByShortCodeResult\x12\x1c\n\x07project\x18\x01 \x01(\x0b\x32\x0b.io.Project\x12\"\n\x08template\x18\x02 \x01(\x0b\x32\x10.io.PassTemplate\"8\n\x13ProjectStatusFilter\x12!\n\x06status\x18\x01 \x01(\x0e\x32\x11.io.ProjectStatus*\xe4\x01\n\rProjectStatus\x12\x15\n\x11NO_PROJECT_STATUS\x10\x00\x12&\n\"PROJECT_ACTIVE_FOR_OBJECT_CREATION\x10\x01\x12(\n$PROJECT_DISABLED_FOR_OBJECT_CREATION\x10\x02\x12\x11\n\rPROJECT_DRAFT\x10\x04\x12\x15\n\x11PROJECT_PUBLISHED\x10\x08\x12\x13\n\x0fPROJECT_PRIVATE\x10\x10\x12\x16\n\x12PROJECT_OVER_QUOTA\x10 \x12\x13\n\x0fPROJECT_DELETED\x10@BG\n\x10\x63om.passkit.grpcZ$stash.passkit.com/io/model/sdk/go/io\xaa\x02\x0cPassKit.Grpcb\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'io.common.project_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\020com.passkit.grpcZ$stash.passkit.com/io/model/sdk/go/io\252\002\014PassKit.Grpc'
  _PROJECTSTATUS._serialized_start=468
  _PROJECTSTATUS._serialized_end=696
  _PROJECT._serialized_start=118
  _PROJECT._serialized_end=313
  _PROJECTBYSHORTCODERESULT._serialized_start=315
  _PROJECTBYSHORTCODERESULT._serialized_end=407
  _PROJECTSTATUSFILTER._serialized_start=409
  _PROJECTSTATUSFILTER._serialized_end=465
# @@protoc_insertion_point(module_scope)
