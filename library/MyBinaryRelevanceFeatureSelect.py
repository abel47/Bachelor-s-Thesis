from skmultilearn.problem_transform import BinaryRelevance
from sklearn.svm import SVC
#from sklearn.base import ProblemTransformationBase


class MyBinaryRelevanceFeatureSelect():
   
    def fit(self, X, y):
        
        # I'm using a gaussian naive bayes base classifier
        self.BinaryRelevanceObject = BinaryRelevance(classifier = SVC(gamma= 'auto', probability=True), require_dense = [True, True])
        #self.BinaryRelevanceObject = BinaryRelevance()

        # fitting the data
        self.BinaryRelevanceObject.fit(X, y)
        
        #the classifiers for each label
        self.classifiers = self.BinaryRelevanceObject.classifiers_

        return self.BinaryRelevanceObject.fit(X, y)
        
#     def partition(self):
#         return self.BinaryRelevanceObject.partition_#BinaryRelevanceObject
    
#     def model_count(self):
#         return self.BinaryRelevanceObject.model_count_

    def predict(self, X, y=None):
        return self.BinaryRelevanceObject.predict(X)

    def predict_proba(self, X):
        return self.BinaryRelevanceObject.predict_proba(X)    
    
#    def feature_select(self, X, y, transformer):   
#        transformer.fit(X, y)
#        selected_attributes_indices = transformer.get_support(indices = True)
#        
#        return selected_attributes_indices
#    
#    def sets_of_selected_features(self, X, predictions, classifier, transformer ): #X is the df with the predictions
#        selected_features_array = []
#
#        for i in predictions:
#            indices_features_selected = classifier.feature_select(X, predictions[i], transformer)
#            selected_features_array.append(indices_features_selected)
#    
#        return selected_features_array