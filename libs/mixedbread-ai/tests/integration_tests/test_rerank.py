import pytest

from langchain_mixedbread_ai import MixedbreadAIRerank


@pytest.mark.vcr()
def test_langchain_mixedbread_ai_rerank() -> None:
    texts = ["Mockingbird", "Moby-Dick"]
    query = "Moby-Dick"
    reranker = MixedbreadAIRerank(top_n=3)
    output = reranker.rerank(documents=texts, query=query)
    assert len(output) == 2
    assert output[0].index == 1
