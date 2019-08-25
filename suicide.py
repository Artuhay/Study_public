# coding: utf-8
import sys
import json
from ibm_watson import ToneAnalyzerV3
from PyQt5 import QtWidgets
from PyQt5.QtGui import *
import mainwindow

def RepresentsFloat(s):
    try:
        float(s)
        return True
    except ValueError:
        return False

def get_features(self, response, threshold):
    watson_output = QStandardItemModel()
    expert_quality = QStandardItemModel()
    i = 0
    max_for_each_sentence = 0.0
    max_for_document = 0.0
    for r in response["document_tone"]["tones"]:
        i +=1
        if(float(r["score"])>float(threshold) and str(r["tone_name"]) == "Sadness"):
            if(float(r["score"]) > max_for_document):
                max_for_document = float(r["score"])
            answer_string = "Document tone number " + str(i) + ", where score: " + str(r["score"]) + ", tone_name: " + str(r["tone_name"])
            item = QStandardItem(answer_string)
            watson_output.appendRow(item)
        if(float(r["score"])>float(threshold) and str(r["tone_name"]) == "Fear"):
            if(float(r["score"]) > max_for_document):
                max_for_document = float(r["score"])
            answer_string = "Document tone number " + str(i) + ", where score: " + str(r["score"]) + ", tone_name: " + str(r["tone_name"])
            item = QStandardItem(answer_string)
            watson_output.appendRow(item)

    if "sentences_tone" in response.keys():
        for r in response["sentences_tone"]:
            for rr in r["tones"]:
                if(float(rr["score"])>float(threshold) and str(rr["tone_name"]) == "Sadness"):
                    if(float(rr["score"]) > max_for_each_sentence):
                        max_for_each_sentence = float(rr["score"])
                    answer_string = "Sentence number " + str(r["sentence_id"]) + ", where score: " + str(rr["score"]) + ", tone_name: " + str(rr["tone_name"])
                    item = QStandardItem(answer_string)
                    watson_output.appendRow(item)
        self.listView.setModel(watson_output)

    if (max_for_document > 0.7 or max_for_each_sentence > 0.91):
        expert_quality.appendRow(QStandardItem("This man need help! Immediatly!"))
    elif(max_for_document > 0.65):
        expert_quality.appendRow(QStandardItem("No problem, but he should go to doctor!"))
    else:
        expert_quality.appendRow(QStandardItem("It's normal emotions."))
    self.listView1.setModel(expert_quality)


class ExampleApp(QtWidgets.QMainWindow, mainwindow.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.tone_analizes)

    def tone_analizes(self):
        self.listView.reset()
        review_text = self.plainTextEdit.toPlainText()
        threshold = self.thresh_text.toPlainText()

        tone_analyzer = ToneAnalyzerV3(
            version='2018-11-16',
            iam_apikey="Yx2IDL3UUBuyEMznwFz9IDDDk12JUD_gL5iNkl1rhwMM",
            url='https://gateway-lon.watsonplatform.net/tone-analyzer/api'
        )
        #text = 'Team, I feel fear and sad.'
        if (str(review_text) and RepresentsFloat(threshold)):
            tone_analysis = tone_analyzer.tone(
                {'text': review_text},
                tones = 'emotion',
                sentences=True,
                content_type='application/json'
            ).get_result()

            print(json.dumps(tone_analysis, indent=2))

            get_features(self, tone_analysis, threshold)
            answer = json.dumps(tone_analysis, indent=2)


def main():
    app = QtWidgets.QApplication(sys.argv)
    window = ExampleApp()
    window.show()
    app.exec_()

if __name__ == '__main__':
    main()





