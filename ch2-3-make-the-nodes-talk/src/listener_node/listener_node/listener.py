import rclpy
from rclpy.node import Node
from msg_package.msg import Broadcast

class ExampleSubscriber(Node):
    def __init__(self):
        super().__init__('listener')
        self.subscription = self.create_subscription(
            Broadcast,
            'topic',
            self.listener_callback,
            10)
        self.subscription  

    def listener_callback(self, msg):
        self.get_logger().info(f'I heard: {msg.num}')

def main(args=None):
    rclpy.init(args=args)
    node = ExampleSubscriber()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
