import numpy as np
from flask import Flask, request, render_template
import pickle
import pandas as pd
import re 
from string import punctuation
import nltk
nltk.download('omw-1.4')
nltk.download('stopwords')
nltk.download('punkt')
nltk.download('wordnet')

app = Flask(__name__)
model = pickle.load(open('modelSEExtraTree.pkl', 'rb'))
    
# Load and read file
df = pd.read_csv("mcf5SE_fullstopword_TFIDF.csv")
df = df.iloc[:1]
df.drop(df.columns[[0,1,2]], axis=1, inplace=True)
dflen = len(df.columns)
df.reset_index(drop=True)
    
col_jd = range(0,19)
df_jd = df.copy()
df_jd.drop(df.columns[col_jd], axis=1, inplace=True)


col_ind = range(19,dflen)
df_ind = df.copy()
df_ind.drop(df_ind.columns[col_ind], axis=1, inplace=True)
df_ind.drop(df_ind.columns[[0,1]], axis=1, inplace=True)



@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict',methods=['POST'])
def predict():
    
    
    input0 = request.form.get("job_title")
    input1 = request.form.get('exp')
    input2 = request.form.get('level')
    input3 = request.form.get('industry')
    input4 = request.form.get('Job Description')
    
    input4 = str(input4)
    text4 = input4.lower()  # Lowercase text
    text4 = re.sub(f"[{re.escape(punctuation)}]", " ", text4)  # Remove punctuation
    text4 = " ".join(text4.split())  # Remove extra spaces, tabs, and new lines
    text4 = re.sub(r'\d+', '', text4)
    tokens4 = nltk.word_tokenize(text4)  # tokenize
    WNlemma = nltk.WordNetLemmatizer()
    tokens4 = [WNlemma.lemmatize(t) for t in tokens4] # lemmatize
    #stops = set(stopwords.words('english'))
    #tokens4 = [word for word in tokens4 if word not in stops] # remove stopword
    input4 = " ".join(tokens4) # join all token separated by a space so that it is a document
    input4 = input4.split()
    #print(input4)
    
    
    input3_array = []
    for column_headers in df_ind.columns:
        if column_headers in input3:
          #print(column_headers)
          input3_array.append(1)
          #print (1)
        else:
          #print(column_headers)
          input3_array.append(0)
          #print (0)
    
    input4_array = []
    for column_headers in df_jd.columns:
        if column_headers in input4:
          #print(column_headers)
          input4_array.append(1)
          #print (1)
        else:
          #print(column_headers)
          input4_array.append(0)
          #print (0)
    
    
    
    
    int_features = list(input1) + list(input2) + input3_array + input4_array 
    final_features = pd.DataFrame(int_features).transpose()
    final_features.columns = df.columns
    prediction = model.predict(final_features)
    output = prediction[0]
    return render_template('index.html', prediction_text='Salary should be $ {}'.format(output))


if __name__ == "__main__":
    app.run(debug=True)
