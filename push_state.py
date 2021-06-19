import serial
import requests

# Converts the Serial port output(in bytes) to integer
def bytes_to_int(bytes):
    result = 0

    for b in bytes:
        result = result * 256 + int(b)

    return result

# Triggers webhook on Integromat, which then writes to evernote
def webhook_trigger():
    pass
    URL = "https://hook.integromat.com/c6otybmvzdjgg4nif9h1g6fik6fi25fd" # REPLACE WITH CORRECT URL
    response = requests.request("GET", URL)
    print (response.text)

# Serial port
ser = serial.Serial('COM6', 9600, timeout=0)
ser.flushInput()

# If push button state is 1, triggers webhook to write time-stamp to Evernote
while True:
        ser_bytes = (ser.readline())
        decoded_bytes = bytes_to_int((ser_bytes[0:len(ser_bytes)-2].decode("utf-8")))
        print(decoded_bytes)
        if decoded_bytes == 1:
            webhook_trigger()
            break
