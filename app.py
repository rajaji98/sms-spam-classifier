from flask import Flask , render_template , request
import pickle   #load the model

app = Flask(__name__)

# load the model
model = pickle.load(open('save_model.sav','rb'))
tf_vec = pickle.load(open('vectorizer.pkl', 'rb'))

@app.route('/')
def home():
    result = ''
    return render_template('index.html')

@app.route('/predict', methods = [ "POST"])
def predict():
    text = request.form.get('input')
    text_vec = tf_vec.transform([text])
    result = model.predict(text_vec)[0]
    return render_template( 'index.html', prediction_text = "This message is {}".format(result))

if __name__ == "__main__":
    app.run( debug= True )

