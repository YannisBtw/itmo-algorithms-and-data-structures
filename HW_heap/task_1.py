import heapq

import numpy as np


def top_k_search(embeddings, query, k):
    """Вернуть k ближайших векторов к запросу."""

    if k <= 0:
        return []

    heap = []

    for index, embedding in enumerate(embeddings):
        distance = np.linalg.norm(embedding - query)

        if len(heap) < k:
            heapq.heappush(heap, (-distance, index))

        else:
            worst_distance = -heap[0][0]

            if distance < worst_distance:
                heapq.heapreplace(heap, (-distance, index))

    result = [
        (-negative_distance, index)
        for negative_distance, index in heap
    ]

    result.sort()

    return result
