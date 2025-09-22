import rclpy
from rclpy.node import Node

from std_msgs.msg import Int16


class numSubscriber(Node):

    def __init__(self):
        super().__init__('numSubscriber')
        self.subscription = self.create_subscription(
            Int16,
            '/pub_num',
            self.listener_callback,
            10)
        self.subscription  # prevent unused variable warning

    def listener_callback(self, msg):
        self.get_logger().info('I heard: "%d"' % msg.data)


def main(args=None):
    rclpy.init(args=args)

    numsubscriber = numSubscriber()

    rclpy.spin(numsubscriber)

    # Destroy the node explicitly
    # (optional - otherwise it will be done automatically
    # when the garbage collector destroys the node object)
    numsubscriber.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()