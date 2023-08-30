import sys
import os
import json
from datetime import datetime, timedelta

# 获取脚本或exe的路径
if getattr(sys, 'frozen', False):
    application_path = os.path.dirname(sys.executable)
else:
    application_path = os.path.dirname(os.path.abspath(__file__))

config_path = os.path.join(application_path, 'config.json')
holiday_path = os.path.join(application_path, 'holiday.json')

# 读取配置数据
with open(config_path, 'r', encoding='utf-8') as f:
    config = json.load(f)

with open(holiday_path, 'r', encoding='utf-8') as f:
    holidays = json.load(f)

# config中的变量
date_str = config['date_str']
days_to_add = config['days_to_add']
contract1 = config['contract1']
contract_amount = config['contract_amount']
factoring_amount = config['factoring_amount']

# 计算到期日
date_obj = datetime.strptime(date_str, '%Y-%m-%d')
date_obj += timedelta(days=days_to_add)
while date_obj.weekday() > 4 or holidays.get(date_obj.strftime('%Y-%m-%d')) in {1, 3}:  # 检查日期是否是周末或休息日
    date_obj += timedelta(days=1)
due_date = date_obj.strftime('%Y年%m月%d日')

# # 打印并确认日期
# print("到期日是：", due_date)
# confirm = input("这个日期是否正确？(yes/no): ")

# 获取当前日期
now = datetime.now()

elements = {
    '[day]': now.strftime('%d'),  # 上报日期
    '[day1]': date_str[-2:],  # 签约日期
    '[month]': now.strftime('%m'),  # 上报月份
    '[contract1]': contract1,  # 订单编号
    '[contract_amount]': contract_amount,  # 订单金额
    '[factoring_amount]': factoring_amount,  # 融资金额
    '[factoring_period]': str(days_to_add) + '天',  # 融资期限
    '[time]': due_date  # 到期日
}

# if confirm.lower() == "yes":
#     elements['[time]'] = due_date  # 到期日
# else:
#     new_date = input("请输入新的日期（格式为 YYYY年MM月DD日）：")
#     elements['[time]'] = new_date  # 到期日

CONFIG = {
    'TEMPLATE_PATH': os.path.join(application_path, "original"),  # 模板路径
    'OUTPUT_PATH': os.path.join(application_path, "contracted")  # 生成文件目录
}
