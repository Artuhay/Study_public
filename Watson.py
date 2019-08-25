
# coding: utf-8

# In[1]:


import sys
from PyQt5 import QtWidgets
from PyQt5.QtGui import *
import mainwindow
import json
from watson_developer_cloud import NaturalLanguageUnderstandingV1
from watson_developer_cloud.natural_language_understanding_v1 import Features, KeywordsOptions


# In[ ]:


class ExampleApp(QtWidgets.QMainWindow, mainwindow.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.process_review)
    def process_review(self):
        self.listView.reset()
        self.listView_2.reset()
        review_text = self.plainTextEdit.toPlainText()
        natural_language_understanding = NaturalLanguageUnderstandingV1(
        version='2018-11-16',
        iam_apikey='DdKqDboeovObUYeC14EbqbhM2L5QSEXuVaece5OUOzpt',
        url='https://gateway-fra.watsonplatform.net/natural-language-understanding/api'
        )
        response = natural_language_understanding.analyze(
            text=review_text,
            features=Features(keywords=KeywordsOptions(sentiment=True,limit=15))).get_result()
        get_features(self, response)
        print(json.dumps(response, indent=2))
def main():
    app = QtWidgets.QApplication(sys.argv) 
    window = ExampleApp()  
    window.show()  
    app.exec_()  

if __name__ == '__main__':  
    main() 


# In[ ]:


def get_features(self, response):
    model_advantages = QStandardItemModel()
    model_disadvantages = QStandardItemModel()
    for r in response["keywords"]:
        item = QStandardItem(r["text"])
        if r["sentiment"]["score"] < (-0.4) and r["relevance"] > 0.5:
            model_disadvantages.appendRow(item)
        elif r["sentiment"]["score"] > 0.4 and r["relevance"] > 0.5:
            model_advantages.appendRow(item)
    self.listView.setModel(model_advantages)
    self.listView_2.setModel(model_disadvantages)

