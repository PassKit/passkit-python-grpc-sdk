# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: passkit/io/flights/passenger.proto
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
    'passkit/io/flights/passenger.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from passkit.io.flights import barcode_pb2 as passkit_dot_io_dot_flights_dot_barcode__pb2
from passkit.io.common import common_objects_pb2 as passkit_dot_io_dot_common_dot_common__objects__pb2
from passkit.io.common import personal_pb2 as passkit_dot_io_dot_common_dot_personal__pb2
from protoc_gen_openapiv2.options import annotations_pb2 as protoc__gen__openapiv2_dot_options_dot_annotations__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\"passkit/io/flights/passenger.proto\x12\x07\x66lights\x1a passkit/io/flights/barcode.proto\x1a&passkit/io/common/common_objects.proto\x1a passkit/io/common/personal.proto\x1a.protoc-gen-openapiv2/options/annotations.proto\"\xc9\x04\n\tPassenger\x12$\n\x10passengerDetails\x18\x01 \x01(\x0b\x32\n.io.Person\x12\x35\n\x11\x66requentFlyerInfo\x18\x02 \x01(\x0b\x32\x1a.flights.FrequentFlyerInfo\x12\x31\n\x0fidentityDetails\x18\x03 \x01(\x0b\x32\x18.flights.IdentityDetails\x12\x12\n\nwithInfant\x18\x04 \x01(\x08\x12&\n\rinfantDetails\x18\x05 \x01(\x0b\x32\x0f.flights.Infant\x12\x1b\n\x13knownTravelerNumber\x18\x07 \x01(\t:\xd2\x02\x92\x41\xce\x02\n\xcb\x02*\tPassenger2\xaa\x02Passenger information can optionally be provided. All fields are optional with the exception of the Passenger name to be rendered on the boarding pass. All passenger is treated as PII and encrypted at rest. Passenger information is deleted or rendered unusable once the pass record has invalidated.\xd2\x01\x10passengerDetails\"a\n\x11\x46requentFlyerInfo\x12\x13\n\x0bprogramName\x18\x01 \x01(\t\x12\x19\n\x11\x61irlineDesignator\x18\x02 \x01(\t\x12\x0e\n\x06number\x18\x03 \x01(\t\x12\x0c\n\x04tier\x18\x04 \x01(\t\"\x82\x02\n\x0fIdentityDetails\x12\x33\n\x10identityDocument\x18\x01 \x01(\x0e\x32\x19.flights.IdentityDocument\x12\x16\n\x0eissuingCountry\x18\x02 \x01(\t\x12\x13\n\x0bnationality\x18\x03 \x01(\t\x12\x16\n\x0e\x64ocumentNumber\x18\x04 \x01(\t\x12\x1d\n\x0b\x64\x61teOfBirth\x18\x05 \x01(\x0b\x32\x08.io.Date\x12\x1a\n\x06gender\x18\x06 \x01(\x0e\x32\n.io.Gender\x12\x1c\n\nissuedDate\x18\x07 \x01(\x0b\x32\x08.io.Date\x12\x1c\n\nexpiryDate\x18\x08 \x01(\x0b\x32\x08.io.Date\"\x92\x03\n\x06Infant\x12!\n\rinfantDetails\x18\x01 \x01(\x0b\x32\n.io.Person\x12\x31\n\x0fidentityDetails\x18\x02 \x01(\x0b\x32\x18.flights.IdentityDetails\x12\x16\n\x0e\x62\x61rcodePayload\x18\x03 \x01(\t\x12\x33\n\x10\x63onditionalItems\x18\x04 \x01(\x0b\x32\x19.flights.ConditionalItems\x12\x1d\n\x15\x62\x61rcodeAdditionalData\x18\x05 \x01(\t\x12\x15\n\rsecurityImage\x18\x06 \x01(\t\x12\x16\n\x0eprivilegeImage\x18\x07 \x01(\t\x12\x13\n\x0b\x66ooterImage\x18\x08 \x01(\t\x12\x10\n\x08ssrCodes\x18\t \x03(\t\x12\x34\n\x0c\x63\x61pabilities\x18\n \x03(\x0e\x32\x1e.flights.PassengerCapabilities\x12:\n\x10securityPrograms\x18\x0b \x03(\x0e\x32 .flights.AirportSecurityPrograms*\x90\x01\n\x10IdentityDocument\x12\x0c\n\x08PASSPORT\x10\x00\x12\x14\n\x10NATIONAL_ID_CARD\x10\x01\x12\x13\n\x0f\x44RIVING_LICENSE\x10\x02\x12\x0f\n\x0b\x43REDIT_CARD\x10\x03\x12\x17\n\x13\x46REQUENT_FLYER_CARD\x10\x04\x12\x19\n\x15OTHER_TRAVEL_DOCUMENT\x10\x05\x42_\n\x18\x63om.passkit.grpc.FlightsZ,stash.passkit.com/io/model/sdk/go/io/flights\xaa\x02\x14PassKit.Grpc.Flightsb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'passkit.io.flights.passenger_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n\030com.passkit.grpc.FlightsZ,stash.passkit.com/io/model/sdk/go/io/flights\252\002\024PassKit.Grpc.Flights'
  _globals['_PASSENGER']._loaded_options = None
  _globals['_PASSENGER']._serialized_options = b'\222A\316\002\n\313\002*\tPassenger2\252\002Passenger information can optionally be provided. All fields are optional with the exception of the Passenger name to be rendered on the boarding pass. All passenger is treated as PII and encrypted at rest. Passenger information is deleted or rendered unusable once the pass record has invalidated.\322\001\020passengerDetails'
  _globals['_IDENTITYDOCUMENT']._serialized_start=1557
  _globals['_IDENTITYDOCUMENT']._serialized_end=1701
  _globals['_PASSENGER']._serialized_start=204
  _globals['_PASSENGER']._serialized_end=789
  _globals['_FREQUENTFLYERINFO']._serialized_start=791
  _globals['_FREQUENTFLYERINFO']._serialized_end=888
  _globals['_IDENTITYDETAILS']._serialized_start=891
  _globals['_IDENTITYDETAILS']._serialized_end=1149
  _globals['_INFANT']._serialized_start=1152
  _globals['_INFANT']._serialized_end=1554
# @@protoc_insertion_point(module_scope)
