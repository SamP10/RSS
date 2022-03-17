;; Auto-generated. Do not edit!


(when (boundp 'rss2_msgsrv_pkg::turtlebot_move_square)
  (if (not (find-package "RSS2_MSGSRV_PKG"))
    (make-package "RSS2_MSGSRV_PKG"))
  (shadow 'turtlebot_move_square (find-package "RSS2_MSGSRV_PKG")))
(unless (find-package "RSS2_MSGSRV_PKG::TURTLEBOT_MOVE_SQUARE")
  (make-package "RSS2_MSGSRV_PKG::TURTLEBOT_MOVE_SQUARE"))
(unless (find-package "RSS2_MSGSRV_PKG::TURTLEBOT_MOVE_SQUAREREQUEST")
  (make-package "RSS2_MSGSRV_PKG::TURTLEBOT_MOVE_SQUAREREQUEST"))
(unless (find-package "RSS2_MSGSRV_PKG::TURTLEBOT_MOVE_SQUARERESPONSE")
  (make-package "RSS2_MSGSRV_PKG::TURTLEBOT_MOVE_SQUARERESPONSE"))

(in-package "ROS")





(defclass rss2_msgsrv_pkg::turtlebot_move_squareRequest
  :super ros::object
  :slots (_sideLength _repetitions ))

(defmethod rss2_msgsrv_pkg::turtlebot_move_squareRequest
  (:init
   (&key
    ((:sideLength __sideLength) 0.0)
    ((:repetitions __repetitions) 0)
    )
   (send-super :init)
   (setq _sideLength (float __sideLength))
   (setq _repetitions (round __repetitions))
   self)
  (:sideLength
   (&optional __sideLength)
   (if __sideLength (setq _sideLength __sideLength)) _sideLength)
  (:repetitions
   (&optional __repetitions)
   (if __repetitions (setq _repetitions __repetitions)) _repetitions)
  (:serialization-length
   ()
   (+
    ;; float64 _sideLength
    8
    ;; int32 _repetitions
    4
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; float64 _sideLength
       (sys::poke _sideLength (send s :buffer) (send s :count) :double) (incf (stream-count s) 8)
     ;; int32 _repetitions
       (write-long _repetitions s)
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; float64 _sideLength
     (setq _sideLength (sys::peek buf ptr- :double)) (incf ptr- 8)
   ;; int32 _repetitions
     (setq _repetitions (sys::peek buf ptr- :integer)) (incf ptr- 4)
   ;;
   self)
  )

(defclass rss2_msgsrv_pkg::turtlebot_move_squareResponse
  :super ros::object
  :slots (_success ))

(defmethod rss2_msgsrv_pkg::turtlebot_move_squareResponse
  (:init
   (&key
    ((:success __success) nil)
    )
   (send-super :init)
   (setq _success __success)
   self)
  (:success
   (&optional __success)
   (if __success (setq _success __success)) _success)
  (:serialization-length
   ()
   (+
    ;; bool _success
    1
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; bool _success
       (if _success (write-byte -1 s) (write-byte 0 s))
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; bool _success
     (setq _success (not (= 0 (sys::peek buf ptr- :char)))) (incf ptr- 1)
   ;;
   self)
  )

(defclass rss2_msgsrv_pkg::turtlebot_move_square
  :super ros::object
  :slots ())

(setf (get rss2_msgsrv_pkg::turtlebot_move_square :md5sum-) "774421ec0e986291577c56de248181db")
(setf (get rss2_msgsrv_pkg::turtlebot_move_square :datatype-) "rss2_msgsrv_pkg/turtlebot_move_square")
(setf (get rss2_msgsrv_pkg::turtlebot_move_square :request) rss2_msgsrv_pkg::turtlebot_move_squareRequest)
(setf (get rss2_msgsrv_pkg::turtlebot_move_square :response) rss2_msgsrv_pkg::turtlebot_move_squareResponse)

(defmethod rss2_msgsrv_pkg::turtlebot_move_squareRequest
  (:response () (instance rss2_msgsrv_pkg::turtlebot_move_squareResponse :init)))

(setf (get rss2_msgsrv_pkg::turtlebot_move_squareRequest :md5sum-) "774421ec0e986291577c56de248181db")
(setf (get rss2_msgsrv_pkg::turtlebot_move_squareRequest :datatype-) "rss2_msgsrv_pkg/turtlebot_move_squareRequest")
(setf (get rss2_msgsrv_pkg::turtlebot_move_squareRequest :definition-)
      "float64 sideLength
int32 repetitions
---
bool success

")

(setf (get rss2_msgsrv_pkg::turtlebot_move_squareResponse :md5sum-) "774421ec0e986291577c56de248181db")
(setf (get rss2_msgsrv_pkg::turtlebot_move_squareResponse :datatype-) "rss2_msgsrv_pkg/turtlebot_move_squareResponse")
(setf (get rss2_msgsrv_pkg::turtlebot_move_squareResponse :definition-)
      "float64 sideLength
int32 repetitions
---
bool success

")



(provide :rss2_msgsrv_pkg/turtlebot_move_square "774421ec0e986291577c56de248181db")

