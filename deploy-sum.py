from flask import Flask, json, request, render_template
import logging
import re
logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)
from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer 
from sumy.summarizers.lex_rank import LexRankSummarizer
from gensim.summarization import summarize

summarizer = LexRankSummarizer()

app = Flask(__name__)
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/response/',methods = ['GET','POST'])
def response():
    if request.method=='POST':
        text_org = request.json['foo']
        text = json.loads(json.dumps(text_org))
        text = re.sub('[^A-Za-z0-9()[]]', ' ', str(text))
        text = text.lower()        
        if len(text.split())<=3:
            resp = ' '.join(['please give some more sentences.'])
            return resp
        else: 
            parser = PlaintextParser.from_string(text,Tokenizer('english'))
            sum_1 = summarizer(parser.document,10)
            sum_lex=[]
            for sent in sum_1:
                resp = sum_lex.append(str(sent))
                resp = ' '.join(resp)
            return resp


if __name__ == "__main__":
    print("**Starting Server...")
   
    #load_model()
    
    app.run(port=5002, debug=True)        
        
