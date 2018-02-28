class Solution(object):
    def licenseKeyFormatting(self, S, K):
        """
        :type S: str
        :type K: int
        :rtype: str
        """

        if not S or not K:
            return ""

        new_s = "".join(S.split("-"))
        ret = []
        index = len(new_s)
        while index > 0:
            print index
            left_index = index - K
            if left_index < 0:
                left_index = 0
            ret.append(new_s[left_index : index])
            index = left_index
        return "-".join(ret)

if __name__ == "__main__":
    solution = Solution()
    import pprint
    pprint.pprint(solution.licenseKeyFormatting("5F3Z-2e-9-w", 4))
