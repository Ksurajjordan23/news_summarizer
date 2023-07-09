#Chain Prompting

from langchain import PromptTemplate, LLMChain
from langchain.llms import OpenAI

#initalize LLM
llm = OpenAI(model_name = "text-davinci-003", temperature = 0)

#prompt1
template_question = """ What is the name of the famous painter who painted Mona Lisa?
                        Answer: """
prompt_question = PromptTemplate(template= template_question, input_variables = [])

#prompt2
template_fact = """ Provide a brief description of {painter}'s life and some of his other famous
                    paintings. Answer: """
prompt_fact = PromptTemplate(input_variables = ["painter"], template = template_fact)

chain_question = LLMChain(llm = llm, prompt=prompt_question)

#create the llm chain for 1st prompt with an open dictionary

response_question= chain_question.run({})

#extract the painter's name from the 1st response
painter = response_question.strip()

#create the LLMChain for the second prompt
chain_fact = LLMChain(llm=llm, prompt = prompt_fact)

#input data for the second prompt
input_data = {"painter":painter}

#run the llm chain for the second prompt

response_fact = chain_fact.run(input_data)

print("Painter:", painter)
print("Facts:", response_fact)
