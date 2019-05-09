{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {},
   "outputs": [],
   "source": [
    "\n",
    "from skmultilearn.problem_transform import LabelPowerset\n",
    "from sklearn.naive_bayes import GaussianNB\n",
    "from sklearn.feature_selection import SelectKBest\n",
    "from sklearn.feature_selection import chi2\n",
    "\n",
    "import pandas as pd"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "metadata": {},
   "outputs": [],
   "source": [
    "class MyPowerSetFeatureSelect():\n",
    "#     def __init__(self, X, y):\n",
    "#         self.X = X\n",
    "#         self.y = y\n",
    "        \n",
    "    def fit(self, X, y):\n",
    "        \n",
    "        # I'm using a gaussian naive bayes base classifier\n",
    "        self.LabelPowerSetObject = LabelPowerset(GaussianNB())\n",
    "        \n",
    "        # fitting the data\n",
    "        self.LabelPowerSetObject = self.LabelPowerSetObject.fit(X, y)\n",
    "        \n",
    "        # transformed y \n",
    "        y_transformed  = self.LabelPowerSetObject.transform(y)\n",
    "        \n",
    "        # the feature selecting\n",
    "        X = SelectKBest(chi2, k=2).fit_transform(X, y_transformed)\n",
    "        \n",
    "        return X\n",
    "        \n",
    "    \n",
    "    def transform(self, X):\n",
    "        \n",
    "        X = self.X\n",
    "        #don't know well what I have to implement in here\n",
    "        return X"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>0</th>\n",
       "      <th>1</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>3.0</td>\n",
       "      <td>6.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>1.0</td>\n",
       "      <td>4.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>3.0</td>\n",
       "      <td>4.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>1.0</td>\n",
       "      <td>3.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>3.0</td>\n",
       "      <td>1.0</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "     0    1\n",
       "0  3.0  6.0\n",
       "1  1.0  4.0\n",
       "2  3.0  4.0\n",
       "3  1.0  3.0\n",
       "4  3.0  1.0"
      ]
     },
     "execution_count": 4,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "#tests\n",
    "from sklearn.datasets import make_multilabel_classification\n",
    "\n",
    "X, y = make_multilabel_classification(n_classes=4, n_labels=2,sparse = True, allow_unlabeled=False, random_state=1)\n",
    "\n",
    "my_object = MyPowerSetFeatureSelect()\n",
    "\n",
    "my_object.fit(X,y)\n",
    "pd.DataFrame(my_object.fit(X,y).toarray()).head()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "metadata": {},
   "outputs": [],
   "source": [
    "#pd.DataFrame(X.toarray())"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.6.7"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
