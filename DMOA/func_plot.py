#_______________________________________________________________________________________#
#  Aquila Optimizer (AO) source codes (version 1.0)                                     #
#                                                                                       #
#  Developed in MATLAB R2015a (7.13)                                                    #
#  Author and programmer: Laith Abualigah                                               #
#  Abualigah, L, Yousri, D, Abd Elaziz, M, Ewees, A, Al-qaness, M, Gandomi, A.          #
#         e-Mail: Aligah.2020@gmail.com                                                 #
#       Homepage:                                                                       #
#         1- https://scholar.google.com/citations?user=39g8fyoAAAAJ&hl=en               #
#         2- https://www.researchgate.net/profile/Laith_Abualigah                       #
#                                                                                       #
#   Main paper:                                                                         #
#_____________Aquila Optimizer: A novel meta-heuristic optimization algorithm___________#
#_______________________________________________________________________________________#
# Abualigah, L, Yousri, D, Abd Elaziz, M, Ewees, A, Al-qaness, M, Gandomi, A. (2021).
# Aquila Optimizer: A novel meta-heuristic optimization algorithm.
# Computers & Industrial Engineering.
#_______________________________________________________________________________________#
import numpy as np
    
def func_plot(func_name = None): 
    LB,UB,Dim,F_obj = Get_F(func_name)
    if 'F1' == func_name:
        x = np.arange(- 100,100+2,2)
        y = x
    else:
        if 'F2' == func_name:
            x = np.arange(- 100,100+2,2)
            y = x
        else:
            if 'F3' == func_name:
                x = np.arange(- 100,100+2,2)
                y = x
            else:
                if 'F4' == func_name:
                    x = np.arange(- 100,100+2,2)
                    y = x
                else:
                    if 'F5' == func_name:
                        x = np.arange(- 200,200+2,2)
                        y = x
                    else:
                        if 'F6' == func_name:
                            x = np.arange(- 100,100+2,2)
                            y = x
                        else:
                            if 'F7' == func_name:
                                x = np.arange(- 1,1+0.03,0.03)
                                y = x
                            else:
                                if 'F8' == func_name:
                                    x = np.arange(- 500,500+10,10)
                                    y = x
                                else:
                                    if 'F9' == func_name:
                                        x = np.arange(- 5,5+0.1,0.1)
                                        y = x
                                    else:
                                        if 'F10' == func_name:
                                            x = np.arange(- 20,20+0.5,0.5)
                                            y = x
                                        else:
                                            if 'F11' == func_name:
                                                x = np.arange(- 500,500+10,10)
                                                y = x
                                            else:
                                                if 'F12' == func_name:
                                                    x = np.arange(- 10,10+0.1,0.1)
                                                    y = x
                                                else:
                                                    if 'F13' == func_name:
                                                        x = np.arange(- 5,5+0.08,0.08)
                                                        y = x
                                                    else:
                                                        if 'F14' == func_name:
                                                            x = np.arange(- 100,100+2,2)
                                                            y = x
                                                        else:
                                                            if 'F15' == func_name:
                                                                x = np.arange(- 5,5+0.1,0.1)
                                                                y = x
                                                            else:
                                                                if 'F16' == func_name:
                                                                    x = np.arange(- 1,1+0.01,0.01)
                                                                    y = x
                                                                else:
                                                                    if 'F17' == func_name:
                                                                        x = np.arange(- 5,5+0.1,0.1)
                                                                        y = x
                                                                    else:
                                                                        if 'F18' == func_name:
                                                                            x = np.arange(- 5,5+0.06,0.06)
                                                                            y = x
                                                                        else:
                                                                            if 'F19' == func_name:
                                                                                x = np.arange(- 5,5+0.1,0.1)
                                                                                y = x
                                                                            else:
                                                                                if 'F20' == func_name:
                                                                                    x = np.arange(- 5,5+0.1,0.1)
                                                                                    y = x
                                                                                else:
                                                                                    if 'F21' == func_name:
                                                                                        x = np.arange(- 5,5+0.1,0.1)
                                                                                        y = x
                                                                                    else:
                                                                                        if 'F22' == func_name:
                                                                                            x = np.arange(- 5,5+0.1,0.1)
                                                                                            y = x
                                                                                        else:
                                                                                            if 'F23' == func_name:
                                                                                                x = np.arange(- 5,5+0.1,0.1)
                                                                                                y = x
    
    L = len(x)
    f = []
    for i in np.arange(1,L+1).reshape(-1):
        for j in np.arange(1,L+1).reshape(-1):
            if str(func_name) == str('F15') == 0 and str(func_name) == str('F19') == 0 and str(func_name) == str('F20') == 0 and str(func_name) == str('F21') == 0 and str(func_name) == str('F22') == 0 and str(func_name) == str('F23') == 0:
                f[i,j] = F_obj(np.array([x(i),y(j)]))
            if str(func_name) == str('F15') == 1:
                f[i,j] = F_obj(np.array([x(i),y(j),0,0]))
            if str(func_name) == str('F19') == 1:
                f[i,j] = F_obj(np.array([x(i),y(j),0]))
            if str(func_name) == str('F20') == 1:
                f[i,j] = F_obj(np.array([x(i),y(j),0,0,0,0]))
            if str(func_name) == str('F21') == 1 or str(func_name) == str('F22') == 1 or str(func_name) == str('F23') == 1:
                f[i,j] = F_obj(np.array([x(i),y(j),0,0]))
    
    surfc(x,y,f,'LineStyle','none')
    return
    