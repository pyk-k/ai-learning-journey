
def clean_text(text):
    """输入原始文本，返回小写、无标点的干净文本"""
    text = text.lower()
    cleaned = ""
    for ch in text:
        if ch.isalpha() or ch==" ":
            cleaned = cleaned + ch
        else:
            cleaned = cleaned + " "    
    return cleaned
def count_words(cleaned):
    """输入干净文本，返回统计好的字典"""
    words = cleaned.split()
    count = {}
    for word in words:
        if word in count:
            count[word] = count[word]+1
        else:  
            count[word] =1   
    return count
def print_results(counts):
    """输入字典，按次数降序打印"""
    words = sorted(counts.items(),key=lambda x:x[1],reverse=True)
    for i in words:
        print(f"{i[0]} : {i[1]}")       

def main():
    """读文件 → 依次调用上面三个函数"""
    try:
        with open("sample.txt","r",encoding="utf-8")as f:
         text = f.read()
    except FileNotFoundError:
        print("错误找不到对应路径")
        return
    cleaned = clean_text(text)
    counts = count_words(cleaned)
    print_results(counts)  
    
if __name__ == "__main__":
    main()
    