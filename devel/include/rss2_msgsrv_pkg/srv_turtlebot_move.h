// Generated by gencpp from file rss2_msgsrv_pkg/srv_turtlebot_move.msg
// DO NOT EDIT!


#ifndef RSS2_MSGSRV_PKG_MESSAGE_SRV_TURTLEBOT_MOVE_H
#define RSS2_MSGSRV_PKG_MESSAGE_SRV_TURTLEBOT_MOVE_H

#include <ros/service_traits.h>


#include <rss2_msgsrv_pkg/srv_turtlebot_moveRequest.h>
#include <rss2_msgsrv_pkg/srv_turtlebot_moveResponse.h>


namespace rss2_msgsrv_pkg
{

struct srv_turtlebot_move
{

typedef srv_turtlebot_moveRequest Request;
typedef srv_turtlebot_moveResponse Response;
Request request;
Response response;

typedef Request RequestType;
typedef Response ResponseType;

}; // struct srv_turtlebot_move
} // namespace rss2_msgsrv_pkg


namespace ros
{
namespace service_traits
{


template<>
struct MD5Sum< ::rss2_msgsrv_pkg::srv_turtlebot_move > {
  static const char* value()
  {
    return "b92c952a9248b3029cefe45f52f6ffde";
  }

  static const char* value(const ::rss2_msgsrv_pkg::srv_turtlebot_move&) { return value(); }
};

template<>
struct DataType< ::rss2_msgsrv_pkg::srv_turtlebot_move > {
  static const char* value()
  {
    return "rss2_msgsrv_pkg/srv_turtlebot_move";
  }

  static const char* value(const ::rss2_msgsrv_pkg::srv_turtlebot_move&) { return value(); }
};


// service_traits::MD5Sum< ::rss2_msgsrv_pkg::srv_turtlebot_moveRequest> should match 
// service_traits::MD5Sum< ::rss2_msgsrv_pkg::srv_turtlebot_move > 
template<>
struct MD5Sum< ::rss2_msgsrv_pkg::srv_turtlebot_moveRequest>
{
  static const char* value()
  {
    return MD5Sum< ::rss2_msgsrv_pkg::srv_turtlebot_move >::value();
  }
  static const char* value(const ::rss2_msgsrv_pkg::srv_turtlebot_moveRequest&)
  {
    return value();
  }
};

// service_traits::DataType< ::rss2_msgsrv_pkg::srv_turtlebot_moveRequest> should match 
// service_traits::DataType< ::rss2_msgsrv_pkg::srv_turtlebot_move > 
template<>
struct DataType< ::rss2_msgsrv_pkg::srv_turtlebot_moveRequest>
{
  static const char* value()
  {
    return DataType< ::rss2_msgsrv_pkg::srv_turtlebot_move >::value();
  }
  static const char* value(const ::rss2_msgsrv_pkg::srv_turtlebot_moveRequest&)
  {
    return value();
  }
};

// service_traits::MD5Sum< ::rss2_msgsrv_pkg::srv_turtlebot_moveResponse> should match 
// service_traits::MD5Sum< ::rss2_msgsrv_pkg::srv_turtlebot_move > 
template<>
struct MD5Sum< ::rss2_msgsrv_pkg::srv_turtlebot_moveResponse>
{
  static const char* value()
  {
    return MD5Sum< ::rss2_msgsrv_pkg::srv_turtlebot_move >::value();
  }
  static const char* value(const ::rss2_msgsrv_pkg::srv_turtlebot_moveResponse&)
  {
    return value();
  }
};

// service_traits::DataType< ::rss2_msgsrv_pkg::srv_turtlebot_moveResponse> should match 
// service_traits::DataType< ::rss2_msgsrv_pkg::srv_turtlebot_move > 
template<>
struct DataType< ::rss2_msgsrv_pkg::srv_turtlebot_moveResponse>
{
  static const char* value()
  {
    return DataType< ::rss2_msgsrv_pkg::srv_turtlebot_move >::value();
  }
  static const char* value(const ::rss2_msgsrv_pkg::srv_turtlebot_moveResponse&)
  {
    return value();
  }
};

} // namespace service_traits
} // namespace ros

#endif // RSS2_MSGSRV_PKG_MESSAGE_SRV_TURTLEBOT_MOVE_H