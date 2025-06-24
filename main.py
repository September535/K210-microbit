def car_direction():
    global speed, RGB_ALL, Follow, Track, Avoidance
    if STR == "0501":
        Acebott.move_time(Acebott.Direction.FORWARD, speed)
    if STR == "0502":
        Acebott.move_time(Acebott.Direction.BACKWARD, speed)
    if STR == "0503":
        Acebott.move_time(Acebott.Direction.LEFT, speed)
    if STR == "0504":
        Acebott.move_time(Acebott.Direction.RIGHT, speed)
    if STR == "0500":
        Acebott.stopcar()
    if STR == "06130":
        speed = 30
    if STR == "06190":
        speed = 90
    if STR == "06255":
        speed = 100
    if STR != "0101" and (STR != "0201" and STR != "0301"):
        RGB_ALL = 0
        Follow = 0
        Track = 0
        Avoidance = 0
def Little_Star():
    if STR == "0408":
        music.play(music.tone_playable(262, music.beat(BeatFraction.WHOLE)),
            music.PlaybackMode.UNTIL_DONE)
        music.rest(music.beat(BeatFraction.SIXTEENTH))
        music.play(music.tone_playable(262, music.beat(BeatFraction.WHOLE)),
            music.PlaybackMode.UNTIL_DONE)
        music.rest(music.beat(BeatFraction.SIXTEENTH))
        music.play(music.tone_playable(392, music.beat(BeatFraction.WHOLE)),
            music.PlaybackMode.UNTIL_DONE)
        music.rest(music.beat(BeatFraction.SIXTEENTH))
        music.play(music.tone_playable(392, music.beat(BeatFraction.WHOLE)),
            music.PlaybackMode.UNTIL_DONE)
        music.rest(music.beat(BeatFraction.SIXTEENTH))
        music.play(music.tone_playable(440, music.beat(BeatFraction.WHOLE)),
            music.PlaybackMode.UNTIL_DONE)
        music.rest(music.beat(BeatFraction.SIXTEENTH))
        music.play(music.tone_playable(440, music.beat(BeatFraction.WHOLE)),
            music.PlaybackMode.UNTIL_DONE)
        music.rest(music.beat(BeatFraction.SIXTEENTH))
        music.play(music.tone_playable(392, music.beat(BeatFraction.DOUBLE)),
            music.PlaybackMode.UNTIL_DONE)
        music.rest(music.beat(BeatFraction.SIXTEENTH))
        music.play(music.tone_playable(349, music.beat(BeatFraction.WHOLE)),
            music.PlaybackMode.UNTIL_DONE)
        music.rest(music.beat(BeatFraction.SIXTEENTH))
        music.play(music.tone_playable(349, music.beat(BeatFraction.WHOLE)),
            music.PlaybackMode.UNTIL_DONE)
        music.rest(music.beat(BeatFraction.SIXTEENTH))
        music.play(music.tone_playable(330, music.beat(BeatFraction.WHOLE)),
            music.PlaybackMode.UNTIL_DONE)
        music.rest(music.beat(BeatFraction.SIXTEENTH))
        music.play(music.tone_playable(330, music.beat(BeatFraction.WHOLE)),
            music.PlaybackMode.UNTIL_DONE)
        music.rest(music.beat(BeatFraction.SIXTEENTH))
        music.play(music.tone_playable(294, music.beat(BeatFraction.WHOLE)),
            music.PlaybackMode.UNTIL_DONE)
        music.rest(music.beat(BeatFraction.SIXTEENTH))
        music.play(music.tone_playable(294, music.beat(BeatFraction.WHOLE)),
            music.PlaybackMode.UNTIL_DONE)
        music.rest(music.beat(BeatFraction.SIXTEENTH))
        music.play(music.tone_playable(262, music.beat(BeatFraction.DOUBLE)),
            music.PlaybackMode.UNTIL_DONE)
