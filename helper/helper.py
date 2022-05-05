import time
import datetime
import random
import string
import uuid
from collections import Counter
from decimal import Decimal
from collections import Counter
# 参数格式化
from datetime import datetime
from decimal import Decimal
from typing import Union, Any, List, Dict


def get_uuid4():
    return str(uuid.uuid4())


def compute_total_tax_amount(num, price, tax_rate):
    """
    金额计算
    :param num: 数量
    :param price: 单价（不含税）
    :param tax_rate: 税率
    :return: 总金额（含税）、总金额（不含税）
    """
    total_amount = num * Decimal(price)
    total_amount_with_tax = total_amount * (1 + Decimal(tax_rate))
    return {
        "total_amount": total_amount,
        "total_amount_with_tax": total_amount_with_tax
    }


# 返回八位随机字符串 或 时间戳 + 字符串
def eight_random_str(int_time=None, mode=1):
    """
    :param int_time:
    :param mode: 模式   1 为 随机字符串 8位   2 为 随机数字 8位
    :return:
    """
    if mode == 1:
        random_str = ''.join(random.sample(string.ascii_letters + string.digits, 8))
    else:
        random_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
        random_str = ''.join([str(num) for num in random.sample(random_list, 8)])
    if not int_time:
        return random_str
    else:
        return str(int_time) + random_str


def get_time_str(prefix="", space_mark=''):
    """
    :param prefix 前缀
    :param space_mark 间隔符
    :return: 'NO20210901103521'
    """
    timestamp = time.time()
    time_struct = time.localtime(timestamp)
    format_str = f'%Y{space_mark}%m{space_mark}%d{space_mark}%H{space_mark}%M{space_mark}%S'
    time_str = time.strftime(format_str, time_struct)
    return f'{prefix}{time_str}'


def is_valid_date(params, format_str='%Y-%m-%d'):
    """判断是否是一个有效的日期字符串"""
    try:
        datetime.datetime.strptime(params, format_str)
        return True
    except Exception as e:
        # print("is_valid_date", e)
        return False


def is_valid_month(params):
    """判断是否是一个有效的年月日期字符串"""
    try:
        fmt = "%Y-%m"
        datetime.datetime.strptime(params, fmt)
        return True
    except Exception as e:
        print("is_valid_month", e)
        return False


def str_to_date(date_str, fmt='%Y-%m-%d'):
    time_str = datetime.datetime.strptime(date_str, fmt)
    return time_str


def str_to_date_time(date_time_str):
    fmt = "%Y-%m-%d %H:%M:%S"
    try:
        time_str = datetime.datetime.strptime(date_time_str, fmt)
        return time_str
    except Exception as e:
        print("str_to_date_time", e)


# 时间字符串转时间戳
def str_to_timestamp(v, format_str='%Y-%m-%d'):
    return str(int(time.mktime(time.strptime(v, format_str))))


def str_to_datetime(timestamp, is_hms=True):
    try:
        timestamp = int(timestamp) / 1000
        date_array = datetime.datetime.fromtimestamp(timestamp)
        if is_hms:
            other_style_time = date_array.strftime("%Y-%m-%d %H:%M:%S")
        else:
            other_style_time = date_array.strftime("%Y-%m-%d")
    except Exception as e:
        other_style_time = ""
    return other_style_time





def find_diff_from_two_li(list1, list2):
    new_li = list(set(list1)) + list(set(list2))
    count = Counter(new_li)
    same, diff = [], []
    for i in count.keys():
        if count.get(i) >= 2:
            same.append(i)
        else:
            diff.append(i)
    return {"same": same, "diff": diff}


def timestamp_to_time_str(timestamp: int, format_str="%Y-%m-%d"):
    try:
        if len(str(timestamp)) == 13:
            timestamp = timestamp / 1000
        else:
            timestamp = timestamp
        date_array = datetime.datetime.fromtimestamp(timestamp)
        other_style_time = date_array.strftime(format_str)
    except Exception as e:
        print(e)
        other_style_time = ""
    return other_style_time


def add2unknown(params1, params2):
    """计算两个可能为空的数字"""
    if params1 is None and params2 is None:
        return ''
    if params1 is None:
        return params2
    if params2 is None:
        return params1
    return params1+params2


def db_replace_params(data: Union[Dict[str, Any], List[Dict[str, Any]]], replace_none=True,
                      replace_datetime=True, format_replace_data_str="%Y-%m-%d %H:%M:%S", is_timestamp=True,
                      is_second=False, is_decimal=False,
                      decimal_two_digit_string=False, int_to_str=False, callback=None, s_to_timestamp=False,
                      format_str='%Y-%m-%d', is_set=True, replace_url_list: list = None) -> None:
    if isinstance(data, list):
        for i in data:
            db_replace_params(i, is_timestamp=is_timestamp, is_second=is_second, is_decimal=is_decimal,
                              decimal_two_digit_string=decimal_two_digit_string, replace_none=replace_none,
                              replace_datetime=replace_datetime, format_replace_data_str=format_replace_data_str,
                              int_to_str=int_to_str, callback=callback, s_to_timestamp=s_to_timestamp,
                              format_str=format_str, is_set=is_set, replace_url_list=replace_url_list)

    elif isinstance(data, dict):
        for k, v in data.items():
            if isinstance(v, list):
                db_replace_params(v, is_timestamp=is_timestamp, is_second=is_second, is_decimal=is_decimal,
                                  decimal_two_digit_string=decimal_two_digit_string, replace_none=replace_none,
                                  replace_datetime=replace_datetime, format_replace_data_str=format_replace_data_str,
                                  int_to_str=int_to_str, callback=callback,
                                  s_to_timestamp=s_to_timestamp, format_str=format_str, is_set=is_set,
                                  replace_url_list=replace_url_list)
            elif isinstance(v, dict):
                db_replace_params(v, is_timestamp=is_timestamp, is_second=is_second, is_decimal=is_decimal,
                                  decimal_two_digit_string=decimal_two_digit_string, replace_none=replace_none,
                                  replace_datetime=replace_datetime, format_replace_data_str=format_replace_data_str,
                                  int_to_str=int_to_str, callback=callback,
                                  s_to_timestamp=s_to_timestamp, format_str=format_str, is_set=is_set,
                                  replace_url_list=replace_url_list)

            if callback:
                data[k] = callback(k, v)
            # if replace_url_list and data[k] and k in replace_url_list:
            #     host = current_app.config['ERP_FILE_HOST']
            #     data[k] = host + data[k]
            if replace_none and v is None:
                data[k] = ""

            if isinstance(v, str):
                data[k] = v.strip()

            if replace_datetime and isinstance(v, datetime):
                if is_timestamp:
                    if is_second:
                        data[k] = int(v.timestamp())
                    else:
                        data[k] = int(v.timestamp() * 1000)
                else:
                    data[k] = v.strftime(format_replace_data_str)

            if int_to_str and isinstance(v, int):
                data[k] = str(v)

            if v == "0000-00-00 00:00:00.000000":
                data[k] = ""

            if s_to_timestamp and is_valid_date(v, format_str):
                data[k] = str_to_timestamp(v, format_str=format_str)

            if decimal_two_digit_string and isinstance(v, Decimal):
                v = Decimal(v).quantize(Decimal('0.00'))
                data[k] = str(v)

            if is_decimal and isinstance(v, Decimal):
                if v == Decimal('0.0'):
                    v = Decimal('0.0')
                data[k] = str(v)
            if is_set and isinstance(v, set):
                data[k] = list(v)