# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: io/flights/flight.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from io.common import common_objects_pb2 as io_dot_common_dot_common__objects__pb2
from io.common import proximity_pb2 as io_dot_common_dot_proximity__pb2
from io.common import links_pb2 as io_dot_common_dot_links__pb2
from io.common import metrics_pb2 as io_dot_common_dot_metrics__pb2
from io.flights import flight_designator_pb2 as io_dot_flights_dot_flight__designator__pb2
from protoc_gen_openapiv2.options import annotations_pb2 as protoc__gen__openapiv2_dot_options_dot_annotations__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x17io/flights/flight.proto\x12\x07\x66lights\x1a\x1eio/common/common_objects.proto\x1a\x19io/common/proximity.proto\x1a\x15io/common/links.proto\x1a\x17io/common/metrics.proto\x1a\"io/flights/flight_designator.proto\x1a.protoc-gen-openapiv2/options/annotations.proto\"\xec\x0b\n\x06\x46light\x12\x1d\n\x0b\x63\x61rrierCode\x18\x01 \x01(\tB\x08\x92\x41\x05x\x03\x80\x01\x02\x12\x1b\n\x0c\x66lightNumber\x18\x02 \x01(\tB\x05\x92\x41\x02x\x05\x12\x1c\n\rboardingPoint\x18\x03 \x01(\tB\x05\x92\x41\x02x\x03\x12\x1d\n\x0e\x64\x65planingPoint\x18\x04 \x01(\tB\x05\x92\x41\x02x\x03\x12\x1f\n\rdepartureDate\x18\x05 \x01(\x0b\x32\x08.io.Date\x12\x19\n\x11\x64\x65partureTerminal\x18\x06 \x01(\t\x12\x17\n\x0f\x61rrivalTerminal\x18\x07 \x01(\t\x12\x15\n\rdepartureGate\x18\x08 \x01(\t\x12\x13\n\x0b\x61rrivalGate\x18\t \x01(\t\x12\x31\n\x16scheduledDepartureTime\x18\n \x01(\x0b\x32\x11.io.LocalDateTime\x12\x31\n\x16\x65stimatedDepartureTime\x18\x0b \x01(\x0b\x32\x11.io.LocalDateTime\x12\'\n\x0c\x62oardingTime\x18\x0c \x01(\x0b\x32\x11.io.LocalDateTime\x12*\n\x0fgateClosingTime\x18\r \x01(\x0b\x32\x11.io.LocalDateTime\x12/\n\x14scheduledArrivalTime\x18\x0e \x01(\x0b\x32\x11.io.LocalDateTime\x12/\n\x14\x65stimatedArrivalTime\x18\x0f \x01(\x0b\x32\x11.io.LocalDateTime\x12&\n\x14operatingCarrierCode\x18\x10 \x01(\tB\x08\x92\x41\x05x\x03\x80\x01\x02\x12$\n\x15operatingFlightNumber\x18\x11 \x01(\tB\x05\x92\x41\x02x\x05\x12\x1e\n\x16\x63odeShareFlightNumbers\x18\x12 \x03(\t\x12\x16\n\x0epassTemplateId\x18\x13 \x01(\t\x12\x13\n\x0b\x62\x61ggageBelt\x18\x15 \x01(\t\x12&\n\x13\x61utoInvalidateAfter\x18\x16 \x01(\rB\t\x92\x41\x06:\x04\x32\x38\x38\x30\x12)\n\x1d\x61utoInvalidateCancelledPasses\x18\x17 \x01(\x08\x42\x02\x18\x01\x12\x31\n\x10locationMessages\x18\x18 \x03(\x0b\x32\x0f.io.GPSLocationB\x06\x92\x41\x03\xa0\x01\n\x12*\n\x0e\x62\x65\x61\x63onMessages\x18\x19 \x03(\x0b\x32\n.io.BeaconB\x06\x92\x41\x03\xa0\x01\n\x12\x1f\n\x05links\x18\x1a \x03(\x0b\x32\x08.io.LinkB\x06\x92\x41\x03\xa0\x01\n\x12\x1f\n\x17suspendAutomaticUpdates\x18\x1b \x01(\x08\x12/\n\x0e\x62oardingPolicy\x18\x1c \x01(\x0e\x32\x17.flights.BoardingPolicy\x12/\n\rseatingPolicy\x18\x1d \x01(\x0e\x32\x18.flights.SeatClassPolicy\x12%\n\x06status\x18\x1e \x01(\x0e\x32\x15.flights.FlightStatus\x12\x18\n\x10\x43onditionalItems\x18\x1f \x01(\x08\x12\x1d\n\x15\x42\x61rcodeAdditionalData\x18  \x01(\t\x12\x1c\n\x07metrics\x18! \x01(\x0b\x32\x0b.io.Metrics\x12/\n\x0c\x63reateMethod\x18\" \x01(\x0e\x32\x19.flights.FlightCreateMode\x12\x14\n\x0c\x64\x65signatorId\x18# \x01(\t\x12\x36\n\x19invalidateCancelledPasses\x18$ \x01(\x0e\x32\n.io.ToggleB\x07\x92\x41\x04:\x02ON:\xdc\x01\x92\x41\xd8\x01\n\xd5\x01*\x06\x46light2SA flight record describes data that is relevant to a single flight on a given date.\xd2\x01\x0b\x63\x61rrierCode\xd2\x01\x0c\x66lightNumber\xd2\x01\rboardingPoint\xd2\x01\x0e\x64\x65planingPoint\xd2\x01\x16scheduledDepartureTime\xd2\x01\x0epassTemplateId\xd2\x01\rdepartureDate\"\x9b\x01\n\rFlightRequest\x12\x1d\n\x0b\x63\x61rrierCode\x18\x01 \x01(\tB\x08\x92\x41\x05x\x03\x80\x01\x02\x12\x1b\n\x0c\x66lightNumber\x18\x02 \x01(\tB\x05\x92\x41\x02x\x05\x12\x1f\n\rdepartureDate\x18\x03 \x01(\x0b\x32\x08.io.Date\x12\x15\n\rboardingPoint\x18\x05 \x01(\t\x12\x16\n\x0e\x64\x65planingPoint\x18\x06 \x01(\t*\xfa\x01\n\x0c\x46lightStatus\x12\x0b\n\x07UNKNOWN\x10\x00\x12\r\n\tSCHEDULED\x10\x01\x12\x0c\n\x08\x44\x45PARTED\x10\x02\x12\t\n\x05INAIR\x10\x03\x12\n\n\x06LANDED\x10\x04\x12\x0b\n\x07\x41RRIVED\x10\x05\x12\r\n\tCANCELLED\x10\x06\x12\x0b\n\x07\x44\x45LAYED\x10\x07\x12\x15\n\x11\x44\x45PARTED_DIVERTED\x10\x08\x12\x12\n\x0eINAIR_DIVERTED\x10\t\x12\x14\n\x10\x41RRIVED_DIVERTED\x10\n\x12\x15\n\x11\x44\x45PARTED_RECOVERY\x10\x0b\x12\x12\n\x0eINAIR_RECOVERY\x10\x0c\x12\x14\n\x10\x41RRIVED_RECOVERY\x10\r*=\n\x10\x46lightCreateMode\x12\x0e\n\nDO_NOT_USE\x10\x00\x12\n\n\x06MANUAL\x10\x01\x12\r\n\tAUTOMATIC\x10\x02\x42_\n\x18\x63om.passkit.grpc.FlightsZ,stash.passkit.com/io/model/sdk/go/io/flights\xaa\x02\x14PassKit.Grpc.Flightsb\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'io.flights.flight_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\030com.passkit.grpc.FlightsZ,stash.passkit.com/io/model/sdk/go/io/flights\252\002\024PassKit.Grpc.Flights'
  _FLIGHT.fields_by_name['carrierCode']._options = None
  _FLIGHT.fields_by_name['carrierCode']._serialized_options = b'\222A\005x\003\200\001\002'
  _FLIGHT.fields_by_name['flightNumber']._options = None
  _FLIGHT.fields_by_name['flightNumber']._serialized_options = b'\222A\002x\005'
  _FLIGHT.fields_by_name['boardingPoint']._options = None
  _FLIGHT.fields_by_name['boardingPoint']._serialized_options = b'\222A\002x\003'
  _FLIGHT.fields_by_name['deplaningPoint']._options = None
  _FLIGHT.fields_by_name['deplaningPoint']._serialized_options = b'\222A\002x\003'
  _FLIGHT.fields_by_name['operatingCarrierCode']._options = None
  _FLIGHT.fields_by_name['operatingCarrierCode']._serialized_options = b'\222A\005x\003\200\001\002'
  _FLIGHT.fields_by_name['operatingFlightNumber']._options = None
  _FLIGHT.fields_by_name['operatingFlightNumber']._serialized_options = b'\222A\002x\005'
  _FLIGHT.fields_by_name['autoInvalidateAfter']._options = None
  _FLIGHT.fields_by_name['autoInvalidateAfter']._serialized_options = b'\222A\006:\0042880'
  _FLIGHT.fields_by_name['autoInvalidateCancelledPasses']._options = None
  _FLIGHT.fields_by_name['autoInvalidateCancelledPasses']._serialized_options = b'\030\001'
  _FLIGHT.fields_by_name['locationMessages']._options = None
  _FLIGHT.fields_by_name['locationMessages']._serialized_options = b'\222A\003\240\001\n'
  _FLIGHT.fields_by_name['beaconMessages']._options = None
  _FLIGHT.fields_by_name['beaconMessages']._serialized_options = b'\222A\003\240\001\n'
  _FLIGHT.fields_by_name['links']._options = None
  _FLIGHT.fields_by_name['links']._serialized_options = b'\222A\003\240\001\n'
  _FLIGHT.fields_by_name['invalidateCancelledPasses']._options = None
  _FLIGHT.fields_by_name['invalidateCancelledPasses']._serialized_options = b'\222A\004:\002ON'
  _FLIGHT._options = None
  _FLIGHT._serialized_options = b'\222A\330\001\n\325\001*\006Flight2SA flight record describes data that is relevant to a single flight on a given date.\322\001\013carrierCode\322\001\014flightNumber\322\001\rboardingPoint\322\001\016deplaningPoint\322\001\026scheduledDepartureTime\322\001\016passTemplateId\322\001\rdepartureDate'
  _FLIGHTREQUEST.fields_by_name['carrierCode']._options = None
  _FLIGHTREQUEST.fields_by_name['carrierCode']._serialized_options = b'\222A\005x\003\200\001\002'
  _FLIGHTREQUEST.fields_by_name['flightNumber']._options = None
  _FLIGHTREQUEST.fields_by_name['flightNumber']._serialized_options = b'\222A\002x\005'
  _FLIGHTSTATUS._serialized_start=1905
  _FLIGHTSTATUS._serialized_end=2155
  _FLIGHTCREATEMODE._serialized_start=2157
  _FLIGHTCREATEMODE._serialized_end=2218
  _FLIGHT._serialized_start=228
  _FLIGHT._serialized_end=1744
  _FLIGHTREQUEST._serialized_start=1747
  _FLIGHTREQUEST._serialized_end=1902
# @@protoc_insertion_point(module_scope)
