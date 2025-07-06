x=int(input("Enter the first valve:"))
y=int(input("Enter the second valve:"))
z=x+y
t=x-y
h=x*y
j=x/y
print("the sum is:",z)
print("the difference is:",t)
print("the mutipliyed is:",h)
print("the divided valve is:",j)
g,l=2,6
g,l=l,g+2
print(g,l)
print(type(j))
b=(10+3==13)
print(b)
k=int(input("Enter the first valve:"))
if(k==9):
    print("k=",k, "is even")
else:
    print ("its odd:")
o=int(input("enter the valve:"))
i=int(input("enter the valve:"))
t=o
o=i
i=t
print(o,i)
import numpy as np
import IPython.display as display
from matplotlib import pyplot as plt
import io
import base64

ys = 200 + np.random.randn(100)
x = [x for x in range(len(ys))]

fig = plt.figure(figsize=(4, 3), facecolor='w')
plt.plot(x, ys, '-')
plt.fill_between(x, ys, 195, where=(ys > 195), facecolor='g', alpha=0.6)
plt.title("Sample Visualization", fontsize=10)

data = io.BytesIO()
plt.savefig(data)
image = F"data:image/png;base64,{base64.b64encode(data.getvalue()).decode()}"
alt = "Sample Visualization"
display.display(display.Markdown(F"""![{alt}]({image})"""))
plt.close(fig)

