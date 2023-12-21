# from flask import Flask, render_template, request
# from addRow import addRow
# from woo_requests.product_details_by_name import product_details_by_name


# app = Flask(__name__)

# @app.route('/')
# def index():
#     return render_template('index.html')


# @app.route('/success', methods=['POST', 'GET'])
# def success():
#     if request.method == 'POST':
#         main_field = request.form['main_field']
#         print(main_field)
#         data = product_details_by_name(main_field)
#         addRow(data) 
#     return render_template('success.html')

# # Debug only
# # app.run(host='0.0.0.0', port=81)

from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return 'Hello, World!'

@app.route('/about')
def about():
    return 'About'

