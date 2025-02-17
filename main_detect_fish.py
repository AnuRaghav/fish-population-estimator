from roboflow import Roboflow
import string
import random
import json
import os
import shutil
    
rf = Roboflow(api_key="K57tUktyTD0l9DKKeQBE")
workspace_ = rf.workspace()
project = workspace_.project("detect-for-me")
version = project.version(1)
model = version.model

def obj_model_predict(image):
    res = 'predictions_' + ''.join(random.choices(string.ascii_uppercase + string.digits, k=7)) + '.jpg'
    base_dir = os.path.dirname(os.path.abspath(__file__))

    source_path = os.path.join(base_dir, res)
    predictions_dir = os.path.join(base_dir, "static", "predictions")
    destination_path = os.path.join(predictions_dir, res)


    os.makedirs(predictions_dir, exist_ok=True)

    prediction = model.predict(image)
    prediction.save(output_path=source_path)  


    if not os.path.exists(source_path):
        print(f"ERROR: Prediction file {source_path} not created!")
        return None, "0"


    shutil.move(source_path, destination_path)


    count = len(prediction.json().get('predictions', []))

    return f"/static/predictions/{res}", str(count)