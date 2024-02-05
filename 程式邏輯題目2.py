def calculate_height(num_bounces):
    initial_height = 100
    down_height = 0
    bounce_height = 0
    all_height = 0
    for _ in range(num_bounces):
        # 計算每次落下反彈的高度
        down_height += bounce_height + initial_height
        # 下一次的高度為原高度的一半
        initial_height /= 2
        # 算出每次反彈的高度
        bounce_height = initial_height
        all_height = down_height + bounce_height
    return all_height - bounce_height, bounce_height #最後一次不用加反彈的高度

# 計算在第10次落地時的總共經歷高度和第10次反彈的高度
num_bounces = 10
result = calculate_height(num_bounces)
all_height, bounce_height = result

print(f"第{num_bounces}次落地時，總共經歷高度：{all_height:.6f} 公分")
print(f"第{num_bounces}次反彈高度：{bounce_height:.6f} 公分")