from flask import Flask, escape, request, render_template
# more imports
# import numpy as np
# import keras
# import io
# import json
# import imageio
# import base64

app = Flask(__name__)

# runs at localhost 5000
@app.route('/')
def application():
    return render_template('drawingcanvas.html')

if __name__ == "__main__":
    app.run(debug = True)
    
    """
    def loadKerasModel():
    model = tf.keras.models.load_model('model-9924.h5')
    return model

    # load our model
    model = loadKerasModel()
    """
    
    # showing knowledge of how to convert the image drawn from client into greyscale and sending back data
    # not working so went with binary files created from tfjs converter instead
    
    """
    # request data from canvas
    imageData = request.get_json(force=True)

    # get image data from request (what you've drawn)
    encodedImageData = imageData['data']

    # 64 base image decoder
    decodedImageData = base64.b64decode(encodedImageData)

    # save as png file
    with open('drawing.png', 'wb') as im:
        im.write(decodedImageData)

    # read as greyscale
    im = imageio.imread('drawing.png', pilmode='L')
    
    # resize to 28 * 28
    imResized = np.array(Image.fromarray(im).resize((28,28)))
    
    
    # reshape canvas
    imReshaped = np.array(imResized, dtype=np.float32).reshape(1,784)
    imReshaped /=255
    
    with sess.as_default():
        with graph.as_default():        
            predictions = model.predict(imReshaped)

    print("predictions")
    print(np.argmax(predictions))

    # give response to localhost:5000
    response = { 'returnData' : str(np.argmax(predictions)) }

    # show prediction
    json_dump = json.dumps({ 'returnData' : predictions }, cls=NumpyEncoder)
    print(json_dump)    

    return response
    
    class NumpyEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, np.ndarray):
            return obj.tolist()
        return json.JSONEncoder.default(self, obj)
        
    """
