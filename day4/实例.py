import asyncio
import math

async def area(radius,delay):
    print("计算圆形的面积")
    await asyncio.sleep(delay)
    print(math.pi*radius**2)

async def perimeter(radius,delay):
    print("计算圆形的周长")
    await asyncio.sleep(delay)
    print(math.pi*radius*2)

async def main():
    # 两个独立任务并发，互不调用
    await asyncio.gather(area(3,2), perimeter(3,2))

if __name__ == "__main__":
    asyncio.run(main())
