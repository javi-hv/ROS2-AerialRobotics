import rclpy
from rclpy.node import Node
from std_msgs.msg import String

class SimplePublisher(Node):
    """
    A simple ROS2 publisher node that publishes a string message to the 'pipeline' topic at a fixed interval.

    Attributes:
        publisher (Publisher): The ROS2 publisher object.
        period (float): The time interval (in seconds) between publishing messages.
        count (int): A counter to keep track of the number of messages published.
        timer (Timer): The ROS2 timer object that triggers the `timer_callback` method at the specified interval.

    Methods:
        __init__(): Initializes the SimplePublisher node, creates the publisher, and sets up the timer.
        timer_callback(): Callback function that gets called at each timer interval to publish a message.
    """

    def __init__(self):
        super().__init__('simple_publisher')
        self.publisher = self.create_publisher(String, "pipeline",10)
        self.period = 1.0 # seconds
        self.count = 0

        self.timer = self.create_timer(self.period, self.timer_callback)

    def timer_callback(self):
        msg = String()
        msg.data = "Hello, World: %d" % self.count
        self.count += 1
        self.get_logger().info("Publishing: '%s'" % msg.data)
        self.publisher.publish(msg)


def main(args=None):
    rclpy.init(args=args)
    simple_publisher = SimplePublisher()
    rclpy.spin(simple_publisher)
    simple_publisher.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
    