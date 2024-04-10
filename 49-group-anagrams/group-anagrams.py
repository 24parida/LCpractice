class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """

        if len(strs) == 1: return [strs]

        ret = []

        for i in strs:
            if len(ret) == 0: 
                ret.append([i])
                continue

            added = False
            for l in ret:
                # only need to check first of every list
                s = l[0]
                # if it is an anagram append to that list
                if len(s) != len(i): continue

                d = {}
                for let in s: 
                    if let in d: d[let] += 1
                    else: d[let] = 1
                
                skip = False
                for let in i:
                    if let not in d or d[let] == 0: 
                        skip = True
                        break
                    d[let] -= 1
                if skip: continue

                l.append(i)
                added=True

            # else append to ret
            if not added: 
                ret.append([i])

        return ret
  
        