word1 = 'tree'
word2 = 'three'

def LevenshteinDistance(word1, word2):
    rows = len(word1) + 1
    cols = len(word2) + 1

    dist = [[0 for _ in range(cols)] for _ in range(rows)]

    for i in range(rows):
        dist[i][0] = i
    for j in range(cols):
        dist[0][j] = j

    for i in range(1, rows):
        for j in range(1, cols):
            if word1[i-1]==word2[j-1]:
                dist[i][j] = dist[i-1][j-1]
            else:
                dist[i][j] = min(dist[i-1][j-1], dist[i-1][j], dist[i][j-1]) + 1
    return dist[-1][-1]
        
        

print(LevenshteinDistance(word1, word2))
        
