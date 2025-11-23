#!/usr/bin/env python3
import sys
import time
import rclpy
from rclpy.node import Node
from msg_package.srv import Transmit

class TransmitClient(Node):
    def __init__(self):
        super().__init__('transmit_client')
        self.cli = self.create_client(Transmit, 'transmit')
        while not self.cli.wait_for_service(timeout_sec=1.0):
            self.get_logger().info('service not available, waiting...')
        self.req = Transmit.Request()

    def send_request(self, a, b, c):
        self.req.value = int(a)
        self.req.value2 = int(b)
        self.req.value3 = int(c)
        return self.cli.call_async(self.req)

def main():
    rclpy.init()
    node = TransmitClient()

    try:
        for i in range(5): 
            a, b, c = i, i + 1, i + 2
            future = node.send_request(a, b, c)
            rclpy.spin_until_future_complete(node, future)
            if future.result() is not None:
                node.get_logger().info(f'[{i+1}] result: {future.result().result}')
            else:
                node.get_logger().error('service call failed')
            time.sleep(1.0)
    except KeyboardInterrupt:
        pass

    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
