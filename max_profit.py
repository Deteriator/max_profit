"""
P


E 
  get_max_profit([10,15,7,25,8]) == 18
  get_max_profit([6,11,9,3,15]) == 12
  get_max_profit([12,20,7,11,5]) == 8
  get_max_profit([12,30,1,24,0,2]) == 23
  get_max_profit([100,120,0,21,300,12]) == 300
  get_max_profit([100,120,21,300,0,12]) == 279
  get_max_profit([100,120,21,300,0,12]) == 20
  get_max_profit([300,120,100,21,12]) == -9
  
D List

Algorithm

"""
def max_profit(prices):
        max = prices[1] - prices[0]
        for i in range(len(prices)):
            for j in range(i + 1,len(prices)):
                if prices[j] - prices[i] > max:
                    max = prices[j] - prices[i]
        return max
        
        
def get_max_profit(prices):
    max_diff = prices[1] - prices[0] 
    min_element = prices[0] 
    for i in range(1,len(prices)):
        if prices[i] - min_element > max_diff:
            max_diff = prices[i] - min_element
        if prices[i] < min_element:
            min_element = prices[i]
    return max_diff
    
print(get_max_profit([300,120,100,21,12]) == -9)