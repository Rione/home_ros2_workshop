import rclpy
from rclpy.node import Node
from hello_msgs.srv import Order

class Client(Node):
    def __init__(self):
        super().__init__("client_node")
        self.order_client = self.create_client(Order, "order")

        while not self.order_client.wait_for_service(timeout_sec=1.0):
            self.get_logger().info("service not avilable, waiting...")

        self.request = Order.Request()

    def send_request(self, menu):
        self.request.menu = menu

        self.future = self.order_client.call_async(self.request)
        rclpy.spin_until_future_complete(self, self.future)

        return self.future.result()


def main():
    rclpy.init()

    node = Client()
    menu = "ラーメン"

    node.get_logger().info(f"Request: {menu}")

    response = node.send_request(menu)
    node.get_logger().info(f"Response: {response.message}")

    node.destroy_node()
    rclpy.shutdown()

if __name__ == "__main__":
    main()
