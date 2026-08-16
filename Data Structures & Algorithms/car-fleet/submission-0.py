class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = {}
        time = []
        for i, pos in enumerate(position):
            cars[pos] = speed[i]
        
        position.sort(reverse=True)
        print(position)
        
        for pos in position:
            arrival_time = (target - pos) / cars[pos] 
            if len(time) > 0:
                if arrival_time > time[-1]:
                    time.append(arrival_time)
            else:
                time.append(arrival_time)

        return len(time)

        
        
            
        