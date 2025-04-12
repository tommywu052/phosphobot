import rclpy
from rclpy.node import Node
import requests
from sensor_msgs.msg import JointState
import math

class JointStatePublisher(Node):
    def __init__(self):
        super().__init__('joint_state_publisher')
        self.publisher_ = self.create_publisher(JointState, 'joint_command', 10)
        self.timer = self.create_timer(0.1, self.timer_callback)  # 10Hz update rate
        self.robot_ip = "192.168.31.28"  # Change this if needed
        self.robot_id = 0  # Adjust if necessary
        self.joint_names = ["Rotation", "Pitch", "Elbow", "Wrist_Pitch", "Wrist_Roll", "Jaw"]
        self.session = requests.Session()  # Use a persistent session

    def timer_callback(self):
        url = f'http://{self.robot_ip}/joints/read?robot_id={self.robot_id}'
        try:
            response = self.session.post(url, headers={'accept': 'application/json'}, data='',timeout=2)
            if response.status_code == 200:
                data = response.json()
                joint_positions = data.get("angles_rad", [])
                
                if len(joint_positions) == len(self.joint_names):
                    #joint_positions_deg = [math.degrees(angle) for angle in joint_positions]
                    msg = JointState()
                    msg.header.stamp = self.get_clock().now().to_msg()
                    msg.name = self.joint_names
                    msg.position = joint_positions
                    self.publisher_.publish(msg)
                else:
                    self.get_logger().error("Unexpected number of joint positions received.")
            else:
                self.get_logger().error(f"Failed to get joint positions: {response.status_code}")
        except requests.RequestException as e:
            self.get_logger().error(f"Error connecting to robot API: {str(e)}")


def main(args=None):
    rclpy.init(args=args)
    node = JointStatePublisher()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
