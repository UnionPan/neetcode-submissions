class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = []
        maps = {}
        for s in strs:
            chars = "".join(sorted(s))
            
            if chars not in maps:
                maps[chars] = [s]
            else:
                maps[chars].append(s)

        for key in maps:
            groups.append(maps[key])
        return groups