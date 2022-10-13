from cvxopt.modeling import variable, op
import time

def timer(func):
    
    def timeit(*args):
        start = time.time()
        result = func(*args)
        stop = time.time()
        total_time = stop - start
        return "ESTIMATED TIME: {}\nReturn to x-values: {}\nObject is: {:.4f}".format(total_time,result[0][1:len(result[0])],result[1])
    return timeit

@timer
def cvxoptOptimization():
    x = variable(9, 'x')
    z=-(8232*x[1] +1965.92*x[2]+x[3]+2000*x[4]+1350*x[5]+800*x[6]+350*x[7])#Функция цели
    mass1 = (x[1]+x[2]+x[3]-2800*x[0] <= 0) 
    mass2 = (4*x[1]+8*x[2]+3*x[3]+6*x[4]+6*x[5]+6*x[6]+6*x[7]-30000*x[0] <=0) 
    mass3 = (2*x[1]+10*x[2]+2*x[3]+3*x[4]+3*x[5]+3*x[6]+3*x[7]-12000*x[0] <=0) 
    mass4 = (x[3]-x[1]>=0) 
    mass5 = (x[1]-x[2]>=0) 
    mass6 = (x[4]+x[5]+x[6]+x[7]-x[8] == 0) 
    mass7 = (x[4]-0.1*x[8] <=0) 
    mass8 = (x[5]-0.2*x[8] <=0) 
    mass9 = (x[6]-0.3*x[8] <=0) 
    mass10 = (x[7]-0.4*x[8] <=0) 
    mass11 = (4.8*0.2*x[1]+2*0.3*x[2]+6*x[3]-5*x[4]-4.7*x[5]-4.4*x[6]-4.1*x[7] >=0) 
    mass12 = (4.8*0.2*x[1]+2*0.3*x[2]+6*x[3]-5*x[4]-4.7*x[5]-4.4*x[6]-4.1*x[7] >=0) 
    mass13 = (30870*x[1]+29720*x[2]+12300*x[3]+3000*x[4]+3150*x[5]+3200*x[6]+3150*x[7] == 1)


    x_non_negative = (x >= 0) 
    problem =op(z,[mass1,mass2,mass3,mass4,mass5,mass6,mass7,mass8,mass9,mass10,mass11,mass12,mass13,x_non_negative])
    problem.solve(solver='glpk')

    returntox = []
    
    for var in x.value:
        returntox.append(round(var/x.value[0],4))
        
    return [returntox,(-1)*problem.objective.value()[0]]

