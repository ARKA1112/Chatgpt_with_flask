from flask import Flask, request, Response, render_template
from PIL import Image
import io

app = Flask(__name__)



@app.route('/', methods=['POST','GET'])
def index():
    if request.method=='POST':
        text = request.form.get("text")
        size = request.form.get("size")
        meta = {'small':'256x256','medium':'512x512','large':'1024x1024'}
        image = imgen(prompt=text,size=meta[size])
        img_io = io.BytesIO()
        image.save(img_io,'PNG')
        img_io.seek(0)
        return Response(img_io, mimetype='image/png')
    return render_template("index.html")

def imgen(prompt,n=1,size='256x256',show_url=False):
    import openai
    from PIL import Image
    import requests
    from io import BytesIO
    import numpy as np
    import matplotlib.pyplot as plt
    
    
    
    resopose = openai.Image.create(
            prompt=prompt,
            n=n,
            size=size,
            api_key='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'
        )
    for i in range(n):
            image_url = resopose['data'][i]['url']

            url = image_url
            response = requests.get(url)
            img = Image.open(BytesIO(response.content))
            if show_url:
                print(url)
            return img
    
if __name__ == '__main__':
     app.run(debug=True)