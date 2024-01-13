import os
env_value = os.getenv({``env_value``})
# os.system('streamlit run app.py --server.address=0.0.0.0 --server.port 7860')
os.system('streamlit run ./code/InternLM/web_demo.py --server.address 127.0.0.1 --server.port 6006')