# Day 4 — 代码规范与类型系统（第 1 阶段第 1 天）

> 8 周计划里，第 1—2 周的目标是「Python 工程能力重塑」：类型、函数、异常、文件、模块、测试、Git。
> Day 1 只干一件事：**把过去一个月积累的坏习惯，从根上清掉。**
> 今天的产出不追求"新功能"，追求"你以前写的代码能过关"。

---

## 一、为什么第 1 天不是学新东西

你的摸底报告里，8 道题的**最终**得分全是 10 分，但**首答**是这样的：

```
题 4（类）   6  →  8  →  10    三次
题 5（异常） 6  →  8  →  10    三次
题 6（Pandas）6  →  9  →  10    三次
题 7（综合） 5  →       10    一次跳到满分（说明是结构性疏漏，不是不会）
```

首答和终答的差距，就是**工程习惯**的差距。而你现在**已经在写 function calling 的 Agent 了**——
一个基础不牢的 Agent 开发者，写的代码是能跑但**没人敢接手**的。第 1 天就是来还这笔债的。

---

## 二、硬性检查清单（今天要过的关）

下面是摸底报告点名的 5 个问题，加上我在你现有代码里**又挖出的 3 个新问题**。
每一项都给你「哪里错了 / 怎么改 / 怎么防」。

### 🔴 1. 运算符不加空格 ← 全仓库最严重

**现状**（`day3/word_counter_v2.py`）：

```python
if ch.isalpha() or ch==" ":        # 第 7 行
            count[word] = count[word]+1    # 第 18 行
    words = sorted(counts.items(),key=lambda x:x[1],reverse=True)  # 第 24 行
```

**要求**：

```python
if ch.isalpha() or ch == " ":
            count[word] = count[word] + 1
    words = sorted(counts.items(), key=lambda x: x[1], reverse=True)
```

**注意最后一行是**：`key=lambda x: x[1]` —— 冒号后要空格，逗号后要空格。你写的是 `key=lambda x:x[1],reverse=True`，
两处都漏了。

**怎么防**：装 PyCharm 自带的格式化（`Ctrl+Alt+L`），每次写完按一次。

---

### 🔴 2. 缩进错乱

**现状**（`day3/word_counter_v2.py` 第 31–32 行）：

```python
    try:
        with open("sample.txt","r",encoding="utf-8")as f:
         text = f.read()
```

`with` 下面缩进 8 格，`text` 却缩进 9 格。能跑，但**这是定时炸弹**——下次在里面加一行，
缩进对不齐直接报 `IndentationError`。

还有一处更隐蔽（`联网项目/art.py` 第 12–16 行）：`if not nums:` 的主干语句缩进 8 格，
`df = pd.DataFrame(nums)` 却缩进 4 格。**能跑，但语义已经错了**——后面那些行已经跑到 `if` 外面去了。

**要求**：一个块内所有语句**左边缘严格对齐**。PyCharm 里选中代码 `Tab` / `Shift+Tab` 统一调。

---

### 🔴 3. 宽泛异常 `except Exception:`

**现状**（`1.py` 第 22 行、`agent2.py`、`自写多轮对话.py` 第 45 行）：

```python
try:
    a = eval(expression)
    return str(round(a, 2))
except:              # ← 裸 except，连 Exception 都没写
    return "算不出来"
```

摸底的题 8 你**已经改对了**——"弃用宽泛的 `except Exception`"。**但你真实项目里还留着。**
这就是典型的「考试会，干活就忘」。

**要求**：只捕获你**真正预期**的异常。

```python
try:
    a = eval(expression)
except (SyntaxError, ZeroDivisionError, NameError):
    return "算不出来"
return str(round(a, 2))
```

注意我把 `return` 挪出 `try` 了——`try` 块里**只放可能出错的那一行**，不要什么都往里塞。

---

### 🟠 4. `print` 和 `return` 职责混淆（你的老毛病）

**现状**（`信息存储.py`）：

```python
def info(self):
    print("姓名:", self.name)
    ...
```

这个方法叫 `info`，但它的**唯一作用就是打印**。如果明天你想把学生信息存成 JSON，
这个方法一点用都没有。

**要求**：把「算」和「显示」分开——这正好是 `day3/word_counter_v2.py` 里你做对的事，把它推广开。

```python
def to_dict(self):
    """返回学生信息的字典"""
    return {"name": self.name, "age": self.age, "gender": self.gender, "score": self.score}

def show(self):
    """打印学生信息"""
    info = self.to_dict()
    print(f"姓名: {info['name']}, 年龄: {info['age']}, ...")
```

**判断标准**：函数名里没有 `print` / `show` / `display` 的，就不该出现 `print()`。
唯一的例外是 `main()` 和专门的显示函数。

---

### 🟠 5. `input()` 返回字符串没转换 ← 你历史上重复踩过

**现状**（`信息存储.py`）：

```python
c = Student(b[0], b[1], b[2], b[3])
```

`b` 是 `i.split("#")` 的结果，里面全是**字符串**。所以 `Student.age` 存的是 `"20"` 不是 `20`。
摸底的题 4（类）你首答 6 分，扣分点就在这。

**要求**：

```python
age = int(b[1])
gender = b[2]
score = float(b[3])
c = Student(b[0], age, gender, score)
```

**怎么防**：见到 `input()` 或 `split()` 的结果要拿去算数，**先在脑子里过一遍"它是 str"**。

---

### 🟠 6. 变量名偷懒

**现状**（`联网项目/art.py`）：

