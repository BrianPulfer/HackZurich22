from model.utils import NEWS_CLASSES
from transformers import pipeline
from happytransformer import HappyTextToText, TTSettings


summ_pipeline = pipeline("summarization")
class_pipeline = pipeline("zero-shot-classification",  model="facebook/bart-large-mnli")
happy_tt = HappyTextToText("T5", "vennify/t5-base-grammar-correction")
args = TTSettings(num_beams=5, min_length=1)


def summarize(news_batch):    
    return summ_pipeline(news_batch)
    

def classify(news_batch):
    return class_pipeline(news_batch, candidate_labels=NEWS_CLASSES)

def grammar(text):
    return happy_tt.generate_text(text, args=args).text
