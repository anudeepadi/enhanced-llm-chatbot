import torch
from transformers import (
    AutoTokenizer, 
    AutoModelForSequenceClassification,
    AutoModelForQuestionAnswering,
    pipeline
)
from sentence_transformers import SentenceTransformer
import numpy as np
from typing import List, Dict, Tuple
import spacy

class NLPEngine:
    def __init__(self, config: dict):
        # Initialize core NLP components
        self.sentiment_analyzer = pipeline("sentiment-analysis")
        self.intent_classifier = AutoModelForSequenceClassification.from_pretrained(config['intent_model'])
        self.qa_model = AutoModelForQuestionAnswering.from_pretrained(config['qa_model'])
        self.sentence_encoder = SentenceTransformer('all-MiniLM-L6-v2')
        self.nlp = spacy.load('en_core_web_lg')
        
        # Load tokenizers
        self.tokenizer = AutoTokenizer.from_pretrained(config['base_model'])
        
        # Initialize response cache
        self.response_cache = {}
        
        # Context window for conversation history
        self.context_window = config.get('context_window', 5)
        
    def analyze_sentiment(self, text: str) -> Dict:
        """Analyze sentiment of input text"""
        return self.sentiment_analyzer(text)[0]
        
    def extract_entities(self, text: str) -> List[Dict]:
        """Extract named entities using spaCy"""
        doc = self.nlp(text)
        return [{'text': ent.text, 'label': ent.label_} for ent in doc.ents]