from __future__ import annotations
from Modules.puplpsolution import optimization
from Modules.scipysolution import cvxoptOptimization




def main():
    print('{:*^80}'.format("Optimization with pulp packet"))
    print(optimization())
    print('{:*^80}'.format("Optimization with cvxopt packet"))
    print(cvxoptOptimization())
    

if __name__=="__main__":
    main()