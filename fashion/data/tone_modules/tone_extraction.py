# -*- coding: utf-8 -*-
from math import sqrt
import cv2
from color_extraction import MainColorExtraction
import colorsys

class ToneExtraction(MainColorExtraction):
    PCCS = ''
    SEASON = ''

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


    def __init__(self,image_url):
        self.URL = image_url
    
    def convert_rgb_to_hsv(self,color):
        hsv = colorsys.rgb_to_hsv(color[0][0] / 255, color[0][1] / 255, color[0][2] / 255)
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
        self.PCCS,self.SEASON = self.get_closet_personal_color(hue,saturation,value)
        return self.SEASON

