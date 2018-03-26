from numpy import *
from euclideanDistance import euclideanDistance

def kNN(k, X, labels, y):
    # Assigns to the test instance the label of the majority of the labels of the k closest 
    # training examples using the kNN with euclidean distance.
    #
    # Input: k: number of nearest neighbors
    #        X: training data           
    #        labels: class labels of training data
    #        y: test data
    
    
    # ====================== ADD YOUR CODE HERE =============================
    # Instructions: Run the kNN algorithm to predict the class of
    #               y. Rows of X correspond to observations, columns
    #               to features. The 'labels' vector contains the 
    #               class to which each observation of the training 
    #               data X belongs. Calculate the distance betweet y and each 
    #               row of X, find  the k closest observations and give y 
    #               the class of the majority of them.
    #
    # Note: To compute the distance betweet two vectors A and B use
    #       use the euclideanDistance(A,B) function.
    #
    label=zeros(y.shape[0])
    for j in range (y.shape[0]):   
        dist=list()
        k_labelmax=list()
        for i in range(X.shape[0]):
            dist_i=euclideanDistance(y[j,:],X[i,:])
            dist.append(dist_i)
        for l in range(k):
            k_labelmax.append(labels[dist.index(min(dist))])
            del dist[dist.index(min(dist))]
        label[j]=max(k_labelmax, key=k_labelmax.count)
    # return the label of the test data
    
    return label

 
