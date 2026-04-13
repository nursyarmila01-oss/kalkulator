from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    keuntungan = None

    if request.method == 'POST':
        modal = float(request.form['modal'])
        harga_jual = float(request.form['harga_jual'])
        jumlah = int(request.form['jumlah'])

        total_modal = modal * jumlah
        total_penjualan = harga_jual * jumlah
        keuntungan = total_penjualan - total_modal

    return render_template('index.html', keuntungan=keuntungan)

if __name__ == '__main__':
    app.run(debug=True)
    