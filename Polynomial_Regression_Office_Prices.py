#my first challenge!!!!
from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression

POLY_DEGREE = 4
X = []
vector = []
predict = []
num_features = 0
num_rows = 0
           
def parse_input():
    
    f_n = [float(i) for i in raw_input().strip().split()] # f_n = ["2", "100"]
    num_features = int(f_n[0]) # num_features = 2
    num_rows = int(f_n[1]) # num_rows = 100
       
    for x in range(num_rows): # iterate from 1 to 100 
        temp = raw_input().strip().split() # grab the line of input, e.g.: 0.44 0.68 511.14 as an array 
        X.append([float(i) for i in temp[0:num_features]]) # add [0.44, 0.68] to the next available index of X
        vector.append(float(temp[num_features])) # add 511.14 to the next available index of vector
        
    num_no_y = int(raw_input().strip())
    
    for y in range(num_no_y):
        temp = raw_input().strip().split()
        predict.append([float(i) for i in temp[0:num_features]])
        
if __name__ == '__main__':
            
    parse_input()
    
    poly = PolynomialFeatures(degree=POLY_DEGREE)
    
    x_poly = poly.fit_transform(X)
    predict_poly = poly.fit_transform(predict)   
           
    lin_reg = LinearRegression()
    lin_reg.fit(x_poly, vector)
    
    predicted_dataset = lin_reg.predict(predict_poly)
    
    # Print predicted output
    for ind in range(len(predict)):
        print predicted_dataset[ind]
