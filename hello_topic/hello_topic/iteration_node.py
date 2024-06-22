import rclpy
from rclpy.node import Node
from std_msgs.msg import UInt64

class Iteration(Node):
    def __init__(self):
        super().__init__("iteration_node")
        self.number_pub = self.create_publisher(UInt64, "number", 10)
        self.timer = self.create_timer(1, self.timer_callback)
        self.i = 0

    def timer_callback(self):
        msg = UInt64()
        msg.data = self.i
        self.number_pub.publish(msg)

        self.get_logger().info(f"Publishing {msg.data}")

        self.i += 1

def main(args=None):
    rclpy.init(args=args)

    node = Iteration()
    rclpy.spin(node)

    node.destroy_node()
    rclpy.shutdown()

if __name__ == "__main__":
    main()
