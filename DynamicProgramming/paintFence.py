# https://leetcode.com/problems/paint-fence/submissions/

# for n posts (index 1) and k ways to paint, return number of ways to paint n posts if only 2 can be consecutive color
# base cases n == 1 -> k ways to paint so far
# base case n == 2 -> k*k ways to paint so far
# generic case n -> k-1 * ways to paint the last 2 posts

class Solution:
    def numWays(self, n: int, k: int) -> int:
        if n == 1:
            return k
        two_posts_back = k
        one_post_back = k*k
        
        # n+1 as we index from 1
        for i in range(3, n+1):
            curr = (k-1) * (one_post_back + two_posts_back)
            two_posts_back = one_post_back
            one_post_back = curr
        
        return one_post_back
    