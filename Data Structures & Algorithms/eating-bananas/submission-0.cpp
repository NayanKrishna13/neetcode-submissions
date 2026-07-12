class Solution {
public:
    int minEatingSpeed(vector<int>& piles, int h) {
        int f=1,l=*max_element(piles.begin(),piles.end());
        int mid;
        int res;
        while(f<=l)
        {
            mid=f+(l-f)/2;
            int sum=0;
            for(int i=0;i<piles.size();i++)
            {
                sum+=ceil((double)piles[i]/mid);
            }
            if (sum<=h)
            {
                res=mid;
                l=mid-1;
            }
            else
            {
                f=mid+1;
            }
        }

        return res;
    }
};
