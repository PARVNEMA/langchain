from langchain_core.prompts import ChatPromptTemplate

chat_template=ChatPromptTemplate([('system','you are a helpful chatbot in domain {domain}'),('human','explain in simple what is {topic}')])

prompt=chat_template.invoke({'domain':'cricket','topic':'batting'})

print(prompt)