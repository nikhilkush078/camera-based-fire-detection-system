import cv2
import numpy as np
import pygame

# Initialize pygame mixer for sound
pygame.mixer.init()
pygame.mixer.music.load("ooo.mp3")  # Load the MP3 file

# Replace with your DroidCam IP
DROIDCAM_URL = "http://192.168.1.8:4747/video"

cap = cv2.VideoCapture(DROIDCAM_URL)

def detect_fire(frame):
    """Detects fire using color filtering and contour detection."""
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # Fire-like color range in HSV
    lower_fire = np.array([10, 100, 100], dtype="uint8")
    upper_fire = np.array([30, 255, 255], dtype="uint8")

    # Create a mask for fire-like colors
    mask = cv2.inRange(hsv, lower_fire, upper_fire)

    # Find contours in the mask
    contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    fire_detected = False

    for contour in contours:
        area = cv2.contourArea(contour)
        
        # Filter based on area size
        if area > 1000:
            fire_detected = True
            x, y, w, h = cv2.boundingRect(contour)
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 0, 255), 2)
            cv2.putText(frame, "🔥 FIRE DETECTED! 🔥", (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)

    return fire_detected, frame

while True:
    ret, frame = cap.read()
    if not ret:
        print("❌ Failed to connect to DroidCam. Check the URL & Wi-Fi connection.")
        break

    fire_detected, frame = detect_fire(frame)

    # Play alarm sound only if fire is detected and it's not already playing
    if fire_detected and not pygame.mixer.music.get_busy():
        pygame.mixer.music.play()

    cv2.imshow("Fire Detection - DroidCam", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
pygame.mixer.quit()  # Stop pygame mixer when the script ends
