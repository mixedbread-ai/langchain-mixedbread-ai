"""Test embedding model integration."""

from langchain_mixedbread_ai.embeddings import MixedbreadAIEmbeddings


def test_initialization() -> None:
    """Test embedding model initialization."""
    MixedbreadAIEmbeddings(mxbai_api_key="test")
