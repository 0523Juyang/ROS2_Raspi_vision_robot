# -*- coding: utf-8 -*-
import RPi.GPIO as GPIO
import time

# --- GPIO 基本設定 ---

GPIO.setmode(GPIO.BCM)         # 使用 BCM 腳位編號
GPIO.setwarnings(False)

# --- 腳位定義 ---
LED_En_PIN   = 22   # 總電源/使能腳 (若你的驅動板需要)
PWM_PIN      = 5    # 中央 LED 的 PWM 輸出
LED_up_PIN   = 12
LED_down_PIN = 26
LED_left_PIN = 6
LED_right_PIN= 13

# --- 腳位方向與預設輸出 ---
'''  #GPIO setting
GPIO.setup(LED_En_PIN,   GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(LED_up_PIN,   GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(LED_down_PIN, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(LED_left_PIN, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(LED_right_PIN,GPIO.OUT, initial=GPIO.LOW)
'''
GPIO.setup(LED_En_PIN,   GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(LED_up_PIN,   GPIO.OUT)
GPIO.setup(LED_down_PIN, GPIO.OUT)
GPIO.setup(LED_left_PIN, GPIO.OUT)
GPIO.setup(LED_right_PIN,GPIO.OUT)

pwm_up = GPIO.PWM(LED_up_PIN, 1000)  # 1 kHz 軟體 PWM
pwm_down = GPIO.PWM(LED_down_PIN, 1000)  # 1 kHz 軟體 PWM
pwm_left = GPIO.PWM(LED_left_PIN, 1000)  # 1 kHz 軟體 PWM
pwm_right = GPIO.PWM(LED_right_PIN, 1000)  # 1 kHz 軟體 PWM
pwm_up.start(0) 
pwm_down.start(0)
pwm_left.start(0)
pwm_right.start(0)  

GPIO.setup(PWM_PIN, GPIO.OUT)
pwm = GPIO.PWM(PWM_PIN, 1000)  # 1 kHz 軟體 PWM
pwm.start(0)                              
time.sleep(1)

#lt = 0.5 #Led light time
# --- 小工具函式 ---
def forward(dt=30, lt=0.5):
    """控制 '上方' 指示 LED 的亮/滅"""
    print("Car forward moving ")
    # 若你的硬體需要使能腳才會亮，這裡打開
    GPIO.output(LED_En_PIN, GPIO.HIGH)
    pwm_up.ChangeDutyCycle(dt)
    time.sleep(lt)
    pwm_up.ChangeDutyCycle(0)

def reverse(dt=30, lt=0.5):
    """控制 '下方' 指示 LED 的亮/滅"""
    print("Car backward moving ")
    GPIO.output(LED_En_PIN, GPIO.HIGH)
    pwm_down.ChangeDutyCycle(dt)
    time.sleep(lt)
    pwm_down.ChangeDutyCycle(0) 

def left(dt=30, lt=0.5):
    """控制 '左方' 指示 LED 的亮/滅"""
    print("Car turn left ")
    GPIO.output(LED_En_PIN, GPIO.HIGH)
    pwm_left.ChangeDutyCycle(dt)
    time.sleep(lt)
    pwm_left.ChangeDutyCycle(0)

def right(dt=30, lt=0.5):
    """控制 '右方' 指示 LED 的亮/滅"""
    print("Car turn right ")
    GPIO.output(LED_En_PIN, GPIO.HIGH)
    pwm_right.ChangeDutyCycle(dt)
    time.sleep(lt)
    pwm_right.ChangeDutyCycle(0)

def pwm_led(duty=0, lt=0.5):
    
    GPIO.output(LED_En_PIN, GPIO.HIGH)
    pwm.ChangeDutyCycle(duty)
    time.sleep(lt)
    pwm.ChangeDutyCycle(0)



def stop():
    """保險起見：一次關閉所有方向 LED"""
    pwm_up.ChangeDutyCycle(0)
    pwm_down.ChangeDutyCycle(0)
    pwm_left.ChangeDutyCycle(0)
    pwm_right.ChangeDutyCycle(0)


def exit():
    stop()
    GPIO.output(LED_En_PIN, GPIO.LOW)
    GPIO.cleanup()

# --- 主流程 ---
def main():

    while True:
        try:
            
            # 讓上方 LED 閃爍示範
            forward(10,2)

            # 讓下方 LED 閃爍示範
            reverse(60,2)


            # 讓左方 LED 閃爍示範
            left(90,2)


            # 讓右方 LED 閃爍示範
            right(80,1)


        # 讓中間 LED 閃爍示範
            pwm_led(50)
            # 也可同時調整 PWM 亮度做呼吸燈或漸變
            # 例如：pwm.ChangeDutyCycle(50)
        except KeyboardInterrupt:
            exit()
        finally:
            # 安全關閉
            stop()
            GPIO.output(LED_En_PIN, GPIO.LOW)


if __name__ == "__main__":
    main()

