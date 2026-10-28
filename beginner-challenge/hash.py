def hash_key(keys):
    result = []
    for key in keys:
        cs = sum(ord(char) for char in key) 
        rem = cs % 7
        result.append((cs, rem))
    return result

print(hash_key(['cat', 'act', 'dog', 'god']))

# Identify any collisions. Explain why different strings can map to the same index and why a matching index does not prove two keys are equal.
# ANS: different keys can map to the same index bcos they have the same hash value when calculated with the hash function, a matching index doesnt prove two keys are equal bcos, two keys may have the same characters and mean the same thing, therfore having different values also


def put(key, value):
    buckets = [[], [], [], [], [], [], []]

    index = hash_key()