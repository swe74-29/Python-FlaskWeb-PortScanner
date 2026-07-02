from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']="sqlite:///scans.db"
db=SQLAlchemy(app)
class ScanHistory(db.Model):
    id=db.Column(db.Integer, primary_key=True)
    ip_address=db.Column(db.String(50), nullable=False)
    open_ports=db.Column(db.String(200))
    timestamp=db.Column(db.DateTime,default=datetime.utcnow)

@app.route("/")
def home_page():
    recent_scans = ScanHistory.query.order_by(ScanHistory.id.desc()).limit(7).all()
    return render_template('index.html', recent_scans=recent_scans)
@app.route('/DOCS')
def DOCS():
   return 'NOT MADE YET!'
@app.route('/GITHUB')
def GITHUB():
   return 'NOT MADE YET!'
@app.route('/ABOUT')
def ABOUT():
   return 'NOT MADE YET!'
@app.route('/MIT_License')
def MIT_License():
   return 'NOT MADE YET!'
@app.route('/Source_Code')
def Source_Code():
   return 'NOT MADE YET!'
@app.route('/Report_Bug')
def Report_Bug():
   return 'NOT MADE YET!'
if __name__ == "__main__":
 app.run(debug=True)



 