#!/usr/bin/env python3
import pandas as pd
from qdrant_client import models, QdrantClient
from sentence_transformers import SentenceTransformer
from openai import OpenAI

# Load and prepare the dataset
df = pd.read_csv('brazilian_cities.csv')
df = df[df['MUNICÍPIO - IBGE'].notna()]  # Remove any NaN values
data = df.sample(700).to_dict('records')  # Sample 700 records for performance
print(f"Loaded {len(data)} records from brazilian_cities.csv")

# Initialize the embedding model
encoder = SentenceTransformer('all-MiniLM-L6-v2')

# Create the vector database client
qdrant = QdrantClient(":memory:")  # In-memory Qdrant instance

# Create collection to store city data
qdrant.recreate_collection(
    collection_name="brazilian_cities",
    vectors_config=models.VectorParams(
        size=encoder.get_sentence_embedding_dimension(),
        distance=models.Distance.COSINE
    )
)

# Vectorize and upload data to Qdrant
qdrant.upload_points(
    collection_name="brazilian_cities",
    points=[
        models.PointStruct(
            id=idx,
            vector=encoder.encode(f"{doc['MUNICÍPIO - IBGE']}, {doc['UF']}").tolist(),
            payload=doc,
        ) for idx, doc in enumerate(data)
    ]
)

# Initialize the llamafile client
client = OpenAI(
    base_url="http://localhost:8080/v1",
    api_key="sk-no-key-required"
)

# Interactive loop for user queries
print("Welcome to the Brazilian Cities RAG System! Type 'exit' to quit.")
while True:
    user_prompt = input("Enter your query (e.g., 'Suggest a city in Rio de Janeiro'): ")
    if user_prompt.lower() == 'exit':
        print("Exiting...")
        break

    # Search for relevant cities
    hits = qdrant.search(
        collection_name="brazilian_cities",
        query_vector=encoder.encode(user_prompt).tolist(),
        limit=3
    )

    # Display search results
    print("\nSearch Results:")
    search_results = [hit.payload for hit in hits]
    for hit in hits:
        print(f"{hit.payload['MUNICÍPIO - IBGE']}, {hit.payload['UF']} (score: {hit.score})")

    # Generate response using llamafile
    completion = client.chat.completions.create(
        model="LLaMA_CPP",
        messages=[
            {"role": "system", "content": "You are a geography expert specializing in Brazilian municipalities. Your top priority is to help users with their queries about Brazilian cities."},
            {"role": "user", "content": user_prompt},
            {"role": "assistant", "content": str(search_results)}
        ]
    )

    # Print the LLM response
    print("\nLLM Response:")
    print(completion.choices[0].message.content)