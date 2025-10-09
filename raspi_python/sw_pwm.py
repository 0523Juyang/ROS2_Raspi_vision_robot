import RPi.GPIO as GPIO
import time

LED_En_PIN = 22     # Led enable
PIN = 5  # GPIO5 (physical pin 29)

def main():
    GPIO.setmode(GPIO.BCM)       # Use BCM numbering
    GPIO.setwarnings(False)
    GPIO.setup(LED_En_PIN, GPIO.OUT, initial=GPIO.HIGH)
    GPIO.setup(PIN, GPIO.OUT)
    pwm = GPIO.PWM(PIN, 500)     # 500 Hz software PWM
    pwm.start(30)                # Start with 30% duty cycle

    try:
        while True:
            # Fade effect demo
            for duty in range(0, 101, 5):  # 0% → 100%
                pwm.ChangeDutyCycle(duty)
                time.sleep(0.05)
            for duty in range(100, -1, -5):  # 100% → 0%
                pwm.ChangeDutyCycle(duty)
                time.sleep(0.05)
    except KeyboardInterrupt:
        pass
    finally:
        pwm.stop()
        GPIO.cleanup()

if __name__ == "__main__":
    main()
