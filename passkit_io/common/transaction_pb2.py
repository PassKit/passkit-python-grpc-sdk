# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: passkit/io/common/transaction.proto
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
    'passkit/io/common/transaction.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from protoc_gen_openapiv2.options import annotations_pb2 as protoc__gen__openapiv2_dot_options_dot_annotations__pb2
from passkit.io.common import common_objects_pb2 as passkit_dot_io_dot_common_dot_common__objects__pb2
from passkit.io.common import proximity_pb2 as passkit_dot_io_dot_common_dot_proximity__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n#passkit/io/common/transaction.proto\x12\x02io\x1a.protoc-gen-openapiv2/options/annotations.proto\x1a&passkit/io/common/common_objects.proto\x1a!passkit/io/common/proximity.proto\"\x94\x04\n\x0bTransaction\x12\x13\n\x0breferenceId\x18\x01 \x01(\t\x12\x12\n\ntotalPrice\x18\x02 \x01(\x02\x12!\n\norderItems\x18\x03 \x03(\x0b\x32\r.io.OrderItem\x12\x10\n\x08\x64iscount\x18\x04 \x01(\x02\x12\'\n\rdiscountItems\x18\x05 \x03(\x0b\x32\x10.io.DiscountItem\x12\x15\n\rserviceCharge\x18\x06 \x01(\x02\x12\x10\n\x08totalTax\x18\x07 \x01(\x02\x12\x12\n\nfinalPrice\x18\x08 \x01(\x02\x12\x1a\n\x12roundingDifference\x18\t \x01(\x02\x12\x12\n\nisRefunded\x18\n \x01(\x08\x12\x1b\n\ttimestamp\x18\x0b \x01(\x0b\x32\x08.io.Date\x12\x10\n\x08\x63urrency\x18\x0c \x01(\t\x12!\n\x08location\x18\r \x01(\x0b\x32\x0f.io.GPSLocation\x12\x19\n\x11transactionSource\x18\x0e \x01(\t:\xa3\x01\x92\x41\x9f\x01\n\x9c\x01*\x0bTransaction2mTransaction information for member programs that want to show latest transactions on back of the member card.\xd2\x01\ttimestamp\xd2\x01\x06\x61mount\xd2\x01\x08\x63urrency\"a\n\x0c\x44iscountItem\x12\x14\n\x0c\x64iscountCode\x18\x01 \x01(\t\x12\x13\n\x0bvoucherCode\x18\x02 \x01(\t\x12\x0e\n\x06\x61mount\x18\x04 \x01(\x02\x12\x10\n\x08itemName\x18\x05 \x01(\tJ\x04\x08\x03\x10\x04\"Y\n\tOrderItem\x12\x0e\n\x06\x61mount\x18\x01 \x01(\x02\x12\x0b\n\x03tax\x18\x02 \x01(\x02\x12\x10\n\x08itemName\x18\x03 \x01(\t\x12\x10\n\x08quantity\x18\x04 \x01(\x05\x12\x0b\n\x03sku\x18\x05 \x01(\tBG\n\x10\x63om.passkit.grpcZ$stash.passkit.com/io/model/sdk/go/io\xaa\x02\x0cPassKit.Grpcb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'passkit.io.common.transaction_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n\020com.passkit.grpcZ$stash.passkit.com/io/model/sdk/go/io\252\002\014PassKit.Grpc'
  _globals['_TRANSACTION']._loaded_options = None
  _globals['_TRANSACTION']._serialized_options = b'\222A\237\001\n\234\001*\013Transaction2mTransaction information for member programs that want to show latest transactions on back of the member card.\322\001\ttimestamp\322\001\006amount\322\001\010currency'
  _globals['_TRANSACTION']._serialized_start=167
  _globals['_TRANSACTION']._serialized_end=699
  _globals['_DISCOUNTITEM']._serialized_start=701
  _globals['_DISCOUNTITEM']._serialized_end=798
  _globals['_ORDERITEM']._serialized_start=800
  _globals['_ORDERITEM']._serialized_end=889
# @@protoc_insertion_point(module_scope)
