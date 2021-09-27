# import the necessary dependencies

import pickle
# from sklearn.preprocessing import StandardScaler
# from sklearn.linear_model import LogisticRegression
from flask import Flask, render_template, request
from flask_cors import cross_origin

app = Flask(__name__)  # initializing flask app


@app.route('/', methods=['GET'])  # rout to display home page
@cross_origin()
def homepage():
    return render_template("index.html")


@app.route('/predict', methods=['POST', 'GET'])  # rout to show prediction in web ui
@cross_origin()
def index():
    if request.method == 'POST':
        try:

            avg_rss_12 = float(request.form['avg_rss_12'])
            var_rss_12 = float(request.form['var_rss_12'])
            avg_rss_13 = float(request.form['avg_rss_13'])
            var_rss_13 = float(request.form['var_rss_13'])
            avg_rss_23 = float(request.form['avg_rss_23'])
            var_rss_23 = float(request.form['var_rss_23'])
            # scalar = StandardScaler()
            # data = scalar.transform([[avg_rss_12,var_rss_12,avg_rss_13,var_rss_13,avg_rss_23,var_rss_23]])
            # print(data)
            model = pickle.load(open('activity_recognition.pickle', 'rb'))
            prediction = model.predict([[avg_rss_12, var_rss_12, avg_rss_13, var_rss_13, avg_rss_23, var_rss_23]])
            print('prediction is {}'.format(prediction))
            return render_template('results.html', prediction=prediction[0])

        except Exception as e:
            print('The Exception message is: ', e)
            return 'Something is wrong'

    else:
        return render_template('index.html')


if __name__ == "__main__":
    # app.run(host='127.0.0.1', port=8001, debug=True)
    app.run(debug=True)  # running the app
