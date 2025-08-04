import asyncio

async def cong(a, b):
    await asyncio.sleep(1)
    return a + b

async def tru(a, b):
    await asyncio.sleep(1)
    return a - b

async def nhan(a, b):
    await asyncio.sleep(1)
    return a * b

async def chia(a, b):
    await asyncio.sleep(1)
    return a / b if b != 0 else "Không thể chia cho 0"

async def main():
    a, b = 10, 5
    ket_qua = await asyncio.gather(
        cong(a, b),
        tru(a, b),
        nhan(a, b),
        chia(a, b)
    )
    print(f"Cộng: {ket_qua[0]}")
    print(f"Trừ: {ket_qua[1]}")
    print(f"Nhân: {ket_qua[2]}")
    print(f"Chia: {ket_qua[3]}")

if __name__ == "__main__":
    asyncio.run(main())