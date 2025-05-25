from crewai import Agent
from utils.llm_model import Agent_LLM
from src.tools import order_detail_data, return_data, recommendation_data

class CustomAgents() : 
    def Query_Categorizer_Agent(self) : 
        # role, goal, backstory, tools, verbose
        return Agent(
            role = 'Customer Query Categorizer Agent', 
            goal = """
                take in a Query from a human which was asked and categorize it 
                into one of the following categories: 
                
                order_tracking - used when someone is asking for information about shipment of their orders 
                returns_request - used when someone is enquiring about returns process 
                prod_recommendations - used when someone is asking for recommendations on product \\
                off_topic when it doesnt relate to any other category 
            """, 
            backstory = "You are a master at understanding what a customer wants when they ask a query and is able to categorize it in a useful way", 
            verbose = True, 
            allow_delegation = False, 
            memory = True, 
            llm = Agent_LLM,
        )
    
    def Order_tracking_agent(self):
        return Agent(
            role='Order Tracking Agent',
            goal="""take in a query from a human and the category 
            that the Query_Categorizer_Agent agent gave. if the Output of Query_Categorizer_Agent is order_tracking, only then perform search operation  
            & provide the details to Response Writer so it can answer the query in a thoughtful and helpful way.
            If you DONT think a search will help just reply 'NO SEARCH NEEDED'
            If you dont find any useful info just reply 'NO USEFUL RESESARCH FOUND'
            otherwise reply with the info you found that is useful for the Response writer
            """,
            backstory="""You are a master at understanding what information Response writer needs to write a reply that 
            will help the customer""",
            llm=Agent_LLM,
            verbose=True,
            max_iter=5,
            allow_delegation=False,
            memory=False,
            tools=[order_detail_data],
           
        )

    def Returns_tracking_agent(self):
        return Agent(
            role='Returns Tracking Agent',
            goal="""take in a query from a human and the category 
            that the Query_Categorizer_Agent agent gave. if the Output of Query_Categorizer_Agent is returns_request, only then perform search operation 
            & provide the details to Response Writer so it can answer the query in a thoughtful and helpful way.
            If you DONT think a search will help just reply 'NO SEARCH NEEDED'
            If you dont find any useful info just reply 'NO USEFUL RESESARCH FOUND'
            otherwise reply with the info you found that is useful for the Response writer
            """,
            backstory="""You are a master at understanding what information Response writer needs to write a reply that 
            will help the customer""",
            llm=Agent_LLM,
            verbose=True,
            max_iter=5,
            allow_delegation=False,
            memory=False,
            tools=[return_data],
           
        )

    def prod_recommendation_agent(self):
        return Agent(
            role='Product Recommendation Agent',
            goal="""take in a query from a human and the category 
            that the Query_Categorizer_Agent agent gave. if the Output of Query_Categorizer_Agent is prod_recommendations, only then perform search operation 
            & provide the details to Response Writer so it can answer the query in a thoughtful and helpful way.
            If you dont find any useful info just reply with General Product Recommendations
            otherwise reply with the info you found that is useful for the Response writer
            """,
            backstory="""The Product Recommendation Agent was designed to mimic a personal shopping assistant.
            Leveraging machine learning algorithms, it analyzes customer behavior and preferences to suggest relevant products
            You are a master at understanding what information Response writer needs to write a reply that 
            will help the customer""",
            llm=Agent_LLM,
            verbose=True,
            max_iter=5,
            allow_delegation=False,
            memory=False,
            tools=[recommendation_data],
           
        )


agents = CustomAgents()

categorizer_agent = agents.Query_Categorizer_Agent()
order_tracking_agent = agents.Order_tracking_agent()
returns_tracking_agent = agents.Returns_tracking_agent()
Prod_recommendation_agent = agents.prod_recommendation_agent()

agents_lst = [categorizer_agent,order_tracking_agent,returns_tracking_agent,Prod_recommendation_agent ]