def New_Year():
    if STR == "0410":
        music.play(music.tone_playable(262, music.beat(BeatFraction.HALF)),
            music.PlaybackMode.UNTIL_DONE)
        music.rest(music.beat(BeatFraction.SIXTEENTH))
        music.play(music.tone_playable(262, music.beat(BeatFraction.HALF)),
            music.PlaybackMode.UNTIL_DONE)
        music.rest(music.beat(BeatFraction.SIXTEENTH))
        music.play(music.tone_playable(262, music.beat(BeatFraction.WHOLE)),
            music.PlaybackMode.UNTIL_DONE)
        music.rest(music.beat(BeatFraction.SIXTEENTH))
        music.play(music.tone_playable(196, music.beat(BeatFraction.WHOLE)),
            music.PlaybackMode.UNTIL_DONE)
        music.rest(music.beat(BeatFraction.SIXTEENTH))
        music.play(music.tone_playable(330, music.beat(BeatFraction.HALF)),
            music.PlaybackMode.UNTIL_DONE)
        music.rest(music.beat(BeatFraction.SIXTEENTH))
        music.play(music.tone_playable(330, music.beat(BeatFraction.HALF)),
            music.PlaybackMode.UNTIL_DONE)
        music.rest(music.beat(BeatFraction.SIXTEENTH))
        music.play(music.tone_playable(330, music.beat(BeatFraction.WHOLE)),
            music.PlaybackMode.UNTIL_DONE)
        music.rest(music.beat(BeatFraction.SIXTEENTH))
        music.play(music.tone_playable(262, music.beat(BeatFraction.WHOLE)),
            music.PlaybackMode.UNTIL_DONE)
        music.rest(music.beat(BeatFraction.SIXTEENTH))
        music.play(music.tone_playable(262, music.beat(BeatFraction.HALF)),
            music.PlaybackMode.UNTIL_DONE)
        music.rest(music.beat(BeatFraction.SIXTEENTH))
        music.play(music.tone_playable(330, music.beat(BeatFraction.HALF)),
            music.PlaybackMode.UNTIL_DONE)
        music.rest(music.beat(BeatFraction.SIXTEENTH))
        music.play(music.tone_playable(392, music.beat(BeatFraction.WHOLE)),
            music.PlaybackMode.UNTIL_DONE)
        music.rest(music.beat(BeatFraction.SIXTEENTH))
        music.play(music.tone_playable(392, music.beat(BeatFraction.WHOLE)),
            music.PlaybackMode.UNTIL_DONE)
        music.rest(music.beat(BeatFraction.SIXTEENTH))
        music.play(music.tone_playable(349, music.beat(BeatFraction.HALF)),
            music.PlaybackMode.UNTIL_DONE)
        music.rest(music.beat(BeatFraction.SIXTEENTH))
        music.play(music.tone_playable(330, music.beat(BeatFraction.HALF)),
            music.PlaybackMode.UNTIL_DONE)

def on_bluetooth_connected():
    basic.show_icon(IconNames.YES)
    basic.pause(2000)
bluetooth.on_bluetooth_connected(on_bluetooth_connected)

def on_bluetooth_disconnected():
    basic.pause(100)
    Acebott.stopcar()
    basic.show_icon(IconNames.NO)
bluetooth.on_bluetooth_disconnected(on_bluetooth_disconnected)

def Jingle_bell():
    if STR == "0409":
        music.play(music.tone_playable(330, music.beat(BeatFraction.HALF)),
            music.PlaybackMode.UNTIL_DONE)
        music.rest(music.beat(BeatFraction.SIXTEENTH))
        music.play(music.tone_playable(330, music.beat(BeatFraction.HALF)),
            music.PlaybackMode.UNTIL_DONE)
        music.rest(music.beat(BeatFraction.SIXTEENTH))
        music.play(music.tone_playable(330, music.beat(BeatFraction.WHOLE)),
            music.PlaybackMode.UNTIL_DONE)
        music.rest(music.beat(BeatFraction.SIXTEENTH))
        music.play(music.tone_playable(330, music.beat(BeatFraction.HALF)),
            music.PlaybackMode.UNTIL_DONE)
        music.rest(music.beat(BeatFraction.SIXTEENTH))
        music.play(music.tone_playable(330, music.beat(BeatFraction.HALF)),
            music.PlaybackMode.UNTIL_DONE)
        music.rest(music.beat(BeatFraction.SIXTEENTH))
        music.play(music.tone_playable(330, music.beat(BeatFraction.WHOLE)),
            music.PlaybackMode.UNTIL_DONE)
        music.rest(music.beat(BeatFraction.SIXTEENTH))
        music.play(music.tone_playable(330, music.beat(BeatFraction.HALF)),
            music.PlaybackMode.UNTIL_DONE)
        music.play(music.tone_playable(392, music.beat(BeatFraction.HALF)),
            music.PlaybackMode.UNTIL_DONE)
        music.play(music.tone_playable(262, music.beat(BeatFraction.HALF)),
            music.PlaybackMode.UNTIL_DONE)
        music.play(music.tone_playable(262, music.beat(BeatFraction.QUARTER)),
            music.PlaybackMode.UNTIL_DONE)
        music.play(music.tone_playable(294, music.beat(BeatFraction.QUARTER)),
            music.PlaybackMode.UNTIL_DONE)
        music.play(music.tone_playable(330, music.beat(BeatFraction.DOUBLE)),
            music.PlaybackMode.UNTIL_DONE)
