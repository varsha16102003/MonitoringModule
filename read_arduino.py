import serial
import time
import firebase_admin
from firebase_admin import credentials, db

# Firebase setup
cred = credentials.Certificate("C:\heart-rate-monitoring-12-firebase-adminsdk-lkau3-088a0ff171.json")
firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://heart-rate-monitoring-12-default-rtdb.firebaseio.com/'
})

# Reference to your Firebase Realtime Database
ref = db.reference('heartrate')

# Setup serial communication with Arduino
arduino = serial.Serial('COM3', 115200, timeout=1)
time.sleep(2)  # wait for the serial connection to initialize

while True:
    try:
        data = arduino.readline().decode('utf-8').strip()
        if data:
            print(f"Received data: {data}")
            ref.set({'BPM': data})  # Send data to Firebase
    except KeyboardInterrupt:
        print("Exiting...")
        break

arduino.close()
