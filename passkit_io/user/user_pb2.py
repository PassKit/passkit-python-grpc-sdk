# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: io/user/user.proto
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
    'io/user/user.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
from passkit_io.common import personal_pb2 as io_dot_common_dot_personal__pb2
from passkit_io.common import attributes_pb2 as io_dot_common_dot_attributes__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x12io/user/user.proto\x12\x02io\x1a\x1fgoogle/protobuf/timestamp.proto\x1a\x18io/common/personal.proto\x1a\x1aio/common/attributes.proto\"\xb4\x02\n\x08\x41uditLog\x12-\n\ttimestamp\x18\x01 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x11\n\tcompanyId\x18\x02 \x01(\t\x12\x10\n\x08username\x18\x03 \x01(\t\x12\x1e\n\x08userType\x18\x04 \x01(\x0e\x32\x0c.io.UserType\x12*\n\x0e\x61uthentication\x18\x05 \x01(\x0e\x32\x12.io.Authentication\x12\x1c\n\x07\x63hannel\x18\x06 \x01(\x0e\x32\x0b.io.Channel\x12\x11\n\tipAddress\x18\x07 \x01(\t\x12\x10\n\x08\x65ndpoint\x18\x08 \x01(\t\x12\x0f\n\x07payload\x18\t \x01(\t\x12\x12\n\nstatusCode\x18\n \x01(\r\x12\x0e\n\x06status\x18\x0b \x01(\t\x12\x10\n\x08response\x18\x0c \x01(\t\"v\n\x0f\x41uditLogRequest\x12\x10\n\x08username\x18\x01 \x01(\t\x12.\n\nbeforeTime\x18\x02 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\r\n\x05limit\x18\x03 \x01(\r\x12\x12\n\nerrorsOnly\x18\x04 \x01(\x08\"\xee\x01\n\x0fNewUserResponse\x12\x0e\n\x06userId\x18\x01 \x01(\t\x12\x11\n\tcompanyId\x18\x02 \x01(\t\x12\x10\n\x08username\x18\x03 \x01(\t\x12\x14\n\x0c\x65mailAddress\x18\x04 \x01(\t\x12\x0e\n\x06secret\x18\x05 \x01(\t\x12\x13\n\x0b\x63\x65rtificate\x18\x06 \x01(\t\x12\x12\n\nprivateKey\x18\x07 \x01(\t\x12\x16\n\x0ejavaPrivateKey\x18\x08 \x01(\t\x12-\n\texpiresAt\x18\t \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x10\n\x08regionId\x18\n \x01(\t\"\xcf\x01\n\x07NewUser\x12\x10\n\x08username\x18\x01 \x01(\t\x12\x10\n\x08password\x18\x02 \x01(\t\x12\x14\n\x0c\x65mailAddress\x18\x03 \x01(\t\x12\x11\n\tsendEmail\x18\x04 \x01(\x08\x12\x13\n\x0b\x63ompanyName\x18\x05 \x01(\t\x12\x14\n\x0cmobileNumber\x18\x06 \x01(\t\x12\x15\n\rtwoFactorAuth\x18\x07 \x01(\x08\x12\x0f\n\x07isOwner\x18\x08 \x01(\x08\x12\x10\n\x08readOnly\x18\t \x01(\x08\x12\x12\n\nteamMember\x18\n \x01(\x08\"\xf5\x01\n\x0fGetUserResponse\x12\r\n\x05\x65mail\x18\x01 \x01(\t\x12\x10\n\x08username\x18\x02 \x01(\t\x12\x11\n\tcompanyId\x18\x03 \x01(\t\x12\x13\n\x0b\x63ompanyName\x18\x04 \x01(\t\x12\x15\n\rcompanyStatus\x18\x05 \x01(\x04\x12-\n\tcreatedAt\x18\x06 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12-\n\texpiresAt\x18\x07 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x10\n\x08regionId\x18\x08 \x01(\t\x12\x12\n\nuserStatus\x18\t \x01(\x04\"i\n\x0b\x42illingMeta\x12\x13\n\x0b\x63ompanyName\x18\x01 \x01(\t\x12\r\n\x05taxId\x18\x02 \x01(\t\x12\x11\n\treference\x18\x03 \x01(\t\x12#\n\x0e\x62illingAddress\x18\x04 \x01(\x0b\x32\x0b.io.Address\"X\n\x0b\x43redentials\x12\x10\n\x08username\x18\x01 \x01(\t\x12\x10\n\x08password\x18\x02 \x01(\t\x12\x12\n\ntwoFAToken\x18\x03 \x01(\t\x12\x11\n\ttwoFACode\x18\x04 \x01(\t\"+\n\rVerifyRequest\x12\x0b\n\x03uid\x18\x01 \x01(\t\x12\r\n\x05token\x18\x02 \x01(\t\"\x14\n\x03JWT\x12\r\n\x05token\x18\x01 \x01(\t\"j\n\x12PasswordResetInput\x12\n\n\x02id\x18\x01 \x01(\t\x12\x17\n\x0fregisteredEmail\x18\x02 \x01(\t\x12\x13\n\x0bnewPassword\x18\x03 \x01(\t\x12\x1a\n\x12\x63onfirmNewPassword\x18\x04 \x01(\t\"\x1c\n\x08Username\x12\x10\n\x08username\x18\x01 \x01(\t\"k\n\x1aOAuth2AuthorizationRequest\x12\x12\n\nclientCode\x18\x01 \x01(\t\x12$\n\x08provider\x18\x02 \x01(\x0e\x32\x12.io.OAuth2Provider\x12\x13\n\x0bredirectUri\x18\x03 \x01(\t\"\x8c\x02\n\x14ScannerConfiguration\x12?\n\x15membershipPermissions\x18\x01 \x03(\x0e\x32 .io.ScannerMembershipPermissions\x12\x37\n\x11\x63ouponPermissions\x18\x02 \x03(\x0e\x32\x1c.io.ScannerCouponPermissions\x12@\n\x17\x64\x65\x66\x61ultMembershipAction\x18\x03 \x03(\x0e\x32\x1f.io.DefaultMembershipScanAction\x12\x38\n\x13\x64\x65\x66\x61ultCouponAction\x18\x04 \x03(\x0e\x32\x1b.io.DefaultCouponScanAction\"\x16\n\x05\x45mail\x12\r\n\x05\x65mail\x18\x01 \x01(\t\"L\n\x17\x43onfirmEmailChangeInput\x12\x10\n\x08username\x18\x01 \x01(\t\x12\x10\n\x08password\x18\x02 \x01(\t\x12\r\n\x05token\x18\x03 \x01(\t\"\"\n\x0b\x43ompanyName\x12\x13\n\x0b\x63ompanyName\x18\x01 \x01(\t\"Z\n\x14\x44\x65leteAccountRequest\x12\x10\n\x08username\x18\x01 \x01(\t\x12\x10\n\x08password\x18\x02 \x01(\t\x12\x1e\n\x16\x63onfirmPermanentDelete\x18\x03 \x01(\x08\" \n\x0cProjectsList\x12\x10\n\x08projects\x18\x01 \x03(\t\"(\n\x10\x43\x65rtificatesList\x12\x14\n\x0c\x63\x65rtificates\x18\x01 \x03(\t\" \n\x0cProtocolList\x12\x10\n\x08\x63lassIds\x18\x01 \x03(\t\"\x8c\x03\n\x13ResourcePermissions\x12+\n\x0f\x61llowedProjects\x18\x01 \x01(\x0b\x32\x10.io.ProjectsListH\x00\x12.\n\x12\x64isallowedProjects\x18\x02 \x01(\x0b\x32\x10.io.ProjectsListH\x00\x12\x33\n\x13\x61llowedCertificates\x18\x03 \x01(\x0b\x32\x14.io.CertificatesListH\x01\x12\x36\n\x16\x64isallowedCertificates\x18\x04 \x01(\x0b\x32\x14.io.CertificatesListH\x01\x12+\n\x0f\x61llowedPrograms\x18\x05 \x01(\x0b\x32\x10.io.ProtocolListH\x02\x12.\n\x12\x64isallowedPrograms\x18\x06 \x01(\x0b\x32\x10.io.ProtocolListH\x02\x42\x14\n\x12ProjectPermissionsB\x18\n\x16\x43\x65rtificatePermissionsB\x1e\n\x1cMembershipProgramPermissions\"\x97\x02\n\x15TeamMemberPermissions\x12\n\n\x02id\x18\x01 \x01(\t\x12\x0e\n\x06userId\x18\x02 \x01(\t\x12,\n\x0fpermissionScope\x18\x03 \x01(\x0e\x32\x13.io.PermissionScope\x12$\n\x06status\x18\x04 \x01(\x0e\x32\x14.io.TeamMemberStatus\x12\x34\n\x13resourcePermissions\x18\x05 \x01(\x0b\x32\x17.io.ResourcePermissions\x12+\n\x07\x63reated\x18\x06 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12+\n\x07updated\x18\x07 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\"Z\n\rNewTeamMember\x12\x19\n\x04user\x18\x01 \x01(\x0b\x32\x0b.io.NewUser\x12.\n\x0bpermissions\x18\x02 \x01(\x0b\x32\x19.io.TeamMemberPermissions\"j\n\x15GetTeamMemberResponse\x12!\n\x04user\x18\x01 \x01(\x0b\x32\x13.io.GetUserResponse\x12.\n\x0bpermissions\x18\x02 \x01(\x0b\x32\x19.io.TeamMemberPermissions\"[\n\x17ListTeamMembersResponse\x12\x0b\n\x03uid\x18\x01 \x01(\t\x12\r\n\x05\x65mail\x18\x02 \x01(\t\x12$\n\x06status\x18\x03 \x01(\x0e\x32\x14.io.TeamMemberStatus*q\n\x0eOAuth2Provider\x12\x14\n\x10OAUTH_DO_NOT_USE\x10\x00\x12\x11\n\rOAUTH_PATREON\x10\n\x12\x10\n\x0cOAUTH_SPROUT\x10\x32\x12\x13\n\x0fOAUTH_MAILCHIMP\x10\x64\x12\x0f\n\nOAUTH_XERO\x10\x96\x01*\xc6\x03\n\x1cScannerMembershipPermissions\x12\x1e\n\x1aMEMBERSHIP_PERMISSION_NONE\x10\x00\x12%\n!MEMBERSHIP_PERMISSION_VIEW_MEMBER\x10\x01\x12%\n!MEMBERSHIP_PERMISSION_EDIT_MEMBER\x10\x02\x12%\n!MEMBERSHIP_PERMISSION_EARN_POINTS\x10\x04\x12%\n!MEMBERSHIP_PERMISSION_BURN_POINTS\x10\x08\x12$\n MEMBERSHIP_PERMISSION_SET_POINTS\x10\x10\x12%\n!MEMBERSHIP_PERMISSION_CHANGE_TIER\x10 \x12%\n!MEMBERSHIP_PERMISSION_VIEW_EVENTS\x10@\x12(\n#MEMBERSHIP_PERMISSION_CHANGE_EXPIRY\x10\x80\x01\x12\'\n\"MEMBERSHIP_PERMISSION_CHECK_IN_OUT\x10\x80\x02\x12#\n\x1eMEMBERSHIP_PERMISSION_VALIDATE\x10\x80\x04*\x82\x02\n\x18ScannerCouponPermissions\x12\x1a\n\x16\x43OUPON_PERMISSION_NONE\x10\x00\x12!\n\x1d\x43OUPON_PERMISSION_VIEW_COUPON\x10\x01\x12!\n\x1d\x43OUPON_PERMISSION_EDIT_COUPON\x10\x02\x12\x1c\n\x18\x43OUPON_PERMISSION_REDEEM\x10\x04\x12!\n\x1d\x43OUPON_PERMISSION_VIEW_EVENTS\x10\x08\x12#\n\x1f\x43OUPON_PERMISSION_CHANGE_EXPIRY\x10\x10\x12\x1e\n\x1a\x43OUPON_PERMISSION_VALIDATE\x10 *\xc8\x01\n\x1b\x44\x65\x66\x61ultMembershipScanAction\x12\x1b\n\x17MEMBERSHIP_DEFAULT_NONE\x10\x00\x12\"\n\x1eMEMBERSHIP_DEFAULT_EARN_POINTS\x10\x01\x12\"\n\x1eMEMBERSHIP_DEFAULT_BURN_POINTS\x10\x02\x12#\n\x1fMEMBERSHIP_DEFAULT_CHECK_IN_OUT\x10\x04\x12\x1f\n\x1bMEMBERSHIP_DEFAULT_VALIDATE\x10\x08*j\n\x17\x44\x65\x66\x61ultCouponScanAction\x12\x17\n\x13\x43OUPON_DEFAULT_NONE\x10\x00\x12\x19\n\x15\x43OUPON_DEFAULT_REDEEM\x10\x01\x12\x1b\n\x17\x43OUPON_DEFAULT_VALIDATE\x10\x02*\xed\x01\n\x0fPermissionScope\x12\x13\n\x0fPERMISSION_NONE\x10\x00\x12\x0e\n\nWEB_ACCESS\x10\x01\x12\x0e\n\nAPP_ACCESS\x10\x02\x12\x10\n\x0c\x41LL_PROJECTS\x10\x04\x12\x14\n\x10\x41LL_CERTIFICATES\x10\x08\x12\x12\n\x0e\x42ILLING_ACCESS\x10\x10\x12\x17\n\x13\x43\x45RTIFICATES_ACCESS\x10 \x12\x12\n\x0eMEMBERS_ACCESS\x10@\x12\x13\n\x0e\x43OUPONS_ACCESS\x10\x80\x01\x12\x12\n\rEVENTS_ACCESS\x10\x80\x02\x12\x13\n\x0e\x46LIGHTS_ACCESS\x10\x80\x04*\x87\x01\n\x10TeamMemberStatus\x12\x0f\n\x0bSTATUS_NONE\x10\x00\x12\x16\n\x12TEAM_MEMBER_ACTIVE\x10\x01\x12\x18\n\x14TEAM_MEMBER_DISABLED\x10\x02\x12\x17\n\x13TEAM_MEMBER_EXPIRED\x10\x04\x12\x17\n\x13TEAM_MEMBER_PENDING\x10\x08\x42G\n\x10\x63om.passkit.grpcZ$stash.passkit.com/io/model/sdk/go/io\xaa\x02\x0cPassKit.Grpcb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'io.user.user_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n\020com.passkit.grpcZ$stash.passkit.com/io/model/sdk/go/io\252\002\014PassKit.Grpc'
  _globals['_OAUTH2PROVIDER']._serialized_start=3339
  _globals['_OAUTH2PROVIDER']._serialized_end=3452
  _globals['_SCANNERMEMBERSHIPPERMISSIONS']._serialized_start=3455
  _globals['_SCANNERMEMBERSHIPPERMISSIONS']._serialized_end=3909
  _globals['_SCANNERCOUPONPERMISSIONS']._serialized_start=3912
  _globals['_SCANNERCOUPONPERMISSIONS']._serialized_end=4170
  _globals['_DEFAULTMEMBERSHIPSCANACTION']._serialized_start=4173
  _globals['_DEFAULTMEMBERSHIPSCANACTION']._serialized_end=4373
  _globals['_DEFAULTCOUPONSCANACTION']._serialized_start=4375
  _globals['_DEFAULTCOUPONSCANACTION']._serialized_end=4481
  _globals['_PERMISSIONSCOPE']._serialized_start=4484
  _globals['_PERMISSIONSCOPE']._serialized_end=4721
  _globals['_TEAMMEMBERSTATUS']._serialized_start=4724
  _globals['_TEAMMEMBERSTATUS']._serialized_end=4859
  _globals['_AUDITLOG']._serialized_start=114
  _globals['_AUDITLOG']._serialized_end=422
  _globals['_AUDITLOGREQUEST']._serialized_start=424
  _globals['_AUDITLOGREQUEST']._serialized_end=542
  _globals['_NEWUSERRESPONSE']._serialized_start=545
  _globals['_NEWUSERRESPONSE']._serialized_end=783
  _globals['_NEWUSER']._serialized_start=786
  _globals['_NEWUSER']._serialized_end=993
  _globals['_GETUSERRESPONSE']._serialized_start=996
  _globals['_GETUSERRESPONSE']._serialized_end=1241
  _globals['_BILLINGMETA']._serialized_start=1243
  _globals['_BILLINGMETA']._serialized_end=1348
  _globals['_CREDENTIALS']._serialized_start=1350
  _globals['_CREDENTIALS']._serialized_end=1438
  _globals['_VERIFYREQUEST']._serialized_start=1440
  _globals['_VERIFYREQUEST']._serialized_end=1483
  _globals['_JWT']._serialized_start=1485
  _globals['_JWT']._serialized_end=1505
  _globals['_PASSWORDRESETINPUT']._serialized_start=1507
  _globals['_PASSWORDRESETINPUT']._serialized_end=1613
  _globals['_USERNAME']._serialized_start=1615
  _globals['_USERNAME']._serialized_end=1643
  _globals['_OAUTH2AUTHORIZATIONREQUEST']._serialized_start=1645
  _globals['_OAUTH2AUTHORIZATIONREQUEST']._serialized_end=1752
  _globals['_SCANNERCONFIGURATION']._serialized_start=1755
  _globals['_SCANNERCONFIGURATION']._serialized_end=2023
  _globals['_EMAIL']._serialized_start=2025
  _globals['_EMAIL']._serialized_end=2047
  _globals['_CONFIRMEMAILCHANGEINPUT']._serialized_start=2049
  _globals['_CONFIRMEMAILCHANGEINPUT']._serialized_end=2125
  _globals['_COMPANYNAME']._serialized_start=2127
  _globals['_COMPANYNAME']._serialized_end=2161
  _globals['_DELETEACCOUNTREQUEST']._serialized_start=2163
  _globals['_DELETEACCOUNTREQUEST']._serialized_end=2253
  _globals['_PROJECTSLIST']._serialized_start=2255
  _globals['_PROJECTSLIST']._serialized_end=2287
  _globals['_CERTIFICATESLIST']._serialized_start=2289
  _globals['_CERTIFICATESLIST']._serialized_end=2329
  _globals['_PROTOCOLLIST']._serialized_start=2331
  _globals['_PROTOCOLLIST']._serialized_end=2363
  _globals['_RESOURCEPERMISSIONS']._serialized_start=2366
  _globals['_RESOURCEPERMISSIONS']._serialized_end=2762
  _globals['_TEAMMEMBERPERMISSIONS']._serialized_start=2765
  _globals['_TEAMMEMBERPERMISSIONS']._serialized_end=3044
  _globals['_NEWTEAMMEMBER']._serialized_start=3046
  _globals['_NEWTEAMMEMBER']._serialized_end=3136
  _globals['_GETTEAMMEMBERRESPONSE']._serialized_start=3138
  _globals['_GETTEAMMEMBERRESPONSE']._serialized_end=3244
  _globals['_LISTTEAMMEMBERSRESPONSE']._serialized_start=3246
  _globals['_LISTTEAMMEMBERSRESPONSE']._serialized_end=3337
# @@protoc_insertion_point(module_scope)