def RGB_state():
    global RGB_ALL, RGB_bit, RGB_Red_ALL, RGB_Red_Left, RGB_Red_Rigth, RGB_Green_ALL, RGB_Green_Left, RGB_Green_Rigth, RGB_Blue_ALL, RGB_Blue_Left, RGB_Blue_Rigth
    if (STR.includes("0801") or (STR.includes("0802") or STR.includes("0803"))) and RGB_bit == 0:
        RGB_ALL = 1
    if (STR.includes("0801") or (STR.includes("0802") or STR.includes("0803"))) and RGB_bit == 1:
        RGB_ALL = 2
    if (STR.includes("0801") or (STR.includes("0802") or STR.includes("0803"))) and RGB_bit == 2:
        RGB_ALL = 3
    if STR == "0701":
        RGB_bit = 0
        RGB_ALL = 1
    elif STR == "0702":
        RGB_bit = 1
        RGB_ALL = 2
    elif STR == "0703":
        RGB_bit = 2
        RGB_ALL = 3
    if RGB_ALL == 1:
        Acebott.singleheadlights(Acebott.RGBLights.ALL,
            parse_float(RGB_Red_ALL),
            parse_float(RGB_Green_ALL),
            parse_float(RGB_Blue_ALL))
    elif RGB_ALL == 2:
        Acebott.singleheadlights(Acebott.RGBLights.RGB_L,
            parse_float(RGB_Red_Left),
            parse_float(RGB_Green_Left),
            parse_float(RGB_Blue_Left))
    elif RGB_ALL == 3:
        Acebott.singleheadlights(Acebott.RGBLights.RGB_R,
            parse_float(RGB_Red_Rigth),
            parse_float(RGB_Green_Rigth),
            parse_float(RGB_Blue_Rigth))
    if STR.includes("0801"):
        if RGB_ALL == 1:
            RGB_Red_ALL = STR.substr(4, len(STR) - 4)
        elif RGB_ALL == 2:
            RGB_Red_Left = STR.substr(4, len(STR) - 4)
        elif RGB_ALL == 3:
            RGB_Red_Rigth = STR.substr(4, len(STR) - 4)
    elif STR.includes("0802"):
        if RGB_ALL == 1:
            RGB_Green_ALL = STR.substr(4, len(STR) - 4)
        elif RGB_ALL == 2:
            RGB_Green_Left = STR.substr(4, len(STR) - 4)
        elif RGB_ALL == 3:
            RGB_Green_Rigth = STR.substr(4, len(STR) - 4)
    elif STR.includes("0803"):
        if RGB_ALL == 1:
            RGB_Blue_ALL = STR.substr(4, len(STR) - 4)
        elif RGB_ALL == 2:
            RGB_Blue_Left = STR.substr(4, len(STR) - 4)
        elif RGB_ALL == 3:
            RGB_Blue_Rigth = STR.substr(4, len(STR) - 4)
