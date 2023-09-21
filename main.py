from fastapi import FastAPI, HTTPException, status

app = FastAPI()

questions = {
    1: {
        "question": "Explique o funcionamento do garbage collector em Python e como ele ajuda a gerenciar a memória.",
        "answers": {
            "answers_a_correta": "O garbage collector em Python é um mecanismo automático que gerencia a memória liberando a memória ocupada por objetos que o programa não reconhece.",
            
            "answers_b": "O garbage collector em Python é um recurso opcional que não está disponível para a maioria dos tipos de objetos, apenas para objetos customizados.",
            
            "answers_c": "O garbage collector em Python é um processo que precisa ser acionado explicitamente pelo desenvolvedor sempre que desejar liberar memória, usando a função gc.collect().",
        } 
    },
    2: {
        "question": "O que é uma closure em Python?",
        "answers": {
            "answers_a": "",
            "answers_b": "",
            "answers_c_correta": "Uma closure em Python é uma função interna que permite que a função interna acesse e manipule as variáveis de uma função externa, mantendo um estado interno.",
    },
    3: {
        "question": "O que é um polimorfismo?",
        "answers": {
            "answers_a": "",
            "answers_b": "",
            "answers_c": "",
        } 
    },
    4: {
        "question": "O que é o ORM (Object-Relational Mapping) em Django?",
        "answers": {
            "answers_a": "",
            "answers_b": "",
            "answers_c": "",
        } 
    },
    5: {
        "question": "O que é um componente controlado em React?",
        "answers": {
            "answers_a": "",
            "answers_b": "",
            "answers_c": "",
        } 
    },
    6: {
        "question": "Qual é a diferença entre 'undefined' e 'null' em JavaScript?",
        "answers": {
            "answers_a": "",
            "answers_b": "",
            "answers_c": "",
        } 
    },
    7: {
        "question": "Byanka Tomaz",
        "answers": {
            "answers_a": "",
            "answers_b": "",
            "answers_c": "",
        } 
    },
    8: {
        "question": "Byanka Tomaz",
        "answers": {
            "answers_a": "",
            "answers_b": "",
            "answers_c": "",
        } 
    },
    9: {
        "question": "Byanka Tomaz",
        "answers": {
            "answers_a": "",
            "answers_b": "",
            "answers_c": "",
        } 
    },
    # 10: {
    #     "question": "Byanka Tomaz",
    # 
    #     "answers": {
    #         "answers_a": "",
    #         "answers_b": "",
    #         "answers_c": "",
    #         "answers_d": "",
    #     } 
    # },
    # 11: {
    #     "question": "Byanka Tomaz",
    # 
    #     "answers": {
    #         "answers_a": "",
    #         "answers_b": "",
    #         "answers_c": "",
    #         "answers_d": "",
    #     } 
    # },
    # 12: {
    #     "question": "Byanka Tomaz",
    # 
    #     "answers": {
    #         "answers_a": "",
    #         "answers_b": "",
    #         "answers_c": "",
    #         "answers_d": "",
    #     } 
    # },
    # 13: {
    #     "question": "Byanka Tomaz",
    # 
    #     "answers": {
    #         "answers_a": "",
    #         "answers_b": "",
    #         "answers_c": "",
    #         "answers_d": "",
    #     } 
    # },
    # 14: {
    #     "question": "Byanka Tomaz",
    # 
    #     "answers": {
    #         "answers_a": "",
    #         "answers_b": "",
    #         "answers_c": "",
    #         "answers_d": "",
    #     } 
    # },
    # 15: {
    #     "question": "Byanka Tomaz",
    # 
    #     "answers": {
    #         "answers_a": "",
    #         "answers_b": "",
    #         "answers_c": "",
    #         "answers_d": "",
    #     } 
    # }
    
}

@app.get('/alunos')
async def get_alunos():
    return alunos

@app.get('/alunos/{aluno_id}')
async def get_aluno(aluno_id: int):
    try:
        aluno = alunos[aluno_id]
        aluno.update({"id": aluno_id})
        return aluno
    except KeyError:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Aluno não encontrado')

if __name__ == '__main__':
    import uvicorn
    uvicorn.run("alunos:app", host='127.0.0.1', port=8000, reload=True)