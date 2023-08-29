from datetime import datetime, timedelta

# 手动输入的变量
date_str = '2023-08-29'  # 出款日
days_to_add = 30  # 应收账款天数
contract1 = '2023-08280001'  # 订单编号
contract_amount = '壹仟伍佰零叁万肆仟柒佰叁拾元整'  # 订单金额
factoring_amount = '壹仟伍佰万元整'  # 融资金额

# 计算到期日
date_obj = datetime.strptime(date_str, '%Y-%m-%d')
date_obj += timedelta(days=days_to_add)
while date_obj.weekday() > 4:  # 0是星期一，6是星期天
    date_obj += timedelta(days=1)
due_date = date_obj.strftime('%Y年%m月%d日')

# 打印并确认日期
print("到期日是：", due_date)
confirm = input("这个日期是否正确？(yes/no): ")

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
}

if confirm.lower() == "yes":
    elements['[time]'] = due_date  # 到期日
else:
    new_date = input("请输入新的日期（格式为 YYYY年MM月DD日）：")
    elements['[time]'] = new_date  # 到期日

CONFIG = {
    'TEMPLATE_PATH': "/Users/wenjia/Documents/original",  # 模板路径
    'OUTPUT_PATH': "/Users/wenjia/Documents/contract"  # 生成文件目录
}