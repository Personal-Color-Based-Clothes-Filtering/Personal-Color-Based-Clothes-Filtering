import cv2
import matplotlib.pyplot as plt
import numpy as np
import requests
from sklearn.cluster import KMeans
from collections import Counter
import colorsys

class MainColorExtraction:
    URL = None
    COLOR = None
    CLUSTERS = 3

    def __init__(self,image_url):
        self.URL = image_url

    def get_main_color(self):
        image_type = self.URL[-3:]
        img = self.read_rgb_image(image_type)
        img = cv2.resize(img,dsize=(500,500),interpolation=cv2.INTER_AREA)

        grabcut_img = self.grabcut(img)
        cluster = self.clustering_image_color(grabcut_img)
        self.COLOR = self.extract_main_color(cluster)

        # palette = self.rgb_palette(self.COLOR)
        # self.show_img_compar(grabcut_img,palette)
        
        return self.COLOR

    def read_rgb_image(self,image_type):
        if image_type == 'gif':
            img = self.get_gif_image()
        else:
            img = self.get_normal_image()
        img = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)

        return img

    def get_gif_image(self):
        gif = cv2.VideoCapture(self.URL)
        ret,frame = gif.read()
        if ret:
            return frame

    def get_normal_image(self):
        image_nparray = np.asarray(bytearray(requests.get(self.URL).content), dtype=np.uint8)
        image = cv2.imdecode(image_nparray, cv2.IMREAD_COLOR)

        return image
        
    def grabcut(self,image):
        init_mask = np.zeros(image.shape[:2],np.uint8)
        background_model = np.zeros((1,65),np.float64)
        foreground_model = np.zeros((1,65),np.float64)
        rect = (100,100,300,400)

        cv2.grabCut(image,init_mask,rect,background_model,foreground_model,5,cv2.GC_INIT_WITH_RECT)
        closet_mask = np.where((init_mask==2)|(init_mask==0),0,1).astype('uint8')
        image = image * closet_mask[:,:,np.newaxis]

        return image

    def remove_grabcut_bg(self,image):
        tmp = cv2.cvtColor(image,cv2.COLOR_RGB2GRAY)
        _,alpha = cv2.threshold(tmp,0,250,cv2.THRESH_BINARY)
        r, g, b = cv2.split(image)
        rgba = [b,g,r,alpha]
        dst = cv2.merge(rgba,4)
        return dst

    def mean_shift_color(self,image):
        mean = cv2.pyrMeanShiftFiltering(image, 30, 30, None, 5)
        return mean

    def clustering_image_color(self,image):
        clt = KMeans(n_clusters=3)
        clt.fit(image.reshape(-1,3))
        clt.labels_

        clt.cluster_centers_
        clt_1 = clt.fit(image.reshape(-1,3))

        return clt_1

    def extract_main_color(self,k_cluster):
        n_pixels = len(k_cluster.labels_)
        counter = Counter(k_cluster.labels_)

        perc = {} 
        for i in counter:
            perc[i] = np.round(counter[i]/n_pixels, 2)

        clustering_color_list = [{},{},{}] 

        for i in range(3):
            clustering_color_list[i]['perc'] = perc[i]
            clustering_color_list[i]['r'] = int(k_cluster.cluster_centers_[i][0])
            clustering_color_list[i]['g'] = int(k_cluster.cluster_centers_[i][1])
            clustering_color_list[i]['b'] = int(k_cluster.cluster_centers_[i][2])

        sorted(clustering_color_list,key=lambda color:color['perc']) 

        if clustering_color_list[0]['r'] < 2 and clustering_color_list[0]['g'] < 2 and clustering_color_list[0]['b'] < 2:
            del clustering_color_list[0] 

        main_color = [[clustering_color_list[0]['r'],clustering_color_list[0]['g'],clustering_color_list[0]['b']]]
        return main_color
    
    def rgb_palette(self,color):
        rgb = [
            color[0],
            color[0],
            color[0]
        ]
        color = np.array([rgb])

        return color
    
    def show_img_compar(self, img_1, img_2):
        f, ax = plt.subplots(1, 2, figsize=(10,10))
        ax[0].imshow(img_1)
        ax[1].imshow(img_2)
        ax[0].axis('off') #hide the axis
        ax[1].axis('off')
        f.tight_layout()
        plt.show()
        