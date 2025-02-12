
<h1 align="center">ecpyecharts: <br/>Easy, Python & Echarts</h1>

<h4 align="center">
    <p>
        <b>简体中文</b> |
        <a href="https://github.com/Aldenhovel/ecpyecharts/blob/main/README.md">English</a>
    <p>
</h4>

## 简介

对于数据可视化来说，选择[Apache echarts](https://github.com/apache/echarts)是明智之举。但由于echarts是基于JavaScript主要用于浏览器前端的数据可视化库，对于一些追求效率的后端开发者来说使用起来并不是特别方便，因此有了基于Python版本的[pyecharts](https://github.com/pyecharts/pyecharts)。

使用pyecharts可以直接在Python脚本中生成echarts报表，它的功能十分强大，基本可以实现echarts原生的所有功能，而且也有非常丰富的文档和社区开发者支持。

**那为什么还要ecpyecharts?**

我们发现其实数据可视化是一门兼顾技术和艺术的学问，丰富且万能的echarts和pyecharts为技术支持打下牢固基础，但是开发者真正使用这些技术自己搭建可视化报表时结果可能会很糟糕，因为不合理的可视化搭配可能会违背视觉偏好。

我们的ecpyecharts开发目的在于简化开发者的设计负担，对echarts和pyecharts做减法，提供使用更加简洁、集成度更高且效果更加漂亮的定制可视化报表模板。



![#1](examples/imgs/demo.gif)

- 支持生成多种不同样式的HTML模板。
- 支持多种设计好的图表模板。
- 只需编写非常简单的代码。
- 支持在 `jupyter notebook / lab` 中使用。
- 支持使用 GUI 构建可视化报表。*（在未来）*

## 如何使用 ecpyecharts

1. 下载或克隆此仓库。
    ```bash
    git clone git@github.com:Aldenhovel/ecpyecharts.git && cd ecpyecharts
    ```

2. 在 `examples/` 中找到想要的模板。


3. 请参考这段代码片段，它简单介绍了 ecpyecharts 的最直接使用方法：
    
    ```python
    import random
    from ecpyecharts.html import HTMLTemplate
    from ecpyecharts.charts import BarTemplate
    
    # create a html template
    html = HTMLTemplate(title="hello", background_color="gray")
    
    # create a bar chart template 
    # init it with data
    chart = BarTemplate(title="Citys", subtitle="this is the subtitle of A", xaxis='Metric', yaxis='Score')
    chart.init_option(xdata=['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K'],
                   ydata={'BJ Score': [random.randint(0, 100) for _ in range(11)],
                          'SH Score': [random.randint(0, 100) for _ in range(11)],
                          'HK Score': [random.randint(0, 100) for _ in range(11)]
                          })
    
    # Once the chart is initialized, 
    # we can append it into the html template
    html.append_chart(chart)
    
    # export the html template to a file
    html.export('../tmp/bar_example.html')
    ```

4. 所有模板的使用示例代码会放在 `examples/` 中，如果想查看运行结果，请在 `tmp/` 中查看对应的 HTML 文件。

## notebook 示例

我们做了一些 jupyter notebook 的教程来展示 `ecpyecharts` 的有趣功能和相关特性，请在 `notebooks/` 下查看它们。
