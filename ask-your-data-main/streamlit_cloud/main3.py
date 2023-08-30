import streamlit as st
import openai
import requests
import base64
#from sqlalchemy import create_engine
import os
import pytz
#import pymysql
#from urllib.parse import quote_plus
import matplotlib
import matplotlib.pyplot as plt
from pandasai import PandasAI
import pandas as pd
from pandasai.llm.openai import OpenAI
#from configuration/apikey import apikey
#from mysql_config import user,pwd,db,host
import csv
import datetime
import streamlit_authenticator as stauth
#print(user,pwd,db,host)

#matplotlib.use("TkAgg")
from pathlib import Path
current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
#from current_dir/configuration/"githubkey.py" import gitapikey
#print(gitapikey)
def main():
    #def logout():
    #    st.session_state.clear()
    #    authenticator.logout('Logout', 'main')
        
    #    write_login_to_csv(operation = "Log out", username=username,gitapikey)
        
    def profit_retailer(df):
        
        profit = df.groupby('retailer')['operating_profit'].sum()
        st.markdown("<h6 style='text-align: center; color: black;'>Total Operating Profit by Retailer </h6>", unsafe_allow_html=True)
        st.bar_chart(data=profit)
    def sales_region(df):
        
        sales = df.groupby('region')['total_sales'].sum()
        st.markdown("<h6 style='text-align: center; color: black;'>Total Sales by Region </h6>", unsafe_allow_html=True)
        st.bar_chart(data=sales)
    def units_sold_product(df):
        
        unit_sold = df.groupby('product')['units_sold'].sum()
        st.markdown("<h6 style='text-align: center; color: black;'>Total Units Sold by Product </h6>", unsafe_allow_html=True)
        st.bar_chart(data=unit_sold)
    def margin_retailer(df):
        margin = df.groupby('retailer')['operating_margin'].mean()
        st.markdown("<h6 style='text-align: center; color: black;'>Average Margin by Retailer </h6>", unsafe_allow_html=True)
        st.bar_chart(data=margin)
    def revenue_industry(df):
        revenue = df.groupby('industry')['revenue_usd_millions'].mean()
        st.markdown("<h6 style='text-align: center; color: black;'>Average revenue(usd millions) by Industry </h6>", unsafe_allow_html=True)
        st.bar_chart(data=revenue)
    def employees_industry(df):
        employee = df.groupby('industry')['employees'].mean()
        st.markdown("<h6 style='text-align: center; color: black;'>Average no of employees by Industry </h6>", unsafe_allow_html=True)
        st.bar_chart(data=employee)
    def revenue_company(df):
        filterdf=df[df['rank']<6][['name','revenue_usd_millions']]
        st.markdown("<h6 style='text-align: center; color: black;'>Revenue for top 5 US Companies </h6>", unsafe_allow_html=True)
        st.bar_chart(data=filterdf,x='name',y='revenue_usd_millions')

    def employees_company(df):
        filterdf=df[df['rank']<6][['name','employees']]
        st.markdown("<h6 style='text-align: center; color: black;'>No of employees for top 5 US Companies </h6>", unsafe_allow_html=True)
        st.bar_chart(data=filterdf,x='name',y='employees')
    def visualize_kpi_by_site(kpi_name,gpr_df):
        
        df=gpr_df
        kpi_data = df[df['kpi_name_w_subtypes'] == kpi_name]
        kpi_by_site = kpi_data.groupby('site_name')['kpi_value'].mean()
        text=f'Average {kpi_name} Value by Site'
        st.markdown("<h6 style='text-align: center; color: black;'>Average Accuracy Value by Site </h6>", unsafe_allow_html=True)
        st.bar_chart(data=kpi_by_site) 

    def visualize_kpi_by_region(kpi_name,gpr_df):
        
        df = gpr_df
        kpi_data = df[df['kpi_name_w_subtypes'] == kpi_name]
        kpi_by_region = kpi_data.groupby('region')['kpi_value'].mean()
        st.markdown("<h6 style='text-align: center; color: black;'>Average Accuracy Value by Region </h6>", unsafe_allow_html=True)
        st.bar_chart(data=kpi_by_region)

    def kpi_vs_goal_regionwise(gpr_df):
        df = gpr_df
        kpi_vs_goal = df.groupby('region')['kpi_value_vs_goal'].mean()
        st.markdown("<h6 style='text-align: center; color: black;'>Average kpi value vs goal by Region </h6>", unsafe_allow_html=True)
        st.bar_chart(data=kpi_vs_goal)
    def work_status(gpr_df):
        df = gpr_df
        kpi_work_site = df.groupby('work_site_status')['kpi_value'].mean()
        st.markdown("<h6 style='text-align: center; color: black;'>Average kpi value for different work status </h6>", unsafe_allow_html=True)
        st.bar_chart(data=kpi_work_site)
    def write_login_to_csv(operation, username, gitapikey):
        now = datetime.datetime.now()
        timestamp = now.strftime("%Y-%m-%d %H:%M:%S")
        with open(current_dir/"login_details.csv", mode="a", newline="") as file:
             writer = csv.writer(file)
             writer.writerow([username, operation, timestamp])
        #ist_timezone = pytz.timezone('Asia/Kolkata')
        #current_time_ist = datetime.datetime.now(ist_timezone)
        #timestamp = current_time_ist.strftime("%Y-%m-%d %H:%M:%S")
        #api_url="https://api.github.com/repos/shwetabhattad/askyourdata/contents/streamlit_cloud/login_details.csv"
        #api_url = f"https://api.github.com/repos/Gkannan03/google-bard-ai/contents/TaskGPT-Google_PaLM/Log_details/login_details.csv"
        #github_token = gitapikey
        #headers = {
        #"Authorization": f"Bearer {github_token}"
        #}
        #response = requests.get(api_url, headers=headers)
        #file_data = response.json()

        #raw_content_url = file_data["download_url"]
        #response = requests.get(raw_content_url)
        #current_content = response.text

        #new_data = f"{operation},{username},{timestamp}\n"
        #new_content = current_content + new_data
        #new_content_encoded = base64.b64encode(new_content.encode("utf-8")).decode("utf-8")
        #commit_message = "Update login details in CSV"
        #payload = {
        #"message": commit_message,
        #"content": new_content_encoded,
        #"sha": file_data["sha"]
        #}

        #response = requests.put(api_url, json=payload, headers=headers)
        #if response.status_code == 200:
        #   print("Data successfully written to the CSV file on GitHub.")
        #else:
        #   print("Failed to update data in the CSV file.")
    st.set_page_config(page_title= 'Ask Your Data - TaskGPT', layout="wide")
    names = ['Join Prime','Join Walmart plus','shweta','aravind','manish','kannan','abdul','aastha','deepika','abhilash','yahya','sangeetha','praveen','shubham','ralph']
    usernames = ['amazon','walmart','shweta.bhattad@taskus.com','aravind.ramesh@taskus.com','manish.pandya@taskus.com','kannan.g@taskus.com',
 'abdul.p@taskus.com','aastha.gour@taskus.com','deepika.s@taskus.com','abhilash.kanimilli@taskus.com','yahya.hussain@taskus.com','sangeetha.yesurajan@taskus.com','praveenkumar@taskus.com','shubham.singh04@taskus.com','ralph.almeida@taskus.com']
    passwords = ['amazonpay','phonepe','shweta','aravind','manish','kannan','abdul','aastha','deepika','abhilash','yahya','sangeetha','praveen','shubham','ralph']
    hashed_passwords = stauth.Hasher(passwords).generate()
    authenticator = stauth.Authenticate(names,usernames,hashed_passwords,'some_cookie_name','some_signature_key',cookie_expiry_days=0)
    name, authentication_status, username = authenticator.login('Login', 'main')
    #names = ['kannan G','Aravind']
    #usernames = ['kannan.g@taskus.com','aravind.ramesh@taskus.com']
    #passwords = ['Taskus123','TaskUs@123'] 
    #hashed_passwords = stauth.Hasher(passwords).generate()
    #authenticator = stauth.Authenticate(names,usernames,hashed_passwords,'some_cookie_name','some_signature_key',cookie_expiry_days=0)
    #name, authentication_status, username = authenticator.login('Login', 'main')
    if st.session_state["authentication_status"]:
        #st.button('Logout', on_click=logout)
        st.write("Welcome!!")
        
        #st.title("Ask Your Data - TaskGPT")
        st.title("Ask Your Data - TaskGPT")
        #os.environ['OPENAI_API_KEY'] = apikey
        col1, col2 = st.columns([1, 2])
        with col1:
            option = st.selectbox("Select the data source", ["Gpr Frontier Data","Largest US Companies","Adidas Sales Data"], key="selectbox")
        with col2:
            st.write("")  
        if option=="Gpr Frontier Data":
            #print('here')
            #engine = create_engine(f"mysql+pymysql://{user}:%s@{host}/{db}" % quote_plus(pwd))
            #cnx=engine.connect()
            #print('connection_done')
            #gpr_df = pd.read_sql_table('gpr_frontier_data', cnx)
            gpr_df=pd.read_csv(current_dir/"frontier_data.csv")
         
            print(gpr_df.head())
            #cnx.close()
            #engine.dispose()
            col1, col2= st.columns([1.5, 1.5])
            with col1:
                visualize_kpi_by_site("Accuracy",gpr_df)
            with col2:
                visualize_kpi_by_region("Accuracy",gpr_df)
            col3,col4 = st.columns([1.5, 1.5])
            with col3:
                kpi_vs_goal_regionwise(gpr_df)
            with col4:
                work_status(gpr_df)
            # Display Data Head
            st.write("Data Preview:")
            st.dataframe(gpr_df.head(3)) 
            st.write("Help Questions: ")
            st.write("What is the average of Numerator where lob is ALE")
            st.write("What is the work site status of the highest Numerator value")
            st.write("Plot the histogram of Numerator")
            st.write("What is the Month Year which has the highest KPI value where region is SEA")
            apikey = st.text_input("Openaiapikey:")
            gitapikey=st.text_input("Gitapikey:")
            question = st.text_input("Question:")
            
            if question and apikey and gitapikey:
                print(question)
                write_login_to_csv(question, username,gitapikey)
                plt.ion()
                llm = OpenAI(api_token=apikey)
                pandas_ai = PandasAI(llm)
                #graphContinueExecutionText = " Use plt.show(block = false)"
                #question += graphContinueExecutionText
                answer = pandas_ai.run(gpr_df,question)
                if type(answer)==str:
                    st.write(answer)

        elif option=='Largest US Companies':
            print('here')
            #engine = create_engine(f"mysql+pymysql://{user}:%s@{host}/{db}" % quote_plus(pwd))
            #cnx=engine.connect()
            #print('connection_done')
            #usdf = pd.read_sql_table('us_data', cnx)
            usdf=pd.read_csv(current_dir/"us_comp.csv")
            print(usdf.head())
            #cnx.close()
            #engine.dispose()
            col1, col2= st.columns([1.5, 1.5])
            with col1:
                revenue_industry(usdf)
            with col2:
                employees_industry(usdf)
            col3,col4 = st.columns([1.5, 1.5])
            with col3:
                revenue_company(usdf)
            with col4:
                employees_company(usdf)
            # Display Data Head
            st.write("Data Preview:")
            st.dataframe(usdf.head(3)) 
            st.write("Help Questions: ")
            st.write("Which company has the first rank")
            st.write("Which company has highest number of employees")
            st.write("Plot the histogram of revenue growth")
            st.write("Show the data where industry is healthcare")
            apikey = st.text_input("Openaiapikey:")
            gitapikey=st.text_input("Gitapikey:")
            question = st.text_input("Question:")
            if question and apikey and gitapikey:
                print(question)
                write_login_to_csv(question, username,gitapikey)
                llm = OpenAI(api_token=apikey)
                pandas_ai = PandasAI(llm)
                answer = pandas_ai.run(usdf,question)
                st.write(answer)
        elif option=='Adidas Sales Data':
            print('here')
            #engine = create_engine(f"mysql+pymysql://{user}:%s@{host}/{db}" % quote_plus(pwd))
            #cnx=engine.connect()
            #print('connection_done')
            #addf = pd.read_sql_table('adidas_data', cnx)
            addf=pd.read_csv(current_dir/"adidas_us_sales.csv")
            print(addf.head())
            #cnx.close()
            #engine.dispose()
            col1, col2= st.columns([1.5, 1.5])
            with col1:
                profit_retailer(addf)
            with col2:
                sales_region(addf)
            col3,col4 = st.columns([1.5, 1.5])
            with col3:
                units_sold_product(addf)
            with col4:
                margin_retailer(addf)
            # Display Data Head
            st.write("Data Preview:")
            st.dataframe(addf.head(3)) 
            st.write("Help Questions: ")
            st.write("Which retailer has the highest profit")
            st.write("Which retailer has sold highest number of products")
            st.write("What is the average profit")
            st.write("What is the total number of units sold")
            apikey = st.text_input("Openaiapikey:")
            gitapikey=st.text_input("Gitapikey:")
            question = st.text_input("Question:")
            if question and apikey and gitapikey:
                print(question)
                write_login_to_csv(question, username,gitapikey)
                llm = OpenAI(api_token=apikey)
                pandas_ai = PandasAI(llm)
                answer = pandas_ai.run(addf,question)
                st.write(answer)        
    elif st.session_state["authentication_status"] == False:
        st.error('Username/password is incorrect')
    elif st.session_state["authentication_status"] == None:
        st.warning('Please enter your username and password')    
if __name__ == "__main__":
    main()
