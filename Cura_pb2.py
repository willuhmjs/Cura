# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: Cura.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='Cura.proto',
  package='Cura',
  serialized_pb=_b('\n\nCura.proto\x12\x04\x43ura\"+\n\nObjectList\x12\x1d\n\x07objects\x18\x01 \x03(\x0b\x32\x0c.Cura.Object\"H\n\x06Object\x12\n\n\x02id\x18\x01 \x01(\x03\x12\x10\n\x08vertices\x18\x02 \x01(\x0c\x12\x0f\n\x07normals\x18\x03 \x01(\x0c\x12\x0f\n\x07indices\x18\x04 \x01(\x0c\"\x1a\n\x08Progress\x12\x0e\n\x06\x61mount\x18\x01 \x01(\x02\"7\n\x10SlicedObjectList\x12#\n\x07objects\x18\x01 \x03(\x0b\x32\x12.Cura.SlicedObject\"7\n\x0cSlicedObject\x12\n\n\x02id\x18\x01 \x01(\x03\x12\x1b\n\x06layers\x18\x02 \x03(\x0b\x32\x0b.Cura.Layer\"4\n\x05Layer\x12\n\n\x02id\x18\x01 \x01(\x05\x12\x1f\n\x08polygons\x18\x02 \x03(\x0b\x32\r.Cura.Polygon\"\x9f\x01\n\x07Polygon\x12 \n\x04type\x18\x01 \x01(\x0e\x32\x12.Cura.Polygon.Type\x12\x0e\n\x06points\x18\x02 \x01(\x0c\"b\n\x04Type\x12\x0c\n\x08NoneType\x10\x00\x12\x0e\n\nInset0Type\x10\x01\x12\x0e\n\nInsetXType\x10\x02\x12\x0c\n\x08SkinType\x10\x03\x12\x0f\n\x0bSupportType\x10\x04\x12\r\n\tSkirtType\x10\x05\"&\n\nGCodeLayer\x12\n\n\x02id\x18\x01 \x01(\x03\x12\x0c\n\x04\x64\x61ta\x18\x02 \x01(\x0c\"+\n\x0fObjectPrintTime\x12\n\n\x02id\x18\x01 \x01(\x03\x12\x0c\n\x04time\x18\x02 \x01(\x02\".\n\x0bSettingList\x12\x1f\n\x08settings\x18\x01 \x03(\x0b\x32\r.Cura.Setting\"&\n\x07Setting\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\x0c\x62\x06proto3')
)
_sym_db.RegisterFileDescriptor(DESCRIPTOR)



_POLYGON_TYPE = _descriptor.EnumDescriptor(
  name='Type',
  full_name='Cura.Polygon.Type',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='NoneType', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='Inset0Type', index=1, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='InsetXType', index=2, number=2,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SkinType', index=3, number=3,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SupportType', index=4, number=4,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SkirtType', index=5, number=5,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=397,
  serialized_end=495,
)
_sym_db.RegisterEnumDescriptor(_POLYGON_TYPE)


_OBJECTLIST = _descriptor.Descriptor(
  name='ObjectList',
  full_name='Cura.ObjectList',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='objects', full_name='Cura.ObjectList.objects', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=20,
  serialized_end=63,
)


_OBJECT = _descriptor.Descriptor(
  name='Object',
  full_name='Cura.Object',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='Cura.Object.id', index=0,
      number=1, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='vertices', full_name='Cura.Object.vertices', index=1,
      number=2, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='normals', full_name='Cura.Object.normals', index=2,
      number=3, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='indices', full_name='Cura.Object.indices', index=3,
      number=4, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=65,
  serialized_end=137,
)


_PROGRESS = _descriptor.Descriptor(
  name='Progress',
  full_name='Cura.Progress',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='amount', full_name='Cura.Progress.amount', index=0,
      number=1, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=139,
  serialized_end=165,
)


_SLICEDOBJECTLIST = _descriptor.Descriptor(
  name='SlicedObjectList',
  full_name='Cura.SlicedObjectList',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='objects', full_name='Cura.SlicedObjectList.objects', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=167,
  serialized_end=222,
)


_SLICEDOBJECT = _descriptor.Descriptor(
  name='SlicedObject',
  full_name='Cura.SlicedObject',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='Cura.SlicedObject.id', index=0,
      number=1, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='layers', full_name='Cura.SlicedObject.layers', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=224,
  serialized_end=279,
)


_LAYER = _descriptor.Descriptor(
  name='Layer',
  full_name='Cura.Layer',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='Cura.Layer.id', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='polygons', full_name='Cura.Layer.polygons', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=281,
  serialized_end=333,
)


_POLYGON = _descriptor.Descriptor(
  name='Polygon',
  full_name='Cura.Polygon',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='type', full_name='Cura.Polygon.type', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='points', full_name='Cura.Polygon.points', index=1,
      number=2, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _POLYGON_TYPE,
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=336,
  serialized_end=495,
)


_GCODELAYER = _descriptor.Descriptor(
  name='GCodeLayer',
  full_name='Cura.GCodeLayer',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='Cura.GCodeLayer.id', index=0,
      number=1, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='data', full_name='Cura.GCodeLayer.data', index=1,
      number=2, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=497,
  serialized_end=535,
)


_OBJECTPRINTTIME = _descriptor.Descriptor(
  name='ObjectPrintTime',
  full_name='Cura.ObjectPrintTime',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='Cura.ObjectPrintTime.id', index=0,
      number=1, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='time', full_name='Cura.ObjectPrintTime.time', index=1,
      number=2, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=537,
  serialized_end=580,
)


