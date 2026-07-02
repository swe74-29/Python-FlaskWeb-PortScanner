from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from scanner import scan_ports, format_ports
import socket

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///scans.db'
app.secret_key = 'change-this-to-something-random'
db = SQLAlchemy(app)


class ScanHistory(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    ip_address = db.Column(db.String(50), nullable=False)
    open_ports = db.Column(db.String(200))
    timestamp = db.Column(db.DateTime, default=datetime.utcnow)


with app.app_context():
    db.create_all()


@app.route('/')
def home_page():
    recent_scans = ScanHistory.query.order_by(ScanHistory.id.desc()).limit(7).all()
    return render_template('index.html', recent_scans=recent_scans)


@app.route('/scan', methods=['POST'])
def scan():
    target = request.form.get('target', '').strip()
    port_start = int(request.form.get('port_start', 1))
    port_end = int(request.form.get('port_end', 1024))
    scan_mode = request.form.get('scan_mode', 'tcp')

    if not target:
        flash('Target host is required.')
        return redirect(url_for('home_page'))
    if not (1 <= port_start <= port_end <= 65535):
        flash('Invalid port range.')
        return redirect(url_for('home_page'))
    if port_end - port_start > 5000:
        flash('Range too large — keep it under 5000 ports for now.')
        return redirect(url_for('home_page'))

    try:
        ip, open_ports = scan_ports(target, port_start, port_end, mode=scan_mode)
    except socket.gaierror:
        flash(f'Could not resolve host: {target}')
        return redirect(url_for('home_page'))

    record = ScanHistory(ip_address=ip, open_ports=format_ports(open_ports))
    db.session.add(record)
    db.session.commit()

    return redirect(url_for('home_page'))


@app.route('/docs')
def docs():
    return render_template('docs.html')


@app.route('/github')
def github():
    return render_template('github.html')


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/license')
def license_page():
    return render_template('license.html')


@app.route('/source')
def source():
    return render_template('source.html')


@app.route('/report_bug')
def report_bug():
    return 'NOT MADE YET!'


if __name__ == "__main__":
    app.run(debug=True)