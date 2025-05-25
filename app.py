from streamlit as st

st.title("CrewAI Powered Customer Support Agents")

query = st.text_input("Enter your query here")

if(query) : 
    pass
    # Goal : to handle various customer service requests, such as order status inquiries, return processing and personalized product recommendations.
    # need what type of query it is ; we need to categorize our query
    # Tasks : based on the query we need to track order, track return, provide recommendations
    # Agents : we need agents for all the mentioned tasks
    # Tools : since all our data is offline, and doesn't need calculations
    # i don't believe we require any tools apart from reading the csv files from sample folder
    # Process : sequential should work since problem statement is easy
    