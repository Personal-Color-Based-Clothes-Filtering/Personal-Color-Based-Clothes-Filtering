# -*- coding: utf-8 -*-
from math import sqrt
import cv2
from color_extraction import MainColorExtraction
import colorsys

class ToneExtraction(MainColorExtraction):
    PCCS = ''
    SEASON = ''

    # PCCS tone dataset [v(명도), s(채도), PCCS tone]
    # PCCS_TONE_DATASET = [
    #     [93.75, 22.22222222, 'p'], [93.75, 55.55555555, 'lt'], [87.5, 88.88888888, 'b'],
    #     [68.75, 22.22222222, 'ltg'], [68.75, 55.55555555, 'sf'], [50, 88.88888888, 's'], [50, 100, 'v'],
    #     [37.5, 22.22222222, 'g'], [37.5, 55.55555555, 'd'], [18.75, 88.88888888, 'dp'],
    #     [12.5, 22.22222222, 'dkg'], [12.5, 55.55555555, 'd']
    # ]
    
    #톤 범위:명도(0~25/25~50/50~75/75~100,25/50/75)->범위의 중간값으로 설정. 채도(0~30/30~60/60~90/90~100)->중간값으로 설정
    PCCS_TONE_DATASET = [
        [93.75, 15, 'p'], [93.75, 45, 'lt'], [87.5, 75, 'b'],
        [68.5, 15, 'ltg'], [68.5, 45, 'sf'], [50, 75, 's'], [50, 95, 'v'],
        [37.5, 15, 'g'], [37.5, 45, 'd'], [18.75, 75, 'dp'],
        [12.5, 15, 'dkg'], [12.5, 45, 'd']
    ]
    # season
    SPRING = ['p', 'lt', 'b', 'v']
    SUMMER = ['p', 'lt', 'b', 'ltg', 'sf', 'g']
    FALL = ['ltg', 'sf', 's', 'g', 'd', 'dp', 'dkg', 'dk']
    WINTER = ['s', 'v', 'dp', 'd', 'dkg', 'dk']


    def __init__(self,image_url):
        self.URL = image_url
    
    def convert_rgb_to_hsv(self,color):
        hsv = colorsys.rgb_to_hsv(color[0][0] / 255, color[0][1] / 255, color[0][2] / 255)
        #h는 0~360,s와 v는 0~100로 정규화
        hue = round(hsv[0] * 360) 
        saturation = round(hsv[1] * 100)  
        value = round(hsv[2] * 100) 

        return hue, saturation, value

    def convert_rgb_to_lab(self,color):
        num = 0
        RGB = [0, 0, 0]
        
        for value in color[0] :
            value = float(value) / 255
            if value > 0.04045 :
                value = ( ( value + 0.055 ) / 1.055 ) ** 2.4
            else :
                value = value / 12.92
            RGB[num] = value * 100
            num = num + 1

        XYZ = [0,0,0,]

        X = RGB[0] * 0.4124 + RGB[1] * 0.3576 + RGB[2] * 0.1805
        Y = RGB[0] * 0.2126 + RGB[1] * 0.7152 + RGB[2] * 0.0722
        Z = RGB[0] * 0.0193 + RGB[1] * 0.1192 + RGB[2] * 0.9505
        XYZ[0] = round(X,4)
        XYZ[1] = round(Y,4)
        XYZ[2] = round(Z,4)

        XYZ[0] = float(XYZ[0]) / 95.047         # ref_X =  95.047   Observer= 2°, Illuminant= D65
        XYZ[1] = float(XYZ[1]) / 100.0          # ref_Y = 100.000
        XYZ[2] = float(XYZ[2]) / 108.883        # ref_Z = 108.883

        num = 0
        for value in XYZ :
            if value > 0.008856 :
                value = value ** (0.3333333333333333)
            else :
                value = (7.787 * value) + (16 / 116)

            XYZ[num] = value
            num = num + 1

        Lab = [0, 0, 0]

        L = (116 * XYZ[1]) - 16
        a = 500 * (XYZ[0] - XYZ[1])
        b = 200 * (XYZ[1] - XYZ[2])

        Lab[0] = round(L,4)
        Lab[1] = round(a,4)
        Lab[2] = round(b,4)

        print(Lab)
        return Lab

    def get_closet_personal_color(self,hue,saturation,value,b):
        main_color_saturation_and_value = [value, saturation]
        main_color_tone = self.get_neighbors(self.PCCS_TONE_DATASET, main_color_saturation_and_value)
        pccs = main_color_tone[0][2]
        season = self.get_season_tone(hue,b,pccs)

        return pccs, season
    
    def get_season_tone(self,hue,b,tone):
        result = ''
        if b > 0:
            if tone in self.SPRING:
                result = 'spring'
            else:
                result = 'autumn'
        elif b <= 0:
            if tone in self.SUMMER:
                result = 'summer'
            else:
                result = 'winter'
        return result                

    def euclidean_distance(self, row1, row2):
        distance = 0.0
        for i in range(len(row1)):
            distance += (row1[i] - row2[i]) ** 2
        return sqrt(distance)

    def get_neighbors(self, tone_dataset, main_color_saturation_and_value, num_neighbors=1):
        distances = list()
        for tone_row in tone_dataset:
            distance = self.euclidean_distance(main_color_saturation_and_value, tone_row)
            distances.append((tone_row, distance))
        distances.sort(key=lambda x: x[1])

        neighbors = list()
        for i in range(num_neighbors):
            neighbors.append(distances[i][0])

        return neighbors
    
    def extract_tone(self):
        self.get_main_color()
        hue,saturation,value = self.convert_rgb_to_hsv(self.COLOR)
        b = self.convert_rgb_to_lab(self.COLOR)[2]
        self.PCCS,self.SEASON = self.get_closet_personal_color(hue,saturation,value,b)
        print(self.PCCS,self.SEASON)
        return self.SEASON


