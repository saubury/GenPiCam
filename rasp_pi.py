from picamera import PiCamera
import RPi.GPIO as GPIO # Import Raspberry Pi GPIO library
import time
import midjourney as mj
import bot_settings as bset

# sudo apt-get install python3-dev python3-rpi.gpio
# pip install RPi.GPIO

GPIO_PIN_SHUTTER = 10
GPIO_PIN_A = 8
GPIO_PIN_B = 36
GPIO_PIN_C = 38
GPIO_PIN_D = 40
GPIO_PIN_E = 35
GPIO_PIN_F = 37

def button_callback(channel):
    if (bset.get_ignorebutton()):
        return
    
    bset.set_ignorebutton(True)
    print('Button was pushed!')
    take_photo()

    if GPIO.input(GPIO_PIN_A) == GPIO.HIGH:
        bset.set_promptprefix('Anime style,')

    elif GPIO.input(GPIO_PIN_B) == GPIO.HIGH:
        bset.set_promptprefix('Hyper Realistic, whimsical with colourful hat and balloons,')     

    elif GPIO.input(GPIO_PIN_C) == GPIO.HIGH:
        bset.set_promptprefix('Blurry brushstrokes,')       

    elif GPIO.input(GPIO_PIN_D) == GPIO.HIGH:
        bset.set_promptprefix('Futuristic, in a space station, hyper realistic,')     

    elif GPIO.input(GPIO_PIN_E) == GPIO.HIGH:
        bset.set_promptprefix('retro pop art-style illustration,')    

    else:
        # no prompt set
        bset.set_promptprefix('')

def take_photo():
    file_prefix = time.strftime('%Y%m%d_%H%M%S')
    camera = PiCamera()
    camera.resolution = (1024, 768)
    camera.start_preview()
    # Camera warm-up time
    time.sleep(2)
    camera_file = f'/home/simon/git/midjourney-bot/camera/{file_prefix}_photo.jpg'
    camera.capture(camera_file)
    camera.close()   

    if bset.get_automode():
        mj.go_describe(camera_file)

def setup_gpio():
    GPIO.setwarnings(False) # Ignore warning for now
    GPIO.setmode(GPIO.BOARD) # Use physical pin numbering

    # Set pins to be an input pin and set initial value to be pulled low (off)
    for this_pin in (GPIO_PIN_SHUTTER, GPIO_PIN_A, GPIO_PIN_B, GPIO_PIN_C, GPIO_PIN_D, GPIO_PIN_E, GPIO_PIN_F):
        GPIO.setup(this_pin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
 
    # Setup event on pin rising edge for shutter push button
    GPIO.add_event_detect(GPIO_PIN_SHUTTER, GPIO.RISING, callback=button_callback, bouncetime=3000) 
