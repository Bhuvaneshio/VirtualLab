import streamlit as st
import matplotlib as mp
import matplotlib.pyplot as plt
import math
import numpy as np
import scipy.io as spio

st.set_page_config(page_title='Exp Two')

mat = spio.loadmat('vswr1.mat', squeeze_me=True)
vswr = mat['vswrant']
rl = mat['rlant']

st.write(vswr)
st.write(rl)
x=[1.0]*141
for i in range(1,141):
    x[i] = x[i-1]+0.1;
    "{:.2f}".format(x[i])
st.write(x)
header = st.container()
features = st.container()
secondary = st.container()

with header:
    st.header('VSWR Measurement of LPDA Antenna')
    x1=st.slider('start:', min_value=1.0,max_value=15.0,value=1.0,step=0.1, key="vswr1")
    x2=st.slider('end:', min_value=1.0,max_value=15.0,value=15.0,step=0.1, key="vswr2")
    
    plt.figure()
    st.write(vswr[1])
    st.write(x[10])
    plt.plot(x,vswr,'b:')
    plt.xlim(x1,x2)
    plt.xlabel('Frequency (GHz)')
    plt.ylabel('VSWR Magnitude')
    yy1 = [2.5]*141
    plt.plot(x,yy1,'k-')
    plt.show()
    st.pyplot(plt)

with features:
    xx1=st.slider('start:', min_value=1.0,max_value=15.0,value=1.0,step=0.1, key="rl1")
    xx2=st.slider('end:', min_value=1.0,max_value=15.0,value=15.0,step=0.1, key="rl2")
    
    plt.figure()
    plt.plot(x,rl,'b:')
    plt.xlabel('Frequency (GHz)')
    plt.ylabel('Return Loss (dB)')
    yy = [10]*141
    plt.plot(x,yy,'k-')
    plt.xlim(xx1,xx2)
    plt.show()
    st.pyplot(plt)

