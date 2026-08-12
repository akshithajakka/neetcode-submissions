class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # create defaultdict - so that empty keys can have default values and empty values
        # are empty lists
        res = defaultdict(list)

        # count the number of each letter in the alphabet in strs
        for s in strs:
            count = [0] * 26

            for c in s:
                count[ord(c) - ord('a')] += 1

            # key = count signature, value = strings that match that count signature
            res[tuple(count)].append(s)
        
        return list(res.values())


        
        







         