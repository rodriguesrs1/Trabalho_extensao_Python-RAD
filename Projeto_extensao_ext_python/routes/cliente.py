from flask import Blueprint, render_template, request
from database.models.cliente import Cliente



cliente_route = Blueprint('cliente', __name__)

@cliente_route.route('/')
def lista_clientes():
        #Listar os clientes
        clientes = Cliente.select()
        return render_template('lista_clientes.html', clientes=clientes)


@cliente_route.route('/', methods=['POST'])
def inserir_cliente():
         #inserir dados do cliente
       
         data = request.json

         novo_usuario = Cliente.create(
                 nome = data['nome'],
                 email = data['email'],
                 telefone = data['telefone'],
                 endereco = data['endereco'],
                 pedido = data['pedido'],
                
         )

         return render_template('item_cliente.html', cliente=novo_usuario)


@cliente_route.route('/new')
def form_cliente():
         #Exibir formulario para cadastro de clientes
         return render_template('form_cliente.html')


@cliente_route.route('/<int:cliente_id>)')
def detalhe_cliente(cliente_id):
         #exibir detalhes do cliente
         
         cliente = Cliente.get_by_id(cliente_id)
         return render_template('detalhe_cliente.html', cliente=cliente)


@cliente_route.route('/<int:cliente_id>/edit')
def form_edit_cliente(cliente_id):
         #formulario para editar cliente

        cliente = Cliente.get_by_id(cliente_id)
        return render_template('form_cliente.html', cliente=cliente)

@cliente_route.route('/<int:cliente_id>/update', methods=['PUT'])
def atualizar_cliente(cliente_id):
        #atualizar informações cliente
        cliente_editado = None
        
        # Obter dados do formulario de edicao
        data = request.json


         # Obter usuario pelo id
        cliente_editado = Cliente.get_by_id(cliente_id)
        cliente_editado.nome = data['nome']
        cliente_editado.email = data['email']
        cliente_editado.telefone = data['telefone']
        cliente_editado.endereco = data['endereco']
        cliente_editado.pedido = data['pedido']
        cliente_editado.save()



        # editar usuario      
        return render_template( 'item_cliente.html', cliente=cliente_editado)
                
@cliente_route.route('/<int:cliente_id>/delete', methods=['DELETE'])
def deletar_cliente(cliente_id):
         #Deletar cliente
        
        cliente_editado = Cliente.get_by_id(cliente_id)
        Cliente.delete_instance()
        Cliente.delete.save()

        return {'deleted': 'ok'}
