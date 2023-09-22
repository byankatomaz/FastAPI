from fastapi import FastAPI, HTTPException, status

app = FastAPI()

questions = {
    1: {
        "question": "Explique o funcionamento do garbage collector em Python e como ele ajuda a gerenciar a memória.",
        "answers": {
            "correct": "O garbage collector em Python é um mecanismo automático que gerencia a memória liberando a memória ocupada por objetos que o programa não reconhece.",    
            "wrong": "O garbage collector em Python é um recurso opcional que não está disponível para a maioria dos tipos de objetos, apenas para objetos customizados.",
            "wrong": "O garbage collector em Python é um processo que precisa ser acionado explicitamente pelo desenvolvedor sempre que desejar liberar memória, usando a função gc.collect().",
        } 
    },
    2: {
        "question": "O que é uma closure em Python?",
        "answers": {
            "wrong": "Uma função que só pode ser chamada uma vez após sua definição",
            "wrong": "Uma estrutura de dados que armazena variáveis locais de uma função, tornando-as inacessíveis para outras funções",
            "correct": "Uma closure em Python é uma função interna que tem permissão para acessar e manipular as variáveis de uma função externa, mantendo um estado interno.",
        }
    },
    3: {
        "question": "O que é um polimorfismo?",
        "answers": {
            "wrong": "Um princípio que requer que todas as classes em um programa compartilhem a mesma implementação de métodos",
            "correct": "É um princípio a partir do qual as classes derivadas de uma única classe base são capazes de invocar os métodos",
            "wrong": "Uma técnica que permite que apenas objetos de uma mesma classe sejam usados em conjunto em um programa",
        } 
    },
    4: {
        "question": "O que é o ORM (Object-Relational Mapping) em Django?",
        "answers": {
            "wrong": "Um sistema que converte automaticamente código Python em código SQL para consultas ao banco de dados.",
            "wrong": "Uma ferramenta que elimina a necessidade de um banco de dados relacional em um projeto Django.",
            "correct": "Uma técnica que permite mapear objetos Python para tabelas em um banco de dados relacional.",
        } 
    },
    5: {
        "question": "O que é um componente controlado em React?",
        "answers": {
            "correct": "Um componente que gerencia seu estado interno usando o estado do React (useState) e responde a eventos.",
            "wrong": "Um componente que não usa o React para gerenciar seu estado e eventos.",
            "wrong": "Um componente que não permite a interação do usuário e é usado apenas para exibir informações estáticas.",
        } 
    },
    6: {
        "question": "Qual é a diferença entre 'undefined' e 'null' em JavaScript?",
        "answers": {
            "correct": "'undefined' é o valor atribuído a uma variavel não iniciada, enquanto 'null' é um valor que é atribuido",
            "wrong": "'undefined' e 'null' são valores idênticos e podem ser usados indistintamente.",
            "wrong": "'undefined' é usado para indicar um erro de código, enquanto 'null' é usado para indicar a falta de um valor definido.",
        } 
    },
    7: {
        "question": "Qual é a diferença entre '== 'e '.equals()' ao comparar strings em Java?",
        "answers": {
            "wrong": " '==' compara o conteúdo das strings, e '.equals()' compara as referências de memória.",
            "correct": "'.equals()' compara o conteúdo das strings, enquanto '==' compara as referências de memória das strings",
            "wrong": "'==' e '.equals()' são usados da mesma forma para comparar strings em Java.",
        } 
    },
    8: {
        "question": "Como você remove um elemento específico de uma lista em Python?",
        "answers": {
            "correct": "Usando o método '.remove()' seguido do valor do elemento a ser removido.",
            "wrong": "Usando o método '.delete()' seguido do índice do elemento a ser removido.",
            "wrong": "Usando o método '.del()' com o valor do elemento a ser removido.",
        } 
    },
    9: {
        "question": "O que é um construtor em Java?",
        "answers": {
            "wrong": "Um método especial em uma classe usado para inicializar objetos daquela classe, mas que é obrigatorio ter parametros.",
            "wrong": "Um método especial em uma classe usado para inicializar objetos da classe apenas com parametros.",
            "correct": "Um método de uma classe para iniciar o objeto na classe.",
        } 
    },
    10: {
        "question": "O que é a serialização em Java e para que ela é usada?",
    
        "answers": {
            "wrong": "A serialização em Java é usada apenas para fins de depuração.",
            "correct": "A serialização em Java é o processo de converter objetos em uma sequência de bytes ",
            "wrong": "A serialização em Java é usada para converter texto em objetos.",
        } 
    },
    
}

@app.get('/questions')
async def get_questions():
    return questions

@app.get('/questions/{question_id}')
async def get_question_answers(question_id: int):
    try:
        question = questions[question_id]
        question.update({"id": question_id})
        
        return question
    except KeyError:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Question not found')





if __name__ == '__main__':
    import uvicorn
    uvicorn.run("main:app", host='127.0.0.1', port=8000, reload=True)