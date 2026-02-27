import numpy as np
a=np.array([2,3,4,5])
b = np.array([8, 5, 4])
c = np.array([5, 4, 6, 8, 3])
ax,bx,cx=np.ix_(a,b,c)
print("ax",ax)
print("bx",bx)
print("cx",cx)
print("Shape of ax:",ax.shape)
print("Shape of bx:",bx.shape)
print("Shape of cx:",cx.shape)
result=ax+bx*cx
print("\nResult:\n",result)
print("result[3,2,4]",result[3,2,4])
result2=a[3]+b[2]*c[4]
print("result2=",result2)