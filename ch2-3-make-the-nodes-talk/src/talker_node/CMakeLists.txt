cmake_minimum_required(VERSION 3.8)
project(talker_node)

if(CMAKE_COMPILER_IS_GNUCXX OR CMAKE_CXX_COMPILER_ID MATCHES "Clang")
  add_compile_options(-Wall -Wextra -Wpedantic)
endif()

find_package(ament_cmake REQUIRED)
find_package(rclcpp REQUIRED)
find_package(msg_package REQUIRED)

add_executable(server_node src/server_node.cpp)
ament_target_dependencies(server_node rclcpp msg_package)

install(TARGETS server_node DESTINATION lib/${PROJECT_NAME})

ament_package()
