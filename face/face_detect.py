import cv2
import numpy as np

def FaceDetect():
    
    # 이미지 파일 읽기
    img = cv2.imread("./face/personal_color_check/image/cropped.jpg", cv2.IMREAD_COLOR)

    img_hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    # 잡음 제거
    img_hsv = cv2.fastNlMeansDenoisingColored(img_hsv,None,10,10,7,21)

    lower = np.array([0,48,80], dtype="uint8") #부호없는 8비트 정수형
    upper = np.array([20,255,255], dtype="uint8")
    img_person = cv2.inRange(img_hsv, lower, upper) #살색 범위를 출력

    #경계선 찾음
    _, contours, hierarchy = cv2.findContours(img_person, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)

    # 가장 큰 영역 찾기
    max = 0
    maxcnt = None
    for cnt in contours :
        area = cv2.contourArea(cnt)
        if(max < area) :
            max = area
            maxcnt = cnt
 
    #maxcontours의 각 꼭지점 다각선 만들기 
    hull = cv2.convexHull(maxcnt)

    # 같은 크기의 배경 검정색인 이미지 만들기
    mask = np.zeros(img.shape).astype(img.dtype)
    color = [255, 255, 255]
    # 경계선 내부 흰색으로 채우기
    cv2.fillPoly(mask, [maxcnt], color)

    img_person = cv2.bitwise_and(img, mask)
    

    # 이미지 보여주기
    cv2.imwrite("./face/personal_color_check/image/skincolor_face.jpg", img_person)

FaceDetect()