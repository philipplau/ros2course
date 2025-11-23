#!/usr/bin/env python3
import time
import rclpy
from rclpy.node import Node
from rclpy.executors import SingleThreadedExecutor

class NodeA(Node):
    def __init__(self):
        super().__init__('node_a')
        self.create_timer(1.0, self._timer_cb)

    def _timer_cb(self):
        self.get_logger().info('NodeA: tick')

class NodeB(Node):
    def __init__(self):
        super().__init__('node_b')
        self.create_timer(1.5, self._timer_cb)

    def _timer_cb(self):
        self.get_logger().info('NodeB: tick (simulating work 0.4s)')
        time.sleep(0.4)

def main():
    rclpy.init()
    a = NodeA()
    b = NodeB()

    execu = SingleThreadedExecutor()
    execu.add_node(a)
    execu.add_node(b)

    try:
        execu.spin()
    finally:
        a.destroy_node()
        b.destroy_node()
        rclpy.shutdown()

if __name__ == '__main__':
    main()
