# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: io/common/filter.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from protoc_gen_openapiv2.options import annotations_pb2 as protoc__gen__openapiv2_dot_options_dot_annotations__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x16io/common/filter.proto\x12\x02io\x1a.protoc-gen-openapiv2/options/annotations.proto\"\xce\x01\n\x07\x46ilters\x12\r\n\x05limit\x18\x01 \x01(\x05\x12\x0e\n\x06offset\x18\x02 \x01(\x05\x12%\n\x0c\x66ilterGroups\x18\x03 \x03(\x0b\x32\x0f.io.FilterGroup\x12\x0f\n\x07orderBy\x18\x04 \x01(\t\x12\x10\n\x08orderAsc\x18\x05 \x01(\x08:Z\x92\x41W\nU*\nPagination2GFilters applies multiple filter conditions to retrieve matched records.\"O\n\x0b\x46ieldFilter\x12\x13\n\x0b\x66ilterField\x18\x01 \x01(\t\x12\x13\n\x0b\x66ilterValue\x18\x02 \x01(\t\x12\x16\n\x0e\x66ilterOperator\x18\x03 \x01(\t\"U\n\x0b\x46ilterGroup\x12\x1f\n\tcondition\x18\x01 \x01(\x0e\x32\x0c.io.Operator\x12%\n\x0c\x66ieldFilters\x18\x02 \x03(\x0b\x32\x0f.io.FieldFilter*\x1b\n\x08Operator\x12\x07\n\x03\x41ND\x10\x00\x12\x06\n\x02OR\x10\x01\x42G\n\x10\x63om.passkit.grpcZ$stash.passkit.com/io/model/sdk/go/io\xaa\x02\x0cPassKit.Grpcb\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'io.common.filter_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\020com.passkit.grpcZ$stash.passkit.com/io/model/sdk/go/io\252\002\014PassKit.Grpc'
  _FILTERS._options = None
  _FILTERS._serialized_options = b'\222AW\nU*\nPagination2GFilters applies multiple filter conditions to retrieve matched records.'
  _OPERATOR._serialized_start=455
  _OPERATOR._serialized_end=482
  _FILTERS._serialized_start=79
  _FILTERS._serialized_end=285
  _FIELDFILTER._serialized_start=287
  _FIELDFILTER._serialized_end=366
  _FILTERGROUP._serialized_start=368
  _FILTERGROUP._serialized_end=453
# @@protoc_insertion_point(module_scope)
