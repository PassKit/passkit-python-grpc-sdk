# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: io/common/integration.proto
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
    'io/common/integration.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from passkit_io.common import pass_pb2 as io_dot_common_dot_pass__pb2
from passkit_io.common import template_pb2 as io_dot_common_dot_template__pb2
from protoc_gen_openapiv2.options import annotations_pb2 as protoc__gen__openapiv2_dot_options_dot_annotations__pb2
from passkit_io.common import protocols_pb2 as io_dot_common_dot_protocols__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1bio/common/integration.proto\x12\x02io\x1a\x14io/common/pass.proto\x1a\x18io/common/template.proto\x1a.protoc-gen-openapiv2/options/annotations.proto\x1a\x19io/common/protocols.proto\x1a\x1fgoogle/protobuf/timestamp.proto\"8\n\x12MembershipEventIds\x12\"\n\x03ids\x18\x01 \x03(\x0e\x32\x15.io.MembershipEventId\"0\n\x0e\x43ouponEventIds\x12\x1e\n\x03ids\x18\x01 \x03(\x0e\x32\x11.io.CouponEventId\"\xa0\x01\n\x12IntegrationConfigs\x12\x0f\n\x07\x63lassId\x18\x01 \x01(\t\x12\x42\n\x0e\x63onfigurations\x18\x02 \x03(\x0b\x32*.io.IntegrationConfigs.ConfigurationsEntry\x1a\x35\n\x13\x43onfigurationsEntry\x12\x0b\n\x03key\x18\x01 \x01(\x05\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\"F\n\x0fProtocolIdInput\x12\"\n\x08protocol\x18\x01 \x01(\x0e\x32\x10.io.PassProtocol\x12\x0f\n\x07\x63lassId\x18\x02 \x01(\t\"Q\n\x13SubscriptionRequest\x12\"\n\x08protocol\x18\x01 \x01(\x0e\x32\x10.io.PassProtocol\x12\x16\n\x0esubscriptionId\x18\x02 \x01(\t\"\x91\x02\n\x1cSubscriptionRequestByClassId\x12\"\n\x08protocol\x18\x01 \x01(\x0e\x32\x10.io.PassProtocol\x12\x0f\n\x07\x63lassId\x18\x02 \x01(\t\x12)\n\nconfigType\x18\x03 \x01(\x0e\x32\x15.io.ConfigurationType\x12&\n\x0bpassEventId\x18\x04 \x01(\x0e\x32\x0f.io.PassEventIdH\x00\x12\x32\n\x11membershipEventId\x18\x05 \x01(\x0e\x32\x15.io.MembershipEventIdH\x00\x12*\n\rcouponEventId\x18\x06 \x01(\x0e\x32\x11.io.CouponEventIdH\x00\x42\t\n\x07\x65ventId\"\x8e\x01\n\x0c\x46ieldMapping\x12\x1b\n\x13\x64\x65stinationFieldKey\x18\x01 \x01(\t\x12.\n\x18\x64\x65stinationFieldDataType\x18\x02 \x01(\x0e\x32\x0c.io.DataType\x12\x12\n\nisRequired\x18\x03 \x01(\x08\x12\x1d\n\x15sourceFieldUniqueName\x18\x04 \x01(\t\"\x89\x01\n\rWebhookConfig\x12\x11\n\ttargetUrl\x18\x01 \x01(\t\x12&\n\x0c\x61\x63tionMethod\x18\x02 \x01(\x0e\x32\x10.io.ActionMethod\x12&\n\x0c\x66ieldMapping\x18\x03 \x01(\x0b\x32\x10.io.FieldMapping\x12\x15\n\rsigningSecret\x18\x04 \x01(\t\"@\n\x17SinkSubscriptionPayload\x12\r\n\x05\x65vent\x18\x01 \x01(\t\x12\x16\n\x04pass\x18\x02 \x01(\x0b\x32\x08.io.Pass\"\xc5\x05\n\x10SinkSubscription\x12\n\n\x02id\x18\x01 \x01(\t\x12\x0f\n\x07\x63lassId\x18\x02 \x01(\t\x12\"\n\x08protocol\x18\x03 \x01(\x0e\x32\x10.io.PassProtocol\x12$\n\x0bpassEventId\x18\x04 \x03(\x0e\x32\x0f.io.PassEventId\x12%\n\x06status\x18\x05 \x01(\x0e\x32\x15.io.IntegrationStatus\x12)\n\nconfigType\x18\x06 \x01(\x0e\x32\x15.io.ConfigurationType\x12\x15\n\rconfiguration\x18\x07 \x01(\t\x12-\n\tcreatedAt\x18\x08 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12-\n\tupdatedAt\x18\t \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x32\n\x10membershipEvents\x18\n \x01(\x0b\x32\x16.io.MembershipEventIdsH\x00\x12*\n\x0c\x63ouponEvents\x18\x0b \x01(\x0b\x32\x12.io.CouponEventIdsH\x00:\x8f\x02\x92\x41\x8b\x02\n\x88\x02*\x11Sink Subscription2\xe0\x01Set up a subscription for sink integration. Sink subscription is triggered after all chain of events finished inside PassKit. E.g. Create a pass holder record and issue a pass, then create a record on a third party platform.\xd2\x01\x0f\x64\x65\x66\x61ultLanguageB\x11\n\x0fprotocolEventId\"\xa3\x01\n\x0f\x44ynamicApiInput\x12\x0f\n\x07\x63lassId\x18\x01 \x01(\t\x12&\n\x07request\x18\x02 \x01(\x0b\x32\x15.io.DynamicApiRequest:W\x92\x41T\nR*\x11\x44ynamic API Input23Used to make an api call to a third party platform.\xd2\x01\x07\x63lassId\"\xef\x01\n\x11\x44ynamicApiRequest\x12\x13\n\x0brequestName\x18\x01 \x01(\t\x12\x31\n\x06params\x18\x02 \x03(\x0b\x32!.io.DynamicApiRequest.ParamsEntry\x12\x0f\n\x07payload\x18\x03 \x01(\t\x1a-\n\x0bParamsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01:R\x92\x41O\nM*\x13\x44ynamic Api Request2(Specifies your request type and payload.\xd2\x01\x0brequestName\"\x95\x01\n\x12\x44ynamicApiResponse\x12\x14\n\x0cresponseBody\x18\x01 \x01(\x0c\x12\x0e\n\x06status\x18\x02 \x01(\x05:Y\x92\x41V\nT*\x14\x44ynamic API Response2<Returns the api response object from a third party platform.*}\n\x11IntegrationStatus\x12\x1b\n\x17INTEGRATION_STATUS_NONE\x10\x00\x12\x18\n\x14INTEGRATION_DISABLED\x10\x01\x12\x16\n\x12INTEGRATION_ACTIVE\x10\x02\x12\x19\n\x15INTEGRATION_SUSPENDED\x10\x03*\xe6\x01\n\x11\x43onfigurationType\x12\x16\n\x12\x43ONFIGURATION_NONE\x10\x00\x12\x0b\n\x07WEBHOOK\x10\x01\x12\x0c\n\x08\x44\x42_MYSQL\x10\x02\x12\x08\n\x04ZOHO\x10\x03\x12\t\n\x05\x42RAZE\x10\x04\x12\r\n\tCODEREADR\x10\x05\x12\n\n\x06ZAPIER\x10\x06\x12\r\n\tMAILCHIMP\x10\x07\x12\n\n\x06SPROUT\x10\x08\x12\r\n\tTESSITURA\x10\t\x12\x0c\n\x08ITERABLE\x10\n\x12\x0c\n\x08MOENGAGE\x10\x0b\x12\x14\n\x10ORACLE_RESPONSYS\x10\x0c\x12\x12\n\x0e_CONFIG_TYPE_1\x10\x64*\xa3\x04\n\x0fIntegrationType\x12\x19\n\x15INTEGRATION_TYPE_NONE\x10\x00\x12\x16\n\x12SOURCE_INTEGRATION\x10\x01\x12&\n\"HOOK_BEFORE_OBJECT_RECORD_CREATION\x10\x04\x12%\n!HOOK_AFTER_OBJECT_RECORD_CREATION\x10\x08\x12\x1a\n\x16HOOK_BEFORE_PASS_ISSUE\x10\x10\x12\x19\n\x15HOOK_AFTER_PASS_ISSUE\x10 \x12\x1b\n\x17HOOK_AFTER_PASS_INSTALL\x10@\x12\x1e\n\x19HOOK_AFTER_PASS_UNINSTALL\x10\x80\x01\x12%\n HOOK_BEFORE_OBJECT_RECORD_UPDATE\x10\x80\x02\x12$\n\x1fHOOK_AFTER_OBJECT_RECORD_UPDATE\x10\x80\x04\x12#\n\x1eHOOK_BEFORE_PASS_RECORD_UPDATE\x10\x80\x08\x12\"\n\x1dHOOK_AFTER_PASS_RECORD_UPDATE\x10\x80\x10\x12\x1c\n\x17HOOK_BEFORE_PASS_UPDATE\x10\x80 \x12\x1b\n\x16HOOK_AFTER_PASS_UPDATE\x10\x80@\x12$\n\x1eHOOK_BEFORE_PASS_RECORD_DELETE\x10\x80\x80\x01\x12#\n\x1dHOOK_AFTER_PASS_RECORD_DELETE\x10\x80\x80\x02*\xdc\x04\n\x10ProtocolIntgType\x12\x1b\n\x17PROTOCOL_INTG_TYPE_NONE\x10\x00\x12$\n HOOK_BEFORE_MEMBER_UPDATE_POINTS\x10\x01\x12#\n\x1fHOOK_AFTER_MEMBER_UPDATE_POINTS\x10\x04\x12\"\n\x1eHOOK_BEFORE_MEMBER_TIER_UPDATE\x10\x08\x12!\n\x1dHOOK_AFTER_MEMBER_TIER_UPDATE\x10\x10\x12\x1f\n\x1bHOOK_BEFORE_MEMBER_CHECK_IN\x10 \x12\x1e\n\x1aHOOK_AFTER_MEMBER_CHECK_IN\x10@\x12!\n\x1cHOOK_BEFORE_MEMBER_CHECK_OUT\x10\x80\x01\x12 \n\x1bHOOK_AFTER_MEMBER_CHECK_OUT\x10\x80\x02\x12\x1e\n\x19HOOK_BEFORE_COUPON_REDEEM\x10\x80\x10\x12\x1d\n\x18HOOK_AFTER_COUPON_REDEEM\x10\x80 \x12$\n\x1fHOOK_BEFORE_UPDATE_COUPON_OFFER\x10\x80@\x12$\n\x1eHOOK_AFTER_UPDATE_COUPON_OFFER\x10\x80\x80\x01\x12%\n\x1fHOOK_BEFORE_CREATE_COUPON_OFFER\x10\x80\x80\x02\x12$\n\x1eHOOK_AFTER_CREATE_COUPON_OFFER\x10\x80\x80\x04\x12\x1d\n\x16HOOK_BEFORE_UPDATE_PII\x10\x80\x80\x80\x01\x12\x1c\n\x15HOOK_AFTER_UPDATE_PII\x10\x80\x80\x80\x02*\xd1\x01\n\x0bPassEventId\x12\x13\n\x0fPASS_EVENT_NONE\x10\x00\x12\x1d\n\x19PASS_EVENT_RECORD_CREATED\x10\x01\x12\x18\n\x14PASS_EVENT_INSTALLED\x10\x02\x12\x1d\n\x19PASS_EVENT_RECORD_UPDATED\x10\x04\x12\x1a\n\x16PASS_EVENT_UNINSTALLED\x10\x08\x12\x1a\n\x16PASS_EVENT_INVALIDATED\x10\x10\x12\x1d\n\x19PASS_EVENT_RECORD_DELETED\x10 *_\n\x11MembershipEventId\x12\x15\n\x11MEMBER_EVENT_NONE\x10\x00\x12\x19\n\x15MEMBER_EVENT_ENROLLED\x10\x01\x12\x18\n\x14MEMBER_EVENT_UPDATED\x10\x02*\x8f\x01\n\rCouponEventId\x12\x15\n\x11\x43OUPON_EVENT_NONE\x10\x00\x12\x18\n\x14\x43OUPON_EVENT_CREATED\x10\x01\x12\x19\n\x15\x43OUPON_EVENT_REDEEMED\x10\x02\x12\x18\n\x14\x43OUPON_EVENT_UPDATED\x10\x04\x12\x18\n\x14\x43OUPON_EVENT_DELETED\x10\x08*S\n\x0c\x41\x63tionMethod\x12\x0f\n\x0bMETHOD_NONE\x10\x00\x12\x0f\n\x0bMETHOD_POST\x10\x01\x12\x0e\n\nMETHOD_PUT\x10\x02\x12\x11\n\rMETHOD_DELETE\x10\x03\x42G\n\x10\x63om.passkit.grpcZ$stash.passkit.com/io/model/sdk/go/io\xaa\x02\x0cPassKit.Grpcb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'io.common.integration_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n\020com.passkit.grpcZ$stash.passkit.com/io/model/sdk/go/io\252\002\014PassKit.Grpc'
  _globals['_INTEGRATIONCONFIGS_CONFIGURATIONSENTRY']._loaded_options = None
  _globals['_INTEGRATIONCONFIGS_CONFIGURATIONSENTRY']._serialized_options = b'8\001'
  _globals['_SINKSUBSCRIPTION']._loaded_options = None
  _globals['_SINKSUBSCRIPTION']._serialized_options = b'\222A\213\002\n\210\002*\021Sink Subscription2\340\001Set up a subscription for sink integration. Sink subscription is triggered after all chain of events finished inside PassKit. E.g. Create a pass holder record and issue a pass, then create a record on a third party platform.\322\001\017defaultLanguage'
  _globals['_DYNAMICAPIINPUT']._loaded_options = None
  _globals['_DYNAMICAPIINPUT']._serialized_options = b'\222AT\nR*\021Dynamic API Input23Used to make an api call to a third party platform.\322\001\007classId'
  _globals['_DYNAMICAPIREQUEST_PARAMSENTRY']._loaded_options = None
  _globals['_DYNAMICAPIREQUEST_PARAMSENTRY']._serialized_options = b'8\001'
  _globals['_DYNAMICAPIREQUEST']._loaded_options = None
  _globals['_DYNAMICAPIREQUEST']._serialized_options = b'\222AO\nM*\023Dynamic Api Request2(Specifies your request type and payload.\322\001\013requestName'
  _globals['_DYNAMICAPIRESPONSE']._loaded_options = None
  _globals['_DYNAMICAPIRESPONSE']._serialized_options = b'\222AV\nT*\024Dynamic API Response2<Returns the api response object from a third party platform.'
  _globals['_INTEGRATIONSTATUS']._serialized_start=2516
  _globals['_INTEGRATIONSTATUS']._serialized_end=2641
  _globals['_CONFIGURATIONTYPE']._serialized_start=2644
  _globals['_CONFIGURATIONTYPE']._serialized_end=2874
  _globals['_INTEGRATIONTYPE']._serialized_start=2877
  _globals['_INTEGRATIONTYPE']._serialized_end=3424
  _globals['_PROTOCOLINTGTYPE']._serialized_start=3427
  _globals['_PROTOCOLINTGTYPE']._serialized_end=4031
  _globals['_PASSEVENTID']._serialized_start=4034
  _globals['_PASSEVENTID']._serialized_end=4243
  _globals['_MEMBERSHIPEVENTID']._serialized_start=4245
  _globals['_MEMBERSHIPEVENTID']._serialized_end=4340
  _globals['_COUPONEVENTID']._serialized_start=4343
  _globals['_COUPONEVENTID']._serialized_end=4486
  _globals['_ACTIONMETHOD']._serialized_start=4488
  _globals['_ACTIONMETHOD']._serialized_end=4571
  _globals['_MEMBERSHIPEVENTIDS']._serialized_start=191
  _globals['_MEMBERSHIPEVENTIDS']._serialized_end=247
  _globals['_COUPONEVENTIDS']._serialized_start=249
  _globals['_COUPONEVENTIDS']._serialized_end=297
  _globals['_INTEGRATIONCONFIGS']._serialized_start=300
  _globals['_INTEGRATIONCONFIGS']._serialized_end=460
  _globals['_INTEGRATIONCONFIGS_CONFIGURATIONSENTRY']._serialized_start=407
  _globals['_INTEGRATIONCONFIGS_CONFIGURATIONSENTRY']._serialized_end=460
  _globals['_PROTOCOLIDINPUT']._serialized_start=462
  _globals['_PROTOCOLIDINPUT']._serialized_end=532
  _globals['_SUBSCRIPTIONREQUEST']._serialized_start=534
  _globals['_SUBSCRIPTIONREQUEST']._serialized_end=615
  _globals['_SUBSCRIPTIONREQUESTBYCLASSID']._serialized_start=618
  _globals['_SUBSCRIPTIONREQUESTBYCLASSID']._serialized_end=891
  _globals['_FIELDMAPPING']._serialized_start=894
  _globals['_FIELDMAPPING']._serialized_end=1036
  _globals['_WEBHOOKCONFIG']._serialized_start=1039
  _globals['_WEBHOOKCONFIG']._serialized_end=1176
  _globals['_SINKSUBSCRIPTIONPAYLOAD']._serialized_start=1178
  _globals['_SINKSUBSCRIPTIONPAYLOAD']._serialized_end=1242
  _globals['_SINKSUBSCRIPTION']._serialized_start=1245
  _globals['_SINKSUBSCRIPTION']._serialized_end=1954
  _globals['_DYNAMICAPIINPUT']._serialized_start=1957
  _globals['_DYNAMICAPIINPUT']._serialized_end=2120
  _globals['_DYNAMICAPIREQUEST']._serialized_start=2123
  _globals['_DYNAMICAPIREQUEST']._serialized_end=2362
  _globals['_DYNAMICAPIREQUEST_PARAMSENTRY']._serialized_start=2233
  _globals['_DYNAMICAPIREQUEST_PARAMSENTRY']._serialized_end=2278
  _globals['_DYNAMICAPIRESPONSE']._serialized_start=2365
  _globals['_DYNAMICAPIRESPONSE']._serialized_end=2514
# @@protoc_insertion_point(module_scope)
