# PC RFID reader

Reads an UID from a RFID tag and types it on a PC as a simple keyboard input. 
Useful for filing forms while registering tags at a desktop interface.
Tested with MEGA 2560 board and Python3

## How does it works?

### Arduino reader
Uses a RFID module with the [MFRC522.h](https://github.com/miguelbalboa/rfid) lib.

Reads the card, sends as HEX to serial.

Inside `arduino/` directory you will find a Platformio project but code can be used normally with the default Arduino IDE.

Don't forget to set the pins you are using with your module.

### Python driver

Uses `pyserial` to read what the Arduino is sending, then types each character as a keyboard input with `pynput`. Install them through `pip` before running `driver.py`
