# #if条件判断 ---> 如果分数考680及以上,就能上清华
# #判断类型bool类型
# score = float(input("请输入你的分数:"))
# if score >= 680:
#     #if中必须前面4个空格或Tab 表示层级
#     print("恭喜你进入清华大学\n请继续努力")
#     print("10086")
# print("--------------------")#不属于if代码块
# #通过缩进表示代码层级


# #案例 ----> B站简易登录模拟(账号18888888888 密码666888)   #if后条件,else
# account = input("账号:")
# password = input("密码:")
# #input()默认输出str类型
# if account == "18888888888" and password == "666888":
#     print("登录成功")
# # if account != "18888888888" or password != "666888":
# else:
#     print("登录失败\n请确认账号或密码是否正确")


#案例 根据输入的年份,判断是平年还是闰年

# year = int(input("请输入年份:"))
#
# if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):#Python中的逻辑运算符优先级顺序 not and or ,不过为了更加规范,通常加()区分
#     print(f"{year}是闰年")
# else:
#     print(f"{year}是平年")


#练习1 判断输入的数的奇偶
# num = int(input("请输入:"))
# if num % 2 == 0:
#     print(f"{num}是偶数")
# else:
#     print(f"{num}是奇数")


#练习2 根据用户输入的年龄判断用户是否成年
# year = int(input("请输入你的年龄:"))
# if year >= 18:
#     print("已成年")
# else:
#     print("未成年")


#案例3 根据用户输入的数字判断数字的正负(不考虑0)
# num = float(input("请输入(0除外):"))
# if num > 0:
#     print(f"{num}是正数")
# if num < 0:
#     print(f"{num}是负数")

#案例4 根据用户输入的分数,判断是否及格(大于等于60分及格)
# score = float(input("请输入你的分数:"))
# if score >= 60:
#     print("及格")
# else:
#     print("不及格")

#if...elif...else,elif可以有多个,判断顺序从上到下,else可选择添加  示例:根据用户输入的数字判断数字的正负
# num = float(input("请输入:"))
# if num > 0:
#     print(f"{num}是正数")
# elif num < 0:
#     print(f"{num}是负数")
# else:
#     print(f"{num}是0")

#案例 根据用户输入的账号和密码进行登录系统(用户名/密码为admin/666888或root/547527或zhangsan/123456)
# account = input("请输入账号:")
# password = input("请输入密码:")
# # if account == "admin" and password == "666888" or account == "root" and password == "547527" or account == "zhangsan" and password == "123456":
# #     print("登录成功")
# if account == "admin" and password == "666888":
#     print("登录成功")
# elif account == "root" and password == "547527":
#     print("登录成功")
# elif account == "zhangsan" and password == "123456":
#     print("登录成功")
# else:
#     print("登录失败,请检查账号或密码是否正确")


#练习 根据输入的考试成绩,判断成绩等级
# score = float(input("请输入成绩:"))
# if score >= 85 :
#     print(f"{score}分为优秀")
# elif 60 <= score < 85:
#     print(f"{score}分及格")
# else:
#     print("不及格")


#练习 根据输入的购物车的总金额,以及对应的折扣规则,计算应付的金额
# total_amount = float(input("请输入总金额:"))
# if total_amount >= 500:
#     print(f"享受8折优惠,应付{total_amount * 0.8}")
# elif 300 <= total_amount < 500:
#     print(f"享受9折优惠,应付{total_amount * 0.9}")
# elif 100 <= total_amount < 300:
#     print(f"享受95折优惠,应付{total_amount * 0.95}")
# else:
#     print(f"不享受优惠,应付{total_amount}")


#案例 根据输入三个边的的边长,判断三角形的类型
# side_legth1 = float(input("请输入第一条边的边长:"))
# side_legth2 = float(input("请输入第二条边的边长:"))
# side_legth3 = float(input("请输入第三条边的边长:"))
# a = side_legth1 ** 2 + side_legth2 ** 2 == side_legth3 ** 2 or side_legth2 ** 2 + side_legth3 ** 2 == side_legth1 ** 2 or side_legth1 ** 2 + side_legth3 ** 2 == side_legth2 ** 2
# if side_legth1 > 0 and side_legth2 > 0 and side_legth3 > 0:
#     if side_legth1 + side_legth2 > side_legth3 and side_legth1 + side_legth3 > side_legth2 and side_legth1 + side_legth3 > side_legth2:
#         if side_legth1 == side_legth2 == side_legth3:
#             print("它是等边三角形")
#         elif side_legth1 == side_legth2 or side_legth1 == side_legth3 or side_legth1 == side_legth2:
#             if a:
#                 print("等腰直角三角形")
#             else:
#                 print("它是等腰三角形")
#         elif a:
#             print("它是直角三角形")
#         else:
#             print("它是普通三角形")
#     else:
#         print("不能构成三角形")
# else:
#     print("请确保输入的边长是正数")


#案例 根据输入的用电度数,计算电费
electricity_bill = float(input("请输入用电度数:"))
if electricity_bill >= 0:
    if electricity_bill < 2880:
        print(f"享受第一档优惠,应付{electricity_bill * 0.4883}")
    elif 2880 <= electricity_bill <= 4800:
        print(f"享受第二档优惠,应付{(electricity_bill -2880) * 0.5383 + 2880 * 0.4838}")
    elif electricity_bill > 4800:
        print(f"享受第三档优惠,应付{(electricity_bill - 4880) * 0.7883 + 2880 * 0.4838 + (4800 - 2880) * 0.5383}")
else:
    print("电费不能为负数")