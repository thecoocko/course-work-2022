from scipy.optimize import linprog
import time
start = time.time()
c = [-8232,1965.98,2000,1350,800,350] #Функция цели
X1 = [[1,1,1,0,0,0,0]]  #'1'   
x1 = [2800]#'1'   
X2 = [[4,8,3,6,6,6,6]] #'2'   
x2 = [3000] #'2'   
X3 = [[2,10,2,3,3,3,3]] #'2'   
x3 = [12000] #'2'   
X4 = [[-1,0,1,0,0,0,0]] #'2'   
x4 = [0] #'2'   
X5 = [[1,-1,0,0,0,0,0]] #'2'   
x5 = [0] #'2'   
X6 = [[4.8*0.2,2*0.3,6,-5,-4.7,-4.4,-4.4]] #'2'   
x6 = [0] #'2'   
X6 = [[30870,29720,12300,3000,3150,3200,3150]] #'2'   
x6 = [1] #'2'   
print (linprog(c, X1, x1, X2, x2,X3,x3,X4,x4,X5,x5,X6,x6))
stop = time.time()
print ("Время :")
print(stop - start)