from crewai import Task
from src.agents import categorizer_agent,order_tracking_agent,returns_tracking_agent,Prod_recommendation_agent 

class CustomTasks() : 
    def categorize_query (self, query) : 
        return Task(
            description = f"""
            Conduct a comprehensive analysis of the Query provided and categorize into \\
            one of the following categories:
            order_tracking - used when someone is asking for information about shipment of their orders \\
            returns_request - used when someone is enquiring about returns process \\
            prod_recommendations - used when someone is asking for recommendations on product \\
            off_topic when it doesnt relate to any other category 

            Customer Query:\n\n {query} \n\n
            Output a single cetgory only""",

            expected_output="""A single categtory for the type of customer query from the types ('order_tracking', 'returns_request', 'prod_recommendations', 'off_topic') \\
            eg:
            'order_tracking' 
            """, 

            output_file = f"Query_category.txt", 
            agent = categorizer_agent,
        )

    def track_order_details(self, query):
        return Task(
            description=f"""Conduct a comprehensive analysis of the query provided and the category 
            provided from categorizer_agent 
            if the category provided is order_tracking then 
            search the order_details_data file from context provided to find info needed to respond to the customer query
            You should never include any information that is not available in context
            Customer Query:\n\n {query} \n\n
            Category :\n\n
            """,
            expected_output="""A well crafted Response for the customer that consits of below details:
            Current status of the order: 
            Order Date:
            Estimated delivery date: 
            sign of with Sales Manager
            """,
            context = [self.categorize_query(query)],
            output_file=f"order_details.txt",
            agent=order_tracking_agent
            )

    def track_returns_details(self, query):
        return Task(
            description=f"""Conduct a comprehensive analysis of the query provided and the category 
            provided from categorizer_agent 
            if the category provided is returns_request then 
            and search the file provided in the context to find info needed to respond to the customer query
            You should never include any information that is not available in context 
            Customer Query:\n\n {query} \n\n
            Only provide the info needed """,
            expected_output="""A well crafted Response for the customer to Provide Returns Details which includes 
            1. Return Eligibility :
            2. Return Reason :
            3. Return Instruction :  
            If the Customer is Eligible then provide the Return Eligibility & Return Instruction. 
            If Customer is not eligible then politely craft response that they are not eligible 
            due to Return Reason & Return Instruction and sign of with Sales Manager
            """,
            context = [self.categorize_query(query)],
            output_file=f"return_details.txt",
            agent=returns_tracking_agent
            )  

    def prod_recommendation_details(self, query):
        return Task(
            description=f"""Conduct a comprehensive analysis of the query provided and the category 
            provided from categorizer_agent
            
            if the category provided is prod_recommendations then 
            search the recommendation_data file to find info needed to respond to the customer query

            Customer Query:\n\n {query} \n\n
            Only provide the info needed """,
            expected_output="""A well crafted Response to showcase the Top 3 product recommendations for user""",
            context = [self.categorize_query(query)],
            output_file=f"prod_recommednations.txt",
            agent=Prod_recommendation_agent
            )      


cust_tasks_obj = CustomTasks()