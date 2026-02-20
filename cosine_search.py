import numpy as np

# -----------------------------
# COSINE SIMILARITY
# -----------------------------
def cosine_similarity(a, b):
    return np.dot(a, b) / (np.linalg.norm(a) * np.linalg.norm(b))

def cosine_search(query, vectors):
    scores = []
    for i, vec in enumerate(vectors):
        score = cosine_similarity(query, vec)
        scores.append((i, score))
    
    scores.sort(key=lambda x: x[1], reverse=True)
    return scores


# -----------------------------
# EUCLIDEAN DISTANCE
# -----------------------------
def euclidean_distance(a, b):
    return np.linalg.norm(a - b)

def euclidean_search(query, vectors):
    scores = []
    for i, vec in enumerate(vectors):
        distance = euclidean_distance(query, vec)
        scores.append((i, distance))
    
    scores.sort(key=lambda x: x[1])
    return scores


# -----------------------------
# SAMPLE DATA
# -----------------------------
vectors = np.array([
    [1, 2, 3],
    [2, 3, 4],
    [10, 10, 10]
])

query = np.array([1, 2, 3])


# -----------------------------
# RUN SEARCHES
# -----------------------------
print("Cosine Search Results:")
print(cosine_search(query, vectors))

print("\nEuclidean Search Results:")
print(euclidean_search(query, vectors))