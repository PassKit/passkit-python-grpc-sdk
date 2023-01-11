# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: io/raw/a_rpc.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2
from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from io.common import common_objects_pb2 as io_dot_common_dot_common__objects__pb2
from io.raw import project_pb2 as io_dot_raw_dot_project__pb2
from io.raw import pass_pb2 as io_dot_raw_dot_pass__pb2
from protoc_gen_openapiv2.options import annotations_pb2 as protoc__gen__openapiv2_dot_options_dot_annotations__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x12io/raw/a_rpc.proto\x12\x03raw\x1a\x1bgoogle/protobuf/empty.proto\x1a\x1cgoogle/api/annotations.proto\x1a\x1eio/common/common_objects.proto\x1a\x14io/raw/project.proto\x1a\x11io/raw/pass.proto\x1a.protoc-gen-openapiv2/options/annotations.proto2\xd8\x0f\n\x03Raw\x12\x7f\n\x11\x63reatePassProject\x12\x10.raw.PassProject\x1a\x06.io.Id\"P\x82\xd3\xe4\x93\x02\x15\"\x10/raw/passProject:\x01*\x92\x41\x32\n\x03Raw\x12\x13\x43reate Pass Project\x1a\x16\x43reates a Pass Project\x12\x93\x01\n\x11updatePassProject\x12\x10.raw.PassProject\x1a\x10.raw.PassProject\"Z\x82\xd3\xe4\x93\x02\x15\x1a\x10/raw/passProject:\x01*\x92\x41<\n\x03Raw\x12\x13Update Pass Project\x1a Updates an existing Pass Project\x12\x82\x01\n\x0egetPassProject\x12\x06.io.Id\x1a\x10.raw.PassProject\"V\x82\xd3\xe4\x93\x02\x17\x12\x15/raw/passProject/{id}\x92\x41\x36\n\x03Raw\x12\x10Get Pass Project\x1a\x1dGets an existing Pass Project\x12\x94\x01\n\x0f\x63opyPassProject\x12\x1b.raw.PassProjectCopyRequest\x1a\x06.io.Id\"\\\x82\xd3\xe4\x93\x02\x1a\"\x15/raw/passProject/copy:\x01*\x92\x41\x39\n\x03Raw\x12\x11\x43opy Pass Project\x1a\x1f\x43opies an existing Pass Project\x12\x84\x02\n\x11\x64\x65letePassProject\x12\x06.io.Id\x1a\x16.google.protobuf.Empty\"\xce\x01\x82\xd3\xe4\x93\x02\x17*\x15/raw/passProject/{id}\x92\x41\xad\x01\n\x03Raw\x12\x13\x44\x65lete Pass Project\x1a\x90\x01\x44\x65letes an existing Pass Project by id. Deleting a Pass Project results in all passes being invalidated and removed. Needs to be used with care.\x12\x65\n\ncreatePass\x12\t.raw.Pass\x1a\x06.io.Id\"D\x82\xd3\xe4\x93\x02\x0e\"\t/raw/pass:\x01*\x92\x41-\n\x03Raw\x12\x0b\x43reate Pass\x1a\x19\x43reates a new Pass record\x12k\n\nupdatePass\x12\t.raw.Pass\x1a\x06.io.Id\"J\x82\xd3\xe4\x93\x02\x0e\x1a\t/raw/pass:\x01*\x92\x41\x33\n\x03Raw\x12\x0bUpdate Pass\x1a\x1fUpdates an existing Pass record\x12\x92\x01\n\x11streamPassUpdates\x12\t.raw.Pass\x1a\x06.io.Id\"f\x92\x41\x63\n\x03Raw\x12\x32Stream Pass Updates (official SDK\'s only, no REST)\x1a(Updates existing Pass records via stream(\x01\x30\x01\x12\x64\n\x0bgetPassById\x12\x06.io.Id\x1a\t.raw.Pass\"B\x82\xd3\xe4\x93\x02\x10\x12\x0e/raw/pass/{id}\x92\x41)\n\x03Raw\x12\x0eGet Pass by ID\x1a\x12Gets a pass record\x12\xc3\x01\n\x13getPassByExternalId\x12\".raw.PassRecordByExternalIdRequest\x1a\t.raw.Pass\"}\x82\xd3\xe4\x93\x02\x33\x12\x31/raw/pass/externalId/{passProjectId}/{externalId}\x92\x41\x41\n\x03Raw\x12\x17Get Pass by External ID\x1a!Gets a pass record by External ID\x12v\n\ndeletePass\x12\t.raw.Pass\x1a\x16.google.protobuf.Empty\"E\x82\xd3\xe4\x93\x02\x13*\x0e/raw/pass/{id}:\x01*\x92\x41)\n\x03Raw\x12\x0b\x44\x65lete Pass\x1a\x15\x44\x65letes a pass record\x12\xc0\x01\n\x17listPassesByPassProject\x12#.raw.ListPassesByPassProjectRequest\x1a\t.raw.Pass\"s\x82\xd3\xe4\x93\x02 \"\x1b/raw/pass/listByPassProject:\x01*\x92\x41J\n\x03Raw\x12\x0bList Passes\x1a\x36List all passes for pass project. Supports pagination.0\x01\x12\xc6\x01\n\x18listPassesByPassTemplate\x12$.raw.ListPassesByPassTemplateRequest\x1a\t.raw.Pass\"w\x82\xd3\xe4\x93\x02!\"\x1c/raw/pass/listByPassTemplate:\x01*\x92\x41M\n\x03Raw\x12\x0bList Passes\x1a\x39List all passes for a pass template. Supports pagination.0\x01\x42\x8a\x07\n\x14\x63om.passkit.grpc.RawZ(stash.passkit.com/io/model/sdk/go/io/raw\xaa\x02\x10PassKit.Grpc.Raw\x92\x41\xb3\x06\x12\xc0\x02\n\x16PassKit Raw Passes API\x12\xa5\x01This protocol is suit for cases where the business logic is handled elsewhere, and the purpose is purely to issue and update content for Apple Wallet and Google Pay.\x1a\x38https://passkit.com/legal/terms-of-subscription-service/\"?\n\x0fPassKit Support\x12\x17https://docs.passkit.io\x1a\x13support@passkit.com2\x03\x30.1*\x01\x02\x32\x10\x61pplication/json:\x10\x61pplication/jsonR9\n\x03\x32\x30\x30\x12\x32\n(Returned when the request is successful.\x12\x06\n\x04\x9a\x02\x01\x07R4\n\x03\x34\x30\x30\x12-\n+Returned when wrong user input is provided.R0\n\x03\x34\x30\x31\x12)\n\'Returned when the user is unauthorized.RP\n\x03\x34\x30\x33\x12I\nGReturned when the user does not have permission to access the resource.R;\n\x03\x34\x30\x34\x12\x34\n*Returned when the resource does not exist.\x12\x06\n\x04\x9a\x02\x01\x07R<\n\x03\x35\x30\x30\x12\x35\n+Returned when there is an unexpected error.\x12\x06\n\x04\x9a\x02\x01\x07RW\n\x03\x35\x30\x33\x12P\nNServer is unavailable. Back off for 250ms and repeat request until successful.b\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'io.raw.a_rpc_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\024com.passkit.grpc.RawZ(stash.passkit.com/io/model/sdk/go/io/raw\252\002\020PassKit.Grpc.Raw\222A\263\006\022\300\002\n\026PassKit Raw Passes API\022\245\001This protocol is suit for cases where the business logic is handled elsewhere, and the purpose is purely to issue and update content for Apple Wallet and Google Pay.\0328https://passkit.com/legal/terms-of-subscription-service/\"?\n\017PassKit Support\022\027https://docs.passkit.io\032\023support@passkit.com2\0030.1*\001\0022\020application/json:\020application/jsonR9\n\003200\0222\n(Returned when the request is successful.\022\006\n\004\232\002\001\007R4\n\003400\022-\n+Returned when wrong user input is provided.R0\n\003401\022)\n\'Returned when the user is unauthorized.RP\n\003403\022I\nGReturned when the user does not have permission to access the resource.R;\n\003404\0224\n*Returned when the resource does not exist.\022\006\n\004\232\002\001\007R<\n\003500\0225\n+Returned when there is an unexpected error.\022\006\n\004\232\002\001\007RW\n\003503\022P\nNServer is unavailable. Back off for 250ms and repeat request until successful.'
  _RAW.methods_by_name['createPassProject']._options = None
  _RAW.methods_by_name['createPassProject']._serialized_options = b'\202\323\344\223\002\025\"\020/raw/passProject:\001*\222A2\n\003Raw\022\023Create Pass Project\032\026Creates a Pass Project'
  _RAW.methods_by_name['updatePassProject']._options = None
  _RAW.methods_by_name['updatePassProject']._serialized_options = b'\202\323\344\223\002\025\032\020/raw/passProject:\001*\222A<\n\003Raw\022\023Update Pass Project\032 Updates an existing Pass Project'
  _RAW.methods_by_name['getPassProject']._options = None
  _RAW.methods_by_name['getPassProject']._serialized_options = b'\202\323\344\223\002\027\022\025/raw/passProject/{id}\222A6\n\003Raw\022\020Get Pass Project\032\035Gets an existing Pass Project'
  _RAW.methods_by_name['copyPassProject']._options = None
  _RAW.methods_by_name['copyPassProject']._serialized_options = b'\202\323\344\223\002\032\"\025/raw/passProject/copy:\001*\222A9\n\003Raw\022\021Copy Pass Project\032\037Copies an existing Pass Project'
  _RAW.methods_by_name['deletePassProject']._options = None
  _RAW.methods_by_name['deletePassProject']._serialized_options = b'\202\323\344\223\002\027*\025/raw/passProject/{id}\222A\255\001\n\003Raw\022\023Delete Pass Project\032\220\001Deletes an existing Pass Project by id. Deleting a Pass Project results in all passes being invalidated and removed. Needs to be used with care.'
  _RAW.methods_by_name['createPass']._options = None
  _RAW.methods_by_name['createPass']._serialized_options = b'\202\323\344\223\002\016\"\t/raw/pass:\001*\222A-\n\003Raw\022\013Create Pass\032\031Creates a new Pass record'
  _RAW.methods_by_name['updatePass']._options = None
  _RAW.methods_by_name['updatePass']._serialized_options = b'\202\323\344\223\002\016\032\t/raw/pass:\001*\222A3\n\003Raw\022\013Update Pass\032\037Updates an existing Pass record'
  _RAW.methods_by_name['streamPassUpdates']._options = None
  _RAW.methods_by_name['streamPassUpdates']._serialized_options = b'\222Ac\n\003Raw\0222Stream Pass Updates (official SDK\'s only, no REST)\032(Updates existing Pass records via stream'
  _RAW.methods_by_name['getPassById']._options = None
  _RAW.methods_by_name['getPassById']._serialized_options = b'\202\323\344\223\002\020\022\016/raw/pass/{id}\222A)\n\003Raw\022\016Get Pass by ID\032\022Gets a pass record'
  _RAW.methods_by_name['getPassByExternalId']._options = None
  _RAW.methods_by_name['getPassByExternalId']._serialized_options = b'\202\323\344\223\0023\0221/raw/pass/externalId/{passProjectId}/{externalId}\222AA\n\003Raw\022\027Get Pass by External ID\032!Gets a pass record by External ID'
  _RAW.methods_by_name['deletePass']._options = None
  _RAW.methods_by_name['deletePass']._serialized_options = b'\202\323\344\223\002\023*\016/raw/pass/{id}:\001*\222A)\n\003Raw\022\013Delete Pass\032\025Deletes a pass record'
  _RAW.methods_by_name['listPassesByPassProject']._options = None
  _RAW.methods_by_name['listPassesByPassProject']._serialized_options = b'\202\323\344\223\002 \"\033/raw/pass/listByPassProject:\001*\222AJ\n\003Raw\022\013List Passes\0326List all passes for pass project. Supports pagination.'
  _RAW.methods_by_name['listPassesByPassTemplate']._options = None
  _RAW.methods_by_name['listPassesByPassTemplate']._serialized_options = b'\202\323\344\223\002!\"\034/raw/pass/listByPassTemplate:\001*\222AM\n\003Raw\022\013List Passes\0329List all passes for a pass template. Supports pagination.'
  _RAW._serialized_start=208
  _RAW._serialized_end=2216
# @@protoc_insertion_point(module_scope)