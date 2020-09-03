"""
    To obtain a solution of f(x)=0 given f continous in theinterval [a,b], where
    f(a) and f(b) have oposite signs
"""
from prettytable import PrettyTable
from bisection.config import create_safe_dict



safe_dict = create_safe_dict()

def bisection(f, a, b, TOL, No):
    """name method

    Parameters
    ----------
    a : float
        upper limit
    b : float
        lower limit
    TOL : float
        error
    No : int
        number of iterations

    Returns
    -------
    p: float
        solution to equation f(x) = 0
    """
    i = 1

    # passing variable x in safe dictionary 
    safe_dict['x'] = a 
  
    # evaluating expression 
    FA = eval(f, safe_dict)     


    x = PrettyTable(["n", "a_n", "b_n", "p_n", "f(p_n)"])
    
    # Save values to plot
    p_x = []
    f_x = []

    while(i <= No):
        p = a + (b - a)/2
        
        safe_dict['x'] = p

        # evaluating expression 
        FB = eval(f, safe_dict) 
        
        x.add_row([i, round(a,4), round(b,4), round(p,4), round(FB,4)])
        p_x.append(p)
        f_x.append(FB)
        
        if(FB == 0 or ((b-a)/2 < TOL)):
            print(x)
            return p, x, p_x, f_x
        i = i + 1

        if (FA * FB > 0):
            a = p
            FA = FB
        else:
            b = p
    
    print("The method faile after {} iterarions".format(No))
    
    return None, None, None, None            

#p1, _ = bisection('ls ', 1.0, 2.0, 0.0001, 14)
print()
#p2, x = bisection("x*cos(x) - 2*x**2 + 3*3 - 1", 0.2, 0.3, 0.00001, 20)

