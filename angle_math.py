import numpy as np

class AngleMath:
    def fingerAngle(self, landmark_a, landmark_b, landmark_c):
        # Create the points with the coords of 3 given landmarks
        point_a = np.array([landmark_a.x, landmark_a.y])
        point_b = np.array([landmark_b.x, landmark_b.y])
        point_c = np.array([landmark_c.x, landmark_c.y])

        # Create two 2-D vectors, BA and BC
        vector_ba = point_a - point_b
        vector_bc = point_c - point_b

        # Calculate the dot product
        dot_product = (vector_ba[0] * vector_bc[0]) + (vector_ba[1] * vector_bc[1])

        # Calculate magnitude of vectors
        magnitude_ba = np.linalg.norm(vector_ba)
        magnitude_bc = np.linalg.norm(vector_bc)
