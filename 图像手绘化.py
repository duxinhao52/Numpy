from PIL import Image
import numpy as np

#图片数组ndarray对象化，图片黑白化并把元素变成浮点型
a=np.asarray(Image.open("C:/Users/19233/Pictures/5.jpg").convert('L')).astype('float')

depth=10 #设置虚拟深度值(0~100)
grad=np.gradient(a) #获取a的梯度值
grad_x,grad_y=grad
#深度对梯度值的影响
grad_x=grad_x*depth/100
grad_y=grad_y*depth/100
#立体三维下，梯度归一化(新增Z轴梯度值)
A=np.sqrt(grad_x**2+grad_y**2+1.0)
uni_x=grad_x/A
uni_y=grad_y/A
uni_z=1.0/A

vec_el=np.pi/2.2 #光源俯视弧度值
vec_az=np.pi/4.0 #光源方位弧度值
dx=np.cos(vec_el)*np.cos(vec_az) #光源对x轴的影响
dy=np.cos(vec_el)*np.sin(vec_az) #光源对y轴的影响
dz=np.sin(vec_el)                #光源对z轴的影响

b=255*(dx*uni_x+dy*uni_y+dz*uni_z) #梯度，光源的影响因子还原灰度值
b=b.clip(0,255) #删除越界的灰度值

im=Image.fromarray(b.astype('uint8'))   #以uint8重构图像
im.save('C:/Users/19233/Pictures/6.jpg')   #保存
