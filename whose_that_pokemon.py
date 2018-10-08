import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np
from sklearn import svm, metrics
from sklearn.externals import joblib
import json
import sys
from functools import reduce

json_file = open('outputs/pokemon_data.json', 'r')
json_data = json.loads(json_file.read())
pokemon_by_id = {x['id']: x['name'] for x in json_data}

pokemon_to_predict = int(sys.argv[-1])
poke = str(pokemon_to_predict)
if pokemon_to_predict < 10:
    poke = "00" + poke
elif pokemon_to_predict >= 10 and pokemon_to_predict < 100:
    poke = "0" + poke

figure = plt.figure()
a = figure.add_subplot(1,2,1)
img1 = mpimg.imread('sprites/Spr_1b_' + poke  + '.png')
flt1 = img1.flatten()
plt.imshow(img1)
a.set_title('Front')
pokemon_model = joblib.load('outputs/pokemon.mdl')
prediction_1 = pokemon_model.predict([flt1])[0]

a = figure.add_subplot(1,2,2)
img2 = mpimg.imread('sprites/' + str(pokemon_to_predict) + '.png')
flt2 = img1.flatten()
plt.imshow(img2)
a.set_title('Back')
pokemon_model = joblib.load('outputs/pokemon.mdl')
prediction_2 = pokemon_model.predict([flt2])[0]

print('From the front: It\'s ' + pokemon_by_id[prediction_1])
print('From the back: It\'s ' + pokemon_by_id[prediction_2])
plt.show()