# import cv2 as cv
# import numpy as np
# import time
# import geocoder
# import os
# from datetime import datetime
# import telepot
# from telepot.loop import MessageLoop
# 
# # Telegram Bot Credentials
# TOKEN = "7881720805:AAG-FUHhQ9zvfG9CfnK1uqkWj_m9gDuzvk4"
# #TOKEN = "8015542205:AAE_8a79qg1Y5ciE-rNVu1a7DQxJ5OpzH-g"
# #CHAT_ID = "5517610101"
# CHAT_ID = "1481176970"
# 
# 
# # Get the current timestamp
# x = datetime.now().strftime('%Y-%m-%d %H-%M-%S')
# print(f"Script Started at: {x}")
# 
# # Load class names for YOLO
# class_name = []
# with open('utils/obj.names', 'r') as f:
#     class_name = [cname.strip() for cname in f.readlines()]
# 
# # Load YOLOv4-Tiny model
# net1 = cv.dnn.readNet('utils/yolov4_tiny.weights', 'utils/yolov4_tiny.cfg')
# 
# # Use OpenCV's default backend for Raspberry Pi
# net1.setPreferableBackend(cv.dnn.DNN_BACKEND_OPENCV)
# net1.setPreferableTarget(cv.dnn.DNN_TARGET_CPU)
# 
# # Configure the model
# model1 = cv.dnn_DetectionModel(net1)
# model1.setInputParams(size=(640, 640), scale=1/255, swapRB=True)  # Increased resolution
# 
# # Initialize webcam
# cap = cv.VideoCapture(0)
# 
# # Check if the camera opened successfully
# if not cap.isOpened():
#     raise Exception("Failed to access the camera")
# 
# # Increase frame resolution to detect smaller potholes
# cap.set(cv.CAP_PROP_FRAME_WIDTH, 640)
# cap.set(cv.CAP_PROP_FRAME_HEIGHT, 480)
# 
# # Get the geolocation
# g = geocoder.ip('me')  # Get location once to avoid slow API calls
# result_path = "pothole_coordinates"
# os.makedirs(result_path, exist_ok=True)
# 
# # Detection parameters
# Conf_threshold = 0.4  # Reduced to detect smaller potholes
# NMS_threshold = 0.3
# frame_counter = 0
# last_capture_time = 0
# starting_time = time.time()
# 
# # Initialize Telegram bot
# telegram_bot = telepot.Bot(TOKEN)
# print(telegram_bot.getMe())
# 
# print("[INFO] Starting Real-Time Pothole Detection...")
# 
# while True:
#     try:
#         ret, frame = cap.read()
#         if not ret:
#             break
# 
#         frame_counter += 1
# 
#         # Apply contrast enhancement for small potholes
#         frame = cv.convertScaleAbs(frame, alpha=1.5, beta=0)
# 
#         # Object detection
#         classes, scores, boxes = model1.detect(frame, Conf_threshold, NMS_threshold)
# 
#         for (classid, score, box) in zip(classes, scores, boxes):
#             if score < 0.6:
#                 continue  
# 
#             label = "pothole"
#             x, y, w, h = box
#             recarea = w * h
#             area = frame.shape[0] * frame.shape[1]
# 
#             # Adjusted severity detection to include smaller potholes
#             severity = "Small" if recarea / area <= 0.005 else "Medium" if recarea / area <= 0.015 else "High"
#             print(severity, "Pothole detected")
# 
#             # Draw bounding box and label
#             cv.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
#             cv.putText(frame, f"{round(score * 100, 2)}% {label} ({severity})", (x, y - 10),
#                        cv.FONT_HERSHEY_SIMPLEX, 0.5, (255, 0, 0), 2)
# 
#             # Save pothole images and location details every 2 seconds
#             current_time = time.time()
#             if current_time - last_capture_time >= 2:
#                 img_path = os.path.join(result_path, f'pot_{frame_counter}.jpg')
#                 txt_path = os.path.join(result_path, f'pot_{frame_counter}.txt')
# 
#                 cv.imwrite(img_path, frame)
#                 with open(txt_path, 'w') as f:
#                     f.write(f"Coordinates: {g.latlng}\nSeverity: {severity}")
# 
#                 last_capture_time = current_time
# 
#                 # Send Telegram alert with image
#                 telegram_bot.sendMessage(CHAT_ID, f"Pothole detected!\nSeverity: {severity}\nLocation: {g.latlng[0]:.6f}, {g.latlng[1]:.6f}")
# 
#                 with open(img_path, "rb") as photo:
#                     telegram_bot.sendPhoto(CHAT_ID, photo)
# 
#         # Calculate FPS
#         elapsed_time = time.time() - starting_time
#         fps = frame_counter / elapsed_time if elapsed_time > 0 else 0
#         cv.putText(frame, f'FPS: {fps:.2f}', (20, 50), cv.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)
# 
#         # Display output frame
#         #cv.imshow('Pothole Detection', frame)
# 
#         # Press 'q' to exit
#         if cv.waitKey(1) == ord('q'):
#             break
# 
#     except Exception as e:
#         print(f"Error: {e}")
# 
# # Cleanup
# cap.release()
# cv.destroyAllWindows()
#

