# Joseph Rice
from __future__ import division
from visual import *
scene.width =1000
scene.height =2000
G = 6.67e-11
delta = 2.6e6
earth=sphere(pos=vector(2.5e12,0,0),radius=100000000000,color=color.red,make_trail=True,trail_type='points',\
meterial=materials.emissive)

comit = sphere(pos=vector(-2e12,0,0),radius=100000000000,color=color.green,make_trail=True)
sun =sphere(pos=vector(0.1,0,0),radius=3e11,color=color.white,meterial=materials.earth)
sun.material=materials.earth
earth.mass =6e12
sun.mass = 20e24
comit.mass = 6e12
comit.p = vector(0,-1.5e14,0)
earth.p = earth.mass*vector(0,25,0)
sun.p = sun.mass*vector(0,0,0)
delta = 5e9

def Total_grave(object,object2,object3):

    if object3 ==0:
        Relative_pos_1 = object.pos - object2.pos
        R1hat = Relative_pos_1/mag(Relative_pos_1)
        F_net_ob_ob2= (-(G*object.mass*object2.mass)/(mag(Relative_pos_1))**2)*R1hat
        return F_net_ob_ob2
    
    else:
        Relative_pos_1 = object.pos - object2.pos
        Relative_pos_2 = object.pos - object3.pos
        R1hat = Relative_pos_1/mag(Relative_pos_1)
        R2hat = Relative_pos_2/mag(Relative_pos_2)
        F_net_ob_ob2= (-(G*object.mass*object3.mass)/(mag(Relative_pos_2))**2)*R2hat
        F_net_ob_ob1 =(-(G*object.mass*object2.mass)/mag(Relative_pos_1)**2)*R1hat
        F_net = F_net_ob_ob2 + F_net_ob_ob1
        return F_net


force = Total_grave(earth,sun,comit)
t = 0
while True:
    rate(100)


    R_e = earth.pos - sun.pos

    rhat = R_e/mag(R_e)
    F_net = Total_grave(earth,sun,comit)
    F_net_comit = Total_grave(comit,sun,earth)

    F_net_2 = -F_net
    comit.p = comit.p + F_net_comit*delta
    earth.p = earth.p + F_net*delta
    F_sun = Total_grave(sun,earth,comit)
    sun.p = sun.p + F_sun*delta


    earth.pos = earth.pos + (earth.p/earth.mass)*delta
    sun.pos = sun.pos + (sun.p/sun.mass)*delta
    comit.pos = comit.pos + (comit.p/comit.mass)*delta
    t = t +  delta
    print(sun.pos)
