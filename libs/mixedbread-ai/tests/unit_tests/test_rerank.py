from langchain_mixedbread_ai.rerank import MixedbreadAIRerank


def test_initialization() -> None:
    """Test embedding model initialization."""
    MixedbreadAIRerank(mxbai_api_key="test")
