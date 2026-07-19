import numpy as np

class AngleMath:
    def fingerAngle(self, landmark_a, landmark_b, landmark_c):
        # Create the points with the coords of 3 given landmarks
        point_a = np.array([landmark_a.x, landmark_a.y])
        point_b = np.array([landmark_b.x, landmark_b.y])
        point_c = np.array([landmark_c.x, landmark_c.y])
