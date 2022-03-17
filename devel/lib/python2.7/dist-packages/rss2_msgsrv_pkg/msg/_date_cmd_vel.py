# This Python file uses the following encoding: utf-8
"""autogenerated by genpy from rss2_msgsrv_pkg/date_cmd_vel.msg. Do not edit."""
import codecs
import sys
python3 = True if sys.hexversion > 0x03000000 else False
import genpy
import struct

import geometry_msgs.msg

class date_cmd_vel(genpy.Message):
  _md5sum = "955a41f9fc79adfa3de160994202c671"
  _type = "rss2_msgsrv_pkg/date_cmd_vel"
  _has_header = False  # flag to mark the presence of a Header object
  _full_text = """string sp_date
geometry_msgs/Twist sp_cmd_vel

================================================================================
MSG: geometry_msgs/Twist
# This expresses velocity in free space broken into its linear and angular parts.
Vector3  linear
Vector3  angular

================================================================================
MSG: geometry_msgs/Vector3
# This represents a vector in free space. 
# It is only meant to represent a direction. Therefore, it does not
# make sense to apply a translation to it (e.g., when applying a 
# generic rigid transformation to a Vector3, tf2 will only apply the
# rotation). If you want your data to be translatable too, use the
# geometry_msgs/Point message instead.

float64 x
float64 y
float64 z"""
  __slots__ = ['sp_date','sp_cmd_vel']
  _slot_types = ['string','geometry_msgs/Twist']

  def __init__(self, *args, **kwds):
    """
    Constructor. Any message fields that are implicitly/explicitly
    set to None will be assigned a default value. The recommend
    use is keyword arguments as this is more robust to future message
    changes.  You cannot mix in-order arguments and keyword arguments.

    The available fields are:
       sp_date,sp_cmd_vel

    :param args: complete set of field values, in .msg order
    :param kwds: use keyword arguments corresponding to message field names
    to set specific fields.
    """
    if args or kwds:
      super(date_cmd_vel, self).__init__(*args, **kwds)
      # message fields cannot be None, assign default values for those that are
      if self.sp_date is None:
        self.sp_date = ''
      if self.sp_cmd_vel is None:
        self.sp_cmd_vel = geometry_msgs.msg.Twist()
    else:
      self.sp_date = ''
      self.sp_cmd_vel = geometry_msgs.msg.Twist()

  def _get_types(self):
    """
    internal API method
    """
    return self._slot_types

  def serialize(self, buff):
    """
    serialize message into buffer
    :param buff: buffer, ``StringIO``
    """
    try:
      _x = self.sp_date
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.Struct('<I%ss'%length).pack(length, _x))
      _x = self
      buff.write(_get_struct_6d().pack(_x.sp_cmd_vel.linear.x, _x.sp_cmd_vel.linear.y, _x.sp_cmd_vel.linear.z, _x.sp_cmd_vel.angular.x, _x.sp_cmd_vel.angular.y, _x.sp_cmd_vel.angular.z))
    except struct.error as se: self._check_types(struct.error("%s: '%s' when writing '%s'" % (type(se), str(se), str(locals().get('_x', self)))))
    except TypeError as te: self._check_types(ValueError("%s: '%s' when writing '%s'" % (type(te), str(te), str(locals().get('_x', self)))))

  def deserialize(self, str):
    """
    unpack serialized message in str into this message instance
    :param str: byte array of serialized message, ``str``
    """
    codecs.lookup_error("rosmsg").msg_type = self._type
    try:
      if self.sp_cmd_vel is None:
        self.sp_cmd_vel = geometry_msgs.msg.Twist()
      end = 0
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.sp_date = str[start:end].decode('utf-8', 'rosmsg')
      else:
        self.sp_date = str[start:end]
      _x = self
      start = end
      end += 48
      (_x.sp_cmd_vel.linear.x, _x.sp_cmd_vel.linear.y, _x.sp_cmd_vel.linear.z, _x.sp_cmd_vel.angular.x, _x.sp_cmd_vel.angular.y, _x.sp_cmd_vel.angular.z,) = _get_struct_6d().unpack(str[start:end])
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e)  # most likely buffer underfill


  def serialize_numpy(self, buff, numpy):
    """
    serialize message with numpy array types into buffer
    :param buff: buffer, ``StringIO``
    :param numpy: numpy python module
    """
    try:
      _x = self.sp_date
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.Struct('<I%ss'%length).pack(length, _x))
      _x = self
      buff.write(_get_struct_6d().pack(_x.sp_cmd_vel.linear.x, _x.sp_cmd_vel.linear.y, _x.sp_cmd_vel.linear.z, _x.sp_cmd_vel.angular.x, _x.sp_cmd_vel.angular.y, _x.sp_cmd_vel.angular.z))
    except struct.error as se: self._check_types(struct.error("%s: '%s' when writing '%s'" % (type(se), str(se), str(locals().get('_x', self)))))
    except TypeError as te: self._check_types(ValueError("%s: '%s' when writing '%s'" % (type(te), str(te), str(locals().get('_x', self)))))

  def deserialize_numpy(self, str, numpy):
    """
    unpack serialized message in str into this message instance using numpy for array types
    :param str: byte array of serialized message, ``str``
    :param numpy: numpy python module
    """
    codecs.lookup_error("rosmsg").msg_type = self._type
    try:
      if self.sp_cmd_vel is None:
        self.sp_cmd_vel = geometry_msgs.msg.Twist()
      end = 0
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.sp_date = str[start:end].decode('utf-8', 'rosmsg')
      else:
        self.sp_date = str[start:end]
      _x = self
      start = end
      end += 48
      (_x.sp_cmd_vel.linear.x, _x.sp_cmd_vel.linear.y, _x.sp_cmd_vel.linear.z, _x.sp_cmd_vel.angular.x, _x.sp_cmd_vel.angular.y, _x.sp_cmd_vel.angular.z,) = _get_struct_6d().unpack(str[start:end])
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e)  # most likely buffer underfill

_struct_I = genpy.struct_I
def _get_struct_I():
    global _struct_I
    return _struct_I
_struct_6d = None
def _get_struct_6d():
    global _struct_6d
    if _struct_6d is None:
        _struct_6d = struct.Struct("<6d")
    return _struct_6d