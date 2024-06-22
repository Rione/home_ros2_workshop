import rclpy
from rclpy.node import Node
from std_msgs.msg import UInt64

class Multiply(Node):
    def __init__(self):
        super().__init__("multiply_node")
        self.number_sub = self.create_subscription(UInt64, "number", self.number_callback, 10)
        self.double_number_pub = self.create_publisher(UInt64, "multiplied_number", 10)

        self.declare_parameter("m_number", 2)
        self.m = self.get_parameter("m_number").get_parameter_value().integer_value

    def number_callback(self, sub_msg):
        self.get_logger().info("Subscribed {}".format(sub_msg.data))

        pub_msg = UInt64()
        pub_msg.data = sub_msg.data * self.m
        self.double_number_pub.publish(pub_msg)

        self.get_logger().info("Publishing {}".format(pub_msg.data))

def main(args=None):
    rclpy.init(args=args)

    node = Multiply()
    rclpy.spin(node)

    node.destroy_node()
    rclpy.shutdown()

if __name__ == "__main__":
    main()
