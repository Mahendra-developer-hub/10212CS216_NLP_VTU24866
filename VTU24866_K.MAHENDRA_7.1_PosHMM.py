import warnings
warnings.filterwarnings("ignore")

import nltk
from nltk.tag import hmm

train_data = [[("Will","MD"),("Jane","NNP"),("see","VB"),("the","DT"),("dog","NN")]]

trainer = hmm.HiddenMarkovModelTrainer()
tagger = trainer.train(train_data)

sentence = ["Will","Jane","see","the","dog"]

print(tagger.tag(sentence))