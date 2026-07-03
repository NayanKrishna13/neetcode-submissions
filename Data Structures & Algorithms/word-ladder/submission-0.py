class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        from collections import deque
        def wordsplit(word):
            l=[]
            t=list(word)
            for j in range(len(word)):
                a=t[j]
                t[j]="_"
                l.append(''.join(t))
                t[j]=a
            return l
        
        visitedict={}
        wordict=defaultdict(list)
        for j in range(len(wordList)):
            visitedict[wordList[j]]=float('inf')
            l=wordsplit(wordList[j])
            for word in l:
                wordict[word].append(wordList[j])

        #print(wordict)
        q=deque()
        q.append((1,beginWord))
        while(q):
            curr,word=q.popleft()
            lists=wordsplit(word)
            for holder in lists:
                #if holder in wordict:
                for w in wordict[holder]:
                    if w==endWord:
                        return curr+1
                    else:
                        if visitedict[w]>curr+1:
                            #print(curr+1,w)
                            q.append((curr+1,w))
                            visitedict[w]=curr+1
        #print(visitedict)
        return 0





            
        







        