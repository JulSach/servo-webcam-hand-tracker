import cv2 as cv
from camera import Camera
from hand_tracker import HandTracker

cam = Camera()
tracker = HandTracker()

time_ms = 0

landmarks = []

while True:
    success, frame = cam.readFrame()

    # If readFrame() fails, break out of loop
    if not success:
        break

    # Convert frame from BGR to RGB to pass into MediaPipe
    corrected_frame = cam.convertFrame(frame)

    # Convert frame to become a MediaPipe Image object
    img = tracker.inputFrame(corrected_frame)

    # Detect hand landmarks on Image object
    tracker.landmarkDetection(img, time_ms)

    # Store list of landmarks
    landmarks = tracker.getLandmarks()
    
    # Display the hand tracked frame
    cam.showFrame(frame)

    # 30 FPS - Timestamp to handle timing
    time_ms += 33 

    # If 'q' pressed, break out of loop
    if cv.waitKey(1) & 0xFF == ord('q'):
        break
        
# Close camera after pressing 'q'
cam.closeCamera()
tracker.closeDetector()
