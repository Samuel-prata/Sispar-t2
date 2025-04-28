
from flask import Blueprint, request, jsonify
from src.model import db
from src.model.colaborador_model import Colaborador
from src.security.security import hash_senha, checar_senha

# request = Trabalhar com as requisições
# jsonify = Trabalha com as respostas -> 

bp_colaborador = Blueprint('colaborador', __name__, url_prefix='/colaborador')


@bp_colaborador.route('/todos-colaboradores')
def pegar_dados_todos_colaboradores(): 
    
    colaboradores = db.session.execute(
        db.select(Colaborador)
    ).scalars().all()
#                       Expressão                   item            iteravel    
    colaboradores = [colaborador.all_data() for colaborador in colaboradores]
    
    return jsonify(colaboradores), 200

@bp_colaborador.route('/cadastrar', methods=['POST']) 
def cadastrar_novo_colaborador():
    dados_requisicao = request.get_json()
    
    novo_colaborador = Colaborador(
        nome=dados_requisicao['nome'],
        email=dados_requisicao['email'],
        senha=hash_senha(dados_requisicao['senha']),
        cargo=dados_requisicao['cargo'],
        salario=dados_requisicao['salario']
    )
    
# INSERT INTO tb_colaborador (nome,email,senha,cargo,salario) VALUES ()
    db.session.add(novo_colaborador)
    db.session.commit()
    
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


@bp_colaborador.route('/login', methods=['POST'])
def login():
    
    dados_requisicao = request.get_json()
    email = dados_requisicao['email']
    senha = dados_requisicao['senha']
    
    if not email or not senha:
        return jsonify({'mensagem': 'Email e senha são obrigatórios'}), 400
    
    colaborador = db.session.execute(
        # Query 
        db.select(Colaborador).where(Colaborador.email == email) # SELECT * FROM colaborador WHERE email == 'algumemail'
    ).scalar() # -> Traz um registro ou None
    print('*'*100)
    print(f'Dado puxada no banco de dados: {colaborador} | Tipo de dados: {type(colaborador)}')
    print('*'*100)
    if not colaborador:
        return jsonify({'mensagem': 'Usuario não encontrado'}), 404
    
    colaborador = colaborador.to_dict()
    print('*'*100)
    print(f'Dado puxada no banco de dados: {colaborador} | Tipo de dados: {type(colaborador)}')
    print('*'*100)
    
    if email == colaborador.get('email') and checar_senha(senha, colaborador.get('senha')):
        return jsonify({'mensagem': 'Login realizado com sucesso'}), 200
    

    