from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()

# Modelo para tabela de Pacientes
class Paciente(db.Model):
    __tablename__ = 'pacientes'
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    idade = db.Column(db.Integer, nullable=False)
    genero = db.Column(db.Enum('Masculino', 'Feminino', 'Outro'), nullable=False)
    historico_medico = db.Column(db.Text)
    consultas = db.relationship('Consulta', backref='paciente', lazy=True)

# Modelo para tabela de Consultas
class Consulta(db.Model):
    __tablename__ = 'consultas'
    id = db.Column(db.Integer, primary_key=True)
    paciente_id = db.Column(db.Integer, db.ForeignKey('pacientes.id'), nullable=False)
    data_hora = db.Column(db.DateTime, nullable=False)
    medico = db.Column(db.String(100), nullable=False)
    descricao = db.Column(db.Text)
    status = db.Column(db.Enum('Agendada', 'Concluída', 'Cancelada'), default='Agendada')
    exames = db.relationship('Exame', backref='consulta', lazy=True)

# Modelo para tabela de Exames
class Exame(db.Model):
    __tablename__ = 'exames'
    id = db.Column(db.Integer, primary_key=True)
    consulta_id = db.Column(db.Integer, db.ForeignKey('consultas.id'), nullable=False)
    tipo_exame = db.Column(db.String(100), nullable=False)
    resultados = db.Column(db.Text)
    imagem_exame = db.Column(db.LargeBinary)

# Modelo para tabela de Médicos
class Medico(db.Model):
    __tablename__ = 'medicos'
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    especialidade = db.Column(db.String(100), nullable=False)
    contato = db.Column(db.String(50))
    agenda = db.relationship('AgendaMedica', backref='medico', lazy=True)

# Modelo para tabela de Agenda Medica
class AgendaMedica(db.Model):
    __tablename__ = 'agenda_medica'
    id = db.Column(db.Integer, primary_key=True)
    medico_id = db.Column(db.Integer, db.ForeignKey('medicos.id'), nullable=False)
    data_hora = db.Column(db.DateTime, nullable=False)
    disponibilidade = db.Column(db.Enum('Disponível', 'Indisponível'), default='Disponível')

# Modelo para tabela de Usuários
class Usuario(db.Model):
    __tablename__ = 'usuarios'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True, nullable=False)
    senha_hash = db.Column(db.String(255), nullable=False)
    tipo_usuario = db.Column(db.Enum('Admin', 'Medico', 'Recepcionista'), nullable=False)

# Modelo para tabela de Logs de Atividades
class LogAtividade(db.Model):
    __tablename__ = 'logs_atividades'
    id = db.Column(db.Integer, primary_key=True)
    usuario_id = db.Column(db.Integer, db.ForeignKey('usuarios.id'))
    acao = db.Column(db.String(255), nullable=False) 
    data_hora = db.Column(db.DateTime, default=datetime.utcnow)

