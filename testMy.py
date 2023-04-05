#!/usr/bin/env python

from cyaron import * # 引入CYaRon的库

_n = ati([2, 6, 51, 110, 152, 303, 311, 635, 657, 664, 692, 772, 877, 985, 1000, 1457, 2513, 2886, 3489, 3509, 4314, 5032, 6445, 6578, 6635, 7445, 7899, 9125, 9211, 10000]) # ati函数将数组中的每一个元素转换为整形，方便您可以使用1E4一类的数来表示数据大小
_m = ati([0, 7, 863, 535, 803, 451, 87, 855, 923, 1000, 182, 226, 902, 420, 491, 641, 631, 178, 88, 176, 640, 702, 566, 86, 265, 141, 174, 768, 426, 1000])

# 这是一个图论题的数据生成器，该题目在洛谷的题号为P1339
for i in range(0, len(_n)): # 即在[1, 4)范围内循环，也就是从1到3
    test_data = IO(file_prefix="test", data_id=i) # 生成 heat[1|2|3].in/out 三组测试数据

    n = _n[i] # 点数
    m = _m[i] # 边数
    s = randint(0, m) # 朋友对数
    t = m - s # 敌人对数
    test_data.input_writeln(n, s, t) # 写入到输入文件里，自动以空格分割并换行
    if m:
        graph = Graph.graph(n, m, self_loop=False, repeated_edges=False) # 生成一个n点，m边的随机图
        test_data.input_writeln(graph.to_str(shuffle=True, output=Edge.unweighted_edge)) # 自动写入到输入文件里，默认以一行一组u v的形式输出

    test_data.output_gen("E:\code\oj\luogu\Debug\ConsoleApplication1.exe") # 标程编译后的可执行文件，不需要freopen等，CYaRon自动给该程序输入并获得输出作为.out