# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: io/flights/barcode.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from io.common import common_objects_pb2 as io_dot_common_dot_common__objects__pb2
from protoc_gen_openapiv2.options import annotations_pb2 as protoc__gen__openapiv2_dot_options_dot_annotations__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x18io/flights/barcode.proto\x12\x07\x66lights\x1a\x1eio/common/common_objects.proto\x1a.protoc-gen-openapiv2/options/annotations.proto\"\xc2\x08\n\x10\x43onditionalItems\x12;\n\x14passengerDescription\x18\x01 \x01(\x0e\x32\x1d.flights.PassengerDescription\x12&\n\rcheckInSource\x18\x02 \x01(\x0e\x32\x0f.flights.Source\x12\x33\n\x1a\x62oardingPassIssuanceSource\x18\x03 \x01(\x0e\x32\x0f.flights.Source\x12\'\n\x15\x62oardingPassIssueDate\x18\x04 \x01(\x0b\x32\x08.io.Date\x12&\n\x0c\x64ocumentType\x18\x05 \x01(\x0e\x32\x10.flights.DocType\x12\x1a\n\x12\x62oardingPassIssuer\x18\x06 \x01(\t\x12\xcc\x04\n\x10\x62\x61ggageTagNumber\x18\x07 \x03(\tB\xb1\x04\x92\x41\xad\x04\x32\xaa\x04This field allows carriers to populate baggage tag numbers and the number of consecutive bags. It contains 13 characters corresponding to the 10 digit bag tag number, as per IATA BCM specifications, Resolution 740 and 3 digits identifying the number of consecutive tags.\n1: leading digit \xe2\x80\x93 0 for interline tag, 1 for fall-back tag, 2 for interline rush tag.\n2-4: carrier numeric code.\n5-10: carrier initial tag number (leading zeros).\n11-13: number of consecutive tags (allows for up to 999 tags).\nUp to 2 additional, non-consecutive tags can be added.\x12\x35\n\x11selecteeIndicator\x18\x08 \x01(\x0e\x32\x1a.flights.SelecteeIndicator\x12K\n\x1cinternationalDocVerification\x18\t \x01(\x0e\x32%.flights.InternationalDocVerification\x12-\n\ridadIndicator\x18\n \x01(\x0e\x32\x16.flights.IDADIndicator\x12%\n\tfastTrack\x18\x0b \x01(\x0e\x32\x12.flights.FastTrack*\xef\x02\n\x0fPassengerStatus\x12\x19\n\x15ISSUED_NOT_CHECKED_IN\x10\x00\x12\x15\n\x11ISSUED_CHECKED_IN\x10\x01\x12,\n(BAGGAGE_CHECKED_PASSENGER_NOT_CHECKED_IN\x10\x02\x12(\n$BAGGAGE_CHECKED_PASSENGER_CHECKED_IN\x10\x03\x12#\n\x1fPASSENGER_PASSED_SECURITY_CHECK\x10\x04\x12\x19\n\x15PASSENGER_PASSED_GATE\x10\x05\x12\x0b\n\x07TRANSIT\x10\x06\x12\x0b\n\x07STANDBY\x10\x07\x12#\n\x1f\x42OARDING_DATA_REVALIDATION_DONE\x10\x08\x12\x32\n.ORIGINAL_BOARDING_LINE_USED_AT_TICKET_ISSUANCE\x10\t\x12\x1f\n\x1bUP_OR_DOWN_GRADING_REQUIRED\x10\n*\x90\x01\n\x14PassengerDescription\x12\t\n\x05\x41\x44ULT\x10\x00\x12\x08\n\x04MALE\x10\x01\x12\n\n\x06\x46\x45MALE\x10\x02\x12\t\n\x05\x43HILD\x10\x03\x12\n\n\x06INFANT\x10\x04\x12\x10\n\x0cNO_PASSENGER\x10\x05\x12\x15\n\x11\x41\x44ULT_WITH_INFANT\x10\x06\x12\x17\n\x13UNACCOMPANIED_MINOR\x10\x07*@\n\x06Source\x12\x05\n\x01W\x10\x00\x12\x05\n\x01K\x10\x01\x12\x05\n\x01X\x10\x02\x12\x05\n\x01R\x10\x03\x12\x05\n\x01M\x10\x04\x12\x05\n\x01O\x10\x05\x12\x05\n\x01T\x10\x06\x12\x05\n\x01V\x10\x07*\x17\n\x07\x44ocType\x12\x05\n\x01\x42\x10\x00\x12\x05\n\x01I\x10\x01*M\n\x1cInternationalDocVerification\x12\x10\n\x0cNOT_REQUIRED\x10\x00\x12\x0c\n\x08REQUIRED\x10\x01\x12\r\n\tCOMPLETED\x10\x02*\xab\x01\n\rIDADIndicator\x12\x08\n\x04NONE\x10\x00\x12\x08\n\x04IDN1\x10\x01\x12\x08\n\x04IDN2\x10\x02\x12\x08\n\x04IDB1\x10\x03\x12\x08\n\x04IDB2\x10\x04\x12\x06\n\x02\x41\x44\x10\x05\x12\x06\n\x02\x44G\x10\x06\x12\x06\n\x02\x44M\x10\x07\x12\x06\n\x02GE\x10\x08\x12\x06\n\x02IG\x10\t\x12\x06\n\x02RG\x10\n\x12\x06\n\x02UD\x10\x0b\x12\x06\n\x02ID\x10\x0c\x12\t\n\x05IDFS1\x10\r\x12\t\n\x05IDFS2\x10\x0e\x12\x08\n\x04IDR1\x10\x0f\x12\x08\n\x04IDR2\x10\x10*E\n\x11SelecteeIndicator\x12\x10\n\x0cNOT_SELECTEE\x10\x00\x12\x0c\n\x08SELECTEE\x10\x01\x12\x10\n\x0cTSA_PRECHECK\x10\x03*\x19\n\tFastTrack\x12\x05\n\x01N\x10\x00\x12\x05\n\x01Y\x10\x01\x42_\n\x18\x63om.passkit.grpc.FlightsZ,stash.passkit.com/io/model/sdk/go/io/flights\xaa\x02\x14PassKit.Grpc.Flightsb\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'io.flights.barcode_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\030com.passkit.grpc.FlightsZ,stash.passkit.com/io/model/sdk/go/io/flights\252\002\024PassKit.Grpc.Flights'
  _CONDITIONALITEMS.fields_by_name['baggageTagNumber']._options = None
  _CONDITIONALITEMS.fields_by_name['baggageTagNumber']._serialized_options = b'\222A\255\0042\252\004This field allows carriers to populate baggage tag numbers and the number of consecutive bags. It contains 13 characters corresponding to the 10 digit bag tag number, as per IATA BCM specifications, Resolution 740 and 3 digits identifying the number of consecutive tags.\n1: leading digit \342\200\223 0 for interline tag, 1 for fall-back tag, 2 for interline rush tag.\n2-4: carrier numeric code.\n5-10: carrier initial tag number (leading zeros).\n11-13: number of consecutive tags (allows for up to 999 tags).\nUp to 2 additional, non-consecutive tags can be added.'
  _PASSENGERSTATUS._serialized_start=1211
  _PASSENGERSTATUS._serialized_end=1578
  _PASSENGERDESCRIPTION._serialized_start=1581
  _PASSENGERDESCRIPTION._serialized_end=1725
  _SOURCE._serialized_start=1727
  _SOURCE._serialized_end=1791
  _DOCTYPE._serialized_start=1793
  _DOCTYPE._serialized_end=1816
  _INTERNATIONALDOCVERIFICATION._serialized_start=1818
  _INTERNATIONALDOCVERIFICATION._serialized_end=1895
  _IDADINDICATOR._serialized_start=1898
  _IDADINDICATOR._serialized_end=2069
  _SELECTEEINDICATOR._serialized_start=2071
  _SELECTEEINDICATOR._serialized_end=2140
  _FASTTRACK._serialized_start=2142
  _FASTTRACK._serialized_end=2167
  _CONDITIONALITEMS._serialized_start=118
  _CONDITIONALITEMS._serialized_end=1208
# @@protoc_insertion_point(module_scope)
