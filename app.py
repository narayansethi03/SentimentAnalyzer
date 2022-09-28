from flask import Flask, request, url_for, render_template
import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer
nltk.download('vader_lexicon')
app=Flask(__name__)

@app.route('/',methods=['GET','POST'])
def main():
	if request.method == "POST" :
		text=request.form.get("text")
		model=SentimentIntensityAnalyzer()
		score=model.polarity_scores(text)
		if score['neg']!=0:
			return render_template ('home.html',message='_Negative_Statement')
		else:
			return render_template ('home.html',message='_Positve_Statement')	
	return render_template('home.html')

if __name__ == '__main__':
	app.run(host='0.0.0.0')