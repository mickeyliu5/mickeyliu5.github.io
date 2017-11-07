import collections
class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        if not nums:
            return []

        counter = collections.Counter(nums)
        buckets = [[] for i in xrange(len(nums) + 1)]
        for num, cnt in counter.iteritems():
            print cnt
            buckets[cnt].append(num)
        ret = []
        for bucket in reversed(buckets):
            if len(ret) < k:
                ret.extend(bucket)
        return ret
if __name__ == "__main__":
    solution = Solution()
    import pprint
    pprint.pprint(solution.topKFrequent([1,1,1,2,2,3], 2))
