# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: io/flights/airport.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from io.common import localization_pb2 as io_dot_common_dot_localization__pb2
from protoc_gen_openapiv2.options import annotations_pb2 as protoc__gen__openapiv2_dot_options_dot_annotations__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x18io/flights/airport.proto\x12\x07\x66lights\x1a\x1cio/common/localization.proto\x1a.protoc-gen-openapiv2/options/annotations.proto\"\xa8\x03\n\x04Port\x12\x1e\n\x0fiataAirportCode\x18\x01 \x01(\tB\x05\x92\x41\x02x\x03\x12\x1e\n\x0ficaoAirportCode\x18\x02 \x01(\tB\x05\x92\x41\x02x\x04\x12\x10\n\x08\x63ityName\x18\x03 \x01(\t\x12.\n\x11localizedCityName\x18\x04 \x01(\x0b\x32\x13.io.LocalizedString\x12\x13\n\x0b\x61irportName\x18\x05 \x01(\t\x12\x31\n\x14localizedAirportName\x18\x06 \x01(\x0b\x32\x13.io.LocalizedString\x12\x13\n\x0b\x63ountryCode\x18\x07 \x01(\t\x12\x10\n\x08timezone\x18\x08 \x01(\t:\xae\x01\x92\x41\xaa\x01\n\xa7\x01*\x0e\x41irport Record2QAirport records are required for each port that a carrier operates in and out of.\xd2\x01\x0fiataAirportCode\xd2\x01\x08\x63ityName\xd2\x01\x0b\x61irportName\xd2\x01\x0b\x63ountryCode\xd2\x01\x08timezone\"\"\n\x0b\x41irportCode\x12\x13\n\x0b\x61irportCode\x18\x01 \x01(\tB_\n\x18\x63om.passkit.grpc.FlightsZ,stash.passkit.com/io/model/sdk/go/io/flights\xaa\x02\x14PassKit.Grpc.Flightsb\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'io.flights.airport_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\030com.passkit.grpc.FlightsZ,stash.passkit.com/io/model/sdk/go/io/flights\252\002\024PassKit.Grpc.Flights'
  _PORT.fields_by_name['iataAirportCode']._options = None
  _PORT.fields_by_name['iataAirportCode']._serialized_options = b'\222A\002x\003'
  _PORT.fields_by_name['icaoAirportCode']._options = None
  _PORT.fields_by_name['icaoAirportCode']._serialized_options = b'\222A\002x\004'
  _PORT._options = None
  _PORT._serialized_options = b'\222A\252\001\n\247\001*\016Airport Record2QAirport records are required for each port that a carrier operates in and out of.\322\001\017iataAirportCode\322\001\010cityName\322\001\013airportName\322\001\013countryCode\322\001\010timezone'
  _PORT._serialized_start=116
  _PORT._serialized_end=540
  _AIRPORTCODE._serialized_start=542
  _AIRPORTCODE._serialized_end=576
# @@protoc_insertion_point(module_scope)
