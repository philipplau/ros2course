#!/usr/bin/env python3
import time
import rclpy
from rclpy.node import Node
from rclpy.executors import SingleThreadedExecutor

class ControlledNode(Node):
    def __init__(self):
        super().__init__('controlled_node')
        self.create_timer(0.5, self._timer_cb)

    def _timer_cb(self):
        self.get_logger().info('ControlledNode: ROS callback tick')

def main():
    rclpy.init()
    node = ControlledNode()
    execu = SingleThreadedExecutor()
    execu.add_node(node)

    try:
        start = time.time()
        while rclpy.ok() and time.time() - start < 10.0:
            execu.spin_once(timeout_sec=0.2)
            print('main(): doing non-ROS work...')
            time.sleep(0.3)
    finally:
        node.destroy_node()
        rclpy.shutdown()

if __name__ == '__main__':
    main()
