import cv2 as cv

class Camera:
    def __init__(self):
        # Open default webcam
        self.cap = cv.VideoCapture(0)

    def readFrame(self):
        # Read and return the static frame
        success, frame = self.cap.read()
        return success, frame

    def convertFrame(self, frame):
        # Convert and return frame from BGR to RGB
        return cv.cvtColor(frame, cv.COLOR_BGR2RGB)
    
    def showFrame(self, frame):
        # Display frame
        cv.imshow('Camera', frame)

    def closeCamera(self):
        self.cap.release()
        cv.destroyAllWindows()
