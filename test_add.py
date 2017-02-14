# numpy to Tensor
import numpy as np
import torch 
a = np.ones(5)
b = torch.from_numpy(a)
np.add(a, 1, out=a)
print(a) # 如果a 变的话， b也会跟着变，说明b只是保存了一个地址而已，并没有深拷贝
print(b)# Variable只是保存Tensor的地址，如果Tensor变的话，Variable也会跟着变


