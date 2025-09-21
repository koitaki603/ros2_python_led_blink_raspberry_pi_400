import rclpy
from rclpy.node import Node
import RPi.GPIO as GPIO
import time

LED_PIN = 18

class LEDNode(Node):
    def __init__(self):
        super().__init__('led_node')
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(LED_PIN, GPIO.OUT)
        self.timer = self.create_timer(1.0, self.toggle_led)
        self.led_state = False

    def toggle_led(self):
        self.led_state = not self.led_state
        GPIO.output(LED_PIN, self.led_state)
        self.get_logger().info(f"LED is {'ON' if self.led_state else 'OFF'}")

def main(args=None):
    rclpy.init(args=args)
    node = LEDNode()

    try:
        rclpy.spin(node)  # ノードを回し続ける
    except KeyboardInterrupt:  # Ctrl+C が押された場合に捕まえる
        pass
    finally:
        GPIO.cleanup()  # プログラム終了時にGPIOのクリーンアップを行う
        node.destroy_node()  # ノードを破棄
        rclpy.shutdown()  # rclpyのシャットダウン

if __name__ == '__main__':
    main()
