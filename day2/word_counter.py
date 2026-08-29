#任务：用户输入一段英文，统计每个单词出现次数，按次数从高到低输出。

#必须处理的两个坑：

#大小写归一——The 和 the 算同一个词
#标点剔除——word. 和 word, 算同一个词
#① text = input("请输入一段英文：")     ← 拿到原始文本② text = text.lower()                  ← 全转小写
# ③ 标点处理：for 循环遍历字符串，字母或空格保留，其他字符替换成空格
# ④ words = text.split()                 ← 切成单词列表
#⑤ 字典计数：for word in words，存在+1，不存在置1
#⑥ 排序输出：sorted(counts.items(), key=lambda x: x[1], reverse=True)
text = input("请输入一段英文文本: ")
text = text.lower()
cleaned = ""                    # 存放结果
for ch in text:                 # 遍历每个字符
    if ch.isalpha() or ch == " ":
        cleaned = cleaned + ch  # 字母或空格，保留
    else:
        cleaned = cleaned + " " # 其他（标点数字等），替换成空格
words = cleaned.split()
counts = {}

for word in words:
    if word in counts:
        counts[word] = counts[word] + 1
    else:
        counts[word] = 1

result = sorted(counts.items(), key=lambda x: x[1], reverse=True)

for item in result:
    print(item[0], item[1])


