from collections import defaultdict
import json
from datasets import load_dataset, DatasetDict
from mteb import AbsTaskRetrieval

def load_retrieval_data(hf_hub_name=None, eval_splits=None):
    eval_split = eval_splits[0]
    queries_dataset = load_dataset(hf_hub_name, name='queries')
    corpus_dataset = load_dataset(hf_hub_name, name='corpus')
    test_dataset = load_dataset(hf_hub_name, name='default')
 
    corpus = {e['id']: {'text': e['text']} for e in corpus_dataset['corpus']}
    queries = {e['id']: e['text'] for e in queries_dataset['queries']}
    relevant_docs = defaultdict(dict)
    for e in test_dataset[eval_split]:
        relevant_docs[e['q_id']][e['p_id']] = e['score']

    corpus = DatasetDict({eval_split:corpus})
    queries = DatasetDict({eval_split:queries})
    relevant_docs = DatasetDict({eval_split:relevant_docs})
    return corpus, queries, relevant_docs


class MedExamRetrieval(AbsTaskRetrieval):
    @property
    def description(self):
        return {
            'name': 'MedExamRetrieval',
            'hf_hub_name': "CMIRB/MedExamRetrieval",
            'description': "medical-exam-retrieval",
            'type': 'Retrieval',
            'category': 's2p',
            'eval_splits': ['test'],
            'eval_langs': ['zh'],
            'main_score': 'ndcg_at_10',
        }

    def load_data(self, **kwargs):
        if self.data_loaded:
            return

        self.corpus, self.queries, self.relevant_docs = load_retrieval_data(self.description['hf_hub_name'],
                                                                            self.description['eval_splits'])
        self.data_loaded = True

class DuBaikeRetrieval(AbsTaskRetrieval):
    @property
    def description(self):
        return {
            'name': 'DuBaikeRetrieval',
            'hf_hub_name': "CMIRB/DuBaikeRetrieval",
            'description': "baidu-baike-retrieval",
            'type': 'Retrieval',
            'category': 's2p',
            'eval_splits': ['test'],
            'eval_langs': ['zh'],
            'main_score': 'ndcg_at_10',
        }

    def load_data(self, **kwargs):
        if self.data_loaded:
            return

        self.corpus, self.queries, self.relevant_docs = load_retrieval_data(self.description['hf_hub_name'],
                                                                            self.description['eval_splits'])
        self.data_loaded = True

class DXYDiseaseRetrieval(AbsTaskRetrieval):
    @property
    def description(self):
        return {
            'name': 'DXYDiseaseRetrieval',
            'hf_hub_name': "CMIRB/DXYDiseaseRetrieval",
            'description': "medical-disease-retrieval",
            'type': 'Retrieval',
            'category': 's2p',
            'eval_splits': ['test'],
            'eval_langs': ['zh'],
            'main_score': 'ndcg_at_10',
        }

    def load_data(self, **kwargs):
        if self.data_loaded:
            return

        self.corpus, self.queries, self.relevant_docs = load_retrieval_data(self.description['hf_hub_name'],
                                                                            self.description['eval_splits'])
        self.data_loaded = True

class MedicalRetrieval(AbsTaskRetrieval):
    @property
    def description(self):
        return {
            'name': 'MedicalRetrieval',
            'hf_hub_name': 'CMIRB/MedicalRetrieval',
            'description': 'Passage retrieval dataset collected from Alibaba search engine systems in medical domain',
            'type': 'Retrieval',
            'category': 's2p',
            'eval_splits': ['dev'],
            'eval_langs': ['zh'],
            'main_score': 'ndcg_at_10',
        }

    def load_data(self, **kwargs):
        if self.data_loaded:
            return

        self.corpus, self.queries, self.relevant_docs = load_retrieval_data(self.description['hf_hub_name'],
                                                                            self.description['eval_splits'])
        self.data_loaded = True

