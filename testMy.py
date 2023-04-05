#!/usr/bin/env python

from cyaron import * # 引入CYaRon的库

_n = ati([2, 9, 47, 98, 141, 169, 627, 702, 880, 915, 920, 956, 977, 993, 1000, 2075, 2540, 3548, 3682, 4033, 4661, 4953, 6560, 6804, 6851, 7950, 8422, 8757, 9928, 10000]) # ati函数将数组中的每一个元素转换为整形，方便您可以使用1E4一类的数来表示数据大小
_m = ati([0, 45, 772, 505, 578, 817, 0, 425, 939, 436, 119, 25, 810, 284, 387, 702, 990, 459, 818, 336, 946, 919, 759, 624, 951, 456, 829, 81, 748, 1000])

# 这是一个图论题的数据生成器，该题目在洛谷的题号为P1339
for i in range(0, len(_n)): # 即在[1, 4)范围内循环，也就是从1到3
    test_data = IO(file_prefix="test", data_id=i) # 生成 heat[1|2|3].in/out 三组测试数据

    n = _n[i] # 点数
    m = _m[i] # 边数
    s = randint(0, m) # 朋友对数
    t = m - s # 敌人对数
    test_data.input_writeln(n, s, t) # 写入到输入文件里，自动以空格分割并换行
    if m:
        graph = Graph.graph(n, m) # 生成一个n点，m边的随机图
        test_data.input_writeln(graph.to_str(shuffle=True, output=Edge.unweighted_edge)) # 自动写入到输入文件里，默认以一行一组u v的形式输出

    test_data.output_gen("E:\code\oj\luogu\Debug\ConsoleApplication1.exe") # 标程编译后的可执行文件，不需要freopen等，CYaRon自动给该程序输入并获得输出作为.out