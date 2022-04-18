import pickle
import streamlit as st
import pandas as pd
file_path = 'C:\\Users\\HP\\OneDrive\\Desktop\\Housing Pred\\Pred_Model.pkl'

with open(file_path,'rb') as f:
    loaded_model = pickle.load(file_path)
    
    
def prediction(data):
    
    return loaded_model.predict(data)

def main():
    
    st.title("House Price Prediction")
    
    
    a = st.text_input("Enter the Class of the house")
    b = st.text_input("Enter the Lot Area")
    c = st.text_input("Enter the Overall Qual")
    d = st.text_input("Enter the BSmt Quality")
    e = st.text_input("Enter the Total BSMT SF")
    f = st.text_input("Enter the 2nd floor SF")
    g = st.text_input("Enter the Bsmt Bathroom")
    h = st.text_input("Enter the full_bath")
    i = st.text_input("Enter the No of Fireplace")
    j = st.text_input("Enter the no of years old")
    k = st.text_input("Enter the Lot Frontage")
    l = st.text_input("Enter the BSMT Sf 1")
    m = st.text_input("Enter the total Bsmt area")
    n = st.text_input("Enter the total rooms")
    o = st.text_input("Enter the Garage cars")
    
    result = ''
    
    if st.button('Predict'):
        prediction([[a,b,c,d,e,f,g,h,i,j,k,l,m,n,o]])
        
    st.success(result)
    
if __name__ == '__main__':
    main()
        
    