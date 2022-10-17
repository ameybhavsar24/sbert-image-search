from flask import Flask, render_template, request
from sentence_transformers import util
import pickle
import os 
app = Flask(__name__)

model = pickle.load(open('models/text_to_image_cpu.model.pkl', 'rb'))
img_embed = pickle.load(open('models/image_embeddings.pkl', 'rb'))
img_names = pickle.load(open('models/image_names.pkl', 'rb'))

@app.route('/')
def hello():
    return render_template('index.html')
@app.route('/search')
def search():
    query = request.args.get('q')
    res = get_images(query)
    return render_template('search.html', query=query, hits=res)

def get_images(query, k=100):
    query_emd = model.encode([query], convert_to_tensor=True, show_progress_bar=False)
    matches = util.semantic_search(query_emd, img_embed, top_k=k)[0]
    hits = []
    for match in matches:
        img_path = img_names[match['corpus_id']]
        img_name = os.path.basename(img_path)
        hits.append(img_name)
    return hits

if __name__ == '__main__':
    app.run(threaded=True, port=5000, debug = True)
    