import rclpy
from rclpy.node import Node
from rclpy.action import ActionServer
from hello_msgs.action import Sum
import time

class Server(Node):
    def __init__(self):
        super().__init__("server_node")
        self.sum_server = ActionServer(self, Sum, "sum", self.sum_callback)

    def sum_callback(self, goal_handle):
        goal = goal_handle.request.goal
        self.get_logger().info(f"Recieved goal: {goal}")

        num = 0
        feedback_msg = Sum.Feedback()
        feedback_msg.tmp_sum = num

        for i in range(1, goal):
            feedback_msg.tmp_sum += i
            goal_handle.publish_feedback(feedback_msg)
            self.get_logger().info(f"Sending feedback: {feedback_msg.tmp_sum}")
            time.sleep(0.5)

        goal_handle.succeed()

        result = Sum.Result()
        result.sum = feedback_msg.tmp_sum
        self.get_logger().info(f"Sending result: {result.sum}")
        return result

def main(args=None):
    rclpy.init(args=args)

    node = Server()
    rclpy.spin(node)
