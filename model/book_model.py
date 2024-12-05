import re
from dotenv import load_dotenv
from operator import itemgetter
from langchain.schema import Document
from langchain.chains.query_constructor.base import AttributeInfo
from langchain_community.document_transformers import LongContextReorder
from langchain.retrievers import SelfQueryRetriever
from langchain_core.output_parsers import StrOutputParser
from langchain_openai import ChatOpenAI
from langchain_openai.embeddings import OpenAIEmbeddings
from langchain_chroma import Chroma
from langchain_core.runnables import (
    RunnableLambda
)
from langchain_core.prompts import PromptTemplate


load_dotenv()
# 이미 저장된 벡터 데이터베이스 불러오기
persist_directory = './db_date'  # 저장된 데이터베이스 경로
collection_name = 'books_date'  # 사용했던 collection 이름

# 벡터 데이터베이스 로드
vectordb = Chroma(
    collection_name=collection_name,
    persist_directory=persist_directory,
    embedding_function=OpenAIEmbeddings(model='text-embedding-3-small')  # 동일한 임베딩 설정 필요
)

# 메타데이터 필드에 대한 정보를 정의합니다.
metadata_field_info = [
    AttributeInfo(
        name='title',  # 출시 연도를 나타내는 필드
        description='책 제목, 책',  # 필드 설명
        type='string',  # 데이터 타입은 정수
    ),
    AttributeInfo(
        name='author',  # 상품 카테고리를 나타내는 필드
        description='작가, 쓴 사람',  # 필드 설명
        type='string',  # 데이터 타입은 문자열
    ),
    AttributeInfo(
        name='publisher',  # 사용자 평점을 나타내는 필드
        description='출판사',  # 필드 설명
        type='string',  # 데이터 타입은 실수
    ),
    AttributeInfo(
        name='pubdate',  # 사용자 평점을 나타내는 필드
        description='출판 연도, 출판일, 출판날',  # 필드 설명
        type='string',  # 데이터 타입은 실수
    ),
]

# SelfQueryRetriever 초기화: LLM과 벡터 저장소를 연결
retriever = SelfQueryRetriever.from_llm(
    llm=ChatOpenAI(model_name='gpt-4o-mini'),  # 사용할 언어 모델 설정
    vectorstore=vectordb,
    document_contents='책 소개',  # 문서 내용 요약
    search_kwargs={'k': 4},  # 검색 결과 개수 설정
    metadata_field_info=metadata_field_info  # 메타데이터 필드 정보
)

# 문서 재정렬 함수 정의
def reorder_documents(documents):
    # LongContextReorder 객체 생성: 긴 문맥을 재정렬하는 기능
    context_reorder = LongContextReorder()
    # 입력된 문서들을 재정렬
    documents_reordered = context_reorder.transform_documents(documents)
    
    # 사람이 볼 수 있도록 각 문서를 정제하여 문자열로 결합
    documents_formatted = '\n\n'.join([
        f"제목: {doc.metadata.get('title', 'N/A')}\n"
        f"작가: {doc.metadata.get('author', 'N/A')}\n"
        f"출판사: {doc.metadata.get('publisher', 'N/A')}\n"
        f"발행연도: {doc.metadata.get('pubdate', 'N/A')}\n"
        f"내용: {doc.page_content}"
        for doc in documents_reordered
    ])
    
    return documents_formatted  # 포맷팅된 문서 내용을 반환

def preprocess_question(inputs, max_results=5):
    question = inputs['question']
    match = re.search(r"\d{4}", question)  # 질문에서 연도를 추출
    if match:
        # 연도 기반 검색
        year = match.group(0)
        query_results = retriever.vectorstore._collection.get(where={"pubdate": year})
        documents = [
            Document(page_content=doc, metadata=meta)
            for doc, meta in zip(query_results["documents"], query_results["metadatas"])
        ][:max_results]
        return {"reference": reorder_documents(documents)}
    else:
        # 일반 검색 (연도 조건이 없는 경우)
        documents = retriever.get_relevant_documents(question)  # 질의에 기반한 기본 검색
        reordered_documents = reorder_documents(documents)  # 문서 재정렬
        return {"reference": reordered_documents}



template = '''
너는 책에 대한 정보를 제공하는 봇이야. 
reference에 있는 정보만 사용해서 질문에 답변해야 해. 
reference 외의 내용을 절대 상상하거나 추가하지 마.  
reference에서 정보를 찾을 수 없으면 "요청하신 책에 대한 정보는 도서관에 없어요"라고 답변해야 해.

reference:
{reference}


질문에 답변할 때 다음 규칙을 반드시 따라:
1. reference에서 정보를 찾을 수 없으면 반드시 "요청하신 책에 대한 정보는 도서관에 없어요"라고 답변해야 해.
2. 모든 답변은 아래 형식을 따라야 해:
   제목: [책 제목]  
   작가: [작가 이름]  
   출판사: [출판사 이름]  
   출판연도: [출판 연도]  
   책소개: [책 내용 또는 관련 설명]  
3. 만약 모든 필드를 reference에서 찾을 수 없으면 "정보가 부족합니다."라고 말해야 해.
4. 여러 작품을 추천할 때는 reference에 있는 작품만 포함하고, 나머지는 제외해야 해.

질문: 
{question}

답변은 반드시 한국어로 작성하고, reference에 없는 내용은 절대 추가하지 마.
요청 개수가 있다면 최대한 지켜줘.
만약 reference에 없는 정보를 포함하면 안 된다는 점을 꼭 기억해.
'''

# 템플릿으로부터 프롬프트 생성
prompt = PromptTemplate.from_template(template)

# 모델과 파서 초기화
model = ChatOpenAI(model_name='gpt-4o-mini')
parser = StrOutputParser()

# chain 구성
# chain = (
#     {
#         # 'reference' 키에 대해 여러 처리를 정의
#         'reference': retriever  # SelfQueryRetriever를 통해 reference 추출
#         | RunnableLambda(reorder_documents),  # 문서를 재정렬 및 포맷팅
#         'question': itemgetter('question')  # 질문을 그대로 가져오기
#     }
#     | prompt  # 프롬프트 템플릿에 데이터 결합
#     | model  # 모델에 프롬프트 전달하여 응답 생성
#     | parser  # 모델의 응답을 파싱
# )

chain = (
    {
        # question을 전처리하는 단계 추가
        "question": itemgetter("question"),
        #"reference": retriever | RunnableLambda(reorder_documents),
        "reference": RunnableLambda(preprocess_question)
    }
    | prompt  # 템플릿에 데이터 결합
    | model  # 모델 호출
    | parser  # 결과 파싱
)

def get_response(input):
    response = chain.invoke({
        'question': input
    })
    
    return response

#print(get_response("2019년에 나온 책을 알려줘"))