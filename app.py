from flask import Flask, render_template, request, redirect
from models import db, YellowpagesModel
 
app = Flask(__name__)
 
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///yellow-pages.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)
 
@app.before_first_request
def create_table():
    db.create_all()
 
@app.route('/create' , methods = ['GET','POST'])
def create():
    if request.method == 'GET':
        return render_template('create.html')
 
    if request.method == 'POST':
        name = request.form['name']
        company_name = request.form['company_name']
        email = request.form['email']
        number = request.form['number']
        address = request.form['address']
        yellowpages = YellowpagesModel(name=name, company_name=company_name, email=email, number=number, address=address)
        db.session.add(yellowpages)
        db.session.commit()
        return redirect('/')
 
 
@app.route('/')
def read_all():
    yellowpages = YellowpagesModel.query.all()
    return render_template('list.html', yellowpages=yellowpages)
 
 
@app.route('/data/<int:id>/update',methods = ['GET','POST'])
def update(id):
    yellowpages = YellowpagesModel.query.filter_by(id=id).first()
    if request.method == 'POST':
        if yellowpages:
            db.session.delete(yellowpages)
            db.session.commit()
            name = request.form['name']
            company_name = request.form['company_name']
            email = request.form['email']
            number = request.form['number']
            address = request.form['address']
            yellowpages = YellowpagesModel(name=name, company_name=company_name, email=email, number=number, address=address)
            db.session.add(yellowpages)
            db.session.commit()
            return redirect('/')
        return f"Yellowpages with id = {id} Does not exist"
 
    return render_template('update.html', yellowpages=yellowpages)
 
 
@app.route('/data/<int:id>/delete', methods=['GET'])
def delete(id):
    yellowpages = YellowpagesModel.query.filter_by(id=id).first()
    if request.method == 'GET':
        if yellowpages:
            db.session.delete(yellowpages)
            db.session.commit()
            return redirect('/')
        abort(404)
 
    return redirect('/')

if __name__ == "__main__":
    app.run(host='localhost', port=5000, debug=True)