# -*- coding: utf-8 -*-
from math import sqrt
import cv2
from color_extraction import MainColorExtraction
import colorsys

class ToneExtraction(MainColorExtraction):
    PCCS = ''
    SEASON = ''

    PCCS_TONE_DATASET = [
        [93.75, 15, 'p'], [93.75, 45, 'lt'], [87.5, 75, 'b'],
        [68.5, 15, 'ltg'], [68.5, 45, 'sf'], [50, 75, 's'], [50, 95, 'v'],
        [37.5, 15, 'g'], [37.5, 45, 'd'], [18.75, 75, 'dp'],
        [12.5, 15, 'dkg'], [12.5, 45, 'd']
    ]
    
    SPRING = ['p', 'lt', 'b', 'v']
    SUMMER = ['p', 'lt', 'b', 'ltg', 'sf', 'g']
    FALL = ['ltg', 'sf', 's', 'g', 'd', 'dp', 'dkg', 'dk']
    WINTER = ['s', 'v', 'dp', 'd', 'dkg', 'dk']


    def __init__(self,image_url):
        self.URL = image_url
    
    def convert_rgb_to_hsv(self,color):
        hsv = colorsys.rgb_to_hsv(color[0][0] / 255, color[0][1] / 255, color[0][2] / 255)
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

        XYZ[0] = float(XYZ[0]) / 95.047        
        XYZ[1] = float(XYZ[1]) / 100.0          
        XYZ[2] = float(XYZ[2]) / 108.883     

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

        return Lab

    def get_closet_personal_color(self,hue,saturation,value,b):
        main_color_saturation_and_value = [value, saturation]
        main_color_tone = self.get_neighbors(self.PCCS_TONE_DATASET, main_color_saturation_and_value)
        pccs = main_color_tone[0][2]
        season = self.get_season_tone(hue,b,pccs)

        return pccs, season
    
    def get_season_tone(self,hue,b,tone):
        result = ''
        if b > 0 or hue < 180:
            if tone in self.SPRING:
                result = 'spring'
            else:
                result = 'autumn'
        elif b <= 0 or hue > 180:
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
        return self.SEASON