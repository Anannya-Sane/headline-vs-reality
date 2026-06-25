from transformers import pipeline

finbert = pipeline("text-classification",
                   model="ProsusAI/finbert")

def get_sentiment(headline):
    result = finbert(headline)[0]
    label = result['label']
    score = round(result['score'] * 100, 2)
    return label, score
    