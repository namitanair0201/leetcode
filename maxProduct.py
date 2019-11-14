
"""
int maxProduct(int A[], int n) {
    // store the result that is the max we have found so far
    int r = A[0];

    // imax/imin stores the max/min product of
    // subarray that ends with the current number A[i]
    for (int i = 1, imax = r, imin = r; i < n; i++) {
        // multiplied by a negative makes big number smaller, small number bigger
        // so we redefine the extremums by swapping them
        if (A[i] < 0)
            swap(imax, imin);

        // max/min product for the current number is either the current number itself
        // or the max/min by the previous number times the current one
        imax = max(A[i], imax * A[i]);
        imin = min(A[i], imin * A[i]);

        // the newly computed max value is a candidate for our global result
        r = max(r, imax);
    }
    return r;
"""
class Solution:
    def maxProduct(self, nums) -> int:
        n = len(nums)
        if n == 0:
            return 0
        elif n == 1:
            return nums[0]
        else:
            result = nums[0]
            i_max = result
            i_min = result
            for i in range(1,n):
                if nums[i] < 0:
                    i_max, i_min = i_min, i_max
                
                i_max = max(nums[i], i_max * nums[i])
                i_min = min(nums[i], i_min*nums[i] )

        return max(i_max, i_min)

if __name__ == "__main__":
    print(Solution().maxProduct([-2,3,-4]))