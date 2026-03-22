from openai import OpenAI

class VocareumEmbeddingFunction:
    def __init__(self, api_key):
        self.client = OpenAI(
            api_key=api_key,
            base_url='https://openai.vocareum.com/v1'
        )

    # ✅ central method
    def _embed(self, input):
        if isinstance(input, str):
            input = [input]

        response = self.client.embeddings.create(
            model='text-embedding-3-small',
            input=input
        )
        return [item.embedding for item in response.data]

    # Used when adding documents
    def __call__(self, input):
        return self._embed(input)

    # Used during query
    def embed_query(self, input):
        return self._embed(input)

    # Sometimes used internally
    def embed_documents(self, input):
        return self._embed(input)

    def name(self):
        return "openai_embedding"