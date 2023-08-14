import time
import board
import digitalio


LED_0= digitalio.DigitalInOut(board.GP0)
LED_0.direction = digitalio.Direction.OUTPUT
LED_1= digitalio.DigitalInOut(board.GP1)
LED_1.direction = digitalio.Direction.OUTPUT
LED_2= digitalio.DigitalInOut(board.GP2)
LED_2.direction = digitalio.Direction.OUTPUT
LED_3=digitalio.DigitalInOut(board.GP3)
LED_3.direction = digitalio.Direction.OUTPUT
LED_4= digitalio.DigitalInOut(board.GP4)
LED_4.direction = digitalio.Direction.OUTPUT
LED_5= digitalio.DigitalInOut(board.GP5)
LED_5.direction = digitalio.Direction.OUTPUT
LED_6= digitalio.DigitalInOut(board.GP6)
LED_6.direction = digitalio.Direction.OUTPUT
LED_7= digitalio.DigitalInOut(board.GP7)
LED_7.direction = digitalio.Direction.OUTPUT
LED_8= digitalio.DigitalInOut(board.GP8)
LED_8.direction = digitalio.Direction.OUTPUT
LED_9= digitalio.DigitalInOut(board.GP9)
LED_9.direction = digitalio.Direction.OUTPUT
LED_10= digitalio.DigitalInOut(board.GP10)
LED_10.direction = digitalio.Direction.OUTPUT
LED_11= digitalio.DigitalInOut(board.GP11)
LED_11.direction = digitalio.Direction.OUTPUT
LED_12= digitalio.DigitalInOut(board.GP12)
LED_12.direction = digitalio.Direction.OUTPUT
LED_13= digitalio.DigitalInOut(board.GP13)
LED_13.direction = digitalio.Direction.OUTPUT
LED_14= digitalio.DigitalInOut(board.GP14)
LED_14.direction = digitalio.Direction.OUTPUT
LED_15= digitalio.DigitalInOut(board.GP15)
LED_15.direction = digitalio.Direction.OUTPUT
LED_16= digitalio.DigitalInOut(board.GP16)
LED_16.direction = digitalio.Direction.OUTPUT
LED_17= digitalio.DigitalInOut(board.GP17)
LED_17.direction = digitalio.Direction.OUTPUT
LED_18= digitalio.DigitalInOut(board.GP18)
LED_18.direction = digitalio.Direction.OUTPUT
LED_19= digitalio.DigitalInOut(board.GP19)
LED_19.direction = digitalio.Direction.OUTPUT
LED_20= digitalio.DigitalInOut(board.GP20)
LED_20.direction = digitalio.Direction.OUTPUT
LED_21= digitalio.DigitalInOut(board.GP21)
LED_21.direction = digitalio.Direction.OUTPUT
LED_22= digitalio.DigitalInOut(board.GP22)
LED_22.direction = digitalio.Direction.OUTPUT
LED_26= digitalio.DigitalInOut(board.GP26)
LED_26.direction = digitalio.Direction.OUTPUT
LED_27= digitalio.DigitalInOut(board.GP27)
LED_27.direction = digitalio.Direction.OUTPUT
LED_28= digitalio.DigitalInOut(board.GP28)
LED_28.direction = digitalio.Direction.OUTPUT

while True:
    LED_0.value = True
    time.sleep(.05)
    LED_0.value = False
    LED_1.value = True
    time.sleep(.05)
    LED_1.value = False
    LED_2.value = True
    time.sleep(.05)
    LED_2.value = False
    LED_3.value = True
    time.sleep(.05)
    LED_3.value = False
    LED_4.value = True
    time.sleep(.05)
    LED_4.value = False
    LED_5.value = True
    time.sleep(.05)
    LED_5.value = False
    LED_6.value = True
    time.sleep(.05)
    LED_6.value = False
    LED_7.value = True
    time.sleep(.05)
    LED_7.value = False
    LED_8.value = True
    time.sleep(.05)
    LED_8.value = False
    LED_9.value = True
    time.sleep(.05)
    LED_9.value = False
    LED_10.value = True
    time.sleep(.05)
    LED_10.value = False
    LED_11.value = True
    time.sleep(.05)
    LED_11.value = False
    LED_12.value = True
    time.sleep(.05)
    LED_12.value = False
    LED_13.value = True
    time.sleep(.05)
    LED_13.value = False
    LED_14.value = True
    time.sleep(.05)
    LED_14.value = False
    LED_15.value = True
    time.sleep(.05)
    LED_15.value = False
    LED_16.value = True
    time.sleep(.05)
    LED_16.value = False
    LED_17.value = True
    time.sleep(.05)
    LED_17.value = False
    LED_18.value = True
    time.sleep(.05)
    LED_18.value = False
    LED_19.value = True
    time.sleep(.05)
    LED_19.value = False
    LED_20.value = True
    time.sleep(.05)
    LED_20.value = False
    LED_21.value = True
    time.sleep(.05)
    LED_21.value = False
    LED_22.value = True
    time.sleep(.2)
    LED_22.value = False
    LED_26.value = True
    time.sleep(.05)
    LED_26.value = False
    LED_27.value = True
    time.sleep(.05)
    LED_27.value = False
    LED_28.value = True
    time.sleep(.05)
    LED_28 .value = False



