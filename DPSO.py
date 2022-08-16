from re import M
import numpy as np


class DPSO():
    def __init__(self, func, constant, ndim = None, machine = None,  pop =40,max_iter=150, p=0.5):
        self.ndim = ndim;
        self.func = func
        self.constant = constant
        self.pop = pop
        self.max_iter = max_iter
        self.machine = machine
        self.p1 =p
        #self.lb, self.ub = np.zeros(self.n_dim), np.ones(self.ndim)*(self.ndim - 1)
        self.x = np.random.randint(self.machine , size = (self.pop, self.ndim))
        #print('x=', self.x)

        self.y = self.gety()
        self.p = self.x.copy()
        self.pg = self.getpg()
        #self.r1 = self.rvs(self.p1, ndim = self.ndim)
        #self.r2 = self.rvs(self.p1, ndim = self.ndim)

    def gety(self):
        return self.func(self.x, self.constant)


    def getpg(self):
        index = np.argmin(self.y)
        return np.repeat( self.x[index].reshape(-1, self.ndim), self.pop, axis=0)
        #self.x[index]
        #np.repeat( self.x[index].reshape(self.ndim, -1), self.pop, axis=0)



    def rvs(self, p = 0.5,ndim=1):
        #p = self.
        #实现伯努利分布
        rvs = np.array([])
        for i in range(0,ndim):
            if np.random.rand() <= p:
                a=1
                rvs = np.append(rvs,a)
            else:
                a=0
                rvs = np.append(rvs,a)
        return rvs



    def sub(self, a, b):
        res = np.zeros((self.pop, self.ndim))
        res = a - b
        nz = np.nonzero(res)
        res[nz] = a[nz]
        '''
        for i in range(self.pop):
            res[i] = a[i] - b[i]
            nz = np.nonzero(res[i])
            #print(nz)
            res[i, nz] = a[i, nz]'''
        
        return res



    def add(self,a, b):
        #随机选择两个位置(切点)，并在这两个位置之间交换维数
        res = np.ones((self.pop, self.ndim))
        for i in range(self.pop):
            # m,n 是断点
            m = np.random.randint(1,self.ndim-1)
            n = np.random.randint(1,self.ndim-1)
            while(m == n):
                n = np.random.randint(1,self.ndim-1)

            if(m > n):
                m = m+n
                n = m -n
                m = m - n

            # comfrim  m is < n 
            #一共有六段 编号分别是
            #1 3 5
            #2,4,6
            #一共八种情况
            flag1 = np.random.randint(1,3)
            flag2 = np.random.randint(3,5)
            flag3 = np.random.randint(5,7)

            if(flag1 % 2 ==1):
                #使用第一条染色体
                res[i, 0: m] = a[i, 0: m]
            else:
                res[i, 0: m] = b[i, 0: m]

            if(flag2 % 2 ==1):
                #使用第一条染色体
                res[i, m: n] = a[i, m: n]
            else:
                res[i, m: n] = b[i, m: n]

            if(flag3 % 2 ==1):
                #使用第一条染色体
                res[i, n: ] = a[i, n: ]
            else:
                res[i, n: ] = b[i, n: ]

        return res



    def mult(self, a, b):
        return a * b
        #for i in range(self.pop):

    def updatav(self):
        r1 = np.ones((self.pop, self.ndim))
        for i in range(self.pop):
            r1[i] = self.rvs(self.p1, self.ndim)

        r2 =np.ones((self.pop, self.ndim)) 
        for i in range(self.pop):
            r2[i] =  self.rvs(self.p1, self.ndim)

        a = self.sub(self.p, self.x)
        #print('a=', a)
        b = self.mult(r1,a)

        c = self.sub(self.pg, self.x)
        d = self.mult(r2, c)

        e = self.add(b, d)
        self.v = self.add(self.p, e)

    def updatax(self):

        self.x = self.add(self.x, self.v)

    def updatap(self):
        yx = self.func(self.x, self.constant)
        yp = self.func(self.p, self.constant)
        for i in range(self.pop):
            if(yx[i] < yp[i]):
                self.p[i] = self.x[i]


    def run(self):
        for i in range(self.max_iter):
            self.updatav()
            self.updatax()

            self.updatap()
            self.pg= self.getpg()
            self.y = self.gety()

        return self.pg[0], self.func(self.pg, self.constant)[0]


def minC(x, constant):
    # x is 分配矩阵 constant是工件相关的参数, 并且是二维np.array()
    x = x.astype(int)
    len = constant.shape[1]
    x = x.reshape(-1, len)

    pop = x.shape[0]

    timelist = np.zeros(pop)
    y = np.zeros(pop)

    for i in range(pop):
        #机器数是
        machine = int(x.max()) + 1


        time = np.zeros( machine)

        for j in range(len):
            index = x[i,j]#.astype(int)
            #print('constant[0, j]=',constant[0, j])
            time[index] = time[index] + constant[0, j]
            #print('time =', time)
        timelist[i] = time.max()


    return timelist


def LPT(constant, machine):
    time = np.zeros(machine)
    constant = constant[0]
    order = -np.sort(-constant)

    jobs = order.shape[0]
    for i in range(jobs):
        index = np.argmin(time)
        time[index] += order[i]

    return time.max()


def generator(ndim = 50,n = 100 ):
    size = (n, ndim)
    res = np.zeros((n,ndim))
    for i in range(n):
        a = np.random.randint(1, 30, size = ndim)
        res[i] = a


    return res 



if __name__ == '__main__':
    constant = [[1,1,2,3,1]]
    constant = [[1,4,2,5,1]]
    

    constant = np.array(constant)

    machine = 4
    ndim = 50
    n =10
    constant = generator(n = n, ndim = ndim)
    res = np.ones((n, 2))
    
    for i in range(n):
        
        constant1 = constant[i].reshape(-1, ndim)

        dpso = DPSO(minC, constant= constant1, ndim = ndim, machine = machine,  pop =100, max_iter=100, p=0.5)

        x, y = dpso.run()
        
        ylpt = LPT(constant1 , machine)
        print(y, ylpt)
        r = np.array([y,ylpt])
        
        res[i] = r
        print('第{}轮结束'.format(i+1))

        #print(x)
    print(res)





    #随机生成数据
    np.random.seed()
    num_veh = 30
    workload=np.random.uniform(820,10000,num_veh)
    #print("workloadis\n",workload)
    # #向上取整
    workload=np.ceil(workload)
    # #print("workloadis\n",workload)
    # #roff is  offload#
    # r is task that i need 
    # so r-roff is local 
    roff=np.zeros(num_veh) 
    for i in range(num_veh):
        roff[i]=np.random.uniform(200,workload[i])
        #print('roffis\n',roff)

    rloc=workload-roff

    d=np.random.randint(1, 10, num_veh)
    constant = 
