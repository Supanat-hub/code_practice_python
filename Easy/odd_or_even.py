# รับค่าเลขจำนวนเต็มแล้วบอกว่าเป็นเลขคู่หรือเลขคี่
'''
Input: 7  
Output: Odd
'''
num = int(input())
if num % 2 == 0:
    print('Even')
else:
    print('Odd')