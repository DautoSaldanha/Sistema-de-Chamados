from rolepermissions.roles import AbstractUserRole

class Administrador(AbstractUserRole):
    available_permissions = {
        'criar_usuario': True,
        'modificar_usuario': True,
        'deletar_usuario': True,
        'visualizar_todos_chamados': True,
        'alterar_status_chamados': True,
    }

class Atendente(AbstractUserRole):
    available_permissions = {
        'responder_chamados': True,
        'visualizar_todos_chamados': True,
        'alterar_status_chamados': True,
    }

class Cliente(AbstractUserRole):
    available_permissions = {
        'criar_chamado': True,
        'visualizar_proprios_chamados': True,
    }