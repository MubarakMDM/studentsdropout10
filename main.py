# Import libraries
import pandas as pd
import streamlit as st
import joblib

model = joblib.load("mypipelineafterfit.pkl")

def predict(data):

    try:
        data.drop(['FinalGrade'], axis = 1, inplace = True) # Excluding target FinalGrade column
    except :
        pass

    predictions = pd.DataFrame(model.predict(data))     
    predictions = predictions.astype('int')
    
    final = pd.concat([predictions, data], axis = 1)     

    return final


def main():  

    st.title("Students dropout Prediction")
    st.sidebar.title("Students dropout Prediction")
    html_temp = """
    <div style="background-color:tomato;padding:10px">
    <h2 style="color:white;text-align:center;">Students dropout Prediction </h2>
    </div>
    
    """
    st.markdown(html_temp, unsafe_allow_html = True)
    st.text("")
    status_variable = 0
    
 
    uploadedFile = st.sidebar.file_uploader("Choose a file", type = ['csv', 'xlsx'], accept_multiple_files = False, key = "fileUploader")
    
    
    if uploadedFile is not None :
        try:

            data = pd.read_csv(uploadedFile)
                     
        except Exception as e :
                try:
                    data = pd.read_excel(uploadedFile)
                   
                except:      
                    data = pd.DataFrame(uploadedFile)
                
    else:
        st.sidebar.warning("You need to upload a csv or excel file.")
    
    result = ""
    
    if st.button("Predict"):         
        result = predict(data)
        import seaborn as sns
        cm = sns.light_palette("blue", as_cmap = True)
        st.table(result.style.background_gradient(cmap = cm))
                           
if __name__=='__main__':
    main()


