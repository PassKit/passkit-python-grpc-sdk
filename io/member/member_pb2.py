# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: io/member/member.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
from io.common import metrics_pb2 as io_dot_common_dot_metrics__pb2
from io.common import note_pb2 as io_dot_common_dot_note__pb2
from io.common import pagination_pb2 as io_dot_common_dot_pagination__pb2
from io.common import filter_pb2 as io_dot_common_dot_filter__pb2
from io.common import pass_pb2 as io_dot_common_dot_pass__pb2
from io.common import personal_pb2 as io_dot_common_dot_personal__pb2
from io.common import expiry_pb2 as io_dot_common_dot_expiry__pb2
from io.member import event_pb2 as io_dot_member_dot_event__pb2
from protoc_gen_openapiv2.options import annotations_pb2 as protoc__gen__openapiv2_dot_options_dot_annotations__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x16io/member/member.proto\x12\x07members\x1a\x1fgoogle/protobuf/timestamp.proto\x1a\x17io/common/metrics.proto\x1a\x14io/common/note.proto\x1a\x1aio/common/pagination.proto\x1a\x16io/common/filter.proto\x1a\x14io/common/pass.proto\x1a\x18io/common/personal.proto\x1a\x16io/common/expiry.proto\x1a\x15io/member/event.proto\x1a.protoc-gen-openapiv2/options/annotations.proto\"\xb4\x07\n\x06Member\x12\n\n\x02id\x18\x01 \x01(\t\x12\x12\n\nexternalId\x18\x02 \x01(\t\x12\x1a\n\x12groupingIdentifier\x18\x03 \x01(\t\x12\x0e\n\x06tierId\x18\x04 \x01(\t\x12\x11\n\tprogramId\x18\x05 \x01(\t\x12\x1a\n\x06person\x18\x06 \x01(\x0b\x32\n.io.Person\x12/\n\x08metaData\x18\x07 \x03(\x0b\x32\x1d.members.Member.MetaDataEntry\x12\x0e\n\x06optOut\x18\r \x01(\x08\x12\x0e\n\x06points\x18\x0e \x01(\x02\x12\x17\n\x0fsecondaryPoints\x18\x0f \x01(\x02\x12\x12\n\ntierPoints\x18\x10 \x01(\r\x12.\n\nexpiryDate\x18\x12 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12%\n\x06status\x18\x13 \x01(\x0e\x32\x15.members.MemberStatus\x12(\n\rpassOverrides\x18\x14 \x01(\x0b\x32\x11.io.PassOverrides\x12\"\n\x0cpassMetaData\x18\x15 \x01(\x0b\x32\x0c.io.Metadata\x12\x17\n\x05notes\x18\x1a \x03(\x0b\x32\x08.io.Note\x12\x36\n\x12\x63urrentTierAwarded\x18\x1b \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x36\n\x12\x63urrentTierExpires\x18\x1c \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12+\n\x07\x63reated\x18\x1d \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12+\n\x07updated\x18\x1e \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x14\n\x0cprofileImage\x18\x1f \x01(\t\x1a/\n\rMetaDataEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01:\xab\x01\x92\x41\xa7\x01\n\xa4\x01*\x06Member2\x84\x01\x42\x61sic member information needs to be provided. Member information is deleted or rendered unusable once the member record is deleted.\xd2\x01\x06tierId\xd2\x01\tprogramIdJ\x04\x08\x08\x10\tJ\x04\x08\t\x10\nJ\x04\x08\n\x10\x0bJ\x04\x08\x0b\x10\x0cJ\x04\x08\x0c\x10\rJ\x04\x08\x16\x10\x17J\x04\x08\x17\x10\x18J\x04\x08\x18\x10\x19J\x04\x08\x19\x10\x1a\"H\n\x1fMemberRecordByExternalIdRequest\x12\x11\n\tprogramId\x18\x01 \x01(\t\x12\x12\n\nexternalId\x18\x02 \x01(\t\"V\n\x14MemberSegmentRequest\x12\x1a\n\x06\x66ilter\x18\x01 \x01(\x0b\x32\n.io.Filter\x12\"\n\tnewValues\x18\x02 \x01(\x0b\x32\x0f.members.Member\"v\n\x13UpdateExpiryRequest\x12\x11\n\tprogramId\x18\x01 \x01(\t\x12\x0e\n\x06tierId\x18\x02 \x01(\t\x12*\n\x0e\x65xpirySettings\x18\x03 \x01(\x0b\x32\x12.io.ExpirySettings\x12\x10\n\x08timezone\x18\x04 \x01(\t\"q\n\x0cMemberExpiry\x12\n\n\x02id\x18\x01 \x01(\t\x12\x12\n\nexternalId\x18\x02 \x01(\t\x12\x11\n\tprogramId\x18\x03 \x01(\t\x12.\n\nexpiryDate\x18\x04 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\"~\n\x0cMemberPoints\x12\n\n\x02id\x18\x01 \x01(\t\x12\x12\n\nexternalId\x18\x02 \x01(\t\x12\x11\n\tprogramId\x18\x03 \x01(\t\x12\x0e\n\x06points\x18\x04 \x01(\x02\x12\x17\n\x0fsecondaryPoints\x18\x05 \x01(\x02\x12\x12\n\ntierPoints\x18\x06 \x01(\r\"\xc4\x01\n\x15\x45\x61rnBurnPointsRequest\x12\n\n\x02id\x18\x01 \x01(\t\x12\x12\n\nexternalId\x18\x02 \x01(\t\x12\x11\n\tprogramId\x18\x03 \x01(\t\x12\x0e\n\x06points\x18\x04 \x01(\x02\x12\x17\n\x0fsecondaryPoints\x18\x05 \x01(\x02\x12\x12\n\ntierPoints\x18\x06 \x01(\r\x12+\n\x0c\x65ventDetails\x18\x07 \x01(\x0b\x32\x15.members.EventDetails\x12\x0e\n\x06tierId\x18\x08 \x01(\t\"\x8b\x02\n\x10SetPointsRequest\x12\n\n\x02id\x18\x01 \x01(\t\x12\x12\n\nexternalId\x18\x02 \x01(\t\x12\x11\n\tprogramId\x18\x03 \x01(\t\x12\x0e\n\x06points\x18\x04 \x01(\x02\x12\x17\n\x0fsecondaryPoints\x18\x05 \x01(\x02\x12\x12\n\ntierPoints\x18\x06 \x01(\r\x12\x13\n\x0bresetPoints\x18\x07 \x01(\x08\x12\x1c\n\x14resetSecondaryPoints\x18\x08 \x01(\x08\x12\x17\n\x0fresetTierPoints\x18\t \x01(\x08\x12+\n\x0c\x65ventDetails\x18\n \x01(\x0b\x32\x15.members.EventDetails\x12\x0e\n\x06tierId\x18\x0b \x01(\t\"\xe0\x02\n\x17MemberCheckInOutRequest\x12\x10\n\x08memberId\x18\x01 \x01(\t\x12\x18\n\x10\x65xternalMemberId\x18\x02 \x01(\t\x12\x11\n\tprogramId\x18\x03 \x01(\t\x12\x0f\n\x07\x61\x64\x64ress\x18\x04 \x01(\t\x12\x0b\n\x03lat\x18\x05 \x01(\x01\x12\x0b\n\x03lon\x18\x06 \x01(\x01\x12\x0b\n\x03\x61lt\x18\x07 \x01(\x05\x12\x17\n\x0f\x65xternalEventId\x18\x08 \x01(\t\x12\x18\n\x10\x65xternalDeviceId\x18\t \x01(\t\x12\x19\n\x11\x65xternalServiceId\x18\n \x01(\t\x12@\n\x08metaData\x18\x0b \x03(\x0b\x32..members.MemberCheckInOutRequest.MetaDataEntry\x12\r\n\x05notes\x18\x0c \x01(\t\x1a/\n\rMetaDataEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\"N\n\x15ListRequestDeprecated\x12\x11\n\tprogramId\x18\x01 \x01(\t\x12\"\n\npagination\x18\x02 \x01(\x0b\x32\x0e.io.Pagination\"R\n\x0bListRequest\x12\x11\n\tprogramId\x18\x01 \x01(\t\x12\x1c\n\x07\x66ilters\x18\x02 \x01(\x0b\x32\x0b.io.Filters\x12\x12\n\nemailAsCsv\x18\x03 \x01(\x08\"\x8f\x01\n\x11\x43hangeTierRequest\x12\x10\n\x08memberId\x18\x01 \x01(\t\x12\x18\n\x10\x65xternalMemberId\x18\x02 \x01(\t\x12\x11\n\tprogramId\x18\x03 \x01(\t\x12\x0e\n\x06tierId\x18\x04 \x01(\t\x12+\n\x0c\x65ventDetails\x18\x07 \x01(\x0b\x32\x15.members.EventDetails*c\n\x0cMemberStatus\x12\x0c\n\x08\x45NROLLED\x10\x00\x12\n\n\x06\x41\x43TIVE\x10\x01\x12\x0e\n\nCHECKED_IN\x10\x02\x12\x0b\n\x07\x45XPIRED\x10\x03\x12\x0f\n\x0b\x43HECKED_OUT\x10\x04\x12\x0b\n\x07\x44\x45LETED\x10\x05\x42_\n\x18\x63om.passkit.grpc.MembersZ,stash.passkit.com/io/model/sdk/go/io/members\xaa\x02\x14PassKit.Grpc.Membersb\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'io.member.member_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\030com.passkit.grpc.MembersZ,stash.passkit.com/io/model/sdk/go/io/members\252\002\024PassKit.Grpc.Members'
  _MEMBER_METADATAENTRY._options = None
  _MEMBER_METADATAENTRY._serialized_options = b'8\001'
  _MEMBER._options = None
  _MEMBER._serialized_options = b'\222A\247\001\n\244\001*\006Member2\204\001Basic member information needs to be provided. Member information is deleted or rendered unusable once the member record is deleted.\322\001\006tierId\322\001\tprogramId'
  _MEMBERCHECKINOUTREQUEST_METADATAENTRY._options = None
  _MEMBERCHECKINOUTREQUEST_METADATAENTRY._serialized_options = b'8\001'
  _MEMBERSTATUS._serialized_start=2920
  _MEMBERSTATUS._serialized_end=3019
  _MEMBER._serialized_start=311
  _MEMBER._serialized_end=1259
  _MEMBER_METADATAENTRY._serialized_start=984
  _MEMBER_METADATAENTRY._serialized_end=1031
  _MEMBERRECORDBYEXTERNALIDREQUEST._serialized_start=1261
  _MEMBERRECORDBYEXTERNALIDREQUEST._serialized_end=1333
  _MEMBERSEGMENTREQUEST._serialized_start=1335
  _MEMBERSEGMENTREQUEST._serialized_end=1421
  _UPDATEEXPIRYREQUEST._serialized_start=1423
  _UPDATEEXPIRYREQUEST._serialized_end=1541
  _MEMBEREXPIRY._serialized_start=1543
  _MEMBEREXPIRY._serialized_end=1656
  _MEMBERPOINTS._serialized_start=1658
  _MEMBERPOINTS._serialized_end=1784
  _EARNBURNPOINTSREQUEST._serialized_start=1787
  _EARNBURNPOINTSREQUEST._serialized_end=1983
  _SETPOINTSREQUEST._serialized_start=1986
  _SETPOINTSREQUEST._serialized_end=2253
  _MEMBERCHECKINOUTREQUEST._serialized_start=2256
  _MEMBERCHECKINOUTREQUEST._serialized_end=2608
  _MEMBERCHECKINOUTREQUEST_METADATAENTRY._serialized_start=984
  _MEMBERCHECKINOUTREQUEST_METADATAENTRY._serialized_end=1031
  _LISTREQUESTDEPRECATED._serialized_start=2610
  _LISTREQUESTDEPRECATED._serialized_end=2688
  _LISTREQUEST._serialized_start=2690
  _LISTREQUEST._serialized_end=2772
  _CHANGETIERREQUEST._serialized_start=2775
  _CHANGETIERREQUEST._serialized_end=2918
# @@protoc_insertion_point(module_scope)