```python
nums = []
dic = {...}
```

摸底报告已经点名：`record → records`、`dic → result`。**改法**：

- `nums` → `records`（这是一组学生记录，不是一组数字）
- `dic` → `summary` 或 `result`

`count` / `num` / `dic` / `x` 这类名字，过两周你自己都看不懂。

---

### 🔴 7. 硬编码 API key ← 安全红线，今天必须清掉

**现状**（`联网项目/1.py` 第 66 行）：

```python
client = OpenAI(
    api_key="96361dffba...",     # ← 明文写死在代码里
    base_url="https://open.bigmodel.cn/api/paas/v4/"
)
```

**同目录 `agent2.py` / `agent3.py` / `自写多轮对话.py` 都做对了**（`os.getenv` + `load_dotenv`）。
只有 `1.py` 漏了。**一个仓库里两种写法，说明你不是不会，是没统一。**

**要求**：

```python
import os
from dotenv import load_dotenv

load_dotenv()
client = OpenAI(
    api_key=os.getenv("api_key"),
    base_url=os.getenv("base_url"),
)
```

**并且**：既然这个 key 已经写在文件里被复制过多次，**去智谱后台把它删掉重新生成一个**。
删旧 key 这一步别省。

---

### 🔴 8. 泄露密钥的 print

**现状**（`联网项目/text_analyze.py` 第 55 行）：

```python
key = load_env_secret()
print(f"成功读取安全密钥：{key}")       # ← 把密钥打进终端了
```

终端输出会进 Shell 历史、可能被截图、可能被 AI 读取。**直接删掉这行**，
或者改成 `print("✅ 密钥加载成功")`。

---

## 三、今日任务

### 任务 A：清理旧代码（45 分钟）

把上面 8 条，逐条落到你**已经写过**的文件上。至少覆盖：

| 文件 | 要改哪几条 |
|---|---|
| `day3/word_counter_v2.py` | 1（空格）、2（缩进） |
| `联网项目/1.py` | 3（裸 except）、7（硬编码 key） |
| `联网项目/text_analyze.py` | 8（删泄露的 print） |
| `联网项目/信息存储.py` | 4（print/return）、5（类型转换） |
| `联网项目/art.py` | 2（缩进）、6（命名） |

**这是今天的重头戏**。改完每个文件都要**重新运行一遍**，确认输出没变。

### 任务 B：新写一个模块（45 分钟）

在 `day4/` 下建 `score_utils.py`，写 3 个函数：

1. `parse_scores(text: str) -> list[float]`
   输入 `"80, 95.5 , 60"`，返回 `[80.0, 95.5, 60.0]`（注意处理空格）
2. `summarize(scores: list[float]) -> dict`
   返回 `{"count": 3, "average": 78.5, "max": 95.5, "min": 60.0}`
3. `main()` 用 `input()` 收一串成绩，调用上面两个函数，打印结果

**硬性要求**：
- 空输入 → `parse_scores` 返回 `[]`，`summarize` 返回全 `None` 的字典（**不准崩**）
- 非法输入 `"80,abc,90"` → 抛 `ValueError`，`main` 里捕获并提示，不准用裸 `except`
- 每个函数一行 docstring，且**代码做的事必须和 docstring 一致**
- 冒号后、逗号后、运算符两侧，全都要空格

### 任务 C：写测试（30 分钟）

新建 `day4/test_score_utils.py`，用 `pytest` 写至少 4 个测试：

- 正常输入
- 空字符串
- 只有空格
- 非法输入抛 `ValueError`

`pytest` 还没装，先装：

```bash
uv pip install pytest
```

---

## 四、通关标准

今天**三条全满足**才算完成（缺一条就是没完成）：

1. **任务 A 的 8 条全部落实**，每个改过的文件都重新跑过，贴出运行输出
2. `pytest` 全绿，贴出 `pytest -v` 的输出
3. `notes.md` 补 Day 4 复盘，**必须包含**：
   - 8 条里哪几条你改的时候"一改就发现还有别的地方也没改"（这能暴露你的习惯性问题）
   - 根因分析：为什么摸底考了 10 分，真实代码里还是犯？（**不准写"粗心""不仔细"，退回重写**）
4. `git commit` + `git push`

---

## 五、提交格式

```bash
git add day3/ day4/ notes.md
git commit -m "day4: fix code style issues and add typed score utils with tests"
git push
```

---

## 六、交之前先自查

- [ ] 8 条全改完了吗？有没有哪条我"看了但跳过了"？
- [ ] 改完的每个文件，我都**运行过**吗？（不是"我觉得能跑"）
- [ ] `score_utils.py` 空输入会崩吗？试过吗？
- [ ] `pytest` 真的跑到全绿了吗？
- [ ] 有没有哪个 `print()` 还留在"算"的函数里？
- [ ] 代码里还有没有 `api_key="sk-..."` 这种明文？

---

## 附：为什么第 1 天要做这些

你现在的技术水平（已经写过 function calling、流式输出、多轮对话）
**已经越过了第 3 周的 LLM API 部分**。但那个诊断报告说的"不适合直接开始复杂 Agent 项目"，
指的不是你的 API 知识不够，而是：

> **你写的代码，别人不敢接手。**

一个 2000 行的 Agent 项目，如果变量叫 `a` / `b` / `dic`、异常全靠 `except Exception` 兜、
密钥硬编码在源码里——**它跑得起来，但它是个定时炸弹**。

第 1 天做的是"清扫"，第 2 天开始才往上加能力。
