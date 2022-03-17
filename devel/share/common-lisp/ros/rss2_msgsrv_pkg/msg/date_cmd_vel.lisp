; Auto-generated. Do not edit!


(cl:in-package rss2_msgsrv_pkg-msg)


;//! \htmlinclude date_cmd_vel.msg.html

(cl:defclass <date_cmd_vel> (roslisp-msg-protocol:ros-message)
  ((sp_date
    :reader sp_date
    :initarg :sp_date
    :type cl:string
    :initform "")
   (sp_cmd_vel
    :reader sp_cmd_vel
    :initarg :sp_cmd_vel
    :type geometry_msgs-msg:Twist
    :initform (cl:make-instance 'geometry_msgs-msg:Twist)))
)

(cl:defclass date_cmd_vel (<date_cmd_vel>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <date_cmd_vel>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'date_cmd_vel)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name rss2_msgsrv_pkg-msg:<date_cmd_vel> is deprecated: use rss2_msgsrv_pkg-msg:date_cmd_vel instead.")))

(cl:ensure-generic-function 'sp_date-val :lambda-list '(m))
(cl:defmethod sp_date-val ((m <date_cmd_vel>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader rss2_msgsrv_pkg-msg:sp_date-val is deprecated.  Use rss2_msgsrv_pkg-msg:sp_date instead.")
  (sp_date m))

(cl:ensure-generic-function 'sp_cmd_vel-val :lambda-list '(m))
(cl:defmethod sp_cmd_vel-val ((m <date_cmd_vel>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader rss2_msgsrv_pkg-msg:sp_cmd_vel-val is deprecated.  Use rss2_msgsrv_pkg-msg:sp_cmd_vel instead.")
  (sp_cmd_vel m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <date_cmd_vel>) ostream)
  "Serializes a message object of type '<date_cmd_vel>"
  (cl:let ((__ros_str_len (cl:length (cl:slot-value msg 'sp_date))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) __ros_str_len) ostream))
  (cl:map cl:nil #'(cl:lambda (c) (cl:write-byte (cl:char-code c) ostream)) (cl:slot-value msg 'sp_date))
  (roslisp-msg-protocol:serialize (cl:slot-value msg 'sp_cmd_vel) ostream)
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <date_cmd_vel>) istream)
  "Deserializes a message object of type '<date_cmd_vel>"
    (cl:let ((__ros_str_len 0))
      (cl:setf (cl:ldb (cl:byte 8 0) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'sp_date) (cl:make-string __ros_str_len))
      (cl:dotimes (__ros_str_idx __ros_str_len msg)
        (cl:setf (cl:char (cl:slot-value msg 'sp_date) __ros_str_idx) (cl:code-char (cl:read-byte istream)))))
  (roslisp-msg-protocol:deserialize (cl:slot-value msg 'sp_cmd_vel) istream)
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<date_cmd_vel>)))
  "Returns string type for a message object of type '<date_cmd_vel>"
  "rss2_msgsrv_pkg/date_cmd_vel")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'date_cmd_vel)))
  "Returns string type for a message object of type 'date_cmd_vel"
  "rss2_msgsrv_pkg/date_cmd_vel")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<date_cmd_vel>)))
  "Returns md5sum for a message object of type '<date_cmd_vel>"
  "955a41f9fc79adfa3de160994202c671")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'date_cmd_vel)))
  "Returns md5sum for a message object of type 'date_cmd_vel"
  "955a41f9fc79adfa3de160994202c671")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<date_cmd_vel>)))
  "Returns full string definition for message of type '<date_cmd_vel>"
  (cl:format cl:nil "string sp_date~%geometry_msgs/Twist sp_cmd_vel~%~%================================================================================~%MSG: geometry_msgs/Twist~%# This expresses velocity in free space broken into its linear and angular parts.~%Vector3  linear~%Vector3  angular~%~%================================================================================~%MSG: geometry_msgs/Vector3~%# This represents a vector in free space. ~%# It is only meant to represent a direction. Therefore, it does not~%# make sense to apply a translation to it (e.g., when applying a ~%# generic rigid transformation to a Vector3, tf2 will only apply the~%# rotation). If you want your data to be translatable too, use the~%# geometry_msgs/Point message instead.~%~%float64 x~%float64 y~%float64 z~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'date_cmd_vel)))
  "Returns full string definition for message of type 'date_cmd_vel"
  (cl:format cl:nil "string sp_date~%geometry_msgs/Twist sp_cmd_vel~%~%================================================================================~%MSG: geometry_msgs/Twist~%# This expresses velocity in free space broken into its linear and angular parts.~%Vector3  linear~%Vector3  angular~%~%================================================================================~%MSG: geometry_msgs/Vector3~%# This represents a vector in free space. ~%# It is only meant to represent a direction. Therefore, it does not~%# make sense to apply a translation to it (e.g., when applying a ~%# generic rigid transformation to a Vector3, tf2 will only apply the~%# rotation). If you want your data to be translatable too, use the~%# geometry_msgs/Point message instead.~%~%float64 x~%float64 y~%float64 z~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <date_cmd_vel>))
  (cl:+ 0
     4 (cl:length (cl:slot-value msg 'sp_date))
     (roslisp-msg-protocol:serialization-length (cl:slot-value msg 'sp_cmd_vel))
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <date_cmd_vel>))
  "Converts a ROS message object to a list"
  (cl:list 'date_cmd_vel
    (cl:cons ':sp_date (sp_date msg))
    (cl:cons ':sp_cmd_vel (sp_cmd_vel msg))
))
