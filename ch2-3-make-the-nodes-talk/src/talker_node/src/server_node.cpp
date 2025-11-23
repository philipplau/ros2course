#include "rclcpp/rclcpp.hpp"
#include "msg_package/srv/transmit.hpp"
#include <memory>
#include <inttypes.h>

void handle_transmit(
  const std::shared_ptr<msg_package::srv::Transmit::Request> request,
  std::shared_ptr<msg_package::srv::Transmit::Response> response)
{
  response->result = request->value + request->value2 + request->value3;
  RCLCPP_INFO(
    rclcpp::get_logger("transmit_server"),
    "Incoming request:\n value: %" PRId64 "  value2: %" PRId64 "  value3: %" PRId64,
    request->value, request->value2, request->value3);
  RCLCPP_INFO(
    rclcpp::get_logger("transmit_server"),
    "sending back response: [%" PRId64 "]", response->result);
}

int main(int argc, char **argv)
{
  rclcpp::init(argc, argv);
  auto node = rclcpp::Node::make_shared("transmit_server");
  auto service = node->create_service<msg_package::srv::Transmit>("transmit", &handle_transmit);
  RCLCPP_INFO(rclcpp::get_logger("transmit_server"), "Ready to sum three int64s.");
  rclcpp::spin(node);
  rclcpp::shutdown();
  return 0;
}
