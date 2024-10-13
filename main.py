from langchain_core.prompts import PromptTemplate
from langchain_openai import ChatOpenAI
from langchain_ollama import ChatOllama
from langchain_core.output_parsers import StrOutputParser

from third_parties.linkedin import scrape_linkedin_profile


if __name__ == "__main__":
    summary_template = """
    given the Linkedin information {information} about a person from I want
    you to create 
    1. a short summary
    2. two interesting facts about name
    """


    summary_prompt_template = PromptTemplate(
        input_variables=["information"],
        template=summary_template
    )

    # llm = ChatOpenAI(
    #     temperature=0,
    #     model_name="gpt-4o-mini",
    # )

    llm = ChatOllama(
        model="mistral",
    )
    information = scrape_linkedin_profile("test", mock=True)

    chain = summary_prompt_template | llm | StrOutputParser()
    res = chain.invoke(input={"information": information})
    print(res)