import pandas as pd
import numpy as np
from pandas import DataFrame
from sklearn.cluster import KMeans
import math
import pickle
import json
from scipy.cluster.vq import kmeans,vq

class Engine :
    threshold = 20
    def __init__(self, restID):
        self.restID = restID

    def set_Dataset_Filename(self, file):
        self.dataset_filename = file

    def get_best_location(self, cent, clus):
        MAX = 0
        IDX = 0
        for i in range(len(clus)):
            if clus[i] > MAX:
                IDX = i
                MAX = clus[i]
        return cent[IDX]
        
    def get_restaurant_data(self, data, ID):
        n = len(data)
        #print(n)
        Data = []
        for  i in range (n) :
            if data['rest_id'][i] == ID and data['distance'][i] > self.threshold :
                Data.append([data['user_long'][i],data['user_lat'][i]])
        return Data
    
    def run (self):
        columns = ['rest_id','distance','user_long','user_lat']
        Data = pd.read_csv("reservations.csv")
        features = Data[columns]
        df = self.get_restaurant_data(features, self.restID)
        #print(df[0][0] , ",", df[0][1])
        '''
        kmeans = KMeans(n_clusters=4).fit(df)
        centroids = kmeans.cluster_centers_
        x = kmeans.
        print(centroids)
        '''
        centroids,_ = kmeans(df,4)
        # assign each sample to a cluster
        idx,_ = vq(df,centroids)
        #Print number of elements per cluster
        print (np.bincount(idx))
        print(centroids)
        return self.get_best_location(centroids, np.bincount(idx))

        











        
        
