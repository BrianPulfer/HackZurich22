from utils import NEWS_CLASSES
from transformers import pipeline

summ_pipeline = pipeline("summarization")
class_pipeline = pipeline("zero-shot-classification",  model="facebook/bart-large-mnli")


def summarize(news_batch):    
    return summ_pipeline(news_batch)
    

def classify(news_batch):
    return class_pipeline(news_batch, candidate_labels=NEWS_CLASSES)
