## Data Collection and Processing

- [Data Collection](#data-collection)
  - [Collection Sources](#collection-sources)
  - [IR Tasks](#ir-tasks)
- [Data Processing](#data-processing)
  - [Corpus Filtering](#corpus-filtering)
  - [Document Matching](#document-matching)
  - [Example Filtering](#example-filtering)

### Data Collection

CMIRB (Chinese Medical Information Retrieval Benchmark) is a specialized multi-task dataset designed specifically for medical information retrieval. 
   
#### Collection Sources

We curated a substantial dataset from various medical resources, as presented in the following Table.

| Dataset |  Query URL |  #Samples | Document URL | #Samples | 
|:-----:|:-----:|:---------------------------:|:-----:|:-----:|
| MedExamRetrieval | [https://github.com/jind11/MedQA](https://github.com/jind11/MedQA) |  3,426  | [https://github.com/jind11/MedQA](https://github.com/jind11/MedQA) | 27,871 |
|  DuBaikeRetrieval | [https://github.com/baidu/DuReader](https://github.com/baidu/DuReader) |  20,000  | [https://baike.baidu.com](https://baike.baidu.com) | 56,441 |
| DXYDiseaseRetrieval | [https://dxy.com/diseases](https://dxy.com/diseases) | 61,840  | [https://dxy.com/diseases](https://dxy.com/diseases) | 61,840 |
| MedicalRetrieval | [https://huggingface.co/datasets/C-MTEB/MedicalRetrieval](https://huggingface.co/datasets/C-MTEB/MedicalRetrieval) | 1,000 | [https://huggingface.co/datasets/C-MTEB/MedicalRetrieval](https://huggingface.co/datasets/C-MTEB/MedicalRetrieval)  | 100,999 |
| CmedqaRetrieval | [https://huggingface.co/datasets/C-MTEB/CmedqaRetrieval](https://huggingface.co/datasets/C-MTEB/CmedqaRetrieval) | 3,999 | [https://huggingface.co/datasets/C-MTEB/CmedqaRetrieval](https://huggingface.co/datasets/C-MTEB/CmedqaRetrieval) | 100,001 |
| DXYConsultRetrieval | [https://dxy.com/questions/](https://dxy.com/questions/) | 13,057 | [https://dxy.com/questions/](https://dxy.com/questions/) | 13,057 |
| CovidRetrieval | [https://huggingface.co/datasets/C-MTEB/CovidRetrieval](https://huggingface.co/datasets/C-MTEB/CovidRetrieval) | 949 | [https://huggingface.co/datasets/C-MTEB/CovidRetrieval](https://huggingface.co/datasets/C-MTEB/CovidRetrieval) | 100,001 |
| IIYiPostRetrieval | [https://bbs.iiyi.com/](https://bbs.iiyi.com/) | 37,065 | [https://bbs.iiyi.com/](https://bbs.iiyi.com/) | 37,065 |
| CSLCiteRetrieval | [https://github.com/ydli-ai/CSL](https://github.com/ydli-ai/CSL) | 934 | [https://med.wanfangdata.com.cn/](https://med.wanfangdata.com.cn/) |  36,783 |
| CSLRelatedRetrieval | [https://github.com/ydli-ai/CSL](https://github.com/ydli-ai/CSL) | 934 | [https://med.wanfangdata.com.cn/](https://med.wanfangdata.com.cn/) | 36,783 |

#### IR Tasks
CMIRB consists of data collected from various medical online websites, encompassing 5 tasks and 10 datasets, and has practical application scenarios.

### Data Processing

Note that we use `gpt-4o-mini-2024-07-18` as the LLM through the generation pipeline.


#### Corpus Filtering

TODO.

#### Document Matching

TODO.

#### Example Filtering

TODO.

