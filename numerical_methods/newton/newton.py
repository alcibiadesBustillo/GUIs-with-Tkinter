"""
    To obtain a solution of f(x)=0 given f diferentiable
"""
from prettytable import PrettyTable
from newton.config import create_safe_dict
from math import pi, e


safe_dict = create_safe_dict()

def newton(f, g, po, TOL, No):
    """name method

    Parameters
    ----------
    
    f : string
        function f(x)
    g : string
        function f'(x)
    po : float
        initial aproximation    
    TOL : float
        error
    No : int
        number of iterations

    Returns
    -------
    p: float
        aproximation of solution or error message
    """
    i = 1

    # passing variable x in safe dictionary 
    safe_dict['x'] = po   


    x = PrettyTable(["n", "p"])  

    while(i <= No):
        p = po - eval(f, safe_dict) / eval(g, safe_dict)
        #print("{}-The value of p is {}".format(i,p))

        x.add_row([i, round(p,7) ])
        if( abs(p - po) < TOL):
            #print(x)
            return p, x 

        i = i + 1
        po = p        
        safe_dict['x'] = po        
    
    #print("The method faile after {} iterarions".format(No))
    
    return None, None

#newton('cos(x) - x', '-sin(x) - 1', pi/4, 1e-9, 40)