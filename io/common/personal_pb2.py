# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: io/common/personal.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from io.common import common_objects_pb2 as io_dot_common_dot_common__objects__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x18io/common/personal.proto\x12\x02io\x1a\x1eio/common/common_objects.proto\"\xd9\x02\n\x06Person\x12\x0f\n\x07surname\x18\x01 \x01(\t\x12\x10\n\x08\x66orename\x18\x02 \x01(\t\x12\x12\n\notherNames\x18\x03 \x03(\t\x12\x12\n\nsalutation\x18\x04 \x01(\t\x12\x0e\n\x06suffix\x18\x05 \x01(\t\x12\x13\n\x0b\x64isplayName\x18\x06 \x01(\t\x12\x1a\n\x06gender\x18\x07 \x01(\x0e\x32\n.io.Gender\x12\x1d\n\x0b\x64\x61teOfBirth\x18\x08 \x01(\x0b\x32\x08.io.Date\x12\x14\n\x0c\x65mailAddress\x18\t \x01(\t\x12\x14\n\x0cmobileNumber\x18\n \x01(\t\x12\x12\n\nexternalId\x18\x0b \x01(\t\x12\x30\n\x0b\x65xternalIds\x18\x0c \x03(\x0b\x32\x1b.io.Person.ExternalIdsEntry\x1a\x32\n\x10\x45xternalIdsEntry\x12\x0b\n\x03key\x18\x01 \x01(\x05\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\"\x8e\x01\n\x07\x41\x64\x64ress\x12\x14\n\x0c\x61\x64\x64ressLine1\x18\x01 \x01(\t\x12\x14\n\x0c\x61\x64\x64ressLine2\x18\x02 \x01(\t\x12\x14\n\x0c\x61\x64\x64ressLine3\x18\x03 \x01(\t\x12\x0c\n\x04\x63ity\x18\x04 \x01(\t\x12\r\n\x05state\x18\x05 \x01(\t\x12\x0f\n\x07zipCode\x18\x06 \x01(\t\x12\x13\n\x0b\x63ountryCode\x18\x07 \x01(\t\"\\\n\rPersonRequest\x12\n\n\x02id\x18\x01 \x01(\t\x12\x12\n\nexternalId\x18\x02 \x01(\t\x12\x0f\n\x07\x63lassId\x18\x03 \x01(\t\x12\x1a\n\x06person\x18\x04 \x01(\x0b\x32\n.io.Person*-\n\x06Gender\x12\r\n\tNOT_KNOWN\x10\x00\x12\x08\n\x04MALE\x10\x01\x12\n\n\x06\x46\x45MALE\x10\x02\x42G\n\x10\x63om.passkit.grpcZ$stash.passkit.com/io/model/sdk/go/io\xaa\x02\x0cPassKit.Grpcb\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'io.common.personal_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\020com.passkit.grpcZ$stash.passkit.com/io/model/sdk/go/io\252\002\014PassKit.Grpc'
  _PERSON_EXTERNALIDSENTRY._options = None
  _PERSON_EXTERNALIDSENTRY._serialized_options = b'8\001'
  _GENDER._serialized_start=651
  _GENDER._serialized_end=696
  _PERSON._serialized_start=65
  _PERSON._serialized_end=410
  _PERSON_EXTERNALIDSENTRY._serialized_start=360
  _PERSON_EXTERNALIDSENTRY._serialized_end=410
  _ADDRESS._serialized_start=413
  _ADDRESS._serialized_end=555
  _PERSONREQUEST._serialized_start=557
  _PERSONREQUEST._serialized_end=649
# @@protoc_insertion_point(module_scope)