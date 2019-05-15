from skmultilearn.problem_transform import LabelPowerset
from sklearn.naive_bayes import GaussianNB
from sklearn.feature_selection import SelectKBest
from sklearn.feature_selection import chi2

# =============================================================================
# from sklearn.model_selection import train_test_split
# 
# 
# import pandas as pd
# =============================================================================


class MyLabelPowerSetFeatureSelect():
   
    def fit(self, X, y):
        
        # I'm using a gaussian naive bayes base classifier
        self.LabelPowerSetObject = LabelPowerset(GaussianNB())
        
        # fitting the data
        self.LabelPowerSetObject.fit(X, y)
        
        # transformed y 
        y_transformed  = self.LabelPowerSetObject.transform(y)
        
        # instanciating with SelectKBest object
        self.X_new = SelectKBest(chi2, k=2)
        
        # the feature selecting
        X_transformed = self.X_new.fit_transform(X, y_transformed)
        
        # save indices of the saved attributes
        self.selected_attributes_indices = self.X_new.get_support(indices = True)
        
        #print(self.attributes_indices,'the indices of the selected atributes')
        
        return X_transformed
        
    
    def transform(self, X):    
        return X[:,self.selected_attributes_indices]
    
    def predict(self, X):
        return self.LabelPowerSetObject.predict(X)
    
    def predict_proba(self, X):
        return self.LabelPowerSetObject.predict_proba(X)
	
	#tests
# =============================================================================
# from sklearn.datasets import make_multilabel_classification
# 
# X, y = make_multilabel_classification(n_classes=4, n_labels=2,sparse = True, allow_unlabeled=False, random_state=1)
# 
# X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.33)
# 
# 
# my_object = MyLabelPowerSetFeatureSelect()
# 
# #my_object.fit(X,y).attributes_indices
# 
# my_object.fit(X,y)
# #pd.DataFrame(my_object.fit(X,y).toarray()).head()
# 
# x = pd.DataFrame(my_object.predict(X_test).toarray()).head()
# 
# print(x)
# 
# xx = pd.DataFrame(my_object.predict_proba(X_test).toarray()).head()
# 
# print(xx)
# 
# =============================================================================