# sm_mint = 'https://image.msscdn.net/images/goods_img/20220221/2375190/2375190_1_500.jpg'
# sm_mint2 = 'https://image.msscdn.net/images/goods_img/20220222/2376456/2376456_1_500.jpg'
# sp_green = 'https://image.msscdn.net/images/goods_img/20180403/748059/748059_7_500.jpg'
# sp_green2 = 'https://image.msscdn.net/images/goods_img/20220216/2362923/2362923_1_500.jpg'
# warm_pk = 'https://image.msscdn.net/images/goods_img/20220212/2356432/2356432_1_500.jpg'
# warm_pk2 = 'https://image.msscdn.net/images/goods_img/20190401/1000708/1000708_1_500.jpg'
# cool_pk = 'https://image.msscdn.net/images/goods_img/20210310/1836752/1836752_1_500.jpg'
# cool_pk2 = 'https://image.msscdn.net/images/goods_img/20220214/2357035/2357035_1_500.jpg'
# wm = 'https://image.msscdn.net/data/curating/23658/23658_1_org.jpg'

# sm1 = ToneExtraction(sm_mint)
# sm2 = ToneExtraction(sm_mint2)
# sp1 = ToneExtraction(sp_green)
# sp2 = ToneExtraction(sp_green2)
# wp1 = ToneExtraction(warm_pk)
# wp2 = ToneExtraction(warm_pk2)
# cp1 = ToneExtraction(cool_pk)
# cp2 = ToneExtraction(cool_pk2)

# sm1_tone = sm1.extract_tone()
# sm2_tone = sm2.extract_tone()
# sp1_tone = sp1.extract_tone()
# sp2_tone = sp2.extract_tone()
# wp1_tone = wp1.extract_tone()
# wp2_tone = wp2.extract_tone()
# cp1_tone = cp1.extract_tone()
# cp2_tone = cp2.extract_tone()


# print(yellow_tone,blue_tone)