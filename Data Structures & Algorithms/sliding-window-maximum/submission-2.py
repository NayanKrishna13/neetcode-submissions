class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        if len(nums)==1 or k==1:
            return nums
        heap=[]
        ans=[]
        def insert(i,k):
            heap.append((i,k))
            curr=len(heap)-1
            while((curr-1)//2>=0):
                parent=(curr-1)//2
                if heap[curr][1]>heap[parent][1]:
                    heap[curr],heap[parent]=heap[parent],heap[curr]
                    curr=parent
                else:
                    break
            
        def delete():
            heap[0]=heap.pop()
            n=len(heap)
            curr=0
            while (2*curr+1)<n:
                left_child=2*curr+1
                right_child=2*curr+2
                largest=left_child
                if right_child<n and heap[right_child][1]>heap[left_child][1]:
                    largest = right_child
                    
                # If parent is smaller than the largest child, swap
                if heap[curr][1]<heap[largest][1]:
                    heap[curr],heap[largest] = heap[largest],heap[curr]
                    curr = largest
                else:
                    break

        i,j=0,0
        while(j<len(nums)):

            if j<k:
                insert(j,nums[j])
                j+=1
                if j==k-1:
                    insert(j,nums[j])
                    i+=1
                    j+=1
                    ans.append(heap[0][1])
            else:
                while(heap[0][0]<i):
                    delete()
                insert(j,nums[j])
                i+=1
                j+=1
                ans.append(heap[0][1])
                #print(heap)
        return ans


        