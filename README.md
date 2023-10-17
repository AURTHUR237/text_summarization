# text_summarization
# to deploy the model on local host 
create a virtual environment 
acvtivate the environment 
u can see the code below
python -m venv summarizer-app
source summarizer-app/bin/activate  # On Windows, use `summarizer-app\Scripts\activate`
# install these packages 
flask
transformers 
nltk
gunicorn 
tensorflow 
torch
pip install flask transformers nltk gunicorn
pip install tensorflow 
pip install torch

open cmd and run the command 
python app.py 
to deploy it on local host 
it will run on Running on http://127.0.0.1:5000
open your browser and type localhost:5000


