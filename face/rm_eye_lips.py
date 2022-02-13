from collections import OrderedDict
import numpy as np
import cv2
import argparse
import dlib
import imutils

facial_features_cordinates = {}

# # 얼굴의 랜드마크 인덱스를 얼굴 부위에 매치시키는 딕셔너리 정의
FACIAL_LANDMARKS_INDEXES = OrderedDict([
    ("Mouth", (48, 68)),
    ("Right_Eyebrow", (17, 22)),
    ("Left_Eyebrow", (22, 27)),
    ("Right_Eye", (36, 42)),
    ("Left_Eye", (42, 48)),
    ("Nose", (30, 36))
])
                                                                                                                                                                                                

def shape_to_numpy_array(shape, dtype="int"):
    
    # (x, y)좌표 리스트 초기화
    coordinates = np.zeros((68, 2), dtype=dtype)

    # 68 facial landmarks 돌면서 2-튜플의 (x, y) 좌표로 변환
    for i in range(0, 68):
        coordinates[i] = (shape.part(i).x, shape.part(i).y)

    # (x, y)좌표 리스트 반환
    return coordinates


def visualize_facial_landmarks(image, shape, colors=None, alpha=0.75):

    # 원본 이미지의 복사본 2개 만들기. 하나는 overlay, 하나는 최종 결과본 이미지를 위함.
    overlay = image.copy()
    output = image.copy()

    # 검정색으로 각 얼굴 영역을 채움.
    if colors is None:
        colors = [(0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0)]

    # 얼굴 랜드마크 영역을 각각 돌면서,
    for (i, name) in enumerate(FACIAL_LANDMARKS_INDEXES.keys()):
        # 얼굴 랜드마크에 대한 (x, y)좌표를 구한다
        (j, k) = FACIAL_LANDMARKS_INDEXES[name]
        pts = shape[j:k]
        facial_features_cordinates[name] = pts

        # 얼굴 랜드마크 좌표 점들의 convex hull을 계산하고 표시한다.
        hull = cv2.convexHull(pts)
        cv2.drawContours(overlay, [hull], -1, colors[i], -1)

    # transparent overlay 적용
    cv2.addWeighted(overlay, alpha, output, 1 - alpha, 0, output)

    # 결과 이미지 반환
    return output


def RmEyeLips():
    
    # dlib의 face detector울 초기화한다
    # facial landmark predictor 생성
    detector = dlib.get_frontal_face_detector()
    predictor = dlib.shape_predictor('shape_predictor_68_face_landmarks.dat')

   # 원본 이미지 로드, 사이즈 조정, grayscale 이미지로 변환
    image = cv2.imread('./face/personal_color_check/image/skincolor_face.jpg')

    image = imutils.resize(image, width=500)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # grayscale이미지에서 얼굴 찾기
    rects = detector(gray, 1)

    #찾은 얼굴들에 대해서,
    for (i, rect) in enumerate(rects):

        # 얼굴 영역을 위한 랜드마크 구하고, 랜드마크 (x, y)좌표를 NumPy배열로 변환
        shape = predictor(gray, rect)
        shape = shape_to_numpy_array(shape)

        output = visualize_facial_landmarks(image, shape)

        cv2.imwrite("./face/personal_color_check/image/removed_eyes.jpg", output)
        print("3")
    
