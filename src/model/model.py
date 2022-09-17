from model.utils import NEWS_CLASSES
from transformers import pipeline
from happytransformer import HappyTextToText, TTSettings
from transformers import FSMTForConditionalGeneration, FSMTTokenizer



summ_pipeline = pipeline("summarization")
class_pipeline = pipeline("zero-shot-classification",  model="facebook/bart-large-mnli")
happy_tt = HappyTextToText("T5", "vennify/t5-base-grammar-correction")
args = TTSettings(num_beams=5, min_length=1)
mname = "facebook/wmt19-de-en"
tokenizer = FSMTTokenizer.from_pretrained(mname)
model = FSMTForConditionalGeneration.from_pretrained(mname)


def summarize(news_batch):    
    return summ_pipeline(news_batch)
    

def classify(news_batch):
    return class_pipeline(news_batch, candidate_labels=NEWS_CLASSES)


def grammar(text):
    return happy_tt.generate_text(text, args=args).text


def translate_ger_en(text):
    input_ids = tokenizer.encode(text, return_tensors="pt")
    outputs = model.generate(input_ids)
    return tokenizer.decode(outputs[0], skip_special_tokens=True) 


translations_models = {"ger_en": translate_ger_en}


def translations(text, language):
    try:
        return translations_models[language](text)
    except KeyError:
        raise Exception(f"Language not supported: {language}")

