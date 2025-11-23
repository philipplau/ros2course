import rclpy
from rclpy.node import node

class SampleNode(Node):
    def __init__(self):
        super().__init__('sample_node')
        print("This node works!")

def main(args=None):
    rclpy.init(args=args)

    try:
        sample_node = SampleNode()
        rclpy.spin(sample_node)
    except KeyboardInterrupt:
        pass
    finally:
        sample_node.destroy_node()
        rclpy.shutdown()
