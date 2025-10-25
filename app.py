from src.search import RAGSearch

if __name__ == "__main__":
    rag_search = RAGSearch()
    query = "What are types of recommendation system?"
    summary = rag_search.search_and_summarize(query)
    print(f"Summary:\n{summary}")

# from src.data_loader import load_all_documents
# from src.vectorstore import FaissVectorStore

# if __name__ == "__main__":
#     data_directory = "data"  # Specify your data directory here
#     docs = load_all_documents(data_directory)
#     print(f"\nTotal documents loaded: {len(docs)}")
#     store = FaissVectorStore("faiss_store")
#     store.build_from_documents(docs)
