from entities import Entities
from transformers import AutoTokenizer, AutoModel, AutoConfig, AutoModelForTokenClassification, TokenClassificationPipeline

def create_pipeline(model_name):
    config = AutoConfig.from_pretrained(model_name)

    tokenizer = AutoTokenizer.from_pretrained(
            model_name,
            use_fast=True,
            return_offsets_mapping=True
        )

    model = AutoModelForTokenClassification.from_pretrained(
            model_name,
            config=config
        )
    NER_pipeline = TokenClassificationPipeline(model= model,tokenizer=tokenizer, framework='pt', task='ner', grouped_entities=True)

    return NER_pipeline

def predict_sequence_ner(NER_pipeline, sequence):
    result = NER_pipeline(sequence)
    entities = Entities(result)
    return entities


