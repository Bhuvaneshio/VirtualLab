import streamlit as st
import matplotlib as mp
import matplotlib.pyplot as plt
import math
import numpy as np

st.set_page_config(page_title='Exp One')

header = st.container()
features = st.container()
secondary = st.container()

with header:
    st.header('Microstrip Patch Antenna')

    freq = st.slider('Frequency ? (GHz)', min_value=1.0, max_value=15.0, value=4.0, step=0.1)
    er = st.slider('Di-electric constant ?', min_value=2.0, max_value=12.0, value=2.4, step=0.1)
    h = st.slider("Height (mils) ?", min_value=0.1, max_value=15.0, value=3.0, step=0.1)

    height = h/1000*2.54
    Width=30.0/(2.0*freq)*math.sqrt(2.0/(er+1.0))*10
    ereff=(er+1.0)/2.0+(er-1)/(2.0*math.sqrt(1.0+12.0*height/Width))
    dl=0.412*height*((ereff+0.3)*(Width/height+0.264))/((ereff-0.258)*(Width/height+0.8))
    lamda=30.0/(freq*math.sqrt(ereff))
    lamda0=30.0/freq
    Leff=lamda/2
    L=Leff-2*dl

    st.write(L)
    st.write(Width)

    Length = L*10
    k0=2*math.pi*freq/30
    phi1=np.linspace(0,360,360)
    theta1=np.linspace(0,180,180)
    phi=np.multiply(phi1/180,math.pi)
    theta=np.multiply(theta1/180,math.pi)

    Rr=120*lamda0/(1-((height*height*k0*k0)/24));

    st.write(Rr)    

    Etheta = np.sin(k0*(height/2)*np.cos(theta))*np.cos(k0*(L/2)*np.cos(theta))/k0/height*(2/np.cos(theta))
    Ethetamax=max(Etheta)
    Ethetanor=np.divide(Etheta,Ethetamax)
    
    st.write('Stage 1 clear')
    
    Ephi=np.sin(k0*(Width/2)*np.cos(phi))*np.sin(phi)/k0/Width*(2/np.cos(phi));
    Ephimax=max(Ephi)
    Ephinor=np.divide(Ephi,Ephimax)

    st.write('Stage 2 clear')


with features:

    st.header('Radiation Plot of E and H plane patterns')
    plt.figure()
    plt.polar(theta,Ethetanor,'-r', label="E plane")
    plt.polar(phi,Ephinor,'-b', label="H Plane")
    plt.ylim(0,1)
    plt.legend(loc='lower center', ncol=2, facecolor='yellow')
    plt.show()
    st.pyplot(plt)

with secondary:
    y1 = st.slider('min value ?', min_value=0.0, max_value=6.0, value=0.0, step=0.1)
    y2 = st.slider('max value ?', min_value=1.0, max_value=6.0, value=6.0, step=0.1)
    plt.figure()
    plt.plot(theta,Ethetanor,'-r', label="E plane")
    plt.plot(phi,Ephinor,'-b', label="H Plane")
    #ax = plt.gca()
    #ax.set_ylim([y1,y2])
    plt.xlim(y1,y2)
    plt.show()
    st.pyplot(plt)