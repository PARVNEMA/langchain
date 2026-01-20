from langchain_core.prompts import ChatPromptTemplate,MessagesPlaceholder

chat_template =ChatPromptTemplate([('system','you are a customer support agent'),MessagesPlaceholder(variable_name='chat_history')])

chat_history=[]
with open('chat_history.txt')as f:
  chat_history.extend(f.readlines())