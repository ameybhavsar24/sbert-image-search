# sbert-image-search

**Do you know how Google's Image search actually works?**


I built an image search app that lets you search from **25,000 nature-themed photos** from Unsplash.

 The application uses [**SentenceTransformers**](https://www.sbert.net/examples/applications/image-search/README.html), a Python framework for state-of-the-art sentence, text and image embeddings. 
It provides models that allow embedding images and text into the same vector space. This allows us to find similar photos and implement image search.


This app uses Flask as the server and TailwindCSS for frontend components.

## Installation
1. Clone this repository.
```
git clone https://github.com/ameybhavsar24/sbert-image-search.git
```
2. Create a python virtual environment and activate it.
```
python -m venv env
(for powershell users)
.\env\Scripts\Activate.ps1
```
3. Install the project dependencies from requirements.txt.
```
pip install -r requirements.txt
```
4. Download the required models (pickle files) from [Google Drive](https://drive.google.com/drive/folders/1TFaxBYLdMU8R-cRvBL6cpU5GlaJk2Hbt?usp=sharing) in a /models folder in the root directory.
You should have the following folder structure for models:
```
sbert-image-search/
    - models/
        - image_embeddings.pkl
        - image_names.pkl
        - text_to_image_cpu.model.pkl

```
5. Run the project, it should start an server at [127.0.0.1:5000](http://127.0.0.1:5000).
```
python app.py
```