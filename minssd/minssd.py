import cv2
import numpy as np

def image_slide(img1, img2):
    
    height, width = img1.shape
    
    ###候補
    #回転角
    angle = [-1, 0, 1]
    # x
    x_slide = [-1, 0, 1]
    # y
    y_slide = [-1, 0, 1]
    
    #回転の中心
    center = (int(width/2), int(height/2))
    #スケールを指定
    scale = 1.0
    
    #アフィン行列27パターン
    trans = []
    # angle
    for a in angle:
        for x in x_slide:
            for y in y_slide:
                rotate = cv2.getRotationMatrix2D(center, a, scale)
                rotate_slide = rotate + np.array([[0,0,x],[0,0,y]])
                trans.append(rotate_slide)
    
    #
    edge = 200 #端ピクセルはSSD計算時に除く
    bestimg2 = img2.copy()
    minssd = 1001001001
    
    #ssdが最小になるまでループ
    while(True):
        bestM = None

        for M in trans:
            img2_trans = cv2.warpAffine(bestimg2, M, (width,height))
            ssd = cv2.matchTemplate(img1[edge:-edge], img2_trans[edge:-edge], cv2.TM_SQDIFF)[0,0]
            if minssd > ssd:
                minssd = ssd
                bestM = M

        if bestM is None:
            break
        else:
            bestimg2 = cv2.warpAffine(bestimg2, bestM, (width,height))
            #print(bestM)

    return bestimg2