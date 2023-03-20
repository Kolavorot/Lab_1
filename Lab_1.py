def num_to_text(s):
    nums = {1: 'один', 2: 'два', 3: 'три', 4: 'четыре', 5: 'пять', 6: 'шесть', 7: 'семь', 8: 'восемь', 9: 'девять', 0: 'ноль'}
    r = []
    for i in s:
        r.append(nums[int(i)])
    return ' '.join(r)
k = 2
buffer_len = 100  # размер буффера чтение
work_buffer = []  # Рабочий буффер
work_buffer_len = buffer_len
with open("text.txt", "r") as file:
    while True:
        buffer = file.read(buffer_len)
        if not buffer:
            print("\nВ файле больше нет символов или файл пустой.")
            break
        buffer = buffer.split()
        for str in buffer:
            if str.isdigit():
                work_buffer.append(str)
                if len(work_buffer) == 10:
                    for str in buffer:
                        if buffer.count(str) == k:
                            print(' '.join(work_buffer[:9]), num_to_text((work_buffer[-1])))
                            work_buffer.clear()
                            break