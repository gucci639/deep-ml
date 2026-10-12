import numpy as np

class NaiveBayes():
    def __init__(self, smoothing=1.0):
        # Initialize smoothing
        self.smoothing = smoothing
        
    def forward(self, X, y):
        # Fit model to binary features X and labels y
        x_1 = X[y==1]
        x_0 = X[y==0]

        self.p1_1 = (x_1.sum(axis=0)+self.smoothing)/(len(x_1)+2*self.smoothing)
        self.p1_0 = (x_0.sum(axis=0)+self.smoothing)/(len(x_0)+2*self.smoothing)

        self.prior_1 = len(x_1)/len(X)
        self.prior_0 = len(x_0)/len(X)

    def predict(self, X):
        # Predict class labels for test set X
        score_1 = np.log(self.prior_1) + X @ np.log(self.p1_1) + (1-X) @ np.log(1 - self.p1_1)
        score_0 = np.log(self.prior_0) + X @ np.log(self.p1_0) + (1-X) @ np.log(1 - self.p1_0)
        return np.where(score_1>score_0,1,0)
