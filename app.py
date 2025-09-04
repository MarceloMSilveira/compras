from flask import Flask, render_template, redirect, url_for, request
from sqlalchemy import text
from config_db import db
from models import Produto
from flask_migrate import Migrate

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql://marcelopostgresuser:73$Rps@localhost/compras"
db.init_app(app)
migrate = Migrate(app,db)

with app.app_context():
    db.create_all()
    

@app.route('/')
def home():
    return '<p>Test</p>'

@app.route('/addProds')
def add_prods():
    laranja = Produto(nome='laranja', quantidade=3)
    ovo = Produto(nome='ovo caipira', quantidade= 36)
    manga = Produto(nome='manga', quantidade=1)

    db.session.add_all([laranja,ovo,manga])
    db.session.commit()
    return redirect(url_for('all_products'))

@app.route('/addNewProd')
def add_new_prod():
    nome = request.args.get('prod_nome')
    qtd = request.args.get('qtd')
    new_prod = Produto(nome=nome, quantidade=qtd)
    db.session.add(new_prod)
    db.session.commit()
    return redirect(url_for('all_products'))

@app.route('/all')
def all_products():
    produtos = db.session.execute(db.select(Produto)).scalars()
    return render_template('allProducts.html', produtos=produtos)

@app.route('/delete')
def delete_prod():
    prod_name = request.args.get('produto')
    produto = db.session.execute(db.select(Produto).filter_by(nome=prod_name)).scalar()
    print(f"{produto.nome} foi deletado!")
    db.session.delete(produto)
    db.session.commit()
    return redirect(url_for('all_products'))

@app.route('/update')
def update():
    nome_atual = request.args.get('nome_atual')
    novo_nome = request.args.get('novo_nome')
    produto = db.session.execute(db.select(Produto).filter_by(nome=nome_atual)).scalar()
    produto.nome=novo_nome
    db.session.commit()
    return redirect(url_for('all_products'))