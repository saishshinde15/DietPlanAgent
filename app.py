import streamlit as st
import warnings
from cline_automation.crew import DietPlanCrew  # Import your crew class

# Ignore specific warnings if necessary
warnings.filterwarnings("ignore", category=SyntaxWarning, module="pysbd")

# --- Streamlit App Configuration ---
st.set_page_config(page_title="Personalized Diet Planner", layout="wide")

st.title("✨ Personalized Diet Plan Generator ✨")
st.markdown("""
Welcome! This tool uses AI agents (powered by CrewAI) to generate a personalized 7-day diet plan 
based on your individual details and goals. Please provide the information below.
""")

# --- User Input Section ---
st.header("Enter Your Details:")

col1, col2 = st.columns(2)

with col1:
    gender = st.text_input("Gender (e.g., Male, Female, Other)", key="gender")
    height = st.number_input("Height (cm)", min_value=1.0, step=1.0, format="%.1f", key="height")
    weight = st.number_input("Weight (kg)", min_value=1.0, step=0.5, format="%.1f", key="weight")

with col2:
    diet_options = ["Veg", "Non-Veg", "Mix"]
    diet_preference = st.selectbox("Dietary Preference", options=diet_options, index=None, placeholder="Select...", key="diet_pref")

    goal_options = ["Gain weight", "Maintain weight", "Lose weight", "Gain muscles"]
    goal = st.selectbox("Primary Goal", options=goal_options, index=None, placeholder="Select...", key="goal")

# --- Generate Button and Logic ---
st.divider()
generate_button = st.button("🚀 Generate My Diet Plan", type="primary", use_container_width=True)

if generate_button:
    # Validate inputs
    if not all([gender, height > 0, weight > 0, diet_preference, goal]):
        st.warning("Please fill in all the details above.")
    else:
        st.info("Generating your personalized diet plan... This may take a moment.")
        
        inputs = {
            'gender': gender,
            'height': height,
            'weight': weight,
            'diet_preference': diet_preference,
            'goal': goal
        }

        try:
            with st.spinner('AI agents are crafting your plan...'):
                # Instantiate and run the DietPlanCrew
                crew_instance = DietPlanCrew()
                result = crew_instance.crew().kickoff(inputs=inputs)
            
            st.success("🎉 Your personalized diet plan is ready!")
            st.divider()
            st.header("Your 7-Day Diet Plan:")
            st.markdown(result) # Display the markdown result directly

            # Optionally, offer download
            st.download_button(
                label="Download Plan as Markdown",
                data=result,
                file_name=f"diet_plan_{gender}_{goal.replace(' ','_')}.md",
                mime="text/markdown",
            )

        except Exception as e:
            st.error(f"An error occurred while generating the plan: {e}")
            st.error("Please check the console or logs for more details. Ensure your API key is valid and has access to the specified model.")

st.markdown("---")
st.caption("Powered by CrewAI and Streamlit")
