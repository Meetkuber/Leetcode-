class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        basket = {}
        left = 0
        max_picked = 0
        
        for right in range(len(fruits)):
            # 1. Add the new fruit to our window
            basket[fruits[right]] = basket.get(fruits[right], 0) + 1
            
            # 2. If we have more than 2 types of fruit, shrink from the left
            while len(basket) > 2:
                left_fruit = fruits[left]
                basket[left_fruit] -= 1
                
                # If a fruit type is completely gone, remove it from the basket
                if basket[left_fruit] == 0:
                    del basket[left_fruit]
                    
                left += 1
                
            # 3. Update the maximum fruits we can collect
            max_picked = max(max_picked, right - left + 1)
            
        return max_picked