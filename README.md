# ✨ AI-Powered Personalized Diet Plan Generator ✨

This project utilizes CrewAI and Google's Gemini LLM to create a sophisticated agentic system capable of generating personalized 7-day diet plans based on user-specific details and goals. It features a user-friendly Streamlit interface for easy interaction.

## 🚀 Features

-   **Personalized Plans**: Generates diet plans tailored to individual gender, height, weight, dietary preferences (Veg, Non-Veg, Mix), and fitness goals (Gain weight, Maintain weight, Lose weight, Gain muscles).
-   **AI Agent System**: Built with CrewAI, leveraging an expert "Nutritionist" agent powered by the Gemini LLM.
-   **Detailed Output**: Provides a 7-day plan including breakfast, lunch, dinner, and snacks, with estimated calorie counts.
-   **Streamlit UI**: Offers an intuitive web interface for easy input and plan visualization.
-   **Configurable**: Agent roles, goals, and task descriptions are defined in YAML files for easy modification.
-   **Environment Variable Management**: Securely handles API keys using a `.env` file.

## 🛠️ Setup Instructions

1.  **Clone the Repository (or use existing code):**
    ```bash
    # If cloning fresh:
    # git clone https://github.com/saishshinde15/DietPlanAgent.git
    # cd DietPlanAgent
    ```

2.  **Create a Virtual Environment (Recommended):**
    ```bash
    python -m venv .venv
    source .venv/bin/activate  # On Windows use `.venv\Scripts\activate`
    ```

3.  **Install Dependencies:**
    The project uses `pyproject.toml`. Install dependencies using pip:
    ```bash
    pip install -e .
    ```
    This command installs all necessary libraries, including `crewai`, `streamlit`, and `python-dotenv`.

4.  **Configure Environment Variables:**
    -   Create a file named `.env` in the project's root directory (`cline_automation`).
    -   Add your Google Gemini API key and the desired model name to the `.env` file:
        ```dotenv
        GEMINI_API_KEY=YOUR_API_KEY_HERE
        MODEL=gemini/gemini-2.5-pro-exp-03-25 
        # Or another compatible Gemini model
        ```
    -   **Important:** Ensure the `.env` file is listed in your `.gitignore` file to prevent accidentally committing your API key.

## ▶️ How to Run

There are two ways to run the application:

1.  **Streamlit Web App :**
    This provides the best user experience. Run the following command from the project's root directory (`cline_automation`):
    ```bash
    streamlit run app.py
    ```
    This will open the application in your default web browser. Enter your details in the interface and click "Generate My Diet Plan".

2.  **Command-Line Interface (CLI)(Recommended):**
    You can also run the core logic via the command line:
    ```bash
    python src/cline_automation/main.py
    ```
    This script will prompt you for your details directly in the terminal.
3. ** Using CrewAi:**
   ```bash
   Run using crewai command i.e crewai run
   ```

## 📁 Project Structure

```
cline_automation/
├── .env                # Environment variables (API Key, Model) - MUST BE CREATED
├── .gitignore          # Git ignore rules
├── app.py              # Streamlit application script
├── diet_plan.md        # Example output file from crew execution
├── pyproject.toml      # Project metadata and dependencies
├── README.md           # This README file
├── src/
│   └── cline_automation/
│       ├── __init__.py
│       ├── config/
│       │   ├── agents.yaml # Agent definitions
│       │   └── tasks.yaml  # Task definitions
│       ├── crew.py         # CrewAI setup (Agents, Tasks, Crew)
│       ├── main.py         # CLI execution script
│       └── tools/          # Directory for custom tools (if any)
└── ... (other files like .venv, etc.)
```

## 🔧 Customization

-   **Agents & Tasks**: Modify `config/agents.yaml` and `config/tasks.yaml` to change agent behavior, goals, or task instructions.
-   **LLM Model**: Update the `MODEL` variable in the `.env` file to use a different compatible Gemini model.
-   **Streamlit UI**: Edit `app.py` to change the appearance or functionality of the web interface.

---

Enjoy your personalized diet plans!
