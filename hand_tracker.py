import mediapipe as mp
from mediapipe.tasks import python
from mediapipe.tasks.python import vision

class HandTracker:
    def __init__(self):
        # Initialize shortcuts for later use
        self.BaseOptions = mp.tasks.BaseOptions
        self.HandLandmarker = mp.tasks.vision.HandLandmarker
        self.HandLandmarkerOptions = mp.tasks.vision.HandLandmarkerOptions
        self.HandLandmarkerResult = mp.tasks.vision.HandLandmarkerResult
        self.VisionRunningMode = mp.tasks.vision.RunningMode

        # Initialize HandLandmarker detector options, BaseOptions sets path for where model is
        self.options = self.HandLandmarkerOptions(base_options = self.BaseOptions(model_asset_path = 'hand_landmarker.task'), running_mode = self.VisionRunningMode.LIVE_STREAM, result_callback = self.result_callback)

        # Initialize HandLandmarker detector with previous options
        self.landmarker = self.HandLandmarker.create_from_options(self.options)

    def result_callback(self, result, output_image, timestamtp_ms):
        # Print X Y and Z coords of each landmark
        print('Hand Landmarker Result: {}'.format(result))

    def inputFrame(self, frame):
        # Frame from OpenCv converted to MediaPipe Image object
        img = mp.Image(mp.ImageFormat.SRGB, frame)
        return img

    def landmarkDetection(self, image, time):
        self.landmarker.detect_async(image, time)
    
    def closeDetector(self):
        self.landmarker.close()
