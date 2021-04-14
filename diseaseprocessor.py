from run_model import *

class DiseaseProcessor:

    def __init__(self, model_name, sequence):
        self.model = create_pipeline(model_name)
        self.sequence = sequence

    def predict(self):
        disease_results = predict_sequence_ner(self.model, self.sequence)
