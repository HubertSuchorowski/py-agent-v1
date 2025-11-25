from langchain_ollama import ChatOllama

agent = ChatOllama(
    model="gemma3:1b",
    validate_model_on_init=True,
    temperature=0.8,
    num_predict=256
)

messages = [
    ("system", "You are a helpful translator. Translate the user sentence to polish."),
    ("human", "I love programming.")
]

wynik = agent.invoke(messages)
print(wynik)