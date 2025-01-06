# LangChain

Welcome to the LangChain tutorial repository! This repo contains all the code examples. By the end of this course, you'll know how to use LangChain to create your own AI agents, build RAG chatbots, and automate tasks with AI.

## Course Outline
- **Setup Environment**
- **Chat Models**
- **Prompt Templates**
- **Chains**
- **RAG (Retrieval-Augmented Generation)**
- **Agents & Tools**

---

## Getting Started

### Prerequisites
- Python 3.10 or 3.11

### Installation
1. **Clone the repository:**
   ```bash
   git clone <your-repo-url>
   cd <your-repo-directory>
   ```

2. **Create and activate a virtual environment:**
   ```bash
   python -m venv venv
   source venv/bin/activate  # For Linux/macOS
   venv\Scripts\activate   # For Windows
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up your environment variables:**
   Rename the `.env.example` file to `.env` and update the variables inside with your own values:
   ```bash
   mv .env.example .env  # For Linux/macOS
   ren .env.example .env  # For Windows
   ```

5. **Run the code examples:**
   ```bash
   python 1_chat_models/1_chat_model_basic.py
   ```

---

## Repository Structure

### 1. Chat Models
Learn how to interact with models like ChatGPT, Claude, and Gemini.

- `1_chat_model_basic.py`
- `2_chat_model_basic_conversation.py`
- `3_chat_model_alternatives.py`
- `4_chat_model_conversation_with_user.py`
- `5_chat_model_save_message_history_firestore.py`

### 2. Prompt Templates
Understand the basics of prompt templates and how to use them effectively.

- `1_prompt_template_basic.py`
- `2_prompt_template_with_chat_model.py`

### 3. Chains
Explore how to create and use chains to link various components together.

- `1_chains_basics.py`
- `2_chains_using_runnable.py`
- `3_chains_using_runnable_example2.py`
- `4_chains_parallel.py`
- `5_chains_branching.py`
---

Feel free to explore, learn, and build amazing AI applications with LangChain. If you encounter any issues, please open an issue or submit a pull request.

Happy coding!
