import cv2 as cv
from camera import Camera

cam = Camera()

while True:
    success, frame = cam.readFrame()

    # If readFrame() fails, break out of loop
    if not success:
        break

    # Correct frame from BGR to RGB
    corrected_frame = cam.convertFrame(frame)

    # Display corrected frame
    cam.showFrame(corrected_frame)

    # If 'q' pressed, break out of loop
    if cv.waitKey(1) & 0xFF == ord('q'):
        break

# Close camera after pressing 'q'
cam.closeCamera()
