# import pandas as pd
# import streamlit as st
# from operator import itemgetter
# from langchain.chains.openai_tools import create_extraction_chain_pydantic
# from pydantic import BaseModel, Field
# from langchain_openai import ChatOpenAI

# # from langchain import LLMChain
# # from langchain.prompts import PromptTemplate


# llm = ChatOpenAI(model="gpt-3.5-turbo-1106", temperature=0)
# from typing import List

# @st.cache_data
# def get_table_details():
#     # Read the CSV file into a DataFrame
#     table_description = pd.read_csv("database_table_descriptions.csv")
#     table_docs = []

#     # Iterate over the DataFrame rows to create Document objects
#     table_details = ""
#     for index, row in table_description.iterrows():
#         table_details = table_details + "Table Name:" + row['Table'] + "\n" + "Table Description:" + row['Description'] + "\n\n"

#     return table_details


# class Table(BaseModel):
#     """Table in SQL database."""

#     name: str = Field(description="Name of table in SQL database.")

# def get_tables(tables: List[Table]) -> List[str]:
#     tables  = [table.name for table in tables]
#     return tables


# # table_names = "\n".join(db.get_usable_table_names())
# table_details = get_table_details()
# table_details_prompt = f"""Return the names of ALL the SQL tables that MIGHT be relevant to the user question. \
# The tables are:

# {table_details}

# Remember to include ALL POTENTIALLY RELEVANT tables, even if you're not sure that they're needed."""


# print("\n\n--------------------------------------\n\n just before table chain creation \n\n--------------------------------------\n\n")
# table_chain = {"input": itemgetter("question")} | create_extraction_chain_pydantic(Table, llm, system_message=table_details_prompt) | get_tables




import pandas as pd
import streamlit as st
from operator import itemgetter
from pydantic import BaseModel, Field  # Use the standard pydantic import
from langchain_openai import ChatOpenAI
from typing import List

llm = ChatOpenAI(model="gpt-3.5-turbo-1106", temperature=0)

@st.cache_data
def get_table_details():
    # Read the CSV file into a DataFrame
    table_description = pd.read_csv("database_table_descriptions.csv")
    table_docs = []

    # Iterate over the DataFrame rows to create Document objects
    table_details = ""
    for index, row in table_description.iterrows():
        table_details = table_details + "Table Name:" + row['Table'] + "\n" + "Table Description:" + row['Description'] + "\n\n"

    return table_details

class Table(BaseModel):
    """Table in SQL database."""
    name: str = Field(description="Name of table in SQL database.")

def get_tables(tables: List[Table]) -> List[str]:
    tables = [table.name for table in tables]
    return tables

table_details = get_table_details()
table_details_prompt = f"""Return the names of ALL the SQL tables that MIGHT be relevant to the user question. \
The tables are:

{table_details}

Remember to include ALL POTENTIALLY RELEVANT tables, even if you're not sure that they're needed."""

# Updated to use with_structured_output and prompt argument
table_chain = (
    {"input": itemgetter("question")} |
    llm.with_structured_output(Table, prompt=table_details_prompt) |
    get_tables
)
