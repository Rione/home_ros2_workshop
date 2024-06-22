import rclpy
from rclpy.node import Node
from std_msgs.msg import UInt64

class Double(Node):
    def __init__(self):
        super().__init__("double_node")
        self.number_sub = self.create_subscription(UInt64, "number", self.number_callback, 10)
        self.double_number_pub = self.create_publisher(UInt64, "double_number", 10)

    def number_callback(self, sub_msg):
        self.get_logger().info(f"Subscribed {sub_msg.data}")

        pub_msg = UInt64()
        pub_msg.data = sub_msg.data * 2
        self.double_number_pub.publish(pub_msg)

        self.get_logger().info(f"Publishing {pub_msg.data}")

def main(args=None):
    rclpy.init(args=args)

    node = Double()
    rclpy.spin(node)

    node.destroy_node()
    rclpy.shutdown()

if __name__ == "__main__":
    main()
