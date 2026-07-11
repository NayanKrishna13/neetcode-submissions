class Solution {
public:
    int findMin(vector<int> &nums) {
        int f=0,l=nums.size()-1;
        //std::cout<<f<<l;
        int mid;
        while(f<=l)
        {
            if (abs(f-l)<=1)
            {
                if (nums[f]<nums[l])
                {
                    mid=f;
                }
                else
                {
                    mid=l;
                }
                break;
            }
            mid=f+(l-f)/2;
            if (nums[f]<=nums[l])
            {
                mid=f;
                break;
            }
            else
            {
                if ((nums[mid]<nums[l]))
                {
                    l=mid;
                }
                else
                {
                    f=mid;
                }

            }

        }
        return nums[mid];
    }
};
