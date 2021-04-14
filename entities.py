class Entities:

  def __init__(self, result, text):
    self. result = result
    self.text = text
    self.ents = dict()

    self.obtain_ents()

  def obtain_ents(self):
    self.ents = [{"start": ent['start'],
                              "end": ent['end'],
                              "label": ent['entity_group']
                  } for ent in self.result if ent['entity_group'] != '0']

  def parse_ner_spacy(self):
    dict_results = {
        "text": self.text,
        "ents": self.ents,
        "title": None
    }
    return dict_results
