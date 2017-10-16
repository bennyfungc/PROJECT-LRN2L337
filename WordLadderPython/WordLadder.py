def ladderLength(beginWord, endWord, wordList):
    """
    :type beginWord: str
    :type endWord: str
    :type wordList: List[str]
    :rtype: int
    """

    visited = set()

    #implement doublesided bfs
    queue1 = []
    queue1.append(beginWord)
    queue2 = []
    path = 1
    if endWord not in wordList:
        return 0
    queue2.append(endWord)

    while queue1 and queue2:
        if len(queue2) < len(queue1):
            temp = queue2
            queue2 = queue1
            queue1 = temp
        newqueue1 = []
        for curr in queue1:
            for i in range(len(curr)):
                for c in "abcdefghijklmnopqrstuvwxyz":
                    newstr = curr[:i] + c + curr[i+1:]
                    if newstr in queue2:
                        return path+1
                    elif newstr in wordList and newstr not in visited:
                        newqueue1.append(newstr)
                        visited.add(newstr)
        queue1 = newqueue1
        path+=1
    return path



               



print ladderLength( "hit", "cog", ["hot","dot","dog","lot","log","cog"])




