from cgitb import small
import numpy as np
import matplotlib.pyplot as plt




class DMOA(): 
    def __init__(self, func = None, ndim = None, npop = None,  max_it = None, LB = None, UB = None ):
        #-----------函数初始化------------
        self.func = func
        self.npop = npop
        self.ndim = ndim
        self.max_it = max_it
        self.UB = UB
        self.LB = LB

        #---------种群 (子种群) 数目 初始化----------
        self.nbs = 3
        self.nalpha= npop - self.nbs
        self.nScout = self.nalpha
        self.peep = 2
        
        #---------种群初始化--------
        self.X = np.random.uniform(self.LB, self.UB, (self.nalpha, self.ndim))
        self.Y = np.ones(self.nalpha)
        for i in range(self.nalpha):
            self.Y[i] = self.func(self.X[i])

        self.newX = np.zeros((self.nalpha, self.ndim))
        self.newY = np.zeros(self.nalpha)

        self.bestx = self.X[np.argmin(self.Y)]
        self.besty = np.min(self.Y)
        #self.it = 1

        #----------参数初始化---------------
        self.L = round(0.6 * ndim * self.nbs)
        self.sm = np.ones(self.nalpha) * np.inf
        #     print(self.sm)
        '''
        C=zeros(nAlphaGroup,1);
        CF=(1-Iter/MaxIt)^(2*Iter/MaxIt);
        '''
        self.c = np.zeros(self.nalpha)
        self.cf = (1 - 1/max_it) ** (2* 1/max_it)
        self.BestCost = np.zeros(max_it)

        self.f = np.zeros(self.nalpha)
        self.tau = np.inf


    def run(self):
        '''
            % Alpha group
        F=zeros(nAlphaGroup,1);
        MeanCost = mean([pop.Cost]);
        '''
        # alpha group
        
        for it in range(self.max_it):
            self.mean = np.mean(self.Y)
        
            '''for i=1:nAlphaGroup
        
            % Calculate Fitness Values and Selection of Alpha
            F(i) = exp(-pop(i).Cost/MeanCost); % Convert Cost to Fitness
            end
            P=F/sum(F);'''

            #    计算适应度   
            #for i in range(self.nalpha):
                #self.f[i] = np.exp(-self.Y[i] / self.mean)
            
            # the f shape is same as the Y is a vector 
            self.f = np.exp(-self.Y / self.mean)

            # p 是f 的概率 f is a vector
            self.p = self.f / np.sum(self.f)
            
            '''
            function i=RouletteWheelSelection(P)
                %  rand函数产生由在(0, 1)之间均匀分布的随机数组成的数组。
                r=rand;

                % 加为一行
                C=cumsum(P);
                
                i=find(r<=C,1,'first');

            end'''
            for m in range(self.nalpha):
                #r = np.random.uniform()

                z = np.arange(0, self.nalpha)

                i = np.random.choice(z, 1, p = self.p)
                i = int(i)
                #print(i)
                
                phi=(self.peep/2) * np.random.uniform(-1, 1, self.ndim)
                K = i

                while(K == i):
                    K = np.random.randint(0, self.nalpha)
                    k = self.X[K]

                self.newX[i] = self.X[i] + phi * (self.X[i]-self.X[K]);
                self.newY[i] = self.func(self.newX[i])

                if(self.newY[i] <= self.Y[i]):
                    self.X[i] = self.newX[i]
                else:
                    self.c[i] += 1
                
        

        #-------------scout group-----------------
            for i in range(self.nScout):
                K = i
                while(K ==i):
                    K = np.random.randint(0, self.nalpha)

                    k = self.X[K]
                phi=(self.peep/2) * np.random.uniform(-1, 1, self.ndim)
                self.newX[i] = self.X[i] + phi * (self.X[i]-self.X[K]);
                self.newY[i] = self.func(self.newX[i])

                self.sm[i] = (self.newY[i] - self.Y[i]) / max(self.newY[i], self.Y[i])

                if(self.newY[i] <= self.Y[i]):
                    self.X[i] = self.newX[i]
                else:
                    self.c[i] += 1

            #------------babysitters--------------
            for i in range(self.nbs):
                if(self.c[i] >= self.L):
                    self.X[i] = np.random.uniform(self.LB, self.UB, self.ndim)
                    self.Y[i] = self.func(self.X[i])
                    self.c[i] = 0

            if self.besty > np.min(self.Y):
                self.besty = np.min(self.Y) 

            # -----------Next Mongoose Position----------
            newtau = np.mean(self.sm)
            for i in range(self.nScout):
                m = (self.X[i] * self.sm[i]) / self.X[i]
                if(newtau > self.tau):
                    self.newX[i] = self.X[i] - self.cf * phi * np.random.random() * (self.X[i] -m)
                else:
                    self.newX[i] = self.X[i] + self.cf * phi * np.random.random() * (self.X[i] -m)

                self.tau = newtau

            self.BestCost[it-1] = self.besty
            self.bestx = self.X[np.argmin(self.Y)]
            besty = np.min(self.Y)

        print('run sussess')
        
        return self.bestx, self.besty



def demo_func(x):
    # the input is np.array, and is a vector
    return x[0] ** 2 + (x[1] - 0.05) ** 2 + x[2] ** 2

if __name__ == '__main__':
    demo = DMOA(func = demo_func, ndim = 3, npop = 100,  max_it = 150, LB = -10, UB = 10)
    bestx , besty = demo.run()
    print(bestx, besty)

    from sko.PSO import PSO

    pso = PSO(func=demo_func, n_dim=3, pop=100, max_iter=150, lb=[-10, -10, -10], ub=[10, 10, 10], w=0.8, c1=0.5, c2=0.5)
    pso.run()
    print('best_x is ', pso.gbest_x, 'best_y is', pso.gbest_y)

    print(demo_func(bestx))
