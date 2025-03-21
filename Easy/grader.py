# คำนวณคะแนนเกรดของนักเรียน
# โดยให้นักเรียนกรอกคะแนนเต็ม 100 คะแนน
# และแสดงเกรดที่ได้
# โดยใช้เกณฑ์ดังนี้
# คะแนน 80-100 ได้เกรด A
# คะแนน 70-79 ได้เกรด B
# คะแนน 60-69 ได้เกรด C
# คะแนน 50-59 ได้เกรด D
# คะแนน 0-49 ได้เกรด F
# ให้แสดงผลเป็น
'''
Input score: 49
Output: F
'''
score = int(input('Input score: '))
if score >= 80:   
    print('A')
elif score >= 70: 
    print('B')
elif score >= 60:
    print('C')
elif score >= 50:
    print('D')
else:
    print('F')