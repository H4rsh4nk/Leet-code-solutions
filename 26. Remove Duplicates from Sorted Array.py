class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        
        if endWord not in wordList:
            return 0

        pattern_dic = collections.defaultdict(list)
        siz = len(beginWord)
        wordList.append(beginWord)

        for i in wordList:
            for j in range(siz):
                pattern = i[:j]  + "*" + i[j+1:]
                pattern_dic[pattern].append(i)
        
        # print(pattern_dic) 

        traverse = set([beginWord])
        q = deque([beginWord])
        res = 1
        while q:
            for i in range(len(q)):
                word = q.popleft()
                if word == endWord:
                    return res
                for j in range(len(word)):
                    pattern = word[:j] + "*" + word[j+1:]
                    for newWord in pattern_dic[pattern]:
                        if newWord not in traverse:
                            traverse.add(newWord)
                            q.append(newWord)
            res +=1
                


        return 0