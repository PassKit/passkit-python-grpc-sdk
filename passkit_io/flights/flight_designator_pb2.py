# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: io/flights/flight_designator.proto
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
    'io/flights/flight_designator.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from passkit_io.common import common_objects_pb2 as io_dot_common_dot_common__objects__pb2
from passkit_io.common import proximity_pb2 as io_dot_common_dot_proximity__pb2
from passkit_io.common import links_pb2 as io_dot_common_dot_links__pb2
from protoc_gen_openapiv2.options import annotations_pb2 as protoc__gen__openapiv2_dot_options_dot_annotations__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\"io/flights/flight_designator.proto\x12\x07\x66lights\x1a\x1eio/common/common_objects.proto\x1a\x19io/common/proximity.proto\x1a\x15io/common/links.proto\x1a.protoc-gen-openapiv2/options/annotations.proto\"\x84\t\n\x10\x46lightDesignator\x12*\n\x0b\x63\x61rrierCode\x18\x01 \x01(\tB\x15\x92\x41\x12\x8a\x01\x0f^[A-Z0-9]{3,4}$\x12\x1b\n\x0c\x66lightNumber\x18\x02 \x01(\tB\x05\x92\x41\x02x\x05\x12\x1b\n\tvalidFrom\x18\x03 \x01(\x0b\x32\x08.io.Date\x12\x10\n\x08revision\x18\x04 \x01(\r\x12\x19\n\x06\x61\x63tive\x18\x05 \x01(\x08\x42\t\x92\x41\x06:\x04TRUE\x12)\n\x08schedule\x18\x06 \x01(\x0b\x32\x17.flights.FlightSchedule\x12&\n\x14operatingCarrierCode\x18\x07 \x01(\tB\x08\x92\x41\x05x\x03\x80\x01\x02\x12$\n\x15operatingFlightNumber\x18\x08 \x01(\tB\x05\x92\x41\x02x\x05\x12\x1e\n\x16\x63odeShareFlightNumbers\x18\t \x03(\t\x12\x0e\n\x06origin\x18\n \x01(\t\x12\x13\n\x0b\x64\x65stination\x18\x0b \x01(\t\x12\x15\n\rtransitPoints\x18\x0c \x03(\t\x12\x19\n\x11\x64\x65partureTerminal\x18\r \x01(\t\x12\x17\n\x0f\x61rrivalTerminal\x18\x0e \x01(\t\x12\x18\n\x10transitTerminals\x18\x0f \x03(\t\x12/\n\x0e\x62oardingPolicy\x18\x10 \x01(\x0e\x32\x17.flights.BoardingPolicy\x12\x31\n\x0fseatClassPolicy\x18\x11 \x01(\x0e\x32\x18.flights.SeatClassPolicy\x12%\n\x06\x61lerts\x18\x12 \x03(\x0e\x32\x15.flights.FlightAlerts\x12\x16\n\x0epassTemplateId\x18\x13 \x01(\t\x12&\n\x13\x61utoInvalidateAfter\x18\x14 \x01(\rB\t\x92\x41\x06:\x04\x32\x38\x38\x30\x12)\n\x1d\x61utoInvalidateCancelledPasses\x18\x15 \x01(\x08\x42\x02\x18\x01\x12\x31\n\x10locationMessages\x18\x16 \x03(\x0b\x32\x0f.io.GPSLocationB\x06\x92\x41\x03\xa0\x01\n\x12*\n\x0e\x62\x65\x61\x63onMessages\x18\x17 \x03(\x0b\x32\n.io.BeaconB\x06\x92\x41\x03\xa0\x01\n\x12\x1e\n\x0c\x64\x65\x66\x61ultLinks\x18\x18 \x03(\x0b\x32\x08.io.Link\x12\x18\n\x10\x43onditionalItems\x18\x19 \x01(\x08\x12\x1d\n\x15\x42\x61rcodeAdditionalData\x18\x1a \x01(\t\x12\x38\n\x19invalidateCancelledPasses\x18\x1b \x01(\x0e\x32\n.io.ToggleB\t\x92\x41\x06:\x04TRUE:\xd1\x01\x92\x41\xcd\x01\n\xca\x01*\x11\x46light Designator2ZA flight designator record describes mostly static data with regard to a flight operation.\xd2\x01\x0b\x63\x61rrierCode\xd2\x01\x0c\x66lightNumber\xd2\x01\x06origin\xd2\x01\x08schedule\xd2\x01\x08revision\xd2\x01\x0b\x64\x65stination\xd2\x01\x0epassTemplateId\"\xe6\x01\n\x17\x46lightDesignatorRequest\x12\x1d\n\x0b\x63\x61rrierCode\x18\x01 \x01(\tB\x08\x92\x41\x05x\x03\x80\x01\x02\x12\x1b\n\x0c\x66lightNumber\x18\x02 \x01(\tB\x05\x92\x41\x02x\x05\x12\x10\n\x08revision\x18\x03 \x01(\r:}\x92\x41z\nx*\x19\x46light Designator Request2>Used for retrieving details of a particular flight designator.\xd2\x01\x0b\x63\x61rrierCode\xd2\x01\x0c\x66lightNumber\"\xa2\x02\n\x0e\x46lightSchedule\x12$\n\x06monday\x18\x01 \x01(\x0b\x32\x14.flights.FlightTimes\x12%\n\x07tuesday\x18\x02 \x01(\x0b\x32\x14.flights.FlightTimes\x12\'\n\twednesday\x18\x03 \x01(\x0b\x32\x14.flights.FlightTimes\x12&\n\x08thursday\x18\x04 \x01(\x0b\x32\x14.flights.FlightTimes\x12$\n\x06\x66riday\x18\x05 \x01(\x0b\x32\x14.flights.FlightTimes\x12&\n\x08saturday\x18\x06 \x01(\x0b\x32\x14.flights.FlightTimes\x12$\n\x06sunday\x18\x07 \x01(\x0b\x32\x14.flights.FlightTimes\"\xa2\x01\n\x0b\x46lightTimes\x12(\n\x16scheduledDepartureTime\x18\x01 \x01(\x0b\x32\x08.io.Time\x12\x1e\n\x0c\x62oardingTime\x18\x02 \x01(\x0b\x32\x08.io.Time\x12!\n\x0fgateClosingTime\x18\x03 \x01(\x0b\x32\x08.io.Time\x12&\n\x14scheduledArrivalTime\x18\x04 \x01(\x0b\x32\x08.io.Time*\xa9\x01\n\x0c\x46lightAlerts\x12\r\n\tNO_ALERTS\x10\x00\x12\x0e\n\nALL_ALERTS\x10\x01\x12\x18\n\x14\x44\x45PARTURE_GATE_ALERT\x10\x02\x12\x18\n\x14\x44\x45PARTURE_TIME_ALERT\x10\x04\x12\x16\n\x12\x41RRIVAL_GATE_ALERT\x10\x08\x12\x16\n\x12\x41RRIVAL_TIME_ALERT\x10\x10\x12\x16\n\x12\x42\x41GGAGE_BELT_ALERT\x10 *m\n\x0e\x42oardingPolicy\x12\x1f\n\x1b\x42OARDING_POLICY_UNSPECIFIED\x10\x00\x12\x0e\n\nZONE_BASED\x10\x01\x12\x0f\n\x0bGROUP_BASED\x10\x02\x12\x19\n\x15\x42OARDING_POLICY_OTHER\x10\x03*\x83\x01\n\x0fSeatClassPolicy\x12!\n\x1dSEAT_CLASS_POLICY_UNSPECIFIED\x10\x00\x12\x0f\n\x0b\x43\x41\x42IN_BASED\x10\x01\x12\x0f\n\x0b\x43LASS_BASED\x10\x02\x12\x0e\n\nTIER_BASED\x10\x03\x12\x1b\n\x17SEAT_CLASS_POLICY_OTHER\x10\x04*\x1f\n\tAuthority\x12\x08\n\x04IATA\x10\x00\x12\x08\n\x04ICAO\x10\x01\x42_\n\x18\x63om.passkit.grpc.FlightsZ,stash.passkit.com/io/model/sdk/go/io/flights\xaa\x02\x14PassKit.Grpc.Flightsb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'io.flights.flight_designator_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n\030com.passkit.grpc.FlightsZ,stash.passkit.com/io/model/sdk/go/io/flights\252\002\024PassKit.Grpc.Flights'
  _globals['_FLIGHTDESIGNATOR'].fields_by_name['carrierCode']._loaded_options = None
  _globals['_FLIGHTDESIGNATOR'].fields_by_name['carrierCode']._serialized_options = b'\222A\022\212\001\017^[A-Z0-9]{3,4}$'
  _globals['_FLIGHTDESIGNATOR'].fields_by_name['flightNumber']._loaded_options = None
  _globals['_FLIGHTDESIGNATOR'].fields_by_name['flightNumber']._serialized_options = b'\222A\002x\005'
  _globals['_FLIGHTDESIGNATOR'].fields_by_name['active']._loaded_options = None
  _globals['_FLIGHTDESIGNATOR'].fields_by_name['active']._serialized_options = b'\222A\006:\004TRUE'
  _globals['_FLIGHTDESIGNATOR'].fields_by_name['operatingCarrierCode']._loaded_options = None
  _globals['_FLIGHTDESIGNATOR'].fields_by_name['operatingCarrierCode']._serialized_options = b'\222A\005x\003\200\001\002'
  _globals['_FLIGHTDESIGNATOR'].fields_by_name['operatingFlightNumber']._loaded_options = None
  _globals['_FLIGHTDESIGNATOR'].fields_by_name['operatingFlightNumber']._serialized_options = b'\222A\002x\005'
  _globals['_FLIGHTDESIGNATOR'].fields_by_name['autoInvalidateAfter']._loaded_options = None
  _globals['_FLIGHTDESIGNATOR'].fields_by_name['autoInvalidateAfter']._serialized_options = b'\222A\006:\0042880'
  _globals['_FLIGHTDESIGNATOR'].fields_by_name['autoInvalidateCancelledPasses']._loaded_options = None
  _globals['_FLIGHTDESIGNATOR'].fields_by_name['autoInvalidateCancelledPasses']._serialized_options = b'\030\001'
  _globals['_FLIGHTDESIGNATOR'].fields_by_name['locationMessages']._loaded_options = None
  _globals['_FLIGHTDESIGNATOR'].fields_by_name['locationMessages']._serialized_options = b'\222A\003\240\001\n'
  _globals['_FLIGHTDESIGNATOR'].fields_by_name['beaconMessages']._loaded_options = None
  _globals['_FLIGHTDESIGNATOR'].fields_by_name['beaconMessages']._serialized_options = b'\222A\003\240\001\n'
  _globals['_FLIGHTDESIGNATOR'].fields_by_name['invalidateCancelledPasses']._loaded_options = None
  _globals['_FLIGHTDESIGNATOR'].fields_by_name['invalidateCancelledPasses']._serialized_options = b'\222A\006:\004TRUE'
  _globals['_FLIGHTDESIGNATOR']._loaded_options = None
  _globals['_FLIGHTDESIGNATOR']._serialized_options = b'\222A\315\001\n\312\001*\021Flight Designator2ZA flight designator record describes mostly static data with regard to a flight operation.\322\001\013carrierCode\322\001\014flightNumber\322\001\006origin\322\001\010schedule\322\001\010revision\322\001\013destination\322\001\016passTemplateId'
  _globals['_FLIGHTDESIGNATORREQUEST'].fields_by_name['carrierCode']._loaded_options = None
  _globals['_FLIGHTDESIGNATORREQUEST'].fields_by_name['carrierCode']._serialized_options = b'\222A\005x\003\200\001\002'
  _globals['_FLIGHTDESIGNATORREQUEST'].fields_by_name['flightNumber']._loaded_options = None
  _globals['_FLIGHTDESIGNATORREQUEST'].fields_by_name['flightNumber']._serialized_options = b'\222A\002x\005'
  _globals['_FLIGHTDESIGNATORREQUEST']._loaded_options = None
  _globals['_FLIGHTDESIGNATORREQUEST']._serialized_options = b'\222Az\nx*\031Flight Designator Request2>Used for retrieving details of a particular flight designator.\322\001\013carrierCode\322\001\014flightNumber'
  _globals['_FLIGHTALERTS']._serialized_start=2028
  _globals['_FLIGHTALERTS']._serialized_end=2197
  _globals['_BOARDINGPOLICY']._serialized_start=2199
  _globals['_BOARDINGPOLICY']._serialized_end=2308
  _globals['_SEATCLASSPOLICY']._serialized_start=2311
  _globals['_SEATCLASSPOLICY']._serialized_end=2442
  _globals['_AUTHORITY']._serialized_start=2444
  _globals['_AUTHORITY']._serialized_end=2475
  _globals['_FLIGHTDESIGNATOR']._serialized_start=178
  _globals['_FLIGHTDESIGNATOR']._serialized_end=1334
  _globals['_FLIGHTDESIGNATORREQUEST']._serialized_start=1337
  _globals['_FLIGHTDESIGNATORREQUEST']._serialized_end=1567
  _globals['_FLIGHTSCHEDULE']._serialized_start=1570
  _globals['_FLIGHTSCHEDULE']._serialized_end=1860
  _globals['_FLIGHTTIMES']._serialized_start=1863
  _globals['_FLIGHTTIMES']._serialized_end=2025
# @@protoc_insertion_point(module_scope)