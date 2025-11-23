#!/usr/bin/env python3
import rclpy
from rclpy.node import Node

class SpinOneNode(Node):
    def __init__(self):
        super().__init__('spin_one_node')
        self.create_timer(1.0, self._fast_timer)
        self.create_timer(2.5, self._slow_timer)

    def _fast_timer(self):
        self.get_logger().info('spin_one: fast timer tick')

    def _slow_timer(self):
        self.get_logger().info('spin_one: slow timer tick')

def main():
    rclpy.init()
    node = SpinOneNode()
    try:
        rclpy.spin(node)  # creates a SingleThreadedExecutor internally
    finally:
        node.destroy_node()
        rclpy.shutdown()

if __name__ == '__main__':
    main()