class CmedqaRetrieval(AbsTaskRetrieval):
    @property
    def description(self):
        return {
            'name': 'CmedqaRetrieval',
            'hf_hub_name': 'CMIRB/CmedqaRetrieval',
            'reference': 'https://aclanthology.org/2022.emnlp-main.357.pdf',
            'description': 'Online medical consultation text',
            'type': 'Retrieval',
            'category': 's2p',
            'eval_splits': ['dev'],
            'eval_langs': ['zh'],
            'main_score': 'ndcg_at_10',
        }

    def load_data(self, **kwargs):
        if self.data_loaded:
            return

        self.corpus, self.queries, self.relevant_docs = load_retrieval_data(self.description['hf_hub_name'],
                                                                            self.description['eval_splits'])
        self.data_loaded = True

class DXYConsultRetrieval(AbsTaskRetrieval):
    @property
    def description(self):
        return {
            'name': 'DXYConsultRetrieval',
            'hf_hub_name': "CMIRB/DXYConsultRetrieval",
            'description': "doctor-patient-consultation-retrieval",
            'type': 'Retrieval',
            'category': 's2p',
            'eval_splits': ['test'],
            'eval_langs': ['zh'],
            'main_score': 'ndcg_at_10',
        }

    def load_data(self, **kwargs):
        if self.data_loaded:
            return

        self.corpus, self.queries, self.relevant_docs = load_retrieval_data(self.description['hf_hub_name'],
                                                                            self.description['eval_splits'])
        self.data_loaded = True

class CovidRetrieval(AbsTaskRetrieval):
    @property
    def description(self):
        return {
            'name': 'CovidRetrieval',
            'hf_hub_name': 'CMIRB/CovidRetrieval',
            'reference': 'https://aclanthology.org/2022.emnlp-main.357.pdf',
            'description': 'COVID-19 news articles',
            'type': 'Retrieval',
            'category': 's2p',
            'eval_splits': ['dev'],
            'eval_langs': ['zh'],
            'main_score': 'ndcg_at_10',
        }

    def load_data(self, **kwargs):
        if self.data_loaded:
            return

        self.corpus, self.queries, self.relevant_docs = load_retrieval_data(self.description['hf_hub_name'],
                                                                            self.description['eval_splits'])
        self.data_loaded = True

class IIYIPostRetrieval(AbsTaskRetrieval):
    @property
    def description(self):
        return {
            'name': 'IIYIPostRetrieval',
            'hf_hub_name': "CMIRB/IIYIPostRetrieval",
            'description': "medical-post-retrieval",
            'type': 'Retrieval',
            'category': 's2p',
            'eval_splits': ['test'],
            'eval_langs': ['zh'],
            'main_score': 'ndcg_at_10',
        }

    def load_data(self, **kwargs):
        if self.data_loaded:
            return

        self.corpus, self.queries, self.relevant_docs = load_retrieval_data(self.description['hf_hub_name'],
                                                                            self.description['eval_splits'])
        self.data_loaded = True

class CSLCiteRetrieval(AbsTaskRetrieval):
    @property
    def description(self):
        return {
            'name': 'CSLCiteRetrieval',
            'hf_hub_name': "CMIRB/CSLCiteRetrieval",
            'description': "chinese-literature-citations-retrieval",
            'type': 'Retrieval',
            'category': 's2p',
            'eval_splits': ['test'],
            'eval_langs': ['zh'],
            'main_score': 'ndcg_at_10',
        }

    def load_data(self, **kwargs):
        if self.data_loaded:
            return

        self.corpus, self.queries, self.relevant_docs = load_retrieval_data(self.description['hf_hub_name'],
                                                                            self.description['eval_splits'])
        self.data_loaded = True

class CSLRelatedRetrieval(AbsTaskRetrieval):
    @property
    def description(self):
        return {
            'name': 'CSLRelatedRetrieval',
            'hf_hub_name': "CMIRB/CSLRelatedRetrieval",
            'description': "Chinese-similar-literature-retrieval",
            'type': 'Retrieval',
            'category': 's2p',
            'eval_splits': ['test'],
            'eval_langs': ['zh'],
            'main_score': 'ndcg_at_10',
        }

    def load_data(self, **kwargs):
        if self.data_loaded:
            return

        self.corpus, self.queries, self.relevant_docs = load_retrieval_data(self.description['hf_hub_name'],
                                                                            self.description['eval_splits'])
        self.data_loaded = True