# opt-lib
Optimization methods I have used

### 1. discrete particle swarm optimization algorithm (DPSO)

#### 1.1使用说明

```
dpso = DPSO(func, constant= constant, ndim = ndim, machine = num_veh,  pop =100, max_iter=100, p=0.1)
    x, y = dpso.run()
    
```

| 参数     | 意义                                                        |
| -------- | ----------------------------------------------------------- |
| func     | 极小化函数, 运行起来是 fun(x, constant), 要支持**矩阵运算** |
| constant | 变量的特征, 也就是在运行过程中不变的量                      |
| ndim     | 作业的数量                                                  |
| machine  | 机器的数量                                                  |
| pop      | 种群数量                                                    |
| max_iter | 迭代次数                                                    |
| p        | 接受改变的概率, 越大则保留变异( 染色体交叉 )的概率越大      |


$$
V_{k}^{t+1}=V_{k}^{t} \stackrel{+}{\mathrm{O}}\left(\left(R_{1} \stackrel{\times}{\mathrm{O}}^{}\left(P_{k}^{t} \overline{\mathrm{O}} X_{k}^{t}\right)\right) \stackrel{+}{\mathrm{O}}\left(R_{2} \stackrel{\times}{\mathrm{O}}^{}\left(P_{g}^{t} \overline{\mathrm{O}} X_{k}^{t}\right)\right)\right)
$$

$$
X_{k}^{t+1}=X_{k}^{t} \stackrel{\times}{O} V_{k}^{t+1}
$$

出处: 

**A discrete particle swarm optimization algorithm for scheduling parallel machines**

#### 1.2 Demo

```
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

constant = [[1,1,2,3,1]]


dpso = DPSO(minC, constant= constant1, ndim = ndim, machine = machine,  pop =100, max_iter=100, p=0.5)

x, y = dpso.run()
```



#### 1.2 operator-   

```
#两个元素相减, 不为零的位置 放入 前操作数
a = np.array([[1, 2, 2, 1, 1], [1, 2, 2, 1, 1]])
b = np.array([[1, 1, 2, 2, 1], [1, 1, 2, 2, 1]])

c = a  - b
nz = np.nonzero(c)
c[nz] = b[nz]
print(c)


'''
[[0 1 0 2 0]
 [0 1 0 2 0]]
'''
```

#### 1.3 operator *

```
# 逐元素相乘
c = a*b
```

#### 1.4 operator +

```
#随机生成两个点, 将其分为三部分, 也就是染色体交叉
# operator+ 随机选择两个位置(切点)，并在这两个位置之间交换维数
a = np.array([0, 1, 0, 1, 0])
b = np.array([1, 1, 2, 2, 1])

ndim = 5
m = np.random.randint(1,ndim-1)
n = np.random.randint(1,ndim-1)
while(m == n):
    n = np.random.randint(1,ndim-1)
print(m,n )
if(m > n):
    m = m + n
    n = m - n
    m = m - n
print(m,n)

flag1 = np.random.randint(1,3)
flag2 = np.random.randint(3,5)
flag3 = np.random.randint(5,7)
res = np.ones(ndim)
if(flag1 % 2 ==1):
    #使用第一条染色体
    res[ 0: m] = a[ 0: m]
else:
    res[ 0: m] = b[ 0: m]

if(flag2 % 2 ==1):
    #使用第一条染色体
    res[ m: n] = a[ m: n]
else:
    res[ m: n] = b[ m: n]

if(flag3 % 2 ==1):
    #使用第一条染色体
    res[n: ] = a[ n: ]
else:
    res[ n: ] = b[ n: ]
    
print(res)
```

 

### 2 Dwarf Mongoose Optimization Algorithm( DMO )

![image-20220928165132834](https://i0.hdslb.com/bfs/album/526f4d5dbf1c70844fd3dfbdc89efb3e1a7a5d19.png)

> begin 
>
> Initialize the algorithm parameters:
> [peep]
> Initialize the mongoose populations (search agents): $n$
> Initialize the number of babysitters: $b s$
> Set $n=n-b s$
> Set babysitter exchange parameter $L$
>
> For iter=1: max_iter 
    > Calculate the fitness of the mongoose 
    > Set time counter $C$
    > Find the alpha based on Equation 3
    >
    > $$\alpha=\frac{f i t_i}{\sum_{i=1}^n f i t_i}$$
    > produce a candidate food position using Equation 4
    >
    > $$\boldsymbol{X}_{i+\mathbf{1}}=X_i+p h i * \text { peep }$$
    > Evaluate new fitness of $\boldsymbol{X}_{i+\mathbf{1}}$Evaluate sleeping mound using equation 5
    >
    > $$s m_i=\frac{f i t_{i+1}-f i t_i}{\max \left\{\left|f i t_{i+1}, f i t_i\right|\right\}}$$
    > Compute the average value of the sleeping mound found using Equation 6.
    >
    > $$\varphi=\frac{\sum_{i=1}^n s m_i}{n}$$
    > Compute the movement vector using 
    > $$\overrightarrow{\boldsymbol{M}}=\sum_{i=1}^n \frac{X_i \times s m_i}{X_i}$$
    > Exchange babysitters if $C \geq L$, and set 
    > Initialize bs position (Equation 1) and calculate fitness $f i t_i \leq \alpha$
    > Simulate the scout mongoose next position using Equation 7.
    > $$\begin{equation}
    > \boldsymbol{X}_{i+1}=\left\{\begin{array}{lcc}
    > X_i-C F * \text { rand } *\left[X_i-\overrightarrow{\boldsymbol{M}}\right] & \text { if } \varphi_{i+1}>\varphi_i & \text { Exploration } \\
    > X_i+C F * \text { rand } *\left[X_i-\overrightarrow{\boldsymbol{M}}\right] & \text { else } & \text { Exploitation }
    > \end{array}\right.
    > \end{equation}$$
>
> End For 
> Return best solution 
> End

Notes:

-  led by an alpha pair( 一对alpha  )
- In the mongoose family, the females outrank the males, and the young outrank their older siblings in each age group. 



#### 种群初始化

X = x^{n*d}

xi, j = unifrnd(V arMin, V arMax, V arSize)

VarSize is the size of decision variables or dimensions of the problem.


$$
\alpha=\frac{f i t_i}{\sum_{i=1}^n f i t_i}
$$
The number of mongooses in the alpha group corresponds to the n − bs. Where bs is the number of babysitters





python matlab2python.py Sphere.m -o Sphere.py
