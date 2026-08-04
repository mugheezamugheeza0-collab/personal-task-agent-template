import os
import datetime
from groq import Groq
from dotenv import load_dotenv

import config

load_dotenv()

# --- Tool Functions ---

def get_system_time():
    """Returns the current system date and time."""
    now = datetime.datetime.now()
    return f"Current date and time: {now.strftime('%Y-%m-%d %H:%M:%S')}"

def calculate_expression(expression: str):
    """Evaluates a mathematical expression safely."""
    try:
        # Basic math evaluation
        allowed_chars = "0123456789+-*/(). "
        if not all(c in allowed_chars for c in expression):
            return "Error: Invalid characters in math expression."
        result = eval(expression)
        return f"Result: {result}"
    except Exception as e:
        return f"Error evaluating expression: {str(e)}"

# --- Schemas for Groq Tool Calling ---

TOOL_SCHEMAS = [
    {
        "type": "function",
        "function": {
            "name": "get_system_time",
            "description": "Get the current real-world date and system time.",
            "parameters": {
                "type": "object",
                "properties": {},
                "required": []
            }
        }
    },
    {
        "type": "function",
        "function": {
            "name": "calculate_expression",
            "description": "Perform basic arithmetic calculations.",
            "parameters": {
                "type": "object",
                "properties": {
                    "expression": {
                        "type": "string",
                        "description": "The math expression to calculate (e.g., '12 * 45 + 100')."
                    }
                },
                "required": ["expression"]
            }
        }
    }
]

# Map tool names to functions
TOOL_FUNCTIONS = {
    "get_system_time": get_system_time,
    "calculate_expression": calculate_expression,
}
