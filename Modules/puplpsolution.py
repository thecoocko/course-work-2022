from pulp import *



def optimization():

    x0 = pulp.LpVariable("x0", lowBound=0)
    x1 = pulp.LpVariable("x1", lowBound=0)
    x2 = pulp.LpVariable("x2", lowBound=0)
    x3 = pulp.LpVariable("x3", lowBound=0)
    x4 = pulp.LpVariable("x4", lowBound=0)
    x5 = pulp.LpVariable("x5", lowBound=0)
    x6 = pulp.LpVariable("x6", lowBound=0)
    x7 = pulp.LpVariable("x7", lowBound=0)
    x8 = pulp.LpVariable("x8", lowBound=0)

    problem = pulp.LpProblem('Problem',LpMaximize)
    problem += 8232*x1+1965.98*x2+2000*x4+1350*x5+800*x6+350*x7
    problem += x1+x2+x3-2800*x0 <= 0
    problem += 4*x1+8*x2+3*x3+6*x4+6*x5+6*x6+6*x7-30000*x0 <= 0
    problem += 2*x1+10*x2+2*x3+3*x4+3*x5+3*x6+3*x7-12000*x0 <= 0
    problem += x3-x1 >=0
    problem += x1-x2 >=0
    problem += x4+x5+x6+x7-x8 == 0
    problem += x4-0.1*x8 <=  0
    problem += x5 -0.2*x8<=0 
    problem += x6-0.3*x8 <= 0
    problem += x7-0.4*x8 <= 0
    problem += 0.96*x1+0.6*x2+6*x3-5*x4-4.7*x5-4.4*x6-4.1*x7 >= 0
    problem += 30870*x1+29720*x2+12300*x3+3000*x4+3150*x5+3200*x6+3150*x7 == 1

    problem.solve()
    
    varsdict = {}
    returntox = []

    for variable in problem.variables():
        print (variable.name, "=", variable.varValue)
        varsdict[variable.name] = variable.varValue

    for variable in varsdict:
        returntox.append(round(varsdict[variable]/varsdict['x0'],4))
        
    return returntox[1:8],value(problem.objective)
   
print("Return to x-values: {} \nObject ist: {:.4f}".format(optimization()[0],optimization()[1]) )