from numpy import *
from sigmoid import sigmoid

def computeCost(theta, X, y): 
	# Computes the cost using theta as the parameter 
	# for logistic regression. 
    
	m = X.shape[0] # number of training examples
	
	J = 0
	
	# ====================== YOUR CODE HERE ======================
    # Instructions: Calculate the error J of the decision boundary
    #               that is described by theta (see the assignment 
    #				for more details).
    
    
    J=-sum(y*log(sigmoid(dot(theta,X.T)).T)+(1-y)*log(1-sigmoid(dot(theta,X.T)).T))/m


    
    
    
    # =============================================================
	
	return J