import cv2 as cv
import numpy as np
import time
import geocoder
import os
from datetime import datetime
import telepot
from telepot.loop import MessageLoop

# Telegram Bot Credentials
TOKEN = ""
CHAT_ID = ""

# Get the current timestamp
x = datetime.now().strftime('%Y-%m-%d %H-%M-%S')
print(f"Script Started at: {x}")

# Load class names for YOLO
class_name = []
with open('utils/obj.names', 'r') as f:
    class_name = [cname.strip() for cname in f.readlines()]

# Load YOLOv4-Tiny model
net1 = cv.dnn.readNet('utils/yolov4_tiny.weights', 'utils/yolov4_tiny.cfg')

# Use OpenCV's default backend for Raspberry Pi
net1.setPreferableBackend(cv.dnn.DNN_BACKEND_OPENCV)
net1.setPreferableTarget(cv.dnn.DNN_TARGET_CPU)

# Configure the model
model1 = cv.dnn_DetectionModel(net1)
model1.setInputParams(size=(640, 640), scale=1/255, swapRB=True)  # Increased resolution

# Initialize webcam
cap = cv.VideoCapture(0)

# Check if the camera opened successfully
if not cap.isOpened():
    raise Exception("Failed to access the camera")

# Increase frame resolution to detect smaller potholes
cap.set(cv.CAP_PROP_FRAME_WIDTH, 640)
cap.set(cv.CAP_PROP_FRAME_HEIGHT, 480)

# Get the geolocation
g = geocoder.ip('me')  # Get location once to avoid slow API calls
result_path = "pothole_coordinates"
os.makedirs(result_path, exist_ok=True)

# Detection parameters
Conf_threshold = 0.4  # Reduced to detect smaller potholes
NMS_threshold = 0.3
frame_counter = 0
last_capture_time = 0
starting_time = time.time()

# Initialize Telegram bot
telegram_bot = telepot.Bot(TOKEN)
print(telegram_bot.getMe())

print("[INFO] Starting Real-Time Pothole Detection...")

while True:
    try:
        ret, frame = cap.read()
        if not ret:
            break

        frame_counter += 1

        # Apply contrast enhancement for small potholes
        frame = cv.convertScaleAbs(frame, alpha=1.5, beta=0)

        # Object detection
        classes, scores, boxes = model1.detect(frame, Conf_threshold, NMS_threshold)

        # Convert numpy arrays to lists if needed
        if isinstance(classes, np.ndarray):
            classes = classes.flatten()
        if isinstance(scores, np.ndarray):
            scores = scores.flatten()
        if isinstance(boxes, np.ndarray):
            boxes = boxes.tolist()

        for (classid, score, box) in zip(classes, scores, boxes):
            if score < 0.6:
                continue  

            label = "pothole"
            x, y, w, h = box
            recarea = w * h
            area = frame.shape[0] * frame.shape[1]

            # Adjusted severity detection to include smaller potholes
            ratio = recarea / area
            if ratio <= 0.005:
                severity = "Small"
            elif ratio <= 0.015:
                severity = "Medium"
            else:
                severity = "High"
            print(severity, "Pothole detected")

            # Draw bounding box and label
            cv.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
            cv.putText(frame, f"{round(float(score) * 100, 2)}% {label} ({severity})", (x, y - 10),
                       cv.FONT_HERSHEY_SIMPLEX, 0.5, (255, 0, 0), 2)

            # Save pothole images and location details every 2 seconds
            current_time = time.time()
            if current_time - last_capture_time >= 2:
                img_path = os.path.join(result_path, f'pot_{frame_counter}.jpg')
                txt_path = os.path.join(result_path, f'pot_{frame_counter}.txt')

                cv.imwrite(img_path, frame)
                with open(txt_path, 'w') as f:
                    f.write(f"Coordinates: {g.latlng}\nSeverity: {severity}")

                last_capture_time = current_time

                # Send Telegram alert with image
                try:
                    telegram_bot.sendMessage(CHAT_ID, f"Pothole detected!\nSeverity: {severity}\nLocation: {g.latlng[0]:.6f}, {g.latlng[1]:.6f}")
                    with open(img_path, "rb") as photo:
                        telegram_bot.sendPhoto(CHAT_ID, photo)
                except Exception as e:
                    print(f"Failed to send Telegram message: {e}")

        # Calculate FPS
        elapsed_time = time.time() - starting_time
        fps = frame_counter / elapsed_time if elapsed_time > 0 else 0
        cv.putText(frame, f'FPS: {fps:.2f}', (20, 50), cv.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)

        # Display output frame
        # cv.imshow('Pothole Detection', frame)

        # Press 'q' to exit
        if cv.waitKey(1) == ord('q'):
            break

    except Exception as e:
        print(f"Error: {e}")

# Cleanup
cap.release()
cv.destroyAllWindows()
