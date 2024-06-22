import rclpy
from rclpy.node import Node
from std_msgs.msg import String

class Publisher(Node):
    def __init__(self):
        super().__init__("publisher")
        self.text_pub = self.create_publisher(String, "text", 10)
        self.timer = self.create_timer(1, self.timer_callback)
        self.i = 0

    def timer_callback(self):
        msg = String()
        msg.data = f"Hello world {self.i}"
        self.text_pub.publish(msg)

        self.get_logger().info(f"Publishing {msg.data}")
        self.i += 1

def main(args=None):
    rclpy.init(args=args)

    node = Publisher()
    rclpy.spin(node)

    node.destroy_node()
    rclpy.shutdown()

if __name__ == "__main__":
    main()
