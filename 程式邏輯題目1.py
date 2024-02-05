def calculate_new_score(original_score):
    
    next_multiple_of_5 = ((original_score + 4) // 5) * 5  # 下一個最接近的5的倍數
    difference = next_multiple_of_5 - original_score
    
    if difference <= 3:
        if next_multiple_of_5 >= 40:
           return next_multiple_of_5  # 新分數為下一個最接近的5的倍數
        else:
           return original_score  # 不予加分，保持原分數
    else:
        return original_score  # 不予加分，保持原分數

# 學生名稱及原始分數
students = {'德瑞克': 33, '尚恩': 73, '傑夫': 63, '馬基': 39}

# 計算並輸出換算後的總成績
for student, original_score in students.items():
    new_score = calculate_new_score(original_score)
    print(f'{student} 換算後的總成績為: {new_score}')