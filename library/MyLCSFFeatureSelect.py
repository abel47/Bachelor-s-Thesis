# -*- coding: utf-8 -*-
"""
Created on Mon May 20 17:47:09 2019

@author: Abel
"""
#from sklearn.base import TransformerMixin
from library.MyBinaryRelevanceFeatureSelect import MyBinaryRelevanceFeatureSelect

import random
import operator
import numpy as np

class lcsf_feature_selection():
#    def __init__():
#        if q is None: #have to fix things in here
#            q = 2
        #self.q = q
        #self.selecting_strategy = selecting_strategy
        #self.combining_strategy = combining_strategy
    def fit(self, X, y):
        
        self.object = MyBinaryRelevanceFeatureSelect() 
        
        self.object.fit(X,y)
#        X_new = self.selecting_strategy.fit_transform(X, y)
#        X_new.shape
        return self
    
    def RS(self, q, y):
        #rand select q diff numbers in range 0 - length of y
        #return the indices of the labels
        labels_selected = random.sample(range(0, len(y[0])), q*2)
        list_tuple_of_indices = list(zip(*[iter(labels_selected)]*2))
        
        return list_tuple_of_indices
           
        
        
    
    def CS(self, q, y):
        
        c_c = [] 
        list_of_tuple_indices = []
        
        cc = 0
        #dictionary_cc = dict(zip(indices, c_e))
        
        for i in range(0, y.shape[0]):
            #cc=0
            for j in range(i+1, y.shape[0]):
                #print(i,j)
                if j!=i:
                    list_of_tuple_indices.append((i,j))
                    cc=0
                    for k in range(0, y.shape[1]):
                        if y[i][k]==y[j][k] and y[i][k] == 1:
                            cc = cc + 1
                    c_c.append(cc)    
                    #print(cc)
        #print(c_c)
        #print(list_of_tuple_indices)
        dictionary_cc = dict(zip(list_of_tuple_indices, c_c))
        sorted_cc = sorted(dictionary_cc.items(), key=operator.itemgetter(1), reverse = True)
        #print(sorted_cc)
        list_tuple_of_indices = []
        
        for i in sorted_cc:
            for j in sorted_cc:
                if i[0][0]!=j[0][0] and i[0][1]!=j[0][0] and i[0][0]!=j[0][1] and i[0][1]!=j[0][1]:
                    #print(i[0],j[0])
                    if len(list_tuple_of_indices) == q:
                        break
                    list_tuple_of_indices.append(i[0])
                    #print(i[0],j[0],'###')
                    list_tuple_of_indices.append(j[0])
                    #rint(len(list_tuple_of_indices),'length')
                
                    if len(list_tuple_of_indices) == q:
                        break
                
        #nb of labels within a pair (1,1)
        #select the first q
        #return the labels
        return list_tuple_of_indices
    
    def LS(self, q, y):
        # nr ex agree (1,1) AND (0,0)
        # c_e]
        indices = []
        
        c_e = []
        c_d = []
        
        ce = 0
        cd = 0
        
        for i in range(0, y.shape[0]):
            #cc=0
            for j in range(i+1, y.shape[0]):
                if j!=i:
                    ce = 0
                    cd = 0
                    indices.append((i,j))
                    for k in range(0, y.shape[1]):
                        if y[i][k]==y[j][k] and y[i][k] == 1:
                            ce = ce + 1
                        if y[i][k]==y[j][k] and y[i][k] == 0:
                            ce = ce + 1
                        if y[i][k]!=y[j][k]:
                            cd = cd + 1
                    c_e.append(ce)  
                    c_d.append(cd)
                    #print(ce)
        print(c_e)
        print(c_d)
        print(type(indices))
        dictionary_ce = dict(zip(indices, c_e))
        dictionary_cd = dict(zip(indices, c_d))
        
        sorted_ce = sorted(dictionary_ce.items(), key=operator.itemgetter(1), reverse = True)
        sorted_cd = sorted(dictionary_cd.items(), key=operator.itemgetter(1), reverse = True)
        
        print(sorted_ce,'====')
        print(sorted_cd,'====')

        indices_of_selected_features = []
        
        k = 0#the one chosen
        umbral = q
        for a in sorted_cd:
            for b in sorted_ce:
                if a[0][0]!=b[0][0] and a[0][0]!=b[0][1]and a[0][1]!=b[0][0]and a[0][1]!=b[0][1]:
                    #print(a[0],b[0])#,a[0],a[1],b[0],b[1])
                    print(a[0],b[0],'###')
                    print(a[1],b[1],'###')
                    if a[1]>b[1]:
                        indices_of_selected_features.append(a[0])
                        indices_of_selected_features.append(b[0])
                        k = k + 2
                        #a = next(sorted_cd)
                    if b[1]>a[1]:
                        indices_of_selected_features.append(b[0])
                        k = k + 2
                        #b = next(sorted_ce)
            if k == umbral:
                break
        #]]]]]]]]]]]]]
        for i in range(0,len(a)):
               for  j in range(i+1,len(b)):
                    print(i,j,'#####')
                    if a[i][0][0]!=b[j][0][0] and a[i][0][0]!=b[j][0][1]and a[i][0][1]!=b[j][0][0]and a[i][0][1]!=b[j][0][1]:
                        #print(a[i][0],a[i][1],'    ',b[i][0],b[i][1],'normal')
                        #print(a[i],'=====',b[i],'normal')
                        print(a[0],b[0])
            #             if a[i][1] >= b[j][1]:
            #                 ce = True
            #                 print(a[i][0],a[i][1],'    ',b[i][0],b[i][1],'ce')
            #                 k = k + 1
            #             if a[i][1] < b[j][1]:
            #                 cd = True
            #                 print(a[i][0],a[i][1],'====',b[i][0],b[i][1],'cd')
            #                 k = k + 1
            
            #         if ce == True:
            #             i = i + 1
            #             ce = False
            #         if cd == True:
            #             j = j + 1
            #             cd = False
        
        return indices_of_selected_features
    
    def generation(self,label_indices_tuples, y, method):
        #AND  y[i][j] = 1 iff y[i]=y[j]=1 else y[i][j]=0
        #XOR  y[i][j] = 1 iff y[i]!=y[j]  else y[i][j]=0
        #XNOR y[i][j] = 1 iff y[i]=y[j]   else y[i][j]=0
        self.AND_labels = []
        self.XOR_labels = []
        self.XNOR_labels = []
        
        for label in range(0,len(label_indices_tuples)):
        
            label1 = y[label_indices_tuples[label][0]]
            label2 = y[label_indices_tuples[label][1]]
            
            #print(label1,'###')
            #print(label2,'###')
            
            new_label_AND = []
            new_label_XOR = []
            new_label_XNOR = []
            for i in range(0,len(y[0])):
                #print(i,'#')
                #AND
                if label1[i] == label2[i] and label1[i]==1:
                    new_label_AND.append(1)
                else:
                    new_label_AND.append(0) 
                #XOR
                if label1[i] != label2[i]:
                    new_label_XOR.append(1)
                else:
                    new_label_XOR.append(0)
                #XNOR
                if label1[i] == label2[i]:
                    new_label_XNOR.append(1)
                else:
                    new_label_XNOR.append(0)
            #print(new_label_AND)
            self.AND_labels.append(new_label_AND)
            #print(new_label_XOR)
            self.XOR_labels.append(new_label_XOR)
            #print(new_label_XNOR)
            self.XNOR_labels.append(new_label_XNOR)
        if method == 'AND':
            return self.AND_labels
        if method == 'XOR':
            return self.XOR_labels
        if method == 'XNOR':
            return self.XNOR_labels
        #return self.AND_labels, self.XOR_labels, self.XNOR_labels
    
    def concatenation(self, y, labels_to_concatenate):
        y = np.concatenate((y,labels_to_concatenate))
        return y
       
    def predict(self, X, y=None):
        return self.object.predict(X)

    def predict_proba(self, X):
        return self.object.predict_proba(X)