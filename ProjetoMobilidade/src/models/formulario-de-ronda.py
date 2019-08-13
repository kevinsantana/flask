from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired

class FormularioDeRonda(FlaskForm):
    tecnico
    escala
    estacao
    portas_plataforma = BooleanField('Portas de Plataforma')
    vetilacao_principal
    inspecao_gerador
    horimetro
    numero_partidas
    bloqueios = BooleanField('Bloqueios')
    pa = BooleanField('Sistema de Som/Public Address')
    ar_condicionado_salas_tecnicas = BooleanField('Ar condicionado das Salas Técnicas')
    elevadores_interfones = BooleanField('Elevadores e Interfones')
    sistema_de_bombas = BooleanField('Sistema de Bombas')
    ramais_e_totem_plataformas = BooleanField('Ramais e Totem das Plataformas')
    paineis_multimidia = BooleanField('Painéis Multimídia')
    concluir_enviar = SubmitField('Concluir e Enviar')
