"""
    To obtain a solution of f(x)=0 given f continous in theinterval [a,b], where
    f(a) and f(b) have oposite signs
"""
from prettytable import PrettyTable
from fix_point.config import create_safe_dict



safe_dict = create_safe_dict()

def fix_point(f, po, TOL, No):
    """name method

    Parameters
    ----------
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
  
    # evaluating expression 
    #FA = eval(f, safe_dict)     


    x = PrettyTable(["n", "p"])
    
    # Save values to plot
    #p_x = []
    #f_x = []

    while(i <= No):
        p = eval(f, safe_dict)
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

#fix_point('0.5 * (10 - x**3)**(0.5)', 1.5, 1e-9, 40)
