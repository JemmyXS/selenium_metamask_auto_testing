import time
import wallet
<<<<<<< HEAD
from config import global_config
import zkSync2_run_test as zkSync
import muteSwitch_run_test as muteSwitch

wallet = wallet.getWallet()
address_list = wallet[0]
result_path = global_config.get('path', 'result_path').strip()
result = open(str(result_path) + 'result.txt', mode='a', encoding='utf-8')

for i in range(1, 101):
    address = address_list[i]
    try:
        zkSync.runTest(address)
        time.sleep(3)
        muteSwitch.runMuteSwitchTestnet(address)
=======
import zkSync2_run_test as zkSync
import muteSwitch_run_test as muteSwitch

filename = '20220317_eth_zkSync_muteSwitch_100.xlsx'
address_list = wallet.getAddress(filename)
result = open('/Users/luoye/Downloads/TestNetwork/zkSync2/full/result.txt', mode='a', encoding='utf-8')
for i in range(1, 101):
    address = address_list[i]
    try:
        zkSync.runTest(filename, address)
        time.sleep(3)
        muteSwitch.runMuteSwitchTestnet(filename, address)
>>>>>>> 04ccdd8665eab17bae54d5aa0f127c387123126c
        time.sleep(3)
    except Exception as e:
        print(e)
        print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()) + " 第" + str(i) + "次执行失败")
        print(address + " run test failed", file=result)
        continue
    else:
        print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()) + " 第" + str(i) + "次执行成功")
        print(address + " run test success", file=result)
