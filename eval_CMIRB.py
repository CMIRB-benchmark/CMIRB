import argparse

from CMIRB.tasks import *
from flag_dres_model import FlagDRESModel
from mteb import MTEB
from time import time

query_instruction_for_retrieval_dict = {
    "bge-large-zh": "为这个句子生成表示以用于检索相关文章：",
    "bge-large-zh-noinstruct": None,
    "bge-base-zh": "为这个句子生成表示以用于检索相关文章：",
    "bge-small-zh": "为这个句子生成表示以用于检索相关文章：",
    "bge-large-zh-v1.5": "为这个句子生成表示以用于检索相关文章：",
    "bge-base-zh-v1.5": "为这个句子生成表示以用于检索相关文章：",
    "bge-small-zh-v.15": "为这个句子生成表示以用于检索相关文章：",
}

def get_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('--model_name_or_path', default="BAAI/bge-large-zh-v1.5", type=str)
    parser.add_argument('--task_type', default=None, type=str)
    parser.add_argument('--add_instruction', action='store_true', help="whether to add instruction for query")
    parser.add_argument('--pooling_method', default='cls', type=str)
    return parser.parse_args()



if __name__ == '__main__':
    args = get_args()

    model = FlagDRESModel(model_name_or_path=args.model_name_or_path,
                          query_instruction_for_retrieval="为这个句子生成表示以用于检索相关文章：",
                          pooling_method=args.pooling_method)

    task_names = ['MedExamRetrieval', "DuBaikeRetrieval", "DXYDiseaseRetrieval",
                  "MedicalRetrieval", "CmedqaRetrieval", "DXYConsultRetrieval", "CovidRetrieval",
                  "IIYIPostRetrieval", "CSLCiteRetrieval", "CSLRelatedRetrieval"]

    for task in task_names:
        t0 = time()
        if task in ['MedExamRetrieval', "DuBaikeRetrieval", "DXYDiseaseRetrieval",
                  "MedicalRetrieval", "CmedqaRetrieval", "DXYConsultRetrieval", "CovidRetrieval",
                  "IIYIPostRetrieval", "CSLCiteRetrieval", "CSLRelatedRetrieval"]:
            if args.model_name_or_path.split('/')[-1] not in query_instruction_for_retrieval_dict and args.add_instruction:
                instruction = None
                print(f"{args.model_name_or_path} not in query_instruction_for_retrieval_dict, set instruction={instruction}")
            elif args.model_name_or_path.split('/')[-1] in query_instruction_for_retrieval_dict:
                instruction = query_instruction_for_retrieval_dict[args.model_name_or_path.split('/')[-1]]
            else:
                instruction = None
        else:
            instruction = None

        model.query_instruction_for_retrieval = instruction
        print(f"current instruction is {model.query_instruction_for_retrieval}")
        evaluation = MTEB(tasks=[task], task_langs=['zh', 'zh-CN'])
        evaluation.run(model, output_folder=f"zh_results/{args.model_name_or_path.split('/')[-1]}")
        print(f"{task} evaluation cost {(time()-t0)/60} minutes!")