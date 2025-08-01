# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: passkit/io/certificate/certificate.proto
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
    'passkit/io/certificate/certificate.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n(passkit/io/certificate/certificate.proto\x12\x02io\x1a\x1fgoogle/protobuf/timestamp.proto\"\xf5\x01\n\x0f\x43\x65rtificateData\x12\x12\n\npassTypeId\x18\x01 \x01(\t\x12\x0e\n\x06teamId\x18\x02 \x01(\t\x12\x10\n\x08teamName\x18\x03 \x01(\t\x12\x14\n\x0cserialNumber\x18\x04 \x01(\t\x12-\n\tvalidFrom\x18\x05 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12+\n\x07validTo\x18\x06 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x0f\n\x07modulus\x18\x07 \x01(\t\x12\x12\n\nnfcCapable\x18\x08 \x01(\x08\x12\x15\n\rownerUsername\x18\t \x01(\t\"v\n\x11PrivateKeyRequest\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x13\n\x0b\x64\x65scription\x18\x02 \x01(\t\x12*\n\x06\x65xpiry\x18\x03 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x12\n\nprivateKey\x18\x04 \x01(\x0c\"Q\n\x15TLSCertificateRequest\x12\x13\n\x0b\x63\x65rtificate\x18\x01 \x01(\x0c\x12\x0f\n\x07\x63\x61\x43hain\x18\x02 \x01(\x0c\x12\x12\n\nprivateKey\x18\x03 \x01(\x0c\"\xef\x01\n\x12TLSCertificateData\x12\n\n\x02id\x18\x01 \x01(\t\x12\x12\n\ncommonName\x18\x02 \x01(\t\x12\x14\n\x0cserialNumber\x18\x03 \x01(\t\x12-\n\tvalidFrom\x18\x04 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12+\n\x07validTo\x18\x05 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x0f\n\x07modulus\x18\x06 \x01(\t\x12\x1f\n\x17subjectAlternativeNames\x18\x07 \x03(\t\x12\x15\n\rownerUsername\x18\x08 \x01(\t\"\x82\x01\n\x0ePrivateKeyData\x12\n\n\x02id\x18\x01 \x01(\t\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\x13\n\x0b\x64\x65scription\x18\x03 \x01(\t\x12*\n\x06\x65xpiry\x18\x04 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x15\n\rownerUsername\x18\x05 \x01(\t\"(\n\x12PassTypeIdentifier\x12\x12\n\npassTypeId\x18\x01 \x01(\t\"(\n\x19\x43\x65rtificateSigningRequest\x12\x0b\n\x03\x63sr\x18\x01 \x01(\t\"F\n\x1cNFCSigningCredentialsRequest\x12\x10\n\x08password\x18\x01 \x01(\t\x12\x14\n\x0cprivateKeyId\x18\x02 \x01(\tBG\n\x10\x63om.passkit.grpcZ$stash.passkit.com/io/model/sdk/go/io\xaa\x02\x0cPassKit.Grpcb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'passkit.io.certificate.certificate_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n\020com.passkit.grpcZ$stash.passkit.com/io/model/sdk/go/io\252\002\014PassKit.Grpc'
  _globals['_CERTIFICATEDATA']._serialized_start=82
  _globals['_CERTIFICATEDATA']._serialized_end=327
  _globals['_PRIVATEKEYREQUEST']._serialized_start=329
  _globals['_PRIVATEKEYREQUEST']._serialized_end=447
  _globals['_TLSCERTIFICATEREQUEST']._serialized_start=449
  _globals['_TLSCERTIFICATEREQUEST']._serialized_end=530
  _globals['_TLSCERTIFICATEDATA']._serialized_start=533
  _globals['_TLSCERTIFICATEDATA']._serialized_end=772
  _globals['_PRIVATEKEYDATA']._serialized_start=775
  _globals['_PRIVATEKEYDATA']._serialized_end=905
  _globals['_PASSTYPEIDENTIFIER']._serialized_start=907
  _globals['_PASSTYPEIDENTIFIER']._serialized_end=947
  _globals['_CERTIFICATESIGNINGREQUEST']._serialized_start=949
  _globals['_CERTIFICATESIGNINGREQUEST']._serialized_end=989
  _globals['_NFCSIGNINGCREDENTIALSREQUEST']._serialized_start=991
  _globals['_NFCSIGNINGCREDENTIALSREQUEST']._serialized_end=1061
# @@protoc_insertion_point(module_scope)
