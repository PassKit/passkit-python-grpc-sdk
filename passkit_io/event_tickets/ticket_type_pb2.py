# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: passkit/io/event_tickets/ticket_type.proto
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
    'passkit/io/event_tickets/ticket_type.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
from passkit.io.common import localization_pb2 as passkit_dot_io_dot_common_dot_localization__pb2
from passkit.io.common import filter_pb2 as passkit_dot_io_dot_common_dot_filter__pb2
from protoc_gen_openapiv2.options import annotations_pb2 as protoc__gen__openapiv2_dot_options_dot_annotations__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n*passkit/io/event_tickets/ticket_type.proto\x12\revent_tickets\x1a\x1fgoogle/protobuf/timestamp.proto\x1a$passkit/io/common/localization.proto\x1a\x1epasskit/io/common/filter.proto\x1a.protoc-gen-openapiv2/options/annotations.proto\"\xbf\x04\n\nTicketType\x12\x11\n\x02id\x18\x01 \x01(\tB\x05\x92\x41\x02@\x01\x12\x0b\n\x03uid\x18\x02 \x01(\t\x12\x14\n\x0cproductionId\x18\x03 \x01(\t\x12\x0c\n\x04name\x18\x04 \x01(\t\x12*\n\rlocalizedName\x18\x05 \x01(\x0b\x32\x13.io.LocalizedString\x12\x1c\n\x14ticketTypeConditions\x18\x06 \x01(\t\x12:\n\x1dlocalizedTicketTypeConditions\x18\x07 \x01(\x0b\x32\x13.io.LocalizedString\x12\"\n\x1a\x62\x65\x66oreRedeemPassTemplateId\x18\x08 \x01(\t\x12!\n\x19\x61\x66terRedeemPassTemplateId\x18\t \x01(\t\x12\x32\n\x07\x63reated\x18\n \x01(\x0b\x32\x1a.google.protobuf.TimestampB\x05\x92\x41\x02@\x01\x12\x32\n\x07updated\x18\x0b \x01(\x0b\x32\x1a.google.protobuf.TimestampB\x05\x92\x41\x02@\x01:\xb7\x01\x92\x41\xb3\x01\n\xb0\x01*\x0bTicket Type2nTicket Type holds details about the ticket type, and links to the before & after redeem Pass Template Designs.\xd2\x01\x0cproductionId\xd2\x01\x04name\xd2\x01\x1a\x62\x65\x66oreRedeemPassTemplateId\"4\n\x0fGetByUidRequest\x12\x14\n\x0cproductionId\x18\x01 \x01(\t\x12\x0b\n\x03uid\x18\x02 \x01(\t\"\xd3\x01\n\x17TicketTypeLimitedFields\x12\n\n\x02id\x18\x01 \x01(\t\x12\x0b\n\x03uid\x18\x02 \x01(\t\x12\x0c\n\x04name\x18\x03 \x01(\t:\x90\x01\x92\x41\x8c\x01\n\x89\x01*\x17Ticket Type (Light ver)2nTicket Type holds details about the ticket type, and links to the before & after redeem Pass Template Designs.\"K\n\x15TicketTypeListRequest\x12\x14\n\x0cproductionId\x18\x01 \x01(\t\x12\x1c\n\x07\x66ilters\x18\x02 \x01(\x0b\x32\x0b.io.FiltersBo\n\x1d\x63om.passkit.grpc.EventTicketsZ2stash.passkit.com/io/model/sdk/go/io/event_tickets\xaa\x02\x19PassKit.Grpc.EventTicketsb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'passkit.io.event_tickets.ticket_type_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n\035com.passkit.grpc.EventTicketsZ2stash.passkit.com/io/model/sdk/go/io/event_tickets\252\002\031PassKit.Grpc.EventTickets'
  _globals['_TICKETTYPE'].fields_by_name['id']._loaded_options = None
  _globals['_TICKETTYPE'].fields_by_name['id']._serialized_options = b'\222A\002@\001'
  _globals['_TICKETTYPE'].fields_by_name['created']._loaded_options = None
  _globals['_TICKETTYPE'].fields_by_name['created']._serialized_options = b'\222A\002@\001'
  _globals['_TICKETTYPE'].fields_by_name['updated']._loaded_options = None
  _globals['_TICKETTYPE'].fields_by_name['updated']._serialized_options = b'\222A\002@\001'
  _globals['_TICKETTYPE']._loaded_options = None
  _globals['_TICKETTYPE']._serialized_options = b'\222A\263\001\n\260\001*\013Ticket Type2nTicket Type holds details about the ticket type, and links to the before & after redeem Pass Template Designs.\322\001\014productionId\322\001\004name\322\001\032beforeRedeemPassTemplateId'
  _globals['_TICKETTYPELIMITEDFIELDS']._loaded_options = None
  _globals['_TICKETTYPELIMITEDFIELDS']._serialized_options = b'\222A\214\001\n\211\001*\027Ticket Type (Light ver)2nTicket Type holds details about the ticket type, and links to the before & after redeem Pass Template Designs.'
  _globals['_TICKETTYPE']._serialized_start=213
  _globals['_TICKETTYPE']._serialized_end=788
  _globals['_GETBYUIDREQUEST']._serialized_start=790
  _globals['_GETBYUIDREQUEST']._serialized_end=842
  _globals['_TICKETTYPELIMITEDFIELDS']._serialized_start=845
  _globals['_TICKETTYPELIMITEDFIELDS']._serialized_end=1056
  _globals['_TICKETTYPELISTREQUEST']._serialized_start=1058
  _globals['_TICKETTYPELISTREQUEST']._serialized_end=1133
# @@protoc_insertion_point(module_scope)
