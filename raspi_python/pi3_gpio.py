# pi3_gpio.py
import RPi.GPIO as GPIO
import time

LED_En_PIN = 22     # 常亮
LED_ON_PIN = 5     # 常亮
PWM_PIN    = 13     # PWM



def setup():
    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)

    # GPIO5 Enable LED
    GPIO.setup(LED_En_PIN, GPIO.OUT, initial=GPIO.HIGH)
    
    # GPI05 常亮
    GPIO.setup(LED_ON_PIN, GPIO.OUT, initial=GPIO.HIGH)

    # GPIO13 PWM
    GPIO.setup(PWM_PIN, GPIO.OUT)
    pwm = GPIO.PWM(PWM_PIN, 1000)  # 1kHz
    pwm.start(30)                  # 30% duty
    return pwm

def main():
    pwm = setup()
    try:
        while True:
            time.sleep(1)  # 保持執行
    except KeyboardInterrupt:
            # GPI05 常亮
        GPIO.setup(LED_ON_PIN, GPIO.OUT, initial=GPIO.LOW)
        
        pass
    finally:
        pwm.stop()
        GPIO.cleanup()

# 範例：每秒 +10%，到 90% 後回到 30%
def demo_ramp():
    pwm = setup()
    duty = 30
    try:
        while True:
            duty = duty + 10 if duty < 90 else 30
            pwm.ChangeDutyCycle(duty)
            time.sleep(1)
    except KeyboardInterrupt:
        pass
    finally:
        pwm.stop()
        GPIO.cleanup()


if __name__ == "__main__":
    #main()
    demo_ramp()
