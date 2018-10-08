import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np
from sklearn import svm, metrics
from sklearn.externals import joblib

'''
    Yes, this is the dumbest model. But I wanted to learn how to do things in scikit learn
    The gen1 pokemon sprites are pretty set, 
'''
images = []
for i in range(1, 152):
    print('Processing pokemon ' + str(i))
    poke = str(i)
    if i < 10:
        poke = "00" + poke
    elif i >= 10 and i < 100:
        poke = "0" + poke
    img1 = mpimg.imread('sprites/Spr_1b_' + poke  + '.png')
    flt1 = img1.flatten()
    pokemon = { 'data' : flt1, 'id': i}
    images.append(pokemon)

    img = mpimg.imread('sprites/' + str(i)+ '.PNG')
    flt = img.flatten()
    for i in range(len(flt1) - len(flt)):
        flt = np.append(flt,0)
    pokemon = { 'data' : flt, 'id': i}
    images.append(pokemon)

x_data = list(map(lambda x: x['data'],images))
y_data = list(map(lambda x: x['id'], images))

classifier = svm.SVC(gamma=0.001)
classifier.fit(x_data, y_data)

joblib.dump(classifier, 'outputs/pokemon.mdl',compress=9)




