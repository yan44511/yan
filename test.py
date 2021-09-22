import pyupbit

access = "EjKGZYbh20Vng55K02E2WEPYaIR2XUrPaYSfu7tU"          # 본인 값으로 변경
secret = "70amWIPNQTkU8JvXxcGDIk4dbdfAnY5tE5bTLMMm"          # 본인 값으로 변경
upbit = pyupbit.Upbit(access, secret)

print(upbit.get_balance("KRW-BTC"))     # KRW-BTC 조회
print(upbit.get_balance("KRW"))         # 보유 현금 조회
