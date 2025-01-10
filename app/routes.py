from flask import Flask, render_template, request, redirect, url_for, flash
from app.models import db, Paciente, Consulta, Exame, Medico, AgendaMedica, Usuario, LogAtividade

app = Flask(__name__)

# Configurações iniciais do Flask
def configure_app(app):
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://usuario:senha@localhost/SistemaHospitalar'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.secret_key = 'sua_chave_secreta'
    db.init_app(app)

configure_app(app)

# Rotas para Pacientes
@app.route('/pacientes', methods=['GET', 'POST'])
def pacientes():
    if request.method == 'POST':
        nome = request.form['nome']
        idade = request.form['idade']
        genero = request.form['genero']
        historico_medico = request.form['historico_medico']
        novo_paciente = Paciente(nome=nome, idade=idade, genero=genero, historico_medico=historico_medico)
        db.session.add(novo_paciente)
        db.session.commit()
        flash('Paciente cadastrado com sucesso!')
        return redirect(url_for('pacientes'))

    lista_pacientes = Paciente.query.all()
    return render_template('pacientes.html', pacientes=lista_pacientes)

# Rotas para Consultas
@app.route('/consultas', methods=['GET', 'POST'])
def consultas():
    if request.method == 'POST':
        paciente_id = request.form['paciente_id']
        data_hora = request.form['data_hora']
        medico = request.form['medico']
        descricao = request.form['descricao']
        nova_consulta = Consulta(paciente_id=paciente_id, data_hora=data_hora, medico=medico, descricao=descricao)
        db.session.add(nova_consulta)
        db.session.commit()
        flash('Consulta agendada com sucesso!')
        return redirect(url_for('consultas'))

    lista_consultas = Consulta.query.all()
    lista_pacientes = Paciente.query.all()
    return render_template('consultas.html', consultas=lista_consultas, pacientes=lista_pacientes)

# Rotas para Exames
@app.route('/exames', methods=['GET', 'POST'])
def exames():
    if request.method == 'POST':
        consulta_id = request.form['consulta_id']
        tipo_exame = request.form['tipo_exame']
        resultados = request.form['resultados']
        nova_exame = Exame(consulta_id=consulta_id, tipo_exame=tipo_exame, resultados=resultados)
        db.session.add(nova_exame)
        db.session.commit()
        flash('Exame registrado com sucesso!')
        return redirect(url_for('exames'))

    lista_exames = Exame.query.all()
    lista_consultas = Consulta.query.all()
    return render_template('exames.html', exames=lista_exames, consultas=lista_consultas)

# Rotas para Médicos
@app.route('/medicos', methods=['GET', 'POST'])
def medicos():
    if request.method == 'POST':
        nome = request.form['nome']
        especialidade = request.form['especialidade']
        contato = request.form['contato']
        novo_medico = Medico(nome=nome, especialidade=especialidade, contato=contato)
        db.session.add(novo_medico)
        db.session.commit()
        flash('Médico cadastrado com sucesso!')
        return redirect(url_for('medicos'))

    lista_medicos = Medico.query.all()
    return render_template('medicos.html', medicos=lista_medicos)

# Rotas para Agenda Médica
@app.route('/agenda', methods=['GET', 'POST'])
def agenda():
    if request.method == 'POST':
        medico_id = request.form['medico_id']
        data_hora = request.form['data_hora']
        disponibilidade = request.form['disponibilidade']
        nova_agenda = AgendaMedica(medico_id=medico_id, data_hora=data_hora, disponibilidade=disponibilidade)
        db.session.add(nova_agenda)
        db.session.commit()
        flash('Agenda criada com sucesso!')
        return redirect(url_for('agenda'))

    lista_agenda = AgendaMedica.query.all()
    lista_medicos = Medico.query.all()
    return render_template('agenda.html', agendas=lista_agenda, medicos=lista_medicos)

# Rotas para página inicial
@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
