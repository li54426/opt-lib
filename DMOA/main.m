%_______________________________________________________________________________________%
%  Dwarf Mongoose Optimization Algorithm source codes (version 1.0)                     %
%                                                                                       %
%  Developed in MATLAB R2015a (7.13)                                                    %
%  Author and programmer: Jeffrey O. Agushaka and Absalom E. Ezugwu and Laith Abualigah %
%         e-Mail:  EzugwuA@ukzn.ac.za                                                   %
%                                                                                       %
%   Main paper:                                                                         %
%__Dwarf Mongoose Optimization Algorithm: A new nature-inspired metaheuristic optimizer %
%__Main paper: please, cite it as follws:_______________________________________________%
%_______________________________________________________________________________________%

clear all 
clc

Solution_no=20;  
F_name='F1';    
M_Iter=1000;    


[LB,UB,Dim,F_obj]=Get_F(F_name); 
[Best_FF,Best_P,conv]=DMOA(Solution_no,M_Iter,LB,UB,Dim,F_obj);  


figure('Position',[454   445   694   297]);
subplot(1,2,1);
func_plot(F_name);
title('Parameter space')
xlabel('x_1');
ylabel('x_2');
zlabel([F_name,'( x_1 , x_2 )'])


subplot(1,2,2);
semilogy(conv,'Color','r','LineWidth',2)
title('Convergence curve')
xlabel('Iteration#');
ylabel('Best fitness function');
axis tight
legend('DMOA')


display(['The best-obtained solution by DMOA is : ', num2str(Best_P)]);
display(['The best optimal values of the objective funciton found by DMOA is : ', num2str(Best_FF)]);

        



