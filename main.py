from fastapi import FastAPI, HTTPException, status
from models import Question, Optional

app = FastAPI()

questions = {
    1: {
        "question": "Explique o funcionamento do garbage collector em Python e como ele ajuda a gerenciar a memória.",
        "options": {
            "answer_a": "O garbage collector em Python é um mecanismo automático que gerencia a memória liberando a memória ocupada por objetos que o programa não reconhece.",    
            "answer_b": "O garbage collector em Python é um recurso opcional que não está disponível para a maioria dos tipos de objetos, apenas para objetos customizados.",
            "answer_c": "O garbage collector em Python é um processo que precisa ser acionado explicitamente pelo desenvolvedor sempre que desejar liberar memória, usando a função gc.collect().",
        },
        "answer": "answer_a"
    },
    2: {
        "question": "O que é uma closure em Python?",
        "options": {
            "answer_a": "Uma função que só pode ser chamada uma vez após sua definição",
            "answer_b": "Uma estrutura de dados que armazena variáveis locais de uma função, tornando-as inacessíveis para outras funções",
            "answer_c": "Uma closure em Python é uma função interna que tem permissão para acessar e manipular as variáveis de uma função externa, mantendo um estado interno.",
        },
        "answer": "answer_c"
    },
    3: {
        "question": "O que é um polimorfismo?",
        "options": {
            "answer_a": "Um princípio que requer que todas as classes em um programa compartilhem a mesma implementação de métodos",
            "answer_b": "É um princípio a partir do qual as classes derivadas de uma única classe base são capazes de invocar os métodos",
            "answer_c": "Uma técnica que permite que apenas objetos de uma mesma classe sejam usados em conjunto em um programa",
        },
        "answer": "answer_b"
    },
    4: {
        "question": "O que é o ORM (Object-Relational Mapping) em Django?",
        "options": {
            "answer_a": "Um sistema que converte automaticamente código Python em código SQL para consultas ao banco de dados.",
            "answer_b": "Uma ferramenta que elimina a necessidade de um banco de dados relacional em um projeto Django.",
            "answer_c": "Uma técnica que permite mapear objetos Python para tabelas em um banco de dados relacional.",
        },
        "answer": "answer_c"
    },
    5: {
        "question": "O que é um componente controlado em React?",
        "options": {
            "answer_a": "Um componente que gerencia seu estado interno usando o estado do React (useState) e responde a eventos.",
            "answer_b": "Um componente que não usa o React para gerenciar seu estado e eventos.",
            "answer_c": "Um componente que não permite a interação do usuário e é usado apenas para exibir informações estáticas.",
        },
        "answer": "answer_a"
    },
    6: {
        "question": "Qual é a diferença entre 'undefined' e 'null' em JavaScript?",
        "options": {
            "answer_a": "'undefined' é o valor atribuído a uma variavel não iniciada, enquanto 'null' é um valor que é atribuido",
            "answer_b": "'undefined' e 'null' são valores idênticos e podem ser usados indistintamente.",
            "answer_c": "'undefined' é usado para indicar um erro de código, enquanto 'null' é usado para indicar a falta de um valor definido.",
        },
        "answer": "answer_a"
    },
    7: {
        "question": "Qual é a diferença entre '== 'e '.equals()' ao comparar strings em Java?",
        "options": {
            "answer_a": " '==' compara o conteúdo das strings, e '.equals()' compara as referências de memória.",
            "answer_b": "'.equals()' compara o conteúdo das strings, enquanto '==' compara as referências de memória das strings",
            "answer_c": "'==' e '.equals()' são usados da mesma forma para comparar strings em Java.",
        },
        "answer": "answer_b"
    },
    8: {
        "question": "Como você remove um elemento específico de uma lista em Python?",
        "options": {
            "answer_a": "Usando o método '.remove()' seguido do valor do elemento a ser removido.",
            "answer_b": "Usando o método '.delete()' seguido do índice do elemento a ser removido.",
            "answer_c": "Usando o método '.del()' com o valor do elemento a ser removido.",
        },
        "answer": "answer_a"
    },
    9: {
        "question": "O que é um construtor em Java?",
        "options": {
            "answer_a": "Um método especial em uma classe usado para inicializar objetos daquela classe, mas que é obrigatorio ter parametros.",
            "answer_b": "Um método especial em uma classe usado para inicializar objetos da classe apenas com parametros.",
            "answer_c": "Um método de uma classe para iniciar o objeto na classe.",
        },
        "answer": "answer_c"
    },
    10: {
        "question": "O que é a serialização em Java e para que ela é usada?",
        "options": {
            "answer_a": "A serialização em Java é usada apenas para fins de depuração.",
            "answer_b": "A serialização em Java é o processo de converter objetos em uma sequência de bytes ",
            "answer_c": "A serialização em Java é usada para converter texto em objetos.",
        },
        "answer": "answer_b" 
    },
    
}

@app.get('/questions')
async def get_questions():
    return questions

@app.get('/questions/{question_id}')
async def get_question_answers(question_id: int):
    try:
        question = questions[question_id]
        
        return question
    except KeyError:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Question not found')

@app.post('/questions', status_code=status.HTTP_201_CREATED)
async def post_question(question: Question):
    print(question)
    question.id = sorted(questions.keys())[-1] + 1
    questions[question.id] = question
    return question

@app.put('/questions/{question_id}')
async def put_question(question_id: int, question: Question):
    if question_id in questions:
        question.id = question_id
        questions[question_id] = question
        
        return question
    
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'This question not found')


if __name__ == '__main__':
    import uvicorn
    uvicorn.run("main:app", host='127.0.0.1', port=8000, reload=True)