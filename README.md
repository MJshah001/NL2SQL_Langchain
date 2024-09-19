# NL2SQL : ContextAware LangChain SQL Chatbot


In a data-driven world, being able to query databases without knowing SQL can empower non-technical users in industries like healthcare, finance, and more. 

Welcome to the **NL2SQL** project! This project aims to revolutionize database querying by enabling natural language queries, eliminating the need for complex SQL syntax. Powered by LangChain, OpenAI GPT models, and MySQL, the system translates user queries into SQL and dynamically interacts with the database, selecting relevant tables and generating responses in plain language.


## Features

- **Natural Language to SQL Translation:**: Converts user input into SQL queries using Large Language Models from OpenAI.

- **Database Integration**:  Queries are executed against a live MySQL database hosted online.

- **Few-Shot Learning**: Improve the accuracy of SQL generation by providing relevant examples.

- **Dynamic Example and Table Selection**: Automatically choose relevant few-shot examples and database tables based on user input.

- **Conversational Memory**: Maintain context across multiple queries to handle follow-up questions.

- **Rephrasing of SQL Results**: Return results in user-friendly natural language.

## Teck Stack

- **LangChain**: Facilitates the natural language processing and query generation.
- **OpenAI API**: Provides the large language models used for natural language processing and for query translation.
- **MySQL**: The database management system where the data is stored and queried.
- **ChromaDB**: A vector database used for dynamic example selection.
- **Python**: The core programming language used for developing this project.

## Project Architecture

This NL2SQL system follows a modular architecture with the following components:


### How It Works

1. The user enters a query in plain English.
2. The input is processed through openai GPT model to generate an SQL query.
3. The correct table from the MySQL database is selected based on the user's query.
4. The query is executed, and the result is returned to the user in a structured format.

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

3. Set up your database connection details in your environment variables using .env file:

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
- Fine-tune language models for more domain-specific use cases, such as healthcare or finance.- Improving error handling for edge cases in input translation.


## Conclusion

This project showcases how LangChain and NLP models can democratize database querying by allowing users to interact with databases using natural language. By combining few-shot learning, dynamic example selection, and rephrasing of SQL results, This system simplifies data access and makes querying as easy as asking a question.

