import rclpy
from rclpy.action import ActionClient
from rclpy.node import Node
from hello_msgs.action import Sum

class Client(Node):
    def __init__(self):
        super().__init__("client_node")
        self.sum_client = ActionClient(self, Sum, "sum")

    def send_goal(self, goal):
        self.get_logger().info(f"Sending goal: {goal}")
        goal_msg = Sum.Goal()
        goal_msg.goal = goal

        self.sum_client.wait_for_server()

        self.send_goal_future = self.sum_client.send_goal_async(goal_msg, feedback_callback=self.feedback_callback)

        self.send_goal_future.add_done_callback(self.goal_response_callback)

    def goal_response_callback(self, future):
        goal_handle = future.result()
        if not goal_handle.accepted:
            self.get_logger().info("Goal rejected...")
            return

        self.get_logger().info("Goal accepted!")

        self.get_result_future = goal_handle.get_result_async()
        self.get_result_future.add_done_callback(self.get_result_callback)

    def get_result_callback(self, future):
        result = future.result().result
        self.get_logger().info(f"Result: {result.sum}")
        rclpy.shutdown()

    def feedback_callback(self, feedback_msg):
        feedback = feedback_msg.feedback
        self.get_logger().info(f"Recieved feedback: {feedback.tmp_sum}")

def main(args=None):
    rclpy.init(args=args)

    node = Client()

    node.send_goal(10)

    rclpy.spin(node)
