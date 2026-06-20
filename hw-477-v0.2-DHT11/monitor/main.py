import serial
import time
import tkinter as tk
from tkinter import ttk

PORT = "COM3"
BAUD = 9600

def main():
    root = tk.Tk()
    root.title("DHT11 Sensor Monitor")
    root.geometry("400x300")

    temp_var = tk.StringVar(value="-- °C")
    hum_var = tk.StringVar(value="-- %")

    ttk.Label(root, textvariable=temp_var, font=("Arial", 24)).pack(pady=10)
    ttk.Label(root, textvariable=hum_var, font=("Arial", 24)).pack(pady=10)

    ser = serial.Serial(PORT, BAUD, timeout=0.1)
    time.sleep(5)

    def poll_serial():
        last_line = b""
        while ser.in_waiting > 0:
             last_line = ser.readline()  # Clear out any old data
        line = last_line.decode("utf-8", errors="ignore").strip().split()
        if len(line) != 0:
            try:
                hum = line[1]
                temp = line[4]
                temp_var.set(f"{temp} °C")
                hum_var.set(f"{hum} %")
            except (IndexError, ValueError):
                print("Received malformed data:", line)
                pass
        
        root.after(100, poll_serial)  # vuelve a revisar en 100ms

    poll_serial()
    root.mainloop()

if __name__ == "__main__":
    main()
