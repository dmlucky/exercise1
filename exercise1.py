# 打开要读取的文件
with open('file_to_read.txt', 'r') as file:
    text = file.read()

# 计算单词 "terrible" 出现的总次数
terrible_count = text.count('terrible')

# 替换偶数次出现的 "terrible" 为 "pathetic"，奇数次出现的为 "marvellous"
if terrible_count % 2 == 0:
    replaced_text = text.replace('terrible', 'pathetic')
else:
    replaced_text = text.replace('terrible', 'marvellous')

# 将替换后的文本写入新文件 result.txt
with open('result.txt', 'w') as result_file:
    result_file.write(replaced_text)

# 打印总次数
print(f"'terrible'出现的次数: {terrible_count}")
