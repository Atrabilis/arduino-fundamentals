import serial
import tkinter as tk
from tkinter import ttk
import time

PORT = "COM3"
BAUD = 9600
TIMEOUT = 0.1


def main():
    ser = get_serial(PORT, BAUD, TIMEOUT)    
    root = tk.Tk()
    root.title("HC-SR04 Sensor Monitor")
    root.geometry("400x300")
    distance_var = tk.StringVar(value="-- cm")
    ttk.Label(root, textvariable=distance_var, font=("Arial", 24)).pack(pady=10)

    def poll_serial(ser, distance_var, root):
        distance = get_distance(ser)
        if distance is not None:
            distance_var.set(f"{distance:.2f} cm")
        root.after(100, poll_serial, ser, distance_var, root)  # vuelve a revisar en 100ms        
    poll_serial(ser, distance_var, root)
    root.mainloop()


def get_distance(ser):
        ser.flushInput()  # Clear the input buffer
        time.sleep(0.1)  # Wait for the sensor to respond
        if ser.in_waiting > 0:
            last_line = ser.readline()  # Clear out any old data
            distance = float(last_line.decode("utf-8", errors="ignore").strip().split()[1])
        else:
            distance = None
        return distance

def get_serial(port, baud, timeout):
    try:
        ser = serial.Serial(port, baud, timeout=timeout)
        time.sleep(2)  # Wait for the serial connection to initialize
        return ser
    except serial.SerialException as e:
        print(f"Error opening serial port {port}: {e}")
        return None

if __name__ == "__main__":
    main()

