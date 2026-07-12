class Solution {
public:
    int findMin(std::vector<int> &nums) {
        int f=0,l=nums.size()-1;
        //std::cout<<"f: "<<f<<" l: "<<l<<"\n";
        int mid;
        while(f<l)
        {
            mid=(f+l)/2;
            //std::cout<<"mid: "<<mid<<"\n";
            if(nums[mid]>nums[l])
                f=mid+1;
            else
                l=mid;

        }
        return f;
    }
    int search(vector<int>& nums, int target) {
        int ind=findMin(nums);
        int n=nums.size();
        int f=0,l=n-1;
        while(f<=l)
        {
            int mid=(f+l)/2;
            int realmid=(mid+ind)%n;
            if(nums[realmid]==target)
                return realmid;
            else if(nums[realmid]<target)
                f=mid+1;
            else
                l=mid-1;
        }
        return -1;
        }
};
