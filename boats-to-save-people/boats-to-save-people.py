class Solution(object):
    def numRescueBoats(self, people, limit):
        """
        :type people: List[int]
        :type limit: int
        :rtype: int
        """
        people.sort()
        boats = 0
        
        while len(people) > 1:
            while people[0] + people[-1] > limit:
                del people[-1]
                boats += 1
                if len(people) < 2:
                    return boats + len(people)
            while people[0] + people[-1] <= limit:
                del people[-1]
                del people[0]
                boats += 1
                if len(people) < 2:
                    return boats + len(people)
    
        return boats + len(people)
        