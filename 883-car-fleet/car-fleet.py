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
            time_left = (target - position[i]) / float(speed[i])
            cars.append((position[i], time_left))
        
        cars.sort()

        fleets = 1
        lc = cars.pop()
        while cars:
            p, t = cars.pop()
            if t > lc[1]:
                lc = (p,t)
                fleets +=1

        return fleets

        
