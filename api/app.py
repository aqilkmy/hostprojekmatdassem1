from flask import Flask, render_template, request
import sympy as sp

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/integral-tak-tentu', methods=['GET', 'POST'])
def integral_tak_tentu():
    hasil = None
    soal = None
    if request.method == 'POST':
        try:
            func = request.form['func']
            x = sp.symbols('x')
            func_expr = sp.sympify(func)
            soal = sp.pretty(func_expr)  # Simpan ekspresi fungsi dalam format pretty
            integral = sp.integrate(func_expr, x)
            hasil = sp.pretty(integral)  # Simpan hasil integral dalam format pretty
        except (KeyError, sp.SympifyError) as e:
            hasil = "Masukkan Fungsi"
    return render_template('integral-tak-tentu.html', hasil=hasil, soal=soal)

@app.route('/integral-tentu', methods=['GET', 'POST'])
def integral_tentu():
    hasil = None
    soal = None
    a = None
    b = None
    if request.method == 'POST':
        try:
            func = request.form['func']
            a = request.form['bts-bwh']
            b = request.form['bts-ats']
            x = sp.symbols('x')
            func_expr = sp.sympify(func)
            soal = sp.pretty(func_expr)  # Simpan ekspresi fungsi dalam format pretty
            integral = sp.integrate((func_expr), (x,a,b))
            hasil = sp.pretty(integral)  # Simpan hasil integral dalam format pretty
        except (KeyError, sp.SympifyError) as e:
            hasil = "Masukkan Fungsi"
    return render_template('integral-tentu.html', hasil=hasil, soal=soal, a=a, b=b)

@app.route('/turunan', methods=['GET', 'POST'])
def turunan():
    hasil = None
    soal = None
    if request.method == 'POST':
        try:
            func = request.form['func']
            x = sp.symbols('x')
            func_expr = sp.sympify(func)
            soal = sp.pretty(func_expr)  # Simpan ekspresi fungsi dalam format pretty
            integral = sp.diff(func_expr)
            hasil = sp.pretty(integral)  # Simpan hasil integral dalam format pretty
        except (KeyError, sp.SympifyError) as e:
            hasil = "Masukkan Fungsi"
    return render_template('turunan.html', hasil=hasil, soal=soal)


if __name__ == '__main__':
    app.run(port=5000, debug=True)
