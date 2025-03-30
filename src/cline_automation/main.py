#!/usr/bin/env python
import sys
import warnings

# Import the new crew class
from cline_automation.crew import DietPlanCrew

warnings.filterwarnings("ignore", category=SyntaxWarning, module="pysbd")

def get_user_input(prompt, input_type=str, options=None):
    """Helper function to get and validate user input."""
    while True:
        try:
            user_input = input(prompt).strip()
            if input_type == float or input_type == int:
                value = input_type(user_input)
                # Add basic validation for positive numbers if relevant
                if value <= 0:
                     print("Please enter a positive value.")
                     continue
                return value
            elif input_type == str:
                 if not user_input:
                     print("Input cannot be empty. Please try again.")
                     continue
                 # Validate against options if provided
                 if options and user_input.lower() not in [opt.lower() for opt in options]:
                     print(f"Invalid option. Please choose from: {', '.join(options)}")
                     continue
                 return user_input
            else:
                 return user_input # No specific validation for other types
        except ValueError:
            print(f"Invalid input. Please enter a valid {input_type.__name__}.")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")


def run():
    """
    Run the DietPlanCrew.
    """
    print("Welcome to the Personalized Diet Plan Generator!")
    print("Please provide the following details:")

    gender = get_user_input("Enter your gender (e.g., Male, Female, Other): ", str)
    height = get_user_input("Enter your height in cm: ", float)
    weight = get_user_input("Enter your weight in kg: ", float)
    
    diet_options = ["Veg", "Non-Veg", "Mix"]
    diet_preference = get_user_input(f"Enter your dietary preference ({'/'.join(diet_options)}): ", str, options=diet_options)

    goal_options = ["Gain weight", "Maintain weight", "Lose weight", "Gain muscles"]
    goal = get_user_input(f"What is your primary goal? ({'/'.join(goal_options)}): ", str, options=goal_options)


    inputs = {
        'gender': gender,
        'height': height,
        'weight': weight,
        'diet_preference': diet_preference,
        'goal': goal
    }
    
    print("\nGenerating your personalized diet plan based on your inputs...")

    try:
        # Instantiate and run the DietPlanCrew
        crew_instance = DietPlanCrew()
        result = crew_instance.crew().kickoff(inputs=inputs)
        
        print("\n--- Diet Plan ---")
        print(result)
        print("\nDiet plan also saved to diet_plan.md")

    except Exception as e:
        print(f"\nAn error occurred while running the crew: {e}")
        # Consider adding more specific error handling or logging here

# The main execution block
if __name__ == "__main__":
    run()

# --- Optional: Keep or remove train/replay/test functions ---
# These functions are related to the old boilerplate and might need
# significant updates to work with the DietPlanCrew if needed.
# For now, they are commented out or can be removed.

# def train():
#     """
#     Train the crew for a given number of iterations. (Needs update for DietPlanCrew)
#     """
#     # ... (Update required) ...
#     pass

# def replay():
#     """
#     Replay the crew execution from a specific task. (Needs update for DietPlanCrew)
#     """
#     # ... (Update required) ...
#     pass

# def test():
#     """
#     Test the crew execution and returns the results. (Needs update for DietPlanCrew)
#     """
#     # ... (Update required) ...
#     pass
