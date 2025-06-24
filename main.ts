// 机器学习函数
function machine_learning () {
    if (set_mode != 9) {
        let data_send = pins.createBuffer(3)
data_send.setNumber(NumberFormat.UInt8LE, 0, 9)
data_send.setNumber(NumberFormat.UInt8LE, 1, 13)
data_send.setNumber(NumberFormat.UInt8LE, 2, 10)
serial.writeBuffer(data_send)
        basic.pause(100)
        set_mode = 9
    }
    received = serial.readBuffer(0)
    if (received && received.length > 0) {
        let data_len = received.getNumber(NumberFormat.UInt8LE, 0)
if (received.length >= data_len + 1 && data_len >= 1) {
            let classNum = received.getNumber(NumberFormat.UInt8LE, 1)
tag = classNum.toString()
return true
        }
    }
    return false
}
function barcode_recognize () {
    if (set_mode != 3) {
        let data_send2 = pins.createBuffer(3)
data_send2.setNumber(NumberFormat.UInt8LE, 0, 3)
data_send2.setNumber(NumberFormat.UInt8LE, 1, 13)
data_send2.setNumber(NumberFormat.UInt8LE, 2, 10)
serial.writeBuffer(data_send2)
        basic.pause(100)
        set_mode = 3
    }
    available = serial.readBuffer(0)
    if (available && available.length > 0) {
        let data_len2 = available.getNumber(NumberFormat.UInt8LE, 0)
if (available.length >= data_len2 + 1) {
            x = available.getNumber(NumberFormat.UInt16BE, 1)
y = available.getNumber(NumberFormat.UInt8LE, 3)
w = available.getNumber(NumberFormat.UInt16BE, 4)
h = available.getNumber(NumberFormat.UInt8LE, 6)
tag = ""
            for (let k = 7; k < data_len2 + 1; k++) {
                tag += String.fromCharCode(available.getNumber(NumberFormat.UInt8LE, k))
            }
return true
        }
    }
    return false
}
function number_recognize () {
    if (set_mode != 6) {
        let data_send3 = pins.createBuffer(3)
data_send3.setNumber(NumberFormat.UInt8LE, 0, 6)
data_send3.setNumber(NumberFormat.UInt8LE, 1, 13)
data_send3.setNumber(NumberFormat.UInt8LE, 2, 10)
serial.writeBuffer(data_send3)
        basic.pause(100)
        set_mode = 6
    }
    received = serial.readBuffer(0)
    if (received && received.length > 0) {
        let data_len3 = received.getNumber(NumberFormat.UInt8LE, 0)
if (received.length >= data_len3 + 1 && data_len3 >= 1) {
            let numberValue = received.getNumber(NumberFormat.UInt8LE, 1)
tag = numberValue.toString()
return true
        }
    }
    return false
}
bluetooth.onBluetoothConnected(function () {
    basic.pause(2000)
    basic.showIcon(IconNames.Yes)
})
bluetooth.onBluetoothDisconnected(function () {
    basic.pause(100)
    Acebott.stopcar()
    basic.showIcon(IconNames.No)
})
input.onButtonPressed(Button.A, function () {
    State = State + 1
    if (State > 9) {
        State = 0
    }
})
// 二维码识别函数
function qrcode_recognize () {
    if (set_mode != 2) {
        let data_send4 = pins.createBuffer(3)
data_send4.setNumber(NumberFormat.UInt8LE, 0, 2)
data_send4.setNumber(NumberFormat.UInt8LE, 1, 13)
data_send4.setNumber(NumberFormat.UInt8LE, 2, 10)
serial.writeBuffer(data_send4)
        basic.pause(100)
        set_mode = 2
    }
    available = serial.readBuffer(0)
    if (available && available.length > 0) {
        let data_len4 = available.getNumber(NumberFormat.UInt8LE, 0)
if (available.length >= data_len4 + 1) {
            x = available.getNumber(NumberFormat.UInt16BE, 1)
y = available.getNumber(NumberFormat.UInt8LE, 3)
w = available.getNumber(NumberFormat.UInt16BE, 4)
h = available.getNumber(NumberFormat.UInt8LE, 6)
tag = ""
            for (let m = 7; m < data_len4 + 1; m++) {
                tag += String.fromCharCode(available.getNumber(NumberFormat.UInt8LE, m))
            }
return true
        }
    }
    return false
}
// 人脸识别函数
function face_recognize () {
    if (set_mode != 4) {
        let data_send5 = pins.createBuffer(3)
data_send5.setNumber(NumberFormat.UInt8LE, 0, 4)
data_send5.setNumber(NumberFormat.UInt8LE, 1, 13)
data_send5.setNumber(NumberFormat.UInt8LE, 2, 10)
serial.writeBuffer(data_send5)
        basic.pause(100)
        set_mode = 4
    }
    received = serial.readBuffer(0)
    if (received && received.length > 0) {
        let data_len5 = received.getNumber(NumberFormat.UInt8LE, 0)
if (received.length >= data_len5 + 1 && data_len5 >= 10) {
            x = received.getNumber(NumberFormat.UInt16BE, 1)
y = received.getNumber(NumberFormat.UInt8LE, 3)
w = received.getNumber(NumberFormat.UInt16BE, 4)
h = received.getNumber(NumberFormat.UInt8LE, 6)
cx = received.getNumber(NumberFormat.UInt16BE, 7)
cy = received.getNumber(NumberFormat.UInt8LE, 9)
let face_id = received.getNumber(NumberFormat.UInt8LE, 10)
tag = " " + face_id
            return true
        }
    }
    return false
}
function image_recognize () {
    if (set_mode != 5) {
        let data_send6 = pins.createBuffer(3)
data_send6.setNumber(NumberFormat.UInt8LE, 0, 5)
data_send6.setNumber(NumberFormat.UInt8LE, 1, 13)
data_send6.setNumber(NumberFormat.UInt8LE, 2, 10)
serial.writeBuffer(data_send6)
        basic.pause(100)
        set_mode = 5
    }
    available = serial.readBuffer(0)
    if (available && available.length > 0) {
        let data_len6 = available.getNumber(NumberFormat.UInt8LE, 0)
if (available.length >= data_len6 + 1) {
            x = available.getNumber(NumberFormat.UInt16BE, 1)
y = available.getNumber(NumberFormat.UInt8LE, 3)
w = available.getNumber(NumberFormat.UInt16BE, 4)
h = available.getNumber(NumberFormat.UInt8LE, 6)
tag = ""
            for (let n = 10; n < data_len6 + 1; n++) {
                tag += String.fromCharCode(available.getNumber(NumberFormat.UInt8LE, n))
            }
return true
        }
    }
    return false
}
// 交通标志识别函数
function Traffic_recognize (mode: number) {
    if (set_mode != 7) {
        let data_send7 = pins.createBuffer(4)
data_send7.setNumber(NumberFormat.UInt8LE, 0, 7)
data_send7.setNumber(NumberFormat.UInt8LE, 1, mode)
data_send7.setNumber(NumberFormat.UInt8LE, 2, 13)
data_send7.setNumber(NumberFormat.UInt8LE, 3, 10)
serial.writeBuffer(data_send7)
        basic.pause(100)
        set_mode = 7
    }
    received = serial.readBuffer(0)
    if (received && received.length > 0) {
        let data_len42 = received.getNumber(NumberFormat.UInt8LE, 0)
if (received.length >= data_len42 + 1 && data_len42 >= 9) {
            x = received.getNumber(NumberFormat.UInt16BE, 1)
y = received.getNumber(NumberFormat.UInt8LE, 3)
w = received.getNumber(NumberFormat.UInt16BE, 4)
h = received.getNumber(NumberFormat.UInt8LE, 6)
cx = received.getNumber(NumberFormat.UInt16BE, 7)
cy = received.getNumber(NumberFormat.UInt8LE, 9)
tag = ""
            for (let i = 10; i < data_len42 + 1; i++) {
                tag += String.fromCharCode(received.getNumber(NumberFormat.UInt8LE, i))
            }
return true
        }
    }
    return false
}
function color_recognize (index: number, pixels_threshold: number, area_threshold: number) {
    if (set_mode != 1 || index != color_index) {
        let data_send8 = pins.createBuffer(8)
data_send8.setNumber(NumberFormat.UInt8LE, 0, 1)
data_send8.setNumber(NumberFormat.UInt8LE, 1, index)
data_send8.setNumber(NumberFormat.UInt8LE, 2, area_threshold >> 8)
data_send8.setNumber(NumberFormat.UInt8LE, 3, area_threshold & 0xFF)
data_send8.setNumber(NumberFormat.UInt8LE, 4, 100 >> 8)
data_send8.setNumber(NumberFormat.UInt8LE, 5, 100 & 0xFF)
data_send8.setNumber(NumberFormat.UInt8LE, 6, 13)
data_send8.setNumber(NumberFormat.UInt8LE, 7, 10)
serial.writeBuffer(data_send8)
        basic.pause(100)
        set_mode = 1
        color_index = index
    }
    received = serial.readBuffer(0)
    if (received && received.length > 0) {
        let data_len7 = received.getNumber(NumberFormat.UInt8LE, 0)
x = received.getNumber(NumberFormat.UInt16LE, 1)
y = received.getNumber(NumberFormat.UInt8LE, 3)
w = received.getNumber(NumberFormat.UInt16LE, 4)
h = received.getNumber(NumberFormat.UInt8LE, 6)
cx = received.getNumber(NumberFormat.UInt16LE, 7)
cy = received.getNumber(NumberFormat.UInt8LE, 9)
tag = ""
        for (let j = 10; j < data_len7; j++) {
            tag += String.fromCharCode(received.getNumber(NumberFormat.UInt8LE, j))
        }
return true
    }
    return false
}
function sendCommand (cmd: string) {
    serial.writeString(cmd)
    serial.writeString("" + ("\r\n"))
}
bluetooth.onUartDataReceived(serial.delimiters(Delimiters.Hash), function () {
    STR = bluetooth.uartReadUntil(serial.delimiters(Delimiters.Hash))
    serial.writeLine(STR)
    State = parseFloat(STR.substr(3, STR.length - 3))
})
input.onButtonPressed(Button.B, function () {
    State = State - 1
    if (State < 0) {
        State = 9
    }
})
function visual_patrol () {
    if (set_mode != 8) {
        let data_send9 = pins.createBuffer(3)
data_send9.setNumber(NumberFormat.UInt8LE, 0, 8)
data_send9.setNumber(NumberFormat.UInt8LE, 1, 13)
data_send9.setNumber(NumberFormat.UInt8LE, 2, 10)
serial.writeBuffer(data_send9)
        basic.pause(100)
        set_mode = 8
    }
    received = serial.readBuffer(0)
    if (received && received.length > 0) {
        let data_len8 = received.getNumber(NumberFormat.UInt8LE, 0)
if (received.length >= data_len8 + 1 && data_len8 >= 1) {
            angle = received.getNumber(NumberFormat.UInt8LE, 1) - 60
            return true
        }
    }
    return false
}
function RGB_set (red: number, green: number, blue: number) {
    if (red_value != red || green_value != green || blue_value != blue) {
        let data_send10 = pins.createBuffer(7)
data_send10.setNumber(NumberFormat.UInt8LE, 0, set_mode)
data_send10.setNumber(NumberFormat.UInt8LE, 1, 255)
data_send10.setNumber(NumberFormat.UInt8LE, 2, red)
data_send10.setNumber(NumberFormat.UInt8LE, 3, green)
data_send10.setNumber(NumberFormat.UInt8LE, 4, blue)
data_send10.setNumber(NumberFormat.UInt8LE, 5, 13)
data_send10.setNumber(NumberFormat.UInt8LE, 6, 10)
serial.writeBuffer(data_send10)
        basic.pause(100)
    }
    red_value = red
    green_value = green
    blue_value = blue
}
function Default_menu () {
    if (set_mode != 0) {
        let data_send11 = pins.createBuffer(3)
data_send11.setNumber(NumberFormat.UInt8LE, 0, 0)
data_send11.setNumber(NumberFormat.UInt8LE, 1, 13)
data_send11.setNumber(NumberFormat.UInt8LE, 2, 10)
serial.writeBuffer(data_send11)
        basic.pause(100)
        set_mode = 0
    }
}
let blue_value = 0
let green_value = 0
let red_value = 0
let angle = 0
let color_index = 0
let STR = ""
let State = 0
let received: Buffer = null
let h = 0
let w = 0
let x = 0
let y = 0
let cx = 0
let cy = 0
let available: Buffer = null
let set_mode = 0
let tag = ""
let received2 = null
State = 0
STR = ""
basic.showIcon(IconNames.Heart)
serial.redirect(
SerialPin.P14,
SerialPin.P15,
BaudRate.BaudRate115200
)
bluetooth.startUartService()
let UartBuff = pins.createBuffer(64)
basic.forever(function () {
    basic.showString("" + (State))
    if (State == 1) {
        barcode_recognize()
    } else if (State == 2) {
        qrcode_recognize()
    } else if (State == 4) {
        color_recognize(1, 1, 1)
    } else if (State == 3) {
        number_recognize()
    } else if (State == 5) {
        image_recognize()
    } else if (State == 6) {
        visual_patrol()
    } else if (State == 7) {
        Traffic_recognize(1)
    } else if (State == 8) {
        face_recognize()
    } else if (State == 9) {
        machine_learning()
    } else if (State == 0) {
        Default_menu()
    }
})
