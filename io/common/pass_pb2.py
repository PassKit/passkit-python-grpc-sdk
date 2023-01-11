# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: io/common/pass.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from io.image import image_pb2 as io_dot_image_dot_image__pb2
from io.common import links_pb2 as io_dot_common_dot_links__pb2
from io.common import metrics_pb2 as io_dot_common_dot_metrics__pb2
from io.common import personal_pb2 as io_dot_common_dot_personal__pb2
from io.common import protocols_pb2 as io_dot_common_dot_protocols__pb2
from io.common import proximity_pb2 as io_dot_common_dot_proximity__pb2
from io.common import template_pb2 as io_dot_common_dot_template__pb2
from protoc_gen_openapiv2.options import annotations_pb2 as protoc__gen__openapiv2_dot_options_dot_annotations__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x14io/common/pass.proto\x12\x02io\x1a\x14io/image/image.proto\x1a\x15io/common/links.proto\x1a\x17io/common/metrics.proto\x1a\x18io/common/personal.proto\x1a\x19io/common/protocols.proto\x1a\x19io/common/proximity.proto\x1a\x18io/common/template.proto\x1a.protoc-gen-openapiv2/options/annotations.proto\"\xe7\x01\n\rPassOverrides\x12\x1e\n\x08imageIds\x18\x01 \x01(\x0b\x32\x0c.io.ImageIds\x12*\n\tlocations\x18\x03 \x03(\x0b\x32\x0f.io.GPSLocationB\x06\x92\x41\x03\xa0\x01\n\x12#\n\x07\x62\x65\x61\x63ons\x18\x04 \x03(\x0b\x32\n.io.BeaconB\x06\x92\x41\x03\xa0\x01\n\x12\x1f\n\x05links\x18\x05 \x03(\x0b\x32\x08.io.LinkB\x06\x92\x41\x03\xa0\x01\n\x12\x1a\n\x06\x63olors\x18\x06 \x01(\x0b\x32\n.io.Colors\x12\"\n\x1a\x61ssociatedStoreIdentifiers\x18\x07 \x03(\rJ\x04\x08\x02\x10\x03\"\\\n\x0bPassOptions\x12&\n\x05\x61pple\x18\x01 \x01(\x0b\x32\x17.io.AppleWalletSettings\x12%\n\x06google\x18\x02 \x01(\x0b\x32\x15.io.GooglePaySettings\"\xff\x01\n\x04Pass\x12\n\n\x02id\x18\x01 \x01(\t\x12\x0f\n\x07\x63lassId\x18\x02 \x01(\t\x12\"\n\x08protocol\x18\x03 \x01(\x0e\x32\x10.io.PassProtocol\x12!\n\rpersonDetails\x18\x04 \x01(\x0b\x32\n.io.Person\x12\x1e\n\x08metadata\x18\x05 \x01(\x0b\x32\x0c.io.Metadata\x12,\n\nrecordData\x18\x06 \x03(\x0b\x32\x18.io.Pass.RecordDataEntry\x12\x12\n\nexternalId\x18\x07 \x01(\t\x1a\x31\n\x0fRecordDataEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\x42G\n\x10\x63om.passkit.grpcZ$stash.passkit.com/io/model/sdk/go/io\xaa\x02\x0cPassKit.Grpcb\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'io.common.pass_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\020com.passkit.grpcZ$stash.passkit.com/io/model/sdk/go/io\252\002\014PassKit.Grpc'
  _PASSOVERRIDES.fields_by_name['locations']._options = None
  _PASSOVERRIDES.fields_by_name['locations']._serialized_options = b'\222A\003\240\001\n'
  _PASSOVERRIDES.fields_by_name['beacons']._options = None
  _PASSOVERRIDES.fields_by_name['beacons']._serialized_options = b'\222A\003\240\001\n'
  _PASSOVERRIDES.fields_by_name['links']._options = None
  _PASSOVERRIDES.fields_by_name['links']._serialized_options = b'\222A\003\240\001\n'
  _PASS_RECORDDATAENTRY._options = None
  _PASS_RECORDDATAENTRY._serialized_options = b'8\001'
  _PASSOVERRIDES._serialized_start=253
  _PASSOVERRIDES._serialized_end=484
  _PASSOPTIONS._serialized_start=486
  _PASSOPTIONS._serialized_end=578
  _PASS._serialized_start=581
  _PASS._serialized_end=836
  _PASS_RECORDDATAENTRY._serialized_start=787
  _PASS_RECORDDATAENTRY._serialized_end=836
# @@protoc_insertion_point(module_scope)
