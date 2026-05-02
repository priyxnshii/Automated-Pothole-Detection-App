Pothole Detection & Alert System (StreetSafe)
->Overview:
StreetSafe is an intelligent pothole detection and alert system that uses Computer Vision, IoT, and Mobile App integration to detect road surface defects in real-time and notify users.
The system combines camera input, ultrasonic sensors, GPS tracking, and ML models to identify potholes, assess severity, and display them on a map for better road safety and maintenance planning.
This project aims to reduce accidents, vehicle damage, and improve smart city infrastructure.

->Key Features:
1. Real-time pothole detection using image processing / ML
2. GPS-based location tracking of potholes
3. Severity detection using sensor data
4. Android app (StreetSafe) with map integration
5. Alerts for nearby potholes
6. Visualization of potholes on Google Maps
7. Optional robotic repair simulation module

->System Architecture:
Camera + Ultrasonic Sensor → Raspberry Pi → ML Model → GPS Tagging
                                      ↓
                                Mobile App (StreetSafe)
                                      ↓
                          Map Visualization + Alerts
The system uses multi-sensor fusion to improve detection accuracy and reduce false positives.

->Tech Stack:
Software:
Python
OpenCV
TensorFlow / Keras
NumPy, Matplotlib
Android (Java)
Google Maps API
Hardware:
Raspberry Pi
Pi Camera Module
Ultrasonic Sensor
GPS Module
Servo Motor
Motor Driver
Power Supply

->Mobile App Features:
RecyclerView-based pothole listing
Google Maps integration with markers
Detailed pothole view (image + location)
Navigation support via Google Maps
Real-time updates
->How It Works:
Camera captures real-time road images
ML model detects potholes from images
Ultrasonic sensor measures depth
GPS module tags the location
Data is sent to the mobile app
App displays potholes on map & alerts users

The system can differentiate potholes from cracks and minor irregularities using ML models.

-> Results:
Accurate detection of potholes, cracks, and uneven surfaces
Real-time monitoring and reporting
Improved road safety through early detection
Reduced manual inspection efforts

The system continuously scans roads and sends live updates with GPS coordinates.

-> Limitations:
Sensor accuracy affected by weather conditions
Requires stable internet for real-time updates
Initial setup cost is high
Hardware requires maintenance
-> Future Enhancements:
Integration with autonomous vehicles
Cloud-based real-time monitoring
AI-based predictive maintenance
Drone-based road inspection
Voice alerts for drivers

-> Python Setup:
pip install opencv-python tensorflow numpy matplotlib
-> Run Detection:
python detect.py
