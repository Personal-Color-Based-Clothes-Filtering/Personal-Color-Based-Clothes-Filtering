# -*- coding: utf-8 -*-
from math import sqrt
import cv2
import colorsys
from color_extraction import MainColorExtraction

class ToneExtraction:
    IMAGE = None
    PCCS = ''
    SEASON = ''
    COLOR_NAME = ''

    # PCCS tone dataset [v(명도), s(채도), PCCS tone]
    PCCS_TONE_DATASET = [
        [93.75, 22.22222222, 'p'], [93.75, 55.55555555, 'lt'], [87.5, 88.88888888, 'b'],
        [68.75, 22.22222222, 'ltg'], [68.75, 55.55555555, 'sf'], [50, 88.88888888, 's'], [50, 100, 'v'],
        [37.5, 22.22222222, 'g'], [37.5, 55.55555555, 'd'], [18.75, 88.88888888, 'dp'],
        [12.5, 22.22222222, 'dkg'], [12.5, 55.55555555, 'd']
    ]

    # season
    SPRING = ['p', 'lt', 'b', 'v']
    SUMMER = ['p', 'lt', 'b', 'ltg', 'sf', 'g', 'd']
    FALL = ['ltg', 'sf', 's', 'g', 'd', 'dp', 'dkg', 'dk']
    WINTER = ['s', 'v', 'dp', 'dkg', 'dk']


    def __init__(self,image):
        self.IMAGE = image
    
    def convert_rgb_to_hsv(self,main_color):
        hsv = colorsys.rgb_to_hsv(main_color[0][0] / 255, main_color[0][1] / 255, main_color[0][2] / 255)
        #h는 0~360,s와 v는 0~100로 정규화
        hue = round(hsv[0] * 360) 
        saturation = round(hsv[1] * 100)  
        value = round(hsv[2] * 100) 

        return hue, saturation, value

    def get_closet_personal_color(self,hue,saturation,value):
        main_color_saturation_and_value = [value, saturation]
        main_color_tone = self.get_neighbors(self.PCCS_TONE_DATASET, main_color_saturation_and_value)
        pccs = main_color_tone[0][2]
        season = self.get_season_tone(hue, value, saturation, main_color_tone[0][2])

        return pccs, season
    
    def get_season_tone(self,h, v, s, tone):
        result = ''
        if h < 180:
            if tone in self.SPRING:
                result = 'spring'
            else:
                result = 'fall'
        elif h > 180:
            if tone in self.SUMMER:
                result = 'summer'
            else:
                result = 'winter'
        return result

    def get_color_name(self,h,s,v):
        color_name = ''
        if s <= 5:
            if v < 5:
                color_name = 'black'
            elif v > 95:
                color_name = 'white'
            else: 
                color_name = 'gray'
        elif s > 5:
            if h >= 343 or h <= 10:
                if s > 5 and s <= 20 and v >= 50 and v <= 80:
                    color_name = 'pink'
                elif s >= 20 and s <= 100 and v >= 12 and v <= 50:
                    color_name = 'brown'
                else:
                    color_name = 'red'
            elif h >= 11 and h <= 37:
                if s > 5 and s <= 20 and v >= 50 and v <= 80:
                    color_name = 'beige'
                elif s >= 20 and s <= 100 and v >= 12 and v <= 50:
                    color_name = 'brown'
                else:
                    color_name = 'orange'
            elif h >= 38 and h <= 64:
                color_name = 'yellow'
            elif h >= 65 and h <= 170:
                color_name = 'green'
            elif h >= 171 and h <= 254:
                color_name = 'blue'
            elif h >= 255 and h <= 295:
                color_name = 'purple'
            elif h >= 296 and h <= 342:
                color_name = 'pink'
            
        return color_name
            

    # Euclidean distance
    # row = [v, s, tone]
    def euclidean_distance(self, row1, row2):
        distance = 0.0
        for i in range(len(row1)):
            distance += (row1[i] - row2[i]) ** 2
        return sqrt(distance)


    # 가장 가까운 점 찾기(num_neighbors개)
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
        img = self.IMAGE

        main_color_instance = MainColorExtraction(img)
        main_color = main_color_instance.extract_main_color()
        hue,saturation,value = self.convert_rgb_to_hsv(main_color)
        pccs,season = self.get_closet_personal_color(hue,saturation,value)
        color_name = self.get_color_name(hue,saturation,value)

        self.PCCS = pccs
        self.SEASON = season
        self.COLOR_NAME = color_name
        
        print('hue:',hue,'\ns(채도):',saturation,'\nv(명도):', value, '\n색상명:', self.COLOR_NAME, '\n세부pccs톤:',self.PCCS, '\n계절 퍼스널컬러:',self.SEASON)

        return self.SEASON,self.COLOR_NAME


img = 'https://image.msscdn.net/images/goods_img/20200928/1628385/1628385_4_500.jpg'
tone_extraction_instance = ToneExtraction(img)
tone,color = tone_extraction_instance.extract_tone()

print(tone,color)
