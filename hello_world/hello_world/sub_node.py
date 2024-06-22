import rclpy
from rclpy.node import Node
from std_msgs.msg import String

class Subscriber(Node):
    def __init__(self):
        super().__init__("subscriber")
        self.text_sub = self.create_subscription(String, "text", self.text_callback, 10)

    def text_callback(self, msg):
        self.get_logger().info(f"Subscribed {msg.data}")

def main(args=None):
    rclpy.init(args=args)

    node = Subscriber()
    rclpy.spin(node)

    node.destroy_node()
    rclpy.shutdown()

if __name__ == "__main__":
    main()
