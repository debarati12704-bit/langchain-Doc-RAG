from rag.pipeline import create_pipeline,ask_question

vector_store=create_pipeline()
query="why does tom befriend jerry?"
answer=ask_question(vector_store,query)
print(query,"\n\n",answer)




"""
"What is LangChain middleware?"
"What is short-term memory?"
"How does LangChain streaming work?"
"What are guardrails?"
"What is human-in-the-loop?"
"What is LangChain Studio?"
"How do I install LangChain?"
"""