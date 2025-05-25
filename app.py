import streamlit as st
from src.tasks import cust_tasks_obj
from src.agents import agents_lst
from crewai import Crew, Process

st.title("CrewAI Powered Customer Support Agents")

query = st.text_input("Enter your query here")

# Goal : to handle various customer service requests, such as order status inquiries, return processing and personalized product recommendations.
    # need what type of query it is ; we need to categorize our query
    # Tasks : based on the query we need to track order, track return, provide recommendations
    # Agents : we need agents for all the mentioned tasks
    # Tools : since all our data is offline, and doesn't need calculations
    # i don't believe we require any tools apart from reading the csv files from sample folder
    # Process : sequential should work since problem statement is easy
if query:
    Customer_Query_catergorize = cust_tasks_obj.categorize_query(query=query)
    Track_Orders = cust_tasks_obj.track_order_details(query=query)
    Track_Returns = cust_tasks_obj.track_returns_details(query=query)
    prod_recom = cust_tasks_obj.prod_recommendation_details(query)

    tasks_lst = [
        Customer_Query_catergorize,
        Track_Orders,
        Track_Returns,
        prod_recom
    ]

    crew = Crew(
        agents=agents_lst,
        tasks=tasks_lst,
        process=Process.sequential,
        verbose=True,
        full_output=True
    )
    print('starting kickoff\n')
    result = crew.kickoff()

    # Optional: Debug full result
    # st.json(result)

    # Extract task outputs
    outputs = result["tasks_output"]
    category_raw = outputs[0]["output"]  # Task 1: categorizer
    order_response = outputs[1]["output"]  # Task 2: order tracking
    return_response = outputs[2]["output"]  # Task 3: return tracking
    recommendation_response = outputs[3]["output"]  # Task 4: recommendations

    # Strip quotes or whitespace if necessary
    category = category_raw.strip().strip("'\"")

    # Display result based on category
    st.subheader(f"Query Category: {category}")
    if category == 'order_tracking':
        st.markdown(f"### Order Details\n{order_response}")
    elif category == 'returns_request':
        st.markdown(f"### Return Details\n{return_response}")
    elif category == 'prod_recommendations':
        st.markdown(f"### Product Recommendations\n{recommendation_response}")
    else:
        st.markdown("### Could not categorize the query. Please try again with a different question.")
