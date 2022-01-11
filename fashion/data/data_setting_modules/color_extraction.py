import cv2
import matplotlib.pyplot as plt
import numpy as np
from sklearn.cluster import KMeans
from collections import Counter

class MainColorExtraction:
    IMAGE = None
    COLOR = None
    COLOR_NAME = ''
    CLUSTERS = 3

    def __init__(self,image):
        self.IMAGE = image
    
    #1)mean_shift filtering 기법을 이용해 색상을 단순화
    def mean_shift_color(self,image):
        mean = cv2.pyrMeanShiftFiltering(image, 30, 30, None, 5)
        return mean
    
    #2)grabcut 알고리즘을 이용한 전경 제거 메소드
    def grabcut(self,image):
        init_mask = np.zeros(image.shape[:2],np.uint8) #초기 마스크
        background_model = np.zeros((1,65),np.float64) #grabcut에 사용할 임시 배열
        foreground_model = np.zeros((1,65),np.float64)
        rect = (100,100,300,400)
        cv2.grabCut(image,init_mask,rect,background_model,foreground_model,5,cv2.GC_INIT_WITH_RECT)
        closet_mask = np.where((init_mask==2)|(init_mask==0),0,1).astype('uint8') #배경인 곳은 0, 그 외에는 1로 설정한 마스크
        image = image * closet_mask[:,:,np.newaxis]

        return image

    #3)색상 클러스터링 
    def clustering_image_color(self,image):
        clt = KMeans(n_clusters=3)
        clt.fit(image.reshape(-1,3))
        clt.labels_

        clt.cluster_centers_
        clt_1 = clt.fit(image.reshape(-1,3))

        return clt_1


    #4)메인 컬러 추출
    def get_main_color(self,k_cluster):
        n_pixels = len(k_cluster.labels_)
        counter = Counter(k_cluster.labels_)

        #perc는 이미지 내의 색상 비율을 담는 객체
        perc = {} 
        for i in counter:
            perc[i] = np.round(counter[i]/n_pixels, 2)

        #클러스터링 된 색상 정보를 담을 객체
        clustering_color_list = [{},{},{}] 

        for i in range(3):
            clustering_color_list[i]['perc'] = perc[i]
            clustering_color_list[i]['r'] = int(k_cluster.cluster_centers_[i][0])
            clustering_color_list[i]['g'] = int(k_cluster.cluster_centers_[i][1])
            clustering_color_list[i]['b'] = int(k_cluster.cluster_centers_[i][2])

        #비율 순서대로 객체 정렬
        sorted(clustering_color_list,key=lambda color:color['perc']) 
        #가장 비율이 높은 색의 r,g,b의 값이 모두 2보다 작으면 배경색인 검정으로 간주하고 제거
        if clustering_color_list[0]['r'] < 2 and clustering_color_list[0]['g'] < 2 and clustering_color_list[0]['b'] < 2:
            del clustering_color_list[0] 

        main_color = [[clustering_color_list[0]['r'],clustering_color_list[0]['g'],clustering_color_list[0]['b']]]
        return main_color
    
    # 5,6은 개발 과정에서 진행 확인 용도
    #5)대표 색상 확인을 위한 팔레트
    def rgb_palette(self,color):
        rgb = [
            color[0],
            color[0],
            color[0]
        ]
        color = np.array([rgb])

        return color
    
    #6)이미지 확인 창
    def show_img_compar(self, img_1, img_2):
        f, ax = plt.subplots(1, 2, figsize=(10,10))
        ax[0].imshow(img_1)
        ax[1].imshow(img_2)
        ax[0].axis('off') #hide the axis
        ax[1].axis('off')
        f.tight_layout()
        plt.show()

    #main)메인색 추출 메소드
    def extract_main_color(self):
        img = cv2.imread(self.IMAGE)
        img = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)

        mean = self.mean_shift_color(img)
        grabcut = self.grabcut(mean)
        cluster = self.clustering_image_color(grabcut)
        main_color = self.get_main_color(cluster)
        
        self.COLOR = main_color
        print('rgb:',self.COLOR)

        # palette = self.rgb_palette(main_color)
        # self.show_img_compar(img,palette)
        
        return self.COLOR