def generate(question, llm, PromptTemplate):
    with open('../input_text.txt', 'r') as file:
        input_text = file.read()  # Reads the entire file
        #print(content)

    template = """
           Você é um analista político e foi solicitado a analisar a eleição presidencial dos Estados Unidos de 2024
           com base nas informações fornecidas abaixo. Você só responde perguntas relacionadas ao documento fornecido
           e responde com "não sei" a outras perguntas não relacionadas ao documento fornecido.

           {input_text}
           
           Por favor, gere uma concisa e clara resposta para a questão.
           Questão: {question}

           Resposta:
           """

    prompt_template = PromptTemplate(template=template, input_variables=["input_text", "question"])


    final_prompt = prompt_template.format(input_text=input_text, question=question)
    #print(final_prompt)
    response = llm.invoke(final_prompt)
    #print(response.content)
    return response.content
