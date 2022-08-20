# -*- coding: utf-8 -*-
"""
Created on Sat Aug 20 15:09:48 2022

@author: Hammad khan
"""

import streamlit as st
import pandas as pd

def main():
    st.title('AirPassengers Analysis')
    data = pd.read_csv('AirPassengers.csv')
    data['Year']= data['Month'].apply(lambda X: X.split('-')[0])
    year = st.selectbox('Select Year', data['Year'].unique())
    button=st.button('Show results')
    if button:
        subset = data[data['Year'] == year]
        st.table(subset)
        
    
if __name__=='__main__':
    main()
