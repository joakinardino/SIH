from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, TextAreaField, SelectField, DateTimeField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Length, EqualTo

# Formulário para cadastro de pacientes
class PacienteForm(FlaskForm):
    nome = StringField('Nome', validators=[DataRequired(), Length(max=100)])
    idade = IntegerField('Idade', validators=[DataRequired()])
    genero = SelectField('Gênero', choices=[('Masculino', 'Masculino'), ('Feminino', 'Feminino'), ('Outro', 'Outro')], validators=[DataRequired()])
    historico_medico = TextAreaField('Histórico Médico')
    submit = SubmitField('Cadastrar')

# Formulário para agendamento de consultas
class ConsultaForm(FlaskForm):
    paciente_id = SelectField('Paciente', coerce=int, validators=[DataRequired()])
    data_hora = DateTimeField('Data e Hora', format='%Y-%m-%d %H:%M:%S', validators=[DataRequired()])
    medico = StringField('Médico', validators=[DataRequired(), Length(max=100)])
    descricao = TextAreaField('Descrição')
    submit = SubmitField('Agendar')

# Formulário para registro de exames
class ExameForm(FlaskForm):
    consulta_id = SelectField('Consulta', coerce=int, validators=[DataRequired()])
    tipo_exame = StringField('Tipo de Exame', validators=[DataRequired(), Length(max=100)])
    resultados = TextAreaField('Resultados')
    submit = SubmitField('Registrar')

# Formulário para cadastro de médicos
class MedicoForm(FlaskForm):
    nome = StringField('Nome', validators=[DataRequired(), Length(max=100)])
    especialidade = StringField('Especialidade', validators=[DataRequired(), Length(max=100)])
    contato = StringField('Contato', validators=[Length(max=50)])
    submit = SubmitField('Cadastrar')

# Formulário para gerenciamento de agenda médica
class AgendaMedicaForm(FlaskForm):
    medico_id = SelectField('Médico', coerce=int, validators=[DataRequired()])
    data_hora = DateTimeField('Data e Hora', format='%Y-%m-%d %H:%M:%S', validators=[DataRequired()])
    disponibilidade = SelectField('Disponibilidade', choices=[('Disponível', 'Disponível'), ('Indisponível', 'Indisponível')], validators=[DataRequired()])
    submit = SubmitField('Salvar')

# Formulário para login de usuários
class LoginForm(FlaskForm):
    username = StringField('Usuário', validators=[DataRequired(), Length(max=50)])
    senha = PasswordField('Senha', validators=[DataRequired()])
    submit = SubmitField('Entrar')

# Formulário para registro de usuários
class UsuarioForm(FlaskForm):
    username = StringField('Usuário', validators=[DataRequired(), Length(max=50)])
    senha = PasswordField('Senha', validators=[DataRequired(), Length(min=6)])
    confirmar_senha = PasswordField('Confirmar Senha', validators=[DataRequired(), EqualTo('senha', message='As senhas devem ser iguais.')])
    tipo_usuario = SelectField('Tipo de Usuário', choices=[('Admin', 'Admin'), ('Medico', 'Medico'), ('Recepcionista', 'Recepcionista')], validators=[DataRequired()])
    submit = SubmitField('Cadastrar')
