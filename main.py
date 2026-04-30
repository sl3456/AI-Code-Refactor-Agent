
from src.core_agent import RefactorAgent
import os

def main():
    api_key = os.getenv("API_KEY", "demo_key")
    agent = RefactorAgent(api_key)
    
    print("--- Starting AI Refactor Agent ---")
    # In a real scenario, this would point to a real repo
    # Here we point to the current project src for demo
    agent.run_pipeline("./src")
    print("--- Pipeline Completed ---")

if __name__ == "__main__":
    main()
