from datetime import datetime

def save_log(user_input, agent_response):
    today = datetime.now().strftime("%Y-%m-%d")
    filename = f"logs/session_{today}.txt"
    with open(filename, "a") as f:
        f.write(f"User: {user_input}\nCoach: {agent_response}\n\n")
