from flask import Flask, render_template, request
# from api.addRow import addRow
# from api.woo_requests.product_details_by_name import product_details_by_name

app = Flask(__name__)

@app.route('/')
def index():
    # return render_template('index.html')
    return "<h1>Welcome to Geeks for Geeks</h1>"


# @app.route('/success', methods=['POST', 'GET'])
# def success():
#     if request.method == 'POST':
#         main_field = request.form['main_field']
#         print(main_field)
#         data = product_details_by_name(main_field)
#         addRow(data)
#     return render_template('success.html')

# Debug only
# app.run(host='0.0.0.0', port=91)