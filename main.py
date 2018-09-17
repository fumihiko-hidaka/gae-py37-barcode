from io import BytesIO

import barcode
from barcode.writer import ImageWriter
from flask import Flask, send_file

app = Flask(__name__)


@app.route('/')
def index():
    byte_io = BytesIO()

    ean = barcode.get_barcode('ean13', '4902102072618', writer=ImageWriter())
    ean.write(byte_io)

    byte_io.seek(0)

    return send_file(
        byte_io,
        as_attachment=True,
        attachment_filename='barcode.png',
        mimetype='image/png',
    )


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080, debug=True)
