// Auto-generated. Do not edit!

// (in-package rss2_msgsrv_pkg.msg)


"use strict";

const _serializer = _ros_msg_utils.Serialize;
const _arraySerializer = _serializer.Array;
const _deserializer = _ros_msg_utils.Deserialize;
const _arrayDeserializer = _deserializer.Array;
const _finder = _ros_msg_utils.Find;
const _getByteLength = _ros_msg_utils.getByteLength;
let geometry_msgs = _finder('geometry_msgs');

//-----------------------------------------------------------

class date_cmd_vel {
  constructor(initObj={}) {
    if (initObj === null) {
      // initObj === null is a special case for deserialization where we don't initialize fields
      this.sp_date = null;
      this.sp_cmd_vel = null;
    }
    else {
      if (initObj.hasOwnProperty('sp_date')) {
        this.sp_date = initObj.sp_date
      }
      else {
        this.sp_date = '';
      }
      if (initObj.hasOwnProperty('sp_cmd_vel')) {
        this.sp_cmd_vel = initObj.sp_cmd_vel
      }
      else {
        this.sp_cmd_vel = new geometry_msgs.msg.Twist();
      }
    }
  }

  static serialize(obj, buffer, bufferOffset) {
    // Serializes a message object of type date_cmd_vel
    // Serialize message field [sp_date]
    bufferOffset = _serializer.string(obj.sp_date, buffer, bufferOffset);
    // Serialize message field [sp_cmd_vel]
    bufferOffset = geometry_msgs.msg.Twist.serialize(obj.sp_cmd_vel, buffer, bufferOffset);
    return bufferOffset;
  }

  static deserialize(buffer, bufferOffset=[0]) {
    //deserializes a message object of type date_cmd_vel
    let len;
    let data = new date_cmd_vel(null);
    // Deserialize message field [sp_date]
    data.sp_date = _deserializer.string(buffer, bufferOffset);
    // Deserialize message field [sp_cmd_vel]
    data.sp_cmd_vel = geometry_msgs.msg.Twist.deserialize(buffer, bufferOffset);
    return data;
  }

  static getMessageSize(object) {
    let length = 0;
    length += object.sp_date.length;
    return length + 52;
  }

  static datatype() {
    // Returns string type for a message object
    return 'rss2_msgsrv_pkg/date_cmd_vel';
  }

  static md5sum() {
    //Returns md5sum for a message object
    return '955a41f9fc79adfa3de160994202c671';
  }

  static messageDefinition() {
    // Returns full string definition for message
    return `
    string sp_date
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
    float64 z
    `;
  }

  static Resolve(msg) {
    // deep-construct a valid message object instance of whatever was passed in
    if (typeof msg !== 'object' || msg === null) {
      msg = {};
    }
    const resolved = new date_cmd_vel(null);
    if (msg.sp_date !== undefined) {
      resolved.sp_date = msg.sp_date;
    }
    else {
      resolved.sp_date = ''
    }

    if (msg.sp_cmd_vel !== undefined) {
      resolved.sp_cmd_vel = geometry_msgs.msg.Twist.Resolve(msg.sp_cmd_vel)
    }
    else {
      resolved.sp_cmd_vel = new geometry_msgs.msg.Twist()
    }

    return resolved;
    }
};

module.exports = date_cmd_vel;
