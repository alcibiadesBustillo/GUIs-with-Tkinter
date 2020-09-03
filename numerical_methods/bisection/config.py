from math import *

def create_safe_dict():
    # list of safe methods 
    safe_key = ['acos', 'asin', 'atan', 'atan2', 'ceil', 'cos', 
                'cosh', 'degrees', 'e', 'exp', 'fabs', 'floor', 
                'fmod', 'frexp', 'hypot', 'ldexp', 'log', 'log10', 
                'modf', 'pi', 'pow', 'radians', 'sin', 'sinh', 'sqrt', 
                'tan', 'tanh']
    safe_value = [acos, asin, atan, atan2, ceil, cos, 
                cosh, degrees, e, exp, fabs, floor, 
                fmod, frexp, hypot, ldexp, log, log10, 
                modf, pi, pow, radians, sin, sinh, sqrt, 
                tan, tanh]  
    return dict(zip(safe_key, safe_value))