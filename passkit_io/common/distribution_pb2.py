# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: passkit/io/common/distribution.proto
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
    'passkit/io/common/distribution.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from passkit.io.common import common_objects_pb2 as passkit_dot_io_dot_common_dot_common__objects__pb2
from passkit.io.common import localization_pb2 as passkit_dot_io_dot_common_dot_localization__pb2
from passkit.io.common import protocols_pb2 as passkit_dot_io_dot_common_dot_protocols__pb2
from passkit.io.common import template_pb2 as passkit_dot_io_dot_common_dot_template__pb2
from protoc_gen_openapiv2.options import annotations_pb2 as protoc__gen__openapiv2_dot_options_dot_annotations__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n$passkit/io/common/distribution.proto\x12\x02io\x1a&passkit/io/common/common_objects.proto\x1a$passkit/io/common/localization.proto\x1a!passkit/io/common/protocols.proto\x1a passkit/io/common/template.proto\x1a.protoc-gen-openapiv2/options/annotations.proto\"\x89\x01\n\x18\x45mailDistributionRequest\x12\n\n\x02id\x18\x01 \x01(\t\x12\x12\n\nexternalId\x18\x02 \x01(\t\x12\x0f\n\x07\x63lassId\x18\x03 \x01(\t\x12\"\n\x08protocol\x18\x04 \x01(\x0e\x32\x10.io.PassProtocol\x12\x18\n\x10\x61lternativeEmail\x18\x05 \x01(\t\"\xa4\x01\n\x14SmartPassLinkRequest\x12\'\n\x16projectDistributionUrl\x18\x01 \x01(\x0b\x32\x07.io.Url\x12\x34\n\x06\x66ields\x18\x02 \x03(\x0b\x32$.io.SmartPassLinkRequest.FieldsEntry\x1a-\n\x0b\x46ieldsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\"\x9b\x01\n\x14\x44istributionSettings\x12\x35\n\x14\x64istributionChannels\x18\x01 \x03(\x0e\x32\x17.io.DistributionChannel\x12\'\n\x0cwelcomeEmail\x18\x02 \x01(\x0b\x32\x11.io.EmailTemplate\x12#\n\nwelcomeSms\x18\x03 \x01(\x0b\x32\x0f.io.SmsTemplate\"\xf6\x06\n\rEmailTemplate\x12\x0f\n\x07subject\x18\x01 \x01(\t\x12-\n\x10localizedSubject\x18\x02 \x01(\x0b\x32\x13.io.LocalizedString\x12\x17\n\x0f\x62odyTextContent\x18\x03 \x01(\t\x12\x35\n\x18localizedBodyTextContent\x18\x04 \x01(\x0b\x32\x13.io.LocalizedString\x12\x17\n\x0f\x62odyHtmlContent\x18\x05 \x01(\t\x12\x35\n\x18localizedBodyHtmlContent\x18\x06 \x01(\x0b\x32\x13.io.LocalizedString\x12-\n\rconfiguration\x18\x07 \x01(\x0b\x32\x16.io.EmailConfiguration\x12\x12\n\nbuttonText\x18\x08 \x01(\t\x12\x17\n\x0f\x62uttonTextColor\x18\t \x01(\t\x12\x1d\n\x15\x62uttonBackgroundColor\x18\n \x01(\t\x12\x1a\n\x12\x62uttonBorderRadius\x18\x0b \x01(\t\x12\x19\n\x11\x66ooterTextContent\x18\x0c \x01(\t\x12\x37\n\x1alocalizedFooterTextContent\x18\r \x01(\x0b\x32\x13.io.LocalizedString\x12\x19\n\x11\x66ooterHtmlContent\x18\x0e \x01(\t\x12\x37\n\x1alocalizedFooterHtmlContent\x18\x0f \x01(\x0b\x32\x13.io.LocalizedString\x12\x1e\n\x16messageBackgroundColor\x18\x10 \x01(\t\x12\x1b\n\x13pageBackgroundColor\x18\x11 \x01(\t\x12\x17\n\x0ftemplateOptions\x18\x12 \x01(\x05\x12\x1f\n\x17\x64\x61rkModeButtonTextColor\x18\x13 \x01(\t\x12%\n\x1d\x64\x61rkModeButtonBackgroundColor\x18\x14 \x01(\t\x12#\n\x1b\x64\x61rkModePageBackgroundColor\x18\x15 \x01(\t\x12&\n\x1e\x64\x61rkModeContentBackgroundColor\x18\x16 \x01(\t\x12\x13\n\x0bheaderLabel\x18\x17 \x01(\t\x12\x31\n\x14localizedHeaderLabel\x18\x18 \x01(\x0b\x32\x13.io.LocalizedString\x12\x13\n\x0bheaderValue\x18\x19 \x01(\t\"z\n\x12\x45mailConfiguration\x12\x11\n\temailFrom\x18\x01 \x01(\t\x12\x15\n\remailFromName\x18\x02 \x01(\t\x12#\n\x1b\x45mailFromVerifiedForSending\x18\x03 \x01(\x08\x12\x15\n\ruseCustomHtml\x18\x04 \x01(\x08\"a\n\x0bSmsTemplate\x12\x16\n\x07\x63ontent\x18\x01 \x01(\tB\x05\x92\x41\x02xF\x12\x34\n\x10localizedContent\x18\x02 \x01(\x0b\x32\x13.io.LocalizedStringB\x05\x92\x41\x02xFJ\x04\x08\x03\x10\x04\"\xae\x02\n\rEnrolmentUrls\x12\x0f\n\x07pageUrl\x18\x01 \x01(\t\x12\x11\n\tqrCodeUrl\x18\x02 \x01(\t\x12\x43\n\x11tierEnrolmentUrls\x18\x03 \x03(\x0b\x32(.io.EnrolmentUrls.TierEnrolmentUrlsEntry\x12\x41\n\x10tierEnrolmentQRs\x18\x04 \x03(\x0b\x32\'.io.EnrolmentUrls.TierEnrolmentQRsEntry\x1a\x38\n\x16TierEnrolmentUrlsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\x1a\x37\n\x15TierEnrolmentQRsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\"?\n\x14\x44\x61taCollectionFields\x12\'\n\x06\x66ields\x18\x01 \x03(\x0b\x32\x17.io.DataCollectionField\"\xe7\x02\n\x13\x44\x61taCollectionField\x12\x12\n\nuniqueName\x18\x01 \x01(\t\x12 \n\tfieldType\x18\x02 \x01(\x0e\x32\r.io.FieldType\x12\x12\n\nisRequired\x18\x03 \x01(\x08\x12\r\n\x05label\x18\x04 \x01(\t\x12+\n\x0elocalizedLabel\x18\x05 \x01(\x0b\x32\x13.io.LocalizedString\x12\x1e\n\x08\x64\x61taType\x18\x06 \x01(\x0e\x32\x0c.io.DataType\x12\x14\n\x0c\x64\x65\x66\x61ultValue\x18\x07 \x01(\t\x12\x32\n\x15localizedDefaultValue\x18\x08 \x01(\x0b\x32\x13.io.LocalizedString\x12\x12\n\nvalidation\x18\t \x01(\t\x12\x17\n\x0fuserCanSetValue\x18\n \x01(\x08\x12\x14\n\x0c\x63urrencyCode\x18\x0b \x01(\t\x12\x1d\n\x15\x64\x65\x66\x61ultTelCountryCode\x18\x0c \x01(\t\"H\n\x19SmartPassCsvUploadRequest\x12\x17\n\x0f\x64istributionUrl\x18\x01 \x01(\t\x12\x12\n\ncsvContent\x18\x02 \x01(\t\"`\n\x15ImportProtocolRequest\x12\x12\n\ncsvContent\x18\x01 \x01(\t\x12\x0f\n\x07\x63lassId\x18\x02 \x01(\t\x12\"\n\x08protocol\x18\x03 \x01(\x0e\x32\x10.io.PassProtocol*N\n\x13\x44istributionChannel\x12\x13\n\x0fNO_DISTRIBUTION\x10\x00\x12\x11\n\rCHANNEL_EMAIL\x10\x01\x12\x0f\n\x0b\x43HANNEL_SMS\x10\x02*x\n\x14\x45mailTemplateOptions\x12\x17\n\x13\x45MAIL_TEMP_OPT_NONE\x10\x00\x12\x1e\n\x1a\x45MAIL_TEMP_OPT_HIDE_EXT_ID\x10\x01\x12!\n\x1d\x45MAIL_TEMP_OPT_HIDE_FULL_NAME\x10\x02\"\x04\x08\x04\x10\x04\x42G\n\x10\x63om.passkit.grpcZ$stash.passkit.com/io/model/sdk/go/io\xaa\x02\x0cPassKit.Grpcb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'passkit.io.common.distribution_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n\020com.passkit.grpcZ$stash.passkit.com/io/model/sdk/go/io\252\002\014PassKit.Grpc'
  _globals['_SMARTPASSLINKREQUEST_FIELDSENTRY']._loaded_options = None
  _globals['_SMARTPASSLINKREQUEST_FIELDSENTRY']._serialized_options = b'8\001'
  _globals['_SMSTEMPLATE'].fields_by_name['content']._loaded_options = None
  _globals['_SMSTEMPLATE'].fields_by_name['content']._serialized_options = b'\222A\002xF'
  _globals['_SMSTEMPLATE'].fields_by_name['localizedContent']._loaded_options = None
  _globals['_SMSTEMPLATE'].fields_by_name['localizedContent']._serialized_options = b'\222A\002xF'
  _globals['_ENROLMENTURLS_TIERENROLMENTURLSENTRY']._loaded_options = None
  _globals['_ENROLMENTURLS_TIERENROLMENTURLSENTRY']._serialized_options = b'8\001'
  _globals['_ENROLMENTURLS_TIERENROLMENTQRSENTRY']._loaded_options = None
  _globals['_ENROLMENTURLS_TIERENROLMENTQRSENTRY']._serialized_options = b'8\001'
  _globals['_DISTRIBUTIONCHANNEL']._serialized_start=2720
  _globals['_DISTRIBUTIONCHANNEL']._serialized_end=2798
  _globals['_EMAILTEMPLATEOPTIONS']._serialized_start=2800
  _globals['_EMAILTEMPLATEOPTIONS']._serialized_end=2920
  _globals['_EMAILDISTRIBUTIONREQUEST']._serialized_start=240
  _globals['_EMAILDISTRIBUTIONREQUEST']._serialized_end=377
  _globals['_SMARTPASSLINKREQUEST']._serialized_start=380
  _globals['_SMARTPASSLINKREQUEST']._serialized_end=544
  _globals['_SMARTPASSLINKREQUEST_FIELDSENTRY']._serialized_start=499
  _globals['_SMARTPASSLINKREQUEST_FIELDSENTRY']._serialized_end=544
  _globals['_DISTRIBUTIONSETTINGS']._serialized_start=547
  _globals['_DISTRIBUTIONSETTINGS']._serialized_end=702
  _globals['_EMAILTEMPLATE']._serialized_start=705
  _globals['_EMAILTEMPLATE']._serialized_end=1591
  _globals['_EMAILCONFIGURATION']._serialized_start=1593
  _globals['_EMAILCONFIGURATION']._serialized_end=1715
  _globals['_SMSTEMPLATE']._serialized_start=1717
  _globals['_SMSTEMPLATE']._serialized_end=1814
  _globals['_ENROLMENTURLS']._serialized_start=1817
  _globals['_ENROLMENTURLS']._serialized_end=2119
  _globals['_ENROLMENTURLS_TIERENROLMENTURLSENTRY']._serialized_start=2006
  _globals['_ENROLMENTURLS_TIERENROLMENTURLSENTRY']._serialized_end=2062
  _globals['_ENROLMENTURLS_TIERENROLMENTQRSENTRY']._serialized_start=2064
  _globals['_ENROLMENTURLS_TIERENROLMENTQRSENTRY']._serialized_end=2119
  _globals['_DATACOLLECTIONFIELDS']._serialized_start=2121
  _globals['_DATACOLLECTIONFIELDS']._serialized_end=2184
  _globals['_DATACOLLECTIONFIELD']._serialized_start=2187
  _globals['_DATACOLLECTIONFIELD']._serialized_end=2546
  _globals['_SMARTPASSCSVUPLOADREQUEST']._serialized_start=2548
  _globals['_SMARTPASSCSVUPLOADREQUEST']._serialized_end=2620
  _globals['_IMPORTPROTOCOLREQUEST']._serialized_start=2622
  _globals['_IMPORTPROTOCOLREQUEST']._serialized_end=2718
# @@protoc_insertion_point(module_scope)
