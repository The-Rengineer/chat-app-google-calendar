from langchain.schema.output_parser import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage, SystemMessage
from langchain_core.prompts import MessagesPlaceholder
from datetime import datetime

class ChatService:
    def __init__(self, cache):
        self.cache = cache
        self.llm = ChatOpenAI(model="gpt-4o")
        self.prompt_template = ChatPromptTemplate.from_messages([
            ("system", "You are a secretary managing the user's schedule. \
                        The user's upcoming schedule is {schedule}. The following is the upcoming schedule in order, starting from number 1."),
            MessagesPlaceholder("chat_history"),
            ("human", "{input}"),
        ])
        self.chain = self.prompt_template | self.llm | StrOutputParser()
        self.chat_history = []

    def continual_chat(self, schedule, user_input):
        if user_input == "cancel":
            self.chat_history = []
            return "Thank you. Nice talking with you!!!" 

        result = self.chain.invoke({
            "input": user_input,
            "chat_history": self.chat_history,
            "schedule": schedule
        })

        self.chat_history.append(HumanMessage(content=user_input))
        self.chat_history.append(SystemMessage(content=result))

        return result
