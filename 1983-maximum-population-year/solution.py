class Solution:
    def maximumPopulation(self, logs: List[List[int]]) -> int:
        OFFSET = 1950
        MAX_YEAR = 2051
        
        diff = [0] * (MAX_YEAR - OFFSET + 1)
        
        for birth, death in logs:
            diff[birth - OFFSET] += 1
            diff[death - OFFSET] -= 1
        
        max_pop = 0
        curr_pop = 0
        answer_year = OFFSET
        
        for year_offset in range(len(diff)):
            curr_pop += diff[year_offset]
            if curr_pop > max_pop:
                max_pop = curr_pop
                answer_year = OFFSET + year_offset
                
        return answer_year
