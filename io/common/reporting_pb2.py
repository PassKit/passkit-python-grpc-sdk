# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: io/common/reporting.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from io.common import protocols_pb2 as io_dot_common_dot_protocols__pb2
from io.common import common_objects_pb2 as io_dot_common_dot_common__objects__pb2
from protoc_gen_openapiv2.options import annotations_pb2 as protoc__gen__openapiv2_dot_options_dot_annotations__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x19io/common/reporting.proto\x12\x02io\x1a\x19io/common/protocols.proto\x1a\x1eio/common/common_objects.proto\x1a.protoc-gen-openapiv2/options/annotations.proto\"\xdf\x06\n\x11\x41nalyticsResponse\x12\x1a\n\x06period\x18\x01 \x01(\x0e\x32\n.io.Period\x12\x0f\n\x07\x63reated\x18\x02 \x01(\r\x12\x11\n\tinstalled\x18\x03 \x01(\r\x12\x0f\n\x07\x64\x65leted\x18\x04 \x01(\r\x12\x13\n\x0binvalidated\x18\x05 \x01(\r\x12,\n\x0f\x64\x65viceBreakdown\x18\x06 \x01(\x0b\x32\x13.io.DeviceBreakdown\x12I\n\x12utmSourceBreakdown\x18\x07 \x03(\x0b\x32-.io.AnalyticsResponse.UtmSourceBreakdownEntry\x12!\n\x04\x64\x61ta\x18\x08 \x03(\x0b\x32\x13.io.ChartDataPoints\x12I\n\x12utmMediumBreakdown\x18\t \x03(\x0b\x32-.io.AnalyticsResponse.UtmMediumBreakdownEntry\x12\x45\n\x10utmNameBreakdown\x18\n \x03(\x0b\x32+.io.AnalyticsResponse.UtmNameBreakdownEntry\x12\x45\n\x10utmTermBreakdown\x18\x0b \x03(\x0b\x32+.io.AnalyticsResponse.UtmTermBreakdownEntry\x12K\n\x13utmContentBreakdown\x18\x0c \x03(\x0b\x32..io.AnalyticsResponse.UtmContentBreakdownEntry\x1a\x39\n\x17UtmSourceBreakdownEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\r:\x02\x38\x01\x1a\x39\n\x17UtmMediumBreakdownEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\r:\x02\x38\x01\x1a\x37\n\x15UtmNameBreakdownEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\r:\x02\x38\x01\x1a\x37\n\x15UtmTermBreakdownEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\r:\x02\x38\x01\x1a:\n\x18UtmContentBreakdownEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\r:\x02\x38\x01\"N\n\x0f\x44\x65viceBreakdown\x12\x13\n\x0b\x61ppleWallet\x18\x01 \x01(\r\x12\x11\n\tgooglePay\x18\x02 \x01(\r\x12\x13\n\x0botherWallet\x18\x03 \x01(\r\"\x8a\x01\n\x0f\x43hartDataPoints\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x0f\n\x07\x63reated\x18\x02 \x01(\r\x12\x11\n\tinstalled\x18\x03 \x01(\r\x12\x0f\n\x07updated\x18\x04 \x01(\r\x12\x0f\n\x07\x64\x65leted\x18\x05 \x01(\r\x12\x13\n\x0binvalidated\x18\x06 \x01(\r\x12\x0e\n\x06\x63ustom\x18\x07 \x01(\r\"\xa4\x03\n\x10\x41nalyticsRequest\x12\"\n\x08protocol\x18\x01 \x01(\x0e\x32\x10.io.PassProtocol\x12\x0f\n\x07\x63lassId\x18\x02 \x01(\t\x12\x1a\n\x06period\x18\x03 \x01(\x0e\x32\n.io.Period\x12\x11\n\tstartDate\x18\x04 \x01(\t\x12\x0f\n\x07\x65ndDate\x18\x05 \x01(\t\x12\x10\n\x08timezone\x18\x06 \x01(\t\x12+\n\x06\x63oupon\x18\x0f \x01(\x0b\x32\x19.io.CouponAnalyticsFilterH\x00\x12+\n\x06\x66light\x18\x10 \x01(\x0b\x32\x19.io.FlightAnalyticsFilterH\x00\x12\x35\n\x0b\x65ventTicket\x18\x11 \x01(\x0b\x32\x1e.io.EventTicketAnalyticsFilterH\x00:n\x92\x41k\ni*\x11\x41nalytics Request2?Retrieves pass created, installed, deleted, invalidated counts.\xd2\x01\x08protocol\xd2\x01\x07\x63lassIdB\x08\n\x06\x66ilter\"(\n\x15\x43ouponAnalyticsFilter\x12\x0f\n\x07offerId\x18\x01 \x01(\t\"}\n\x15\x46lightAnalyticsFilter\x12\x14\n\x0c\x66lightNumber\x18\x01 \x01(\t\x12\x1f\n\rdepartureDate\x18\x02 \x01(\x0b\x32\x08.io.Date\x12\x15\n\rboardingPoint\x18\x03 \x01(\t\x12\x16\n\x0e\x64\x65planingPoint\x18\x04 \x01(\t\"}\n\x1a\x45ventTicketAnalyticsFilter\x12\x14\n\x0cticketTypeId\x18\x01 \x01(\t\x12\x15\n\rticketTypeUid\x18\x02 \x01(\t\x12\x0f\n\x07venueId\x18\x03 \x01(\t\x12\x10\n\x08venueUid\x18\x04 \x01(\t\x12\x0f\n\x07\x65ventId\x18\x05 \x01(\t*&\n\x06Period\x12\x07\n\x03\x44\x41Y\x10\x00\x12\t\n\x05MONTH\x10\x01\x12\x08\n\x04YEAR\x10\x02\x42G\n\x10\x63om.passkit.grpcZ$stash.passkit.com/io/model/sdk/go/io\xaa\x02\x0cPassKit.Grpcb\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'io.common.reporting_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\020com.passkit.grpcZ$stash.passkit.com/io/model/sdk/go/io\252\002\014PassKit.Grpc'
  _ANALYTICSRESPONSE_UTMSOURCEBREAKDOWNENTRY._options = None
  _ANALYTICSRESPONSE_UTMSOURCEBREAKDOWNENTRY._serialized_options = b'8\001'
  _ANALYTICSRESPONSE_UTMMEDIUMBREAKDOWNENTRY._options = None
  _ANALYTICSRESPONSE_UTMMEDIUMBREAKDOWNENTRY._serialized_options = b'8\001'
  _ANALYTICSRESPONSE_UTMNAMEBREAKDOWNENTRY._options = None
  _ANALYTICSRESPONSE_UTMNAMEBREAKDOWNENTRY._serialized_options = b'8\001'
  _ANALYTICSRESPONSE_UTMTERMBREAKDOWNENTRY._options = None
  _ANALYTICSRESPONSE_UTMTERMBREAKDOWNENTRY._serialized_options = b'8\001'
  _ANALYTICSRESPONSE_UTMCONTENTBREAKDOWNENTRY._options = None
  _ANALYTICSRESPONSE_UTMCONTENTBREAKDOWNENTRY._serialized_options = b'8\001'
  _ANALYTICSREQUEST._options = None
  _ANALYTICSREQUEST._serialized_options = b'\222Ak\ni*\021Analytics Request2?Retrieves pass created, installed, deleted, invalidated counts.\322\001\010protocol\322\001\007classId'
  _PERIOD._serialized_start=1946
  _PERIOD._serialized_end=1984
  _ANALYTICSRESPONSE._serialized_start=141
  _ANALYTICSRESPONSE._serialized_end=1004
  _ANALYTICSRESPONSE_UTMSOURCEBREAKDOWNENTRY._serialized_start=714
  _ANALYTICSRESPONSE_UTMSOURCEBREAKDOWNENTRY._serialized_end=771
  _ANALYTICSRESPONSE_UTMMEDIUMBREAKDOWNENTRY._serialized_start=773
  _ANALYTICSRESPONSE_UTMMEDIUMBREAKDOWNENTRY._serialized_end=830
  _ANALYTICSRESPONSE_UTMNAMEBREAKDOWNENTRY._serialized_start=832
  _ANALYTICSRESPONSE_UTMNAMEBREAKDOWNENTRY._serialized_end=887
  _ANALYTICSRESPONSE_UTMTERMBREAKDOWNENTRY._serialized_start=889
  _ANALYTICSRESPONSE_UTMTERMBREAKDOWNENTRY._serialized_end=944
  _ANALYTICSRESPONSE_UTMCONTENTBREAKDOWNENTRY._serialized_start=946
  _ANALYTICSRESPONSE_UTMCONTENTBREAKDOWNENTRY._serialized_end=1004
  _DEVICEBREAKDOWN._serialized_start=1006
  _DEVICEBREAKDOWN._serialized_end=1084
  _CHARTDATAPOINTS._serialized_start=1087
  _CHARTDATAPOINTS._serialized_end=1225
  _ANALYTICSREQUEST._serialized_start=1228
  _ANALYTICSREQUEST._serialized_end=1648
  _COUPONANALYTICSFILTER._serialized_start=1650
  _COUPONANALYTICSFILTER._serialized_end=1690
  _FLIGHTANALYTICSFILTER._serialized_start=1692
  _FLIGHTANALYTICSFILTER._serialized_end=1817
  _EVENTTICKETANALYTICSFILTER._serialized_start=1819
  _EVENTTICKETANALYTICSFILTER._serialized_end=1944
# @@protoc_insertion_point(module_scope)