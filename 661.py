import math

n, k = [int(i) for i in input().split()]
a, b = [int(i) for i in input().split()]

days_needed_to_go_from_a_to_b = math.ceil(abs(a - b) / k)
days_to_get_min_max_temperature = n - days_needed_to_go_from_a_to_b

max_delta_temp = days_to_get_min_max_temperature // 2 * k

min_temp = min(a, b) - max_delta_temp
max_temp = max(a, b) + max_delta_temp

print(max_temp, min_temp)
