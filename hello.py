import random
from datetime import datetime

def get_time_based_greeting():
    """
    Returns a greeting based on the current time of day
    
    Returns:
        str: A time-appropriate greeting
    """
    hour = datetime.now().hour
    if 5 <= hour < 12:
        return "Good morning"
    elif 12 <= hour < 17:
        return "Good afternoon"
    elif 17 <= hour < 22:
        return "Good evening"
    else:
        return "Hello"

def get_random_greeting():
    """
    Returns a random friendly greeting
    
    Returns:
        str: A randomly selected greeting
    """
    greetings = [
        "Hi there",
        "Hey",
        "Greetings",
        "Welcome",
        "Nice to see you",
        "Howdy"
    ]
    return random.choice(greetings)

def greet_user(name, formal=False, random_greeting=False):
    """
    A function that takes a name and returns a greeting with additional options
    
    Args:
        name (str): The name of the person to greet
        formal (bool): Whether to use a formal time-based greeting
        random_greeting (bool): Whether to use a random casual greeting
        
    Returns:
        str: A personalized greeting message
    """
    if formal:
        base_greeting = get_time_based_greeting()
    elif random_greeting:
        base_greeting = get_random_greeting()
    else:
        base_greeting = "Hello"
        
    greeting = f"{base_greeting}, {name}! Hope you're having a great day!"
    return greeting

