## Data Collection and Processing

- [Data Collection](#data-collection)
  - [IR Tasks](#ir-tasks)
  - [Collection Sources](#collection-sources)
- [Data Processing](#data-processing)
  - [Corpus Filtering](#corpus-filtering)
  - [Document Matching](#document-matching)
  - [Example Filtering](#example-filtering)
- [Final Data](#final-data)

### Data Collection

CMIRB (Chinese Medical Information Retrieval Benchmark) is a specialized multi-task dataset designed specifically for medical information retrieval. 

#### IR Tasks
CMIRB consists of data collected from various medical online websites, encompassing 5 tasks and 10 datasets, and has practical application scenarios.

| Task |  Description |
|:-----:|:-----:|
| Medical Knowledge Retrieval | Retrieve relevant medical knowledge snippets from textbooks or encyclopedias based on a given medical entity query. |
| Medical Consultation Retrieval | Extract relevant doctor's responses to online medical consultation questions posed by patients, simulating the retrieval of expert medical advice |
| Medical News Retrieval | Focus on retrieving news articles that address queries related to COVID-19 |
| Medical Post Retrieval | Retrieve the content of a forum post corresponding to its title |
| Medical Literature Retrieval | Retrieve abstracts of cited references based on the title of a medical paper or find a similar paper based on the text of a given medical paper |
   
#### Collection Sources

We curated a substantial dataset from various medical resources, as presented in the following Table.

| Task | Dataset |  Query URL |  #Samples | Document URL | #Samples | 
|:-----:|:-----:|:-----:|:---------------------------:|:-----:|:-----:|
| Knowledge | MedExamRetrieval | [https://github.com/jind11/MedQA](https://github.com/jind11/MedQA) |  3,426  | [https://github.com/jind11/MedQA](https://github.com/jind11/MedQA) | 27,871 |
| Knowledge |  DuBaikeRetrieval | [https://github.com/baidu/DuReader](https://github.com/baidu/DuReader) |  20,000  | [https://baike.baidu.com](https://baike.baidu.com) | 56,441 |
| Knowledge | DXYDiseaseRetrieval | [https://dxy.com/diseases](https://dxy.com/diseases) | 61,840  | [https://dxy.com/diseases](https://dxy.com/diseases) | 61,840 |
| Consultation | MedicalRetrieval | [https://huggingface.co/datasets/C-MTEB/MedicalRetrieval](https://huggingface.co/datasets/C-MTEB/MedicalRetrieval) | 1,000 | [https://huggingface.co/datasets/C-MTEB/MedicalRetrieval](https://huggingface.co/datasets/C-MTEB/MedicalRetrieval)  | 100,999 |
| Consultation | CmedqaRetrieval | [https://huggingface.co/datasets/C-MTEB/CmedqaRetrieval](https://huggingface.co/datasets/C-MTEB/CmedqaRetrieval) | 3,999 | [https://huggingface.co/datasets/C-MTEB/CmedqaRetrieval](https://huggingface.co/datasets/C-MTEB/CmedqaRetrieval) | 100,001 |
| Consultation | DXYConsultRetrieval | [https://dxy.com/questions/](https://dxy.com/questions/) | 13,057 | [https://dxy.com/questions/](https://dxy.com/questions/) | 13,057 |
| News | CovidRetrieval | [https://huggingface.co/datasets/C-MTEB/CovidRetrieval](https://huggingface.co/datasets/C-MTEB/CovidRetrieval) | 949 | [https://huggingface.co/datasets/C-MTEB/CovidRetrieval](https://huggingface.co/datasets/C-MTEB/CovidRetrieval) | 100,001 |
| Post | IIYiPostRetrieval | [https://bbs.iiyi.com/](https://bbs.iiyi.com/) | 37,065 | [https://bbs.iiyi.com/](https://bbs.iiyi.com/) | 37,065 |
| Literature | CSLCiteRetrieval | [https://github.com/ydli-ai/CSL](https://github.com/ydli-ai/CSL) | 934 | [https://med.wanfangdata.com.cn/](https://med.wanfangdata.com.cn/) |  36,783 |
| Literature | CSLRelatedRetrieval | [https://github.com/ydli-ai/CSL](https://github.com/ydli-ai/CSL) | 934 | [https://med.wanfangdata.com.cn/](https://med.wanfangdata.com.cn/) | 36,783 |

### Data Processing

Note that we use `gpt-4o-mini-2024-07-18` as the LLM through the processing pipeline.

Our data preprocessing pipeline, depicted in Algorithm 1

<p align="center">
  <img src="images/data_processing.png" alt="DATA-PROCESSING" width="600"/>  
</p>

#### Corpus Filtering
Initially, we use ChatGPT to perform medical relevance detection on the texts, eliminating non-medical content (lines 3-8).

#### Document Matching
For the MedExam and DuBaike datasets, the direct query-document signal isn't initially provided. 

We leverage ChatGPT's capabilities to identify the most relevant documents. Starting with a query, we use the BM25 to retrieve the top 20 relevant documents, which GPT then ranks to identify the top 3 most relevant. Ideally, these documents should be semantically related and provide sufficient answers or evidence for the query. Therefore, ChatGPT extracts document segments as evidence details for the query.

To verify the sufficiency of this evidence, GPT generates an answer to the query based on the extracted evidence fragment. A self-verification step follows: if the GPT-generated answer aligns with the document, the document is deemed a positive match for the query. 

For MedExam, where queries are multiple-choice questions, we verify model answers against correct ones. For DuBaike, queries are medical knowledge questions, and answers are encyclopedic. GPT scores the generated and reference answers for consistency in expressing the same medical knowledge. This detailed process is outlined in lines 10-26.

#### Example Filtering

Subsequently, ChatGPT assesses query-document relevance, filtering out low-relevance examples (lines 27-33). Our relevance assessment considers semantic alignment and the practical significance of data samples for their respective tasks.

### Final Data
Through this iterative loop of self-ranking, evidence searching, answering, and verification, combined with ChatGPT's advanced knowledge capabilities, we ensure high-quality, highly relevant query-document pairs.

| Name |  Hub URL | Description | Query #Samples | Doc #Samples | 
|:-----:|:-----:|:---------------------------:|:-----:|:-----:|
| MedExamRetrieval | [CMIRB/MedExamRetrieval](https://huggingface.co/datasets/CMIRB/MedExamRetrieval) | Medical multi-choice exam  | 697 | 27,871 |
| DuBaikeRetrieval | [CMIRB/DuBaikeRetrieval](https://huggingface.co/datasets/CMIRB/DuBaikeRetrieval) | Medical search query from BaiDu Search  | 318 | 56,441 |
| DXYDiseaseRetrieval | [CMIRB/DXYDiseaseRetrieval](https://huggingface.co/datasets/CMIRB/DXYDiseaseRetrieval) | Disease question from medical website  | 1,255 | 54,021 |
| MedicalRetrieval | [CMIRB/MedicalRetrieval](https://huggingface.co/datasets/C-MTEB/MedicalRetrieval) | Passage retrieval dataset collected from Alibaba search engine systems in medical domain | 1,000  | 100,999 |
| CmedqaRetrieval | [CMIRB/CmedqaRetrieval](https://huggingface.co/datasets/C-MTEB/CmedqaRetrieval) |  Online medical consultation text | 3,999 | 100,001 |
| DXYConsultRetrieval | [CMIRB/DXYConsultRetrieval](https://huggingface.co/datasets/CMIRB/DXYConsultRetrieval) | Online medical consultation text  | 943 | 12,577 |
| CovidRetrieval | [CMIRB/CovidRetrieval](https://huggingface.co/datasets/C-MTEB/CovidRetrieval) | COVID-19 news articles | 949  | 100,001 |
| IIYiPostRetrieval | [CMIRB/IIYiPostRetrieval](https://huggingface.co/datasets/CMIRB/IIYiPostRetrieval) | Medical post articles  | 789 | 27,570 |
| CSLCiteRetrieval | [CMIRB/CSLCiteRetrieval](https://huggingface.co/datasets/CMIRB/CSLCiteRetrieval) | Medical literature citation prediction  | 573 | 36,703 |
| CSLRelatedRetrieval | [CMIRB/CSLRelatedRetrieval](https://huggingface.co/datasets/CMIRB/CSLRelatedRetrieval) | Medical similar literatue  | 439 | 36,758 |
