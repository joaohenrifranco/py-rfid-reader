# PC RFID reader

Reads an UID from a RFID tag and types it on a PC as a simple keyboard input. 
Useful for filing forms while registering tags at a desktop interface.
Tested with MEGA 2560 board and Python3

## How does it works?
Uses python code running on the computer connected to the Arduino to read from serial and send data as keystrokes.

### Arduino reader
Uses a RFID module with the [MFRC522.h](https://github.com/miguelbalboa/rfid) lib.

Reads the card, sends as HEX to serial.

Inside `arduino/` directory you will find a Platformio project however code can be used normally with the default Arduino IDE.

Don't forget to set the pins you are using with your module.

### Python driver

Inside `driver/` directory.

Uses `pyserial` to read what the Arduino is sending, then types each character as a keyboard input with `pynput`. Install them through `pip` before running `driver.py`
