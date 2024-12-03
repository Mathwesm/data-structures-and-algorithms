def bucket_sort(notas):
    max_nota = 100
    bucket_count = 10  
    buckets = [[] for _ in range(bucket_count)]


    for nota in notas:
        index = int((nota / max_nota) * (bucket_count - 1))
        buckets[index].append(nota)


    for bucket in buckets:
        bucket.sort()

    notas_ordenadas = []
    for bucket in buckets:
        notas_ordenadas.extend(bucket)

    return notas_ordenadas