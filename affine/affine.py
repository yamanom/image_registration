import random

import cv2
import numpy as np

def getAffineTransformRANSAC(kp_after, kp_before, thresh=3.0, max_iters=2000):
    
    n = kp_after.shape[0]
    m = int(n * 0.8)
        
    inliers = []
    matrixs = []
    for i in range(max_iters):
        idx = random.sample(range(n), m)
        A = np.append(kp_after[idx].reshape(-1 ,2), np.ones([m,1]), axis=-1).T
        B = np.append(kp_before[idx].reshape(-1 ,2), np.ones([m,1]), axis=-1).T
        matrix = A @ B.T @ np.linalg.inv(B @ B.T) # F

        v = np.append(kp_before.reshape(-1 ,2), np.ones([n,1]), axis=-1).T
        dv = np.append(kp_after.reshape(-1 ,2), np.ones([n,1]), axis=-1).T
        fv = matrix @ v

        nijou = (dv-fv)[:2,:]**2
        nijouwa = nijou[0,:] + nijou[1,:]

        inliers.append(np.sum(nijouwa < thresh**2))
        matrixs.append(matrix)

    return matrixs[inliers.index(max(inliers))][:2,:]