import streamlit as st
from PIL import Image
import matplotlib as mp
import matplotlib.pyplot as plt
import math
import numpy as np
import scipy.io as spio
def showDet():
    img1 = Image.open("functionGenerator.png")
    img2 = Image.open("cable.png")
    img3 = Image.open("lpda.png")
    img4 = Image.open("vswrbridge.png")
    img5 = Image.open("cro.png")


    img = Image.open("circuit.png")

    st.subheader("Apparatus required:")

    colu1, colu2, colu3, colu4, colu5 = st.columns([3,1,3,1,3])

    with colu1:
        result= st.checkbox("Network Analyzer")
        result2 = st.checkbox("Cables")
        result3 = st.checkbox("LPDA Antenna")
        result4 = st.checkbox("VSWR Bridge")
        result5 = st.checkbox("CRO")
        
        st.markdown('#')
        done = st.button("Done")

    with colu3:
        row1= st.container()
        row2= st.container()
        row3= st.container()
        if result:
            with row1:
                st.image(img1, width = 100)
        if result2:
            with row2:
                st.image(img2, width = 100)
        if result3:
            with row3:
                st.image(img3, width = 100)

    with colu5:
        row4= st.container()
        row5= st.container()
        
        if result4:
            with row4:
                st.image(img4, width = 100)
        if result5:
            with row5:
                st.image(img5, width = 100) 
        

    st.markdown('#')

    

    if done:
        if result5 :
            st.warning("Wrongly choosen apparatus")
        else:    
            st.subheader("Set-up:")
            st.success("Apparatus are choosen correctly")
            st.image(img, width = 600)
            st.balloons()
