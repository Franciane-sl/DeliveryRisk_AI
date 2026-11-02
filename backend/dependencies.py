from fastapi import Request

#Recupera o pipeline armazenado durante a inicialização da API
def get_pipeline(request: Request):
    
    return request.app.state.pipeline
