import serial
import time
import tkinter as tk
from tkinter import ttk

PORT = "COM3"
BAUD = 9600


def main():
    root = tk.Tk()
    root.title("Rotary Encoder Monitor")
    root.geometry("400x300")

    pos_var = tk.StringVar(value="--")
    button_var = tk.StringVar(value="--")

    main_frame = ttk.Frame(root, padding=20)
    main_frame.grid(row=0, column=0, sticky="nsew")

    root.columnconfigure(0, weight=1)
    root.rowconfigure(0, weight=1)

    main_frame.columnconfigure(0, weight=1)
    main_frame.columnconfigure(1, weight=1)

    ttk.Label(
        main_frame,
        text="Position:",
        font=("Arial", 24)
    ).grid(row=0, column=0, sticky="w", padx=10, pady=10)

    ttk.Label(
        main_frame,
        textvariable=pos_var,
        font=("Arial", 24)
    ).grid(row=0, column=1, sticky="e", padx=10, pady=10)

    ttk.Label(
        main_frame,
        text="Button:",
        font=("Arial", 24)
    ).grid(row=1, column=0, sticky="w", padx=10, pady=10)

    ttk.Label(
        main_frame,
        textvariable=button_var,
        font=("Arial", 24)
    ).grid(row=1, column=1, sticky="e", padx=10, pady=10)

    ser = serial.Serial(PORT, BAUD, timeout=0.1)
    time.sleep(5)

    def poll_serial():
        last_line = b""

        while ser.in_waiting > 0:
            last_line = ser.readline()

        if last_line:
            fields = last_line.decode("utf-8", errors="ignore").strip().split(",")

            if len(fields) >= 2:
                try:
                    pos = fields[0]
                    button = fields[1]

                    pos_var.set(pos)
                    button_var.set(button)

                except ValueError:
                    print("Received malformed data:", fields)
            else:
                print("Received incomplete data:", fields)

        root.after(100, poll_serial)

    poll_serial()
    root.mainloop()


if __name__ == "__main__":
    main()