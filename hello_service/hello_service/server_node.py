import rclpy
from rclpy.node import Node
from hello_msgs.srv import Order

class Service(Node):
    def __init__(self):
        super().__init__("service_node")
        self.order_service = self.create_service(Order, "order", self.order_service_callback)
        self.get_logger().info("service is ready")

    def order_service_callback(self, request, response):
        self.get_logger().info(f"Recieved: {request.menu}")

        response.message = f"へい!{request.menu}、お待ち!"
        self.get_logger().info(f"Sending: {response.message}")

        return response

def main():
    rclpy.init()

    node = Service()
    rclpy.spin(node)

    rclpy.shutdown()

if __name__ == "__main__":
    main()
