from app import create_app, db

# Criar a aplicação
app = create_app()

# Comando para inicializar o banco de dados, se necessário
@app.before_first_request
def initialize_database():
    db.create_all()

if __name__ == '__main__':
    app.run(debug=True)
