from flask import Flask, render_template, request, redirect, url_for
import db

app = Flask(__name__)
db.init_db()

@app.route('/',  methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        db.add_device(request.form)
        return redirect(url_for('index'))
    devices = db.get_all_devices()
    return render_template('index.html', devices=devices)

@app.route('/edit/<int:device_id>', methods=['GET', 'POST'])
def edit_device(device_id):
    device = db.get_device(device_id)
    if request.method == 'POST':
        db.update_device(device_id, request.form)
        return redirect(url_for('index'))
    return render_template('edit.html', device=device)

@app.route('/delete/<int:device_id>', methods=['POST'])
def delete_device(device_id):
    db.delete_device(device_id)
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)