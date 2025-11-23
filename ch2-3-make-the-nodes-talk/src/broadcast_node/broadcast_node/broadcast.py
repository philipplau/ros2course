import rclpy
from rclpy.node import Node
from msg_package.msg import Broadcast

class ExamplePublisher(Node):
    def __init__(self):
        super().__init__('publish_information')
        self.publisher_ = self.create_publisher(Broadcast, 'topic', 10)
        self.timer = self.create_timer(0.5, self.timer_callback)
        self.i = 0

    def timer_callback(self):
        msg = Broadcast()
        msg.num = self.i
        self.publisher_.publish(msg)
        self.get_logger().info(f'Publishing: {msg.num}')
        self.i += 1

def main(args=None):
    rclpy.init(args=args)
    node = ExamplePublisher()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