_SETTINGLIST = _descriptor.Descriptor(
  name='SettingList',
  full_name='Cura.SettingList',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='settings', full_name='Cura.SettingList.settings', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=582,
  serialized_end=628,
)


_SETTING = _descriptor.Descriptor(
  name='Setting',
  full_name='Cura.Setting',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='Cura.Setting.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='value', full_name='Cura.Setting.value', index=1,
      number=2, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=630,
  serialized_end=668,
)

_OBJECTLIST.fields_by_name['objects'].message_type = _OBJECT
_SLICEDOBJECTLIST.fields_by_name['objects'].message_type = _SLICEDOBJECT
_SLICEDOBJECT.fields_by_name['layers'].message_type = _LAYER
_LAYER.fields_by_name['polygons'].message_type = _POLYGON
_POLYGON.fields_by_name['type'].enum_type = _POLYGON_TYPE
_POLYGON_TYPE.containing_type = _POLYGON
_SETTINGLIST.fields_by_name['settings'].message_type = _SETTING
DESCRIPTOR.message_types_by_name['ObjectList'] = _OBJECTLIST
DESCRIPTOR.message_types_by_name['Object'] = _OBJECT
DESCRIPTOR.message_types_by_name['Progress'] = _PROGRESS
DESCRIPTOR.message_types_by_name['SlicedObjectList'] = _SLICEDOBJECTLIST
DESCRIPTOR.message_types_by_name['SlicedObject'] = _SLICEDOBJECT
DESCRIPTOR.message_types_by_name['Layer'] = _LAYER
DESCRIPTOR.message_types_by_name['Polygon'] = _POLYGON
DESCRIPTOR.message_types_by_name['GCodeLayer'] = _GCODELAYER
DESCRIPTOR.message_types_by_name['ObjectPrintTime'] = _OBJECTPRINTTIME
DESCRIPTOR.message_types_by_name['SettingList'] = _SETTINGLIST
DESCRIPTOR.message_types_by_name['Setting'] = _SETTING

ObjectList = _reflection.GeneratedProtocolMessageType('ObjectList', (_message.Message,), dict(
  DESCRIPTOR = _OBJECTLIST,
  __module__ = 'Cura_pb2'
  # @@protoc_insertion_point(class_scope:Cura.ObjectList)
  ))
_sym_db.RegisterMessage(ObjectList)

Object = _reflection.GeneratedProtocolMessageType('Object', (_message.Message,), dict(
  DESCRIPTOR = _OBJECT,
  __module__ = 'Cura_pb2'
  # @@protoc_insertion_point(class_scope:Cura.Object)
  ))
_sym_db.RegisterMessage(Object)

Progress = _reflection.GeneratedProtocolMessageType('Progress', (_message.Message,), dict(
  DESCRIPTOR = _PROGRESS,
  __module__ = 'Cura_pb2'
  # @@protoc_insertion_point(class_scope:Cura.Progress)
  ))
_sym_db.RegisterMessage(Progress)

SlicedObjectList = _reflection.GeneratedProtocolMessageType('SlicedObjectList', (_message.Message,), dict(
  DESCRIPTOR = _SLICEDOBJECTLIST,
  __module__ = 'Cura_pb2'
  # @@protoc_insertion_point(class_scope:Cura.SlicedObjectList)
  ))
_sym_db.RegisterMessage(SlicedObjectList)

SlicedObject = _reflection.GeneratedProtocolMessageType('SlicedObject', (_message.Message,), dict(
  DESCRIPTOR = _SLICEDOBJECT,
  __module__ = 'Cura_pb2'
  # @@protoc_insertion_point(class_scope:Cura.SlicedObject)
  ))
_sym_db.RegisterMessage(SlicedObject)

Layer = _reflection.GeneratedProtocolMessageType('Layer', (_message.Message,), dict(
  DESCRIPTOR = _LAYER,
  __module__ = 'Cura_pb2'
  # @@protoc_insertion_point(class_scope:Cura.Layer)
  ))
_sym_db.RegisterMessage(Layer)

Polygon = _reflection.GeneratedProtocolMessageType('Polygon', (_message.Message,), dict(
  DESCRIPTOR = _POLYGON,
  __module__ = 'Cura_pb2'
  # @@protoc_insertion_point(class_scope:Cura.Polygon)
  ))
_sym_db.RegisterMessage(Polygon)

GCodeLayer = _reflection.GeneratedProtocolMessageType('GCodeLayer', (_message.Message,), dict(
  DESCRIPTOR = _GCODELAYER,
  __module__ = 'Cura_pb2'
  # @@protoc_insertion_point(class_scope:Cura.GCodeLayer)
  ))
_sym_db.RegisterMessage(GCodeLayer)

ObjectPrintTime = _reflection.GeneratedProtocolMessageType('ObjectPrintTime', (_message.Message,), dict(
  DESCRIPTOR = _OBJECTPRINTTIME,
  __module__ = 'Cura_pb2'
  # @@protoc_insertion_point(class_scope:Cura.ObjectPrintTime)
  ))
_sym_db.RegisterMessage(ObjectPrintTime)

SettingList = _reflection.GeneratedProtocolMessageType('SettingList', (_message.Message,), dict(
  DESCRIPTOR = _SETTINGLIST,
  __module__ = 'Cura_pb2'
  # @@protoc_insertion_point(class_scope:Cura.SettingList)
  ))
_sym_db.RegisterMessage(SettingList)

Setting = _reflection.GeneratedProtocolMessageType('Setting', (_message.Message,), dict(
  DESCRIPTOR = _SETTING,
  __module__ = 'Cura_pb2'
  # @@protoc_insertion_point(class_scope:Cura.Setting)
  ))
_sym_db.RegisterMessage(Setting)


# @@protoc_insertion_point(module_scope)
