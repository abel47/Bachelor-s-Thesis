# -*- coding: utf-8 -*-
"""
Created on Mon May 20 17:47:09 2019

@author: Abel
"""
#from sklearn.base import TransformerMixin

import random

#from skmultilearn.base.problem_transformation import ProblemTransformationBase
#import numpy as np
#from scipy import sparse

class lcsf_feature_selection():
    def __init__():
#        if q is None: #have to fix things in here
#            q = 2
        self.q = q
        self.selecting_strategy = selecting_strategy
        self.combining_strategy = combining_strategy
    def fit(self, X, y):
        
        #self.lcsf_object =  
        
#        X_new = self.selecting_strategy.fit_transform(X, y)
#        X_new.shape
        
        
        return self
    
    def RS(self, q, y):
        #rand select two diff numbers in range 0 - length of y
        #return the labels
        labels_selected = random.sample(range(0, len(y)), 2)
        
        y_prim = []
        y_prim.append(labels_selected[0])
        y_prim.append(labels_selected[1])        
        
        return y_prim
    
    def CS(self, q, y):
#        dictionary = dict() #or tuple or matrix
#        k = 0
#        for i in range(0,len(y)):
#            for j in range(0,len(y)):
#                if i!=j and y[i]==y[j] and y[j] == 1:
#                    dictionary[k]
#                    pass
        c_c = [] 

        cc = 0
        
        for i in range(0, y.shape[0]):
            #cc=0
            for j in range(i+1, y.shape[0]):
                if j!=i:
                    cc=0
                    for k in range(0, y.shape[1]):
                        if y[i][k]==y[j][k] and y[i][k] == 1:
                            cc = cc + 1
                    c_c.append(cc)    
                    print(cc)
        
        #nb of labels within a pair (1,1)
        #select the first q
        #return the labels
        pass
    
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
                    indices.append([i+1,j+1])
                    for k in range(0, y.shape[1]):
                        if y[i][k]==y[j][k] and y[i][k] == 1:
                            ce = ce + 1
                        if y[i][k]==y[j][k] and y[i][k] == 0:
                            ce = ce + 1
                        if y[i][k]!=y[j][k]:
                            cd = cd + 1
                    c_e.append(ce)  
                    c_d.append(cd)
                    print(ce)
        print(c_e)
        print(c_d)
        print(indices)
        
        pass
    
    def generation(self):
        #AND  y[i][j] = 1 iff y[i]=y[j]=1 else y[i][j]=0
        #XOR  y[i][j] = 1 iff y[i]!=y[j]  else y[i][j]=0
        #XNOR y[i][j] = 1 iff y[i]=y[j]   else y[i][j]=0
        pass
#def doSomething(self, a=None):
#    if a is None:
#        a = self.z
#    self.z = 3
#    self.b = a
    