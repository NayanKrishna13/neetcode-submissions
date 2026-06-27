class Twitter:

    def __init__(self):
        self.following={}
        self.tweetstack=[]

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweetstack.append([userId,tweetId])
        #print(self.tweetstack)
        
        

    def getNewsFeed(self, userId: int) -> List[int]:
        count=0
        i=len(self.tweetstack)-1
        ans=[]
        while(i>=0 and count<10):
            if (self.tweetstack[i][0]==userId) or ((userId in self.following) and (self.tweetstack[i][0] in self.following[userId])):
                count+=1
                ans.append(self.tweetstack[i][1])
            i-=1
        return ans
        

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId in self.following:
            self.following[followerId].add(followeeId)
        else:
            self.following[followerId]=set()
            self.following[followerId].add(followeeId)
        


    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.following[followerId]:
            self.following[followerId].remove(followeeId)
        