def follow():
    global Follow
    if STR == "0301":
        Follow = 1
    elif STR == "0300":
        Follow = 0
        Acebott.stopcar()
    if Follow == 1:
        if Acebott.ultrasonic_distance(DigitalPin.P15, DigitalWritePin.P14, DistanceUnit.CM) <= 10:
            Acebott.move_time(Acebott.Direction.BACKWARD, 60)
            basic.pause(200)
        if Acebott.ultrasonic_distance(DigitalPin.P15, DigitalWritePin.P14, DistanceUnit.CM) >= 15 and Acebott.ultrasonic_distance(DigitalPin.P15, DigitalWritePin.P14, DistanceUnit.CM) <= 20:
            basic.pause(200)
            Acebott.stopcar()
        if Acebott.ultrasonic_distance(DigitalPin.P15, DigitalWritePin.P14, DistanceUnit.CM) >= 20 and Acebott.ultrasonic_distance(DigitalPin.P15, DigitalWritePin.P14, DistanceUnit.CM) <= 25:
            basic.pause(200)
            Acebott.move_time(Acebott.Direction.FORWARD, 45)
        if Acebott.ultrasonic_distance(DigitalPin.P15, DigitalWritePin.P14, DistanceUnit.CM) >= 25 and Acebott.ultrasonic_distance(DigitalPin.P15, DigitalWritePin.P14, DistanceUnit.CM) <= 50:
            Acebott.move_time(Acebott.Direction.FORWARD, 45)
        if Acebott.ultrasonic_distance(DigitalPin.P15, DigitalWritePin.P14, DistanceUnit.CM) >= 51:
            Acebott.stopcar()
def track():
    global Track
    if STR == "0101":
        Track = 1
    elif STR == "0100":
        Track = 0
        Acebott.stopcar()
    if Track == 1:
        if Acebott.tracking(Acebott.MbPins.RIGHT) >= 900 and Acebott.tracking(Acebott.MbPins.LEFT) >= 900:
            Acebott.stopcar()
        if Acebott.tracking(Acebott.MbPins.RIGHT) <= 310 and Acebott.tracking(Acebott.MbPins.LEFT) <= 310:
            Acebott.stopcar()
        if Acebott.tracking(Acebott.MbPins.RIGHT) >= 700 and Acebott.tracking(Acebott.MbPins.RIGHT) <= 900:
            Acebott.move_time(Acebott.Direction.LEFT, 10)
        if Acebott.tracking(Acebott.MbPins.LEFT) >= 700 and Acebott.tracking(Acebott.MbPins.LEFT) <= 900:
            Acebott.move_time(Acebott.Direction.RIGHT, 10)
        if Acebott.tracking(Acebott.MbPins.LEFT) >= 240 and Acebott.tracking(Acebott.MbPins.LEFT) <= 800 and (Acebott.tracking(Acebott.MbPins.RIGHT) >= 240 and Acebott.tracking(Acebott.MbPins.RIGHT) <= 700):
            Acebott.move_time(Acebott.Direction.FORWARD, 30)
def avoidance():
    global Avoidance
    if STR == "0201":
        Avoidance = 1
    elif STR == "0200":
        Avoidance = 0
        Acebott.stopcar()
    if Avoidance == 1:
        if Acebott.ultrasonic_distance(DigitalPin.P15, DigitalWritePin.P14, DistanceUnit.CM) <= 10:
            Acebott.stopcar()
            basic.pause(500)
            if Math.random_boolean():
                Acebott.move_time(Acebott.Direction.RIGHT, 60)
                basic.pause(250)
            else:
                Acebott.move_time(Acebott.Direction.LEFT, 60)
                basic.pause(250)
        else:
            basic.pause(150)
            Acebott.move_time(Acebott.Direction.FORWARD, 45)
def Have_a_farm():
    if STR == "0411":
        music.play(music.tone_playable(262, music.beat(BeatFraction.WHOLE)),
            music.PlaybackMode.UNTIL_DONE)
        music.rest(music.beat(BeatFraction.SIXTEENTH))
        music.play(music.tone_playable(262, music.beat(BeatFraction.WHOLE)),
            music.PlaybackMode.UNTIL_DONE)
        music.rest(music.beat(BeatFraction.SIXTEENTH))
        music.play(music.tone_playable(262, music.beat(BeatFraction.WHOLE)),
            music.PlaybackMode.UNTIL_DONE)
        music.rest(music.beat(BeatFraction.SIXTEENTH))
        music.play(music.tone_playable(196, music.beat(BeatFraction.WHOLE)),
            music.PlaybackMode.UNTIL_DONE)
        music.rest(music.beat(BeatFraction.SIXTEENTH))
        music.play(music.tone_playable(220, music.beat(BeatFraction.WHOLE)),
            music.PlaybackMode.UNTIL_DONE)
        music.rest(music.beat(BeatFraction.SIXTEENTH))
        music.play(music.tone_playable(220, music.beat(BeatFraction.WHOLE)),
            music.PlaybackMode.UNTIL_DONE)
        music.rest(music.beat(BeatFraction.SIXTEENTH))
        music.play(music.tone_playable(196, music.beat(BeatFraction.DOUBLE)),
            music.PlaybackMode.UNTIL_DONE)
        music.rest(music.beat(BeatFraction.SIXTEENTH))
        music.play(music.tone_playable(330, music.beat(BeatFraction.WHOLE)),
            music.PlaybackMode.UNTIL_DONE)
        music.rest(music.beat(BeatFraction.SIXTEENTH))
        music.play(music.tone_playable(330, music.beat(BeatFraction.WHOLE)),
            music.PlaybackMode.UNTIL_DONE)
        music.rest(music.beat(BeatFraction.SIXTEENTH))
        music.play(music.tone_playable(294, music.beat(BeatFraction.WHOLE)),
            music.PlaybackMode.UNTIL_DONE)
        music.rest(music.beat(BeatFraction.SIXTEENTH))
        music.play(music.tone_playable(294, music.beat(BeatFraction.WHOLE)),
            music.PlaybackMode.UNTIL_DONE)
        music.rest(music.beat(BeatFraction.SIXTEENTH))
        music.play(music.tone_playable(262, music.beat(BeatFraction.DOUBLE)),
            music.PlaybackMode.UNTIL_DONE)
        music.play(music.tone_playable(262, music.beat(BeatFraction.WHOLE)),
            music.PlaybackMode.UNTIL_DONE)

def on_uart_data_received():
    global STR
    STR = bluetooth.uart_read_until(serial.delimiters(Delimiters.HASH))
    Buzzer()
    car_direction()
    RGB_state()
    New_Year()
    Little_Star()
    Have_a_farm()
    Jingle_bell()
bluetooth.on_uart_data_received(serial.delimiters(Delimiters.HASH), on_uart_data_received)

def Buzzer():
    if STR == "0401":
        music.play(music.tone_playable(262, music.beat(BeatFraction.HALF)),
            music.PlaybackMode.IN_BACKGROUND)
    if STR == "0402":
        music.play(music.tone_playable(294, music.beat(BeatFraction.HALF)),
            music.PlaybackMode.IN_BACKGROUND)
    if STR == "0403":
        music.play(music.tone_playable(330, music.beat(BeatFraction.HALF)),
            music.PlaybackMode.IN_BACKGROUND)
    if STR == "0404":
        music.play(music.tone_playable(349, music.beat(BeatFraction.HALF)),
            music.PlaybackMode.IN_BACKGROUND)
    if STR == "0405":
        music.play(music.tone_playable(392, music.beat(BeatFraction.HALF)),
            music.PlaybackMode.IN_BACKGROUND)
    if STR == "0406":
        music.play(music.tone_playable(440, music.beat(BeatFraction.HALF)),
            music.PlaybackMode.IN_BACKGROUND)
    if STR == "0407":
        music.play(music.tone_playable(494, music.beat(BeatFraction.HALF)),
            music.PlaybackMode.IN_BACKGROUND)
RGB_Blue_Rigth = ""
RGB_Green_Rigth = ""
RGB_Red_Rigth = ""
RGB_Blue_Left = ""
RGB_Green_Left = ""
RGB_Red_Left = ""
RGB_Blue_ALL = ""
RGB_Green_ALL = ""
RGB_Red_ALL = ""
RGB_bit = 0
Avoidance = 0
Track = 0
Follow = 0
RGB_ALL = 0
speed = 0
STR = ""
STR = ""
speed = 90
basic.show_icon(IconNames.HEART)
bluetooth.start_uart_service()

def on_forever():
    track()
    follow()
    avoidance()
basic.forever(on_forever)
