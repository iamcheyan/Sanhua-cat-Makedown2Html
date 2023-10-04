import datetime

"""
# 获取默认格式的当前时间
current_time = get_current_time()
print(current_time)  # 输出 YYYY-MM-DD HH:MM:SS 格式的时间

# 获取指定格式的当前时间
year = get_current_time('year')
print(year)  # 输出当前年份

month = get_current_time('month')
print(month)  # 输出当前月份

day = get_current_time('day')
print(day)  # 输出当前日期

hour = get_current_time('hour')
print(hour)  # 输出当前小时

minute = get_current_time('minute')
print(minute)  # 输出当前分钟

second = get_current_time('second')
print(second)  # 输出当前秒数

custom_format = get_current_time('%Y年%m月%d日 %H:%M:%S')
print(custom_format)  # 输出自定义格式的时间
"""

def get_current_time(format_args=''):
    """获取当前时间"""
    now = datetime.datetime.now()
    if not format_args:
        # 默认返回 YYYY-MM-DD HH:MM:SS 格式的时间
        return now.strftime('%Y-%m-%d %H:%M:%S')
    else:
        # 解析格式参数并返回相应格式的时间
        try:
            format_str = format_args.strip().lower()
            year = now.strftime('%Y')
            month = now.strftime('%m')
            day = now.strftime('%d')
            hour = now.strftime('%H')
            minute = now.strftime('%M')
            second = now.strftime('%S')
            if 'year' in format_str:
                return year
            elif 'month' in format_str:
                return month
            elif 'day' in format_str:
                return day
            elif 'hour' in format_str:
                return hour
            elif 'minute' in format_str:
                return minute
            elif 'second' in format_str:
                return second
            else:
                return now.strftime(format_args)
        except ValueError:
            # 格式参数解析错误，返回默认格式的时间
            return now.strftime('%Y-%m-%d %H:%M:%S')
