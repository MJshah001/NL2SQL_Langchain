# NL2SQL : ContextAware LangChain SQL Chatbot


In a data-driven world, being able to query databases without knowing SQL can empower non-technical users in industries like healthcare, finance, and more. 

Welcome to the **NL2SQL** project! This project aims to revolutionize database querying by enabling natural language queries, eliminating the need for complex SQL syntax. Powered by LangChain, OpenAI GPT models, and MySQL, the system translates user queries into SQL and dynamically interacts with the database, selecting relevant tables and generating responses in plain language.


![Architecture](https://github.com/MJshah001/NL2SQL_Langchain/blob/main/Resources/NL2SQL%20Application%20Diagram.jpg)



## Live Demo
Streamlit Live Application : [click here](https://nl2sql-langchain.onrender.com/)

*(Initial load might take up to a minute or so.)*

checkout sample chat here : [PDF](https://github.com/MJshah001/NL2SQL_Langchain/blob/main/Resources/nl2sql_sample_chat.pdf) |  [screenshot](https://github.com/MJshah001/NL2SQL_Langchain/blob/main/Resources/sample%20chat%20screenhot.png)

Sample Database used for this demo : [classicmodels](https://www.mysqltutorial.org/getting-started-with-mysql/mysql-sample-database/)

## Features

- **Natural Language to SQL Translation**:
  
   - This feature enables the chatbot to take user input in plain English (or another language) and convert it into a valid SQL query. By leveraging OpenAI's large language models (LLMs), such as GPT, the system can interpret the user's intent and map it to a corresponding SQL command, without requiring the user to know SQL syntax.
- **Database Integration**:

   - The chatbot is connected to a live MySQL database hosted online. Once the natural language input is converted into an SQL query, it is executed directly against this MySQL database. 
- **Few-Shot Learning**: 
   - This technique improves the chatbot's ability to understand and generate accurate SQL queries by providing it with a few relevant examples. Instead of learning from scratch, the model uses these examples as a guide, which helps it generalize better and handle similar user queries more accurately. This is especially useful when working with ambiguous or complex queries, allowing the chatbot to produce better results with fewer mistakes.
- **Dynamic Example and Table Selection**: 

   - This feature ensures that the chatbot picks the most relevant examples and database tables based on the user's query. When a user asks a question, the system dynamically identifies which table(s) contain the required data and uses examples related to the user's input to generate an accurate SQL query.
- **Conversational Memory**:

  - The chatbot maintains a memory of previous interactions, allowing it to handle follow-up questions more effectively. It retains the context of earlier queries, meaning users don’t need to repeat themselves or reframe their queries entirely. This makes the conversation flow more naturally and enables multi-step database interactions.
- **Rephrasing of SQL Results**:

   - After generating SQL queries and fetching the results from the database, the system takes those results and rephrases them in natural language. This ensures that users get clear, understandable answers rather than raw data, which might be difficult to interpret without SQL knowledge.

## Tech Stack

- **LangChain**: Facilitates the natural language processing and query generation.
- **OpenAI API**: Provides the large language models used for natural language processing and for query translation.
- **MySQL**: The database management system where the data is stored and queried.
- **ChromaDB**: A vector database used for dynamic example selection.
- **Python**: The core programming language used for developing this project.

## How It Works

1. The user enters a query in plain English.
2. The input is processed through openai GPT model to generate an SQL query.
3. The correct table from the MySQL database is selected based on the user's query.
4. The query is executed, and the result is returned to the user in a structured format.

https://github.com/user-attachments/assets/567014cc-6eaf-45bc-b8b5-f680848f731c


## Installation

### Dependencies

Ensure you have the following tools installed:

- Python 3.11
- MySQL (or a compatible database)
- OpenAI API Key (for LangChain)

### Steps

1. Clone the repository:

   ```bash
   git clone https://github.com/MJshah001/NL2SQL_Langchain.git
   cd NL2SQL_LangChain
   ```

2. Install the required Python libraries:

   ```bash
   pip install -r requirements.txt
   ```

3. Set up your database connection details in your environment variables using `.env` file:

   ```python
   os.environ["OPENAI_API_KEY"] = "<Your OpenAI API Key>"
   ```

   Replace the placeholders with your database credentials:

   ```python
   db_user = "<Your DB Username>"
   db_password = "<Your DB Password>"
   db_host = "<Your DB Host>"
   db_name = "<Your Database Name>"
   ```
   
   **check sample_dot_env_file for structure and format.**

4. Start the application:

   ```bash
   streamlit run main.py
   ```


## Future Enhancements

- Extend the system to support additional databases like PostgreSQL and SQLite.
- Fine-tune language models for more domain-specific use cases, such as healthcare or finance.
- Improving error handling for edge cases in input translation.


## Conclusion

This project showcases how LangChain and NLP models can democratize database querying by allowing users to interact with databases using natural language. By combining few-shot learning, dynamic example selection, and rephrasing of SQL results, This system simplifies data access and makes querying as easy as asking a question.

