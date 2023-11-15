# def m_date(d, m, y):
#     dm = d * m
#     print(dm)
#     lst_num = y % 100
#     print(lst_num)
#     if dm == lst_num:
#         return True
#     else:
#         return False
# print(m_date(10,2,2020))


def get_m(m, y):
    month_day = {
        1:31, 2:28, 3:31, 4:30,
        5:31, 6:30, 7:31, 8:31,
        9:30, 10:31, 11:30, 12:31
    }

    

    if y % 4 == 0:
        month_day[2] = 29
    if y % 4 == 0 and y % 100 == 0:
        month_day[2] = 28
    if y % 4 == 0 and y % 100 == 0 and y % 400 == 0:
        month_day[2] = 29
    else:
        return month_day
    

get_m(2,2020)




