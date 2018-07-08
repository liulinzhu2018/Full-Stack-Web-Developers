project:还剩8h (2week)
project3:22h   (4week)
project4:7h    (2week)

# html
html元素

<p>This is a paragraph,</p>
<h1>This is a heading.</h1>
<span>This is a span.</span>

opening tag           closing tag

<dev></dev>表示区域，可包含元素

html元素中的id在一个网页中是唯一的，class可以出现在多个html元素中，一个html元素也可以有多个class,class="a b c" 用空格分隔。
<p id="name">This is name</p>
对应的选择器格式--> #id {color:blue}
 
<p class="class-a">This is class a</p>
对应的选择器格式--> .class-a {color:red}

评论<!--comment-->


# 配置环境

## 1. 文本编辑器
- rich text: formatted
- plain text: ASCII chars
- IDE: Integrated Development Environment
- 推荐用：Visual Studio Code

## 2. 浏览器
- chrome, firefox 都带有dev tools
- 打开文件的快捷键：ctrl+o
- 刷新：ctrl+r
- 开发者工具：ctrl+shift+i

- html文档：https://developer.mozilla.org/en-US/docs/Web/HTML/Element
- html检查器：https://validator.w3.org/check


# css
## 1.基本配置
<style>
	p { color: blue}
	/* this is a comment*/
</style>

- 单位: px像素
- 颜色：表示方法
  * RGB(red,green,blue) 
  * color:blue 
  * color:rgb(0,0,255) 
  * color:#0000ff 
  * color:#00f 

- cMozilla Developer Network：https://developer.mozilla.org/en-US/docs/Web/CSS/Reference
- CSS Almanac： https://css-tricks.com/almanac/
- https://www.cssmatic.com/box-shadow

- border: 5px dashed salmon;
- border-radius: 5px;
- cursor: pointer;
- box-shadow: 5px 5px 20px #ccc;

- <link href="path-to-stylesheet/stylesheet.css" rel="stylesheet">

## 2.尺寸
盒模型，语义化标签
content
padding内边距
border边框
margin外边距

width包含content,padding,border的像素
box-sizing：采用border-box,而不是content-box计算的

width设置为百分比，表示占父元素的百分比，可以随父元素的大小放缩。
https://developer.mozilla.org/en-US/docs/Web/HTML/Element


## 3.位置
display: inline-block;

position: relative;
position: absolute;
position: fixed;

vertical-align 垂直对齐方式
text-align 文本对齐方式

## 4.浮动
float:
clear:
overflow: 

pseudo-elements
::after
::before

# 响应式设计
- 模拟器来模拟各个设备展示web.
- 浏览器上的模拟器 ctrl+shift+j 出来的左上角手机平板的图标。
- https://developers.google.com/web/tools/chrome-devtools/shortcuts
