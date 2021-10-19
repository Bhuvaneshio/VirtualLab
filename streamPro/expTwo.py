import streamlit as st
import matplotlib as mp
import matplotlib.pyplot as plt
import math
import numpy as np
import scipy.io as spio

def showDet():

    #st.set_page_config(page_title='Exp Two', page_icon="👾")

    mat = spio.loadmat('vswr1.mat', squeeze_me=True)
    vswr = mat['vswrant']
    rl = mat['rlant']

    matt = spio.loadmat('vswr2.mat', squeeze_me=True)
    vswrr = matt['vswrant']
    rll = matt['rlant']

    #st.write(vswr)
    #st.write(rl)
    #st.write(vswrr)
    #st.write(rll)

    #myform = st.form(key = "myform1")
    with st.form(key = "myform1"):
        ant = st.selectbox('Select Antenna ',['Log Periodic Dipole Array', 'Yagi-Uda'], key=1)
        submit = st.form_submit_button('Submit')


    x=[1.0]*141
    for i in range(1,141):
        x[i] = x[i-1]+0.1;
        "{:.2f}".format(x[i])
    st.write(x)

    xp=[1.0]*150
    for i in range(1,150):
        xp[i] = xp[i-1]+0.1;
        "{:.2f}".format(xp[i])
    st.write(xp)

    header = st.container()
    features = st.container()
    primary = st.container()
    secondary = st.container()

    with header:
            st.header('VSWR Measurement of LPDA Antenna')
            x1=st.slider('start:', min_value=1.0,max_value=15.0,value=1.0,step=0.1, key="vswr1")
            x2=st.slider('end:', min_value=1.0,max_value=15.0,value=4.0,step=0.1, key="vswr2")
            
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
        xx2=st.slider('end:', min_value=1.0,max_value=15.0,value=4.0,step=0.1, key="rl2")
        
        plt.figure()
        plt.plot(x,rl,'b:')
        plt.xlabel('Frequency (GHz)')
        plt.ylabel('Return Loss (dB)')
        yy = [10]*141
        plt.plot(x,yy,'k-')
        plt.xlim(xx1,xx2)
        plt.show()
        st.pyplot(plt)


    
    with primary:
        st.header('VSWR Measurement of Horn Antenna')
        x1=st.slider('start:', min_value=1.0,max_value=15.0,value=1.0,step=0.1, key="vswr3")
        x2=st.slider('end:', min_value=1.0,max_value=15.0,value=15.0,step=0.1, key="vswr4")
        
        plt.figure()
        st.write(vswrr[1])
        st.write(x[10])
        plt.plot(x,vswrr,'b:')
        plt.xlim(x1,x2)
        plt.xlabel('Frequency (GHz)')
        plt.ylabel('VSWR Magnitude')
        yy1 = [2.5]*141
        plt.plot(x,yy1,'k-')
        plt.show()
        st.pyplot(plt)

    with secondary:
        xx1=st.slider('start:', min_value=1.0,max_value=15.0,value=1.0,step=0.1, key="rl3")
        xx2=st.slider('end:', min_value=1.0,max_value=15.0,value=15.0,step=0.1, key="rl4")
        
        plt.figure()
        plt.plot(xp,rll,'b:')
        plt.xlabel('Frequency (GHz)')
        plt.ylabel('Return Loss (dB)')
        yy = [10]*150
        plt.plot(xp,yy,'k-')
        plt.xlim(xx1,xx2)
        plt.show()
        st.pyplot(plt)

    btn = st.button('Done!')
    if btn:
        st.balloons()