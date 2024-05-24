from langchain_community.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter

# PDF 파일 불러오기
loader = PyPDFLoader("./static/download/resume.pdf")

        # Chunk(block) 단위로 Split(쪼개기)
text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000,
        chunk_overlap=200
    )
       
docs = loader.load()
print(len(docs))
print(docs[0])
exit()
       
        # 임베딩 → 형태소를 숫자로 표현
        #  ex) 5차원 텍스트 임베딩
        #      dog : 0.3 0.7 1.5 59 32
# embeddings = OpenAIEmbeddings()
       
# cache_dir = LocalFileStore("./.cache/")
# cached_embeddings = CacheBackedEmbeddings.from_bytes_store(embeddings, cache_dir)
# vectorstore = Chroma.from_documents(docs, cached_embeddings)
       
#         # Vector DB: Chroma 저장
# directory = "./llm/chroma_db"
# vector_index = Chroma.from_documents(
#     docs,                          # Documents       
#     OpenAIEmbeddings(),            # Text embeddings model
#     persist_directory=directory    # file system(저장경로)
#     )
# vector_index.persist()  # Save