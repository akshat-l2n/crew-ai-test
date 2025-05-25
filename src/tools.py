from crewai_tools import FileReadTool

order_detail_data = FileReadTools(file_path='/home/akshatjain/Desktop/store/genai_project/CrewAI/sample_data/order_management_data.csv')
return_data = FileReadTool(file_path = '/home/akshatjain/Desktop/store/genai_project/CrewAI/sample_data/returns_and_refunds_data.csv')
recommendation_data = FileReadTool(file_path = '/home/akshatjain/Desktop/store/genai_project/CrewAI/sample_data/recommendation_data.csv')