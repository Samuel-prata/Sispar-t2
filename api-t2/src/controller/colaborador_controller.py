
from flask import Blueprint, request, jsonify

# request = Trabalhar com as requisições
# jsonify = Trabalha com as respostas -> 

bp_colaborador = Blueprint('colaborador', __name__, url_prefix='/colaborador')

dados = [
        {'id': 1, 'nome': 'Karynne Moreira', 'cargo': 'CEO', 'cracha':'010101'},
        {'id': 2, 'nome': 'Samuel Silverio', 'cargo': 'CTO', 'cracha':'215487'},
        {'id': 3,'nome': 'Wisney Oliveira', 'cargo': 'Desenvolvedor Back-end', 'cracha':'147852'},
        {'id': 4,'nome': 'Romulo Rosa', 'cargo': 'Devops', 'cracha':'171171'},
        {'id': 5,'nome': 'Marcos Monte', 'cargo': 'QA', 'cracha':'000000'}
    ]

@bp_colaborador.route('/pegar-dados')
def pegar_dados():
    return dados

@bp_colaborador.route('/cadastrar', methods=['POST']) 
def cadastrar_novo_colaborador():
    
    dados_requisicao = request.get_json()
    
    novo_colaborador = {
        'id': len(dados) + 1,
        'nome': dados_requisicao['nome'],
        'cargo': dados_requisicao['cargo'],
        'cracha': dados_requisicao['cracha']
    }
    
    dados.append(novo_colaborador)
    
    return jsonify( {'mensagem': 'Colaborador cadastrado com sucesso'} ), 201

# Sinaliza que os dados enviados 
# endereco/colaborador/atualizar/10030
@bp_colaborador.route('/atualizar/<int:id_colaborador>', methods=['PUT'])
def atualizar_dados_colaborador(id_colaborador):
    
    dados_requisicao = request.get_json()
    
    for colaborador in dados:
        if colaborador['id'] == id_colaborador:
            colaborador_encontrado = colaborador
            break
        
    if 'nome' in dados_requisicao:
        colaborador_encontrado['nome'] = dados_requisicao['nome']
    if 'cargo' in dados_requisicao:
        colaborador_encontrado['cargo'] = dados_requisicao['cargo']
        
    return jsonify( {'mensagem': 'Dados do colaborador atualizado com sucesso'}), 200