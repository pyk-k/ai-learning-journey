# 导入需要使用的库
import json
import os
from dotenv import load_dotenv
import re

def load_env_secret():
    """【函数1】读取环境变量中的密钥"""
    # 加载 .env 文件
    load_dotenv()
    secret = os.getenv("SECRET_KEY")
    if secret is None:
        raise Exception("没有读取到密钥，请检查.env文件！")
    return secret


def read_text_file(file_path: str) -> str:
    """【函数2】读取txt文本文件"""
    with open(file_path, "r", encoding="utf-8") as f:
        content = f.read()
    return content


def count_text_info(text: str) -> dict:
    """【函数3】统计文本数据，返回字典"""
    # 全部字符（包含标点换行）
    total_chars = len(text)
    # 只匹配汉字
    chinese_list = re.findall(r'[\u4e00-\u9fff]', text)
    chinese_count = len(chinese_list)
    # 英文单词数量
    word_list = re.findall(r'[a-zA-Z]+', text)
    word_count = len(word_list)

    result_data = {
        "total_characters": total_chars,
        "chinese_count": chinese_count,
        "english_word_count": word_count
    }
    return result_data


def save_json(data: dict, save_path: str):
    """【函数4】将统计结果保存为json文件"""
    with open(save_path, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)


def main():
    """主入口函数，串联全部功能"""
    print("===== 文本分析工具启动 =====")

    # 读取密钥
    key = load_env_secret()
    print(f"成功读取安全密钥：{key}")

    # 读取文本
    file_content = read_text_file("input.txt")
    print("\n读取到的文本内容：")
    print(file_content)

    # 数据分析
    analyze_result = count_text_info(file_content)
    print("\n文本统计结果：", analyze_result)

    # 保存json
    save_json(analyze_result, "result.json")
    print("\n✅ 统计数据已经保存到 result.json")

    # ==================== 故意制造错误的测试代码（练习排错） ====================
    # 取消下面一行注释，运行就会报错 KeyError，练习定位bug
    # print(analyze_result["not_exist_key"])


if __name__ == "__main__":
    main()
