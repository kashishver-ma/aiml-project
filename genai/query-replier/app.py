
import ollama

# Initialize the Ollama client
client = ollama.Client()

# Define a function to generate SQL queries
def generate_sql_query(prompt):
    response = client.chat(
        model="tinyllama",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ]
    )
    return response['message']['content']

#input from user terminal
prompt = input("Enter your query: ")
sql_query = generate_sql_query(prompt)
print("Generated SQL Query:")
print(sql_query)

# # Example usage
# prompt = "Generate a SQL query to select all records from the employees table where the salary is greater than 50000."
# sql_query = generate_sql_query(prompt)
# print(sql_query)