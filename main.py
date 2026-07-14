import cv2 as cv
from camera import Camera
from hand_tracker import HandTracker

def convertToPixelCoords(x, y):
    pixel_x = x * 640 # X multiplied by 640 pixel width
    pixel_y = y * 480 # Y multiplied by 480 pixel height
    return pixel_x, pixel_y

def drawLandmarks(pixel_x, pixel_y, frame):
    drawn_frame = cv.circle(frame, (pixel_x, pixel_y), 15, (0,0,255), thickness = 2) # Use OpenCV circle method to draw circle onto frame
    return drawn_frame

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
