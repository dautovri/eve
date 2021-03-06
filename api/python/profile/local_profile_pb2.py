# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: profile/local_profile.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='profile/local_profile.proto',
  package='org.lfedge.eve.profile',
  syntax='proto3',
  serialized_options=b'\n\026org.lfedge.eve.profileZ%github.com/lf-edge/eve/api/go/profile',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x1bprofile/local_profile.proto\x12\x16org.lfedge.eve.profile\";\n\x0cLocalProfile\x12\x15\n\rlocal_profile\x18\x01 \x01(\t\x12\x14\n\x0cserver_token\x18\x02 \x01(\tB?\n\x16org.lfedge.eve.profileZ%github.com/lf-edge/eve/api/go/profileb\x06proto3'
)




_LOCALPROFILE = _descriptor.Descriptor(
  name='LocalProfile',
  full_name='org.lfedge.eve.profile.LocalProfile',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='local_profile', full_name='org.lfedge.eve.profile.LocalProfile.local_profile', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='server_token', full_name='org.lfedge.eve.profile.LocalProfile.server_token', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=55,
  serialized_end=114,
)

DESCRIPTOR.message_types_by_name['LocalProfile'] = _LOCALPROFILE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

LocalProfile = _reflection.GeneratedProtocolMessageType('LocalProfile', (_message.Message,), {
  'DESCRIPTOR' : _LOCALPROFILE,
  '__module__' : 'profile.local_profile_pb2'
  # @@protoc_insertion_point(class_scope:org.lfedge.eve.profile.LocalProfile)
  })
_sym_db.RegisterMessage(LocalProfile)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
