#_______________________________________________________________________________________#
#  Dwarf Mongoose Optimization Algorithm source codes (version 1.0)                     #
#                                                                                       #
#  Developed in MATLAB R2015a (7.13)                                                    #
#  Author and programmer: Jeffrey O. Agushaka and Absalom E. Ezugwu and Laith Abualigah #
#         e-Mail:  EzugwuA@ukzn.ac.za                                                   #
#                                                                                       #
#   Main paper:                                                                         #
#__Dwarf Mongoose Optimization Algorithm: A new nature-inspired metaheuristic optimizer #
#__Main paper: please, cite it as follws:_______________________________________________#
#_______________________________________________________________________________________#
#_______________________________________________________________________________________#
import numpy as np
import numpy.matlib
    
def DMOA(nPop = None,MaxIt = None,VarMin = None,VarMax = None,nVar = None,F_obj = None): 
    #nVar=5;             # Number of Decision Variables
    
    VarSize = np.array([1,nVar])
    
    #VarMin=-10;         # Decision Variables Lower Bound
#VarMax= 10;         # Decision Variables Upper Bound
    
    ## ABC Settings
    
    # MaxIt=1000;              # Maximum Number of Iterations
    
    # nPop=100;               # Population Size (Family Size)
    
    nBabysitter = 3
    
    nAlphaGroup = nPop - nBabysitter
    
    nScout = nAlphaGroup
    
    L = np.round(0.6 * nVar * nBabysitter)
    
    peep = 2
    
    ########################################################################
    
    # Empty Mongoose Structure
    empty_mongoose.Position = []
    empty_mongoose.Cost = []
    # Initialize Population Array
    pop = np.matlib.repmat(empty_mongoose,nAlphaGroup,1)
    # Initialize Best Solution Ever Found
    BestSol.Cost = inf
    tau = inf
    Iter = 1
    sm = inf(nAlphaGroup,1)
    # Create Initial Population
    for i in np.arange(1,nAlphaGroup+1).reshape(-1):
        pop(i).Position = unifrnd(VarMin,VarMax,VarSize)
        pop(i).Cost = F_obj(pop(i).Position)
        if pop(i).Cost <= BestSol.Cost:
            BestSol = pop(i)
    
    # Abandonment Counter
    C = np.zeros((nAlphaGroup,1))
    CF = (1 - Iter / MaxIt) ** (2 * Iter / MaxIt)
    # Array to Hold Best Cost Values
    BestCost = np.zeros((MaxIt,1))
    ## DMOA Main Loop
    
    for it in np.arange(1,MaxIt+1).reshape(-1):
        # Alpha group
        F = np.zeros((nAlphaGroup,1))
        MeanCost = mean(np.array([pop.Cost]))
        for i in np.arange(1,nAlphaGroup+1).reshape(-1):
            # Calculate Fitness Values and Selection of Alpha
            F[i] = np.exp(- pop(i).Cost / MeanCost)
        P = F / sum(F)
        # Foraging led by Alpha female
        for m in np.arange(1,nAlphaGroup+1).reshape(-1):
            # Select Alpha female
            i = RouletteWheelSelection(P)
            # Choose k randomly, not equal to Alpha
            K = np.array([np.arange(1,i - 1+1),np.arange(i + 1,nAlphaGroup+1)])
            k = K(randi(np.array([1,np.asarray(K).size])))
            # Define Vocalization Coeff.
            phi = (peep / 2) * unifrnd(- 1,+ 1,VarSize)
            # New Mongoose Position
            newpop.Position = pop(i).Position + np.multiply(phi,(pop(i).Position - pop(k).Position))
            # Evaluation
            newpop.Cost = F_obj(newpop.Position)
            # Comparision
            if newpop.Cost <= pop(i).Cost:
                pop[i] = newpop
            else:
                C[i] = C(i) + 1
        # Scout group
        for i in np.arange(1,nScout+1).reshape(-1):
            # Choose k randomly, not equal to i
            K = np.array([np.arange(1,i - 1+1),np.arange(i + 1,nAlphaGroup+1)])
            k = K(randi(np.array([1,np.asarray(K).size])))
            # Define Vocalization Coeff.
            phi = (peep / 2) * unifrnd(- 1,+ 1,VarSize)
            # New Mongoose Position
            newpop.Position = pop(i).Position + np.multiply(phi,(pop(i).Position - pop(k).Position))
            # Evaluation
            newpop.Cost = F_obj(newpop.Position)
            # Sleeping mould
            sm[i] = (newpop.Cost - pop(i).Cost) / np.amax(newpop.Cost,pop(i).Cost)
            # Comparision
            if newpop.Cost <= pop(i).Cost:
                pop[i] = newpop
            else:
                C[i] = C(i) + 1
        # Babysitters
        for i in np.arange(1,nBabysitter+1).reshape(-1):
            if C(i) >= L:
                pop(i).Position = unifrnd(VarMin,VarMax,VarSize)
                pop(i).Cost = F_obj(pop(i).Position)
                C[i] = 0
        # Update Best Solution Ever Found
        for i in np.arange(1,nAlphaGroup+1).reshape(-1):
            if pop(i).Cost <= BestSol.Cost:
                BestSol = pop(i)
        # Next Mongoose Position
        newtau = mean(sm)
        for i in np.arange(1,nScout+1).reshape(-1):
            M = (np.multiply(pop(i).Position,sm(i))) / pop(i).Position
            if newtau > tau:
                newpop.Position = pop(i).Position - np.multiply(CF * phi * rand,(pop(i).Position - M))
            else:
                newpop.Position = pop(i).Position + np.multiply(CF * phi * rand,(pop(i).Position - M))
            tau = newtau
        # Update Best Solution Ever Found
        for i in np.arange(1,nAlphaGroup+1).reshape(-1):
            if pop(i).Cost <= BestSol.Cost:
                BestSol = pop(i)
        # Store Best Cost Ever Found
        BestCost[it] = BestSol.Cost
        BEF = BestSol.Cost
        BEP = BestSol.Position
        # Display Iteration Information
        print(np.array(['Iteration ',num2str(it),': Best Cost = ',num2str(BestCost(it))]))
    
    return BEF,BEP,BestCost