class Solution(object):
    def carFleet(self, target, position, speed):
        """
        :type target: int
        :type position: List[int]
        :type speed: List[int]
        :rtype: int
        """
        
        cars = []
        for i in range(len(position)):
            cars.append((position[i], speed[i]))
        
        cars.sort()

        fleets = 1
        lc = cars.pop()
        while cars:
            p, s = cars.pop()
            time1 = (target - lc[0]) / float(lc[1])
            time2 = (target-p) / float(s)
            print(time1, time2, p, s)

            if time2 > time1:
                lc = (p,s)
                fleets +=1

        return fleets

        
