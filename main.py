from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_openai import ChatOpenAI


load_dotenv()

def main():
    print("Hello from langchain-course!")
information = """ 
Musk attended Queen’s University in Kingston, Ontario, and in 1992 he transferred to the University of Pennsylvania, Philadelphia, where he received bachelor’s degrees in physics and economics in 1997. He enrolled in graduate school in physics at Stanford University in California, but he left after only two days because he felt that the Internet had much more potential to change society than work in physics. In 1995, he founded Zip2, a company that provided maps and business directories to online newspapers. In 1999, Zip2 was bought by the computer manufacturer Compaq for $307 million, and Musk then founded an online financial services company, X.com, which later became PayPal, which specialized in transferring money online. The online auction eBay bought PayPal in 2002 for $1.5 billion.
Musk was long convinced that for life to survive, humanity has to become a multiplanet species, but he was dissatisfied with the great expense of rocket launchers. In 2002, he founded Space Exploration Technologies (SpaceX) to make more affordable rockets. Its first two rockets were the Falcon 1 (first launched in 2006) and the larger Falcon 9 (first launched in 2010), which were designed to cost much less than competing rockets. A third rocket, the Falcon Heavy (first launched in 2018), was designed to carry 117,000 pounds (53,000 kg) to orbit, nearly twice as much as its largest competitor, the Boeing Company’s Delta IV Heavy, for one-third the cost. The Falcon 9 and Falcon Heavy eventually dominated the launch vehicle market, and in 2024 more than half of the world’s orbital launches were done by SpaceX.
"""
summary_template ="""
Given the information {information} about the person I want you to create: 
1. A short summary
2. Two interesting facts about them
"""
summary_prompt_template = PromptTemplate(
    input_variables=["information"], template=summary_template
)
llm=ChatOpenAI(temperature=0, model="gpt-5")
chain=summary_prompt_template | llm
respponse=chain.invoke(input={"information": information})

print(respponse.content)

if __name__ == "__main__":
    main()
