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

- 视角宽度 = 实际像素/像素比
  * <meta name="viewport" content="width=device-width, initial-scale=1"> 
  * width-device-width 根据屏幕大小设置页面大小，放在html文件的<head></head>里面。  
  * initial-scale=1 初始缩放比例，如果不设置为1的话，屏幕横过来，可能页面不会自适应屏幕。  
  * https://developer.mozilla.org/en-US/docs/Mozilla/Mobile/Viewport_meta_tag  

- css允许元素溢出，可以设置相对宽度，来适应不同尺寸的屏幕（响应式设计）
  * eg. 
    img, embed,
    object, video {
	max-width: 100%;
    }
  * 如果width和max-width都存在的话，max-width会覆盖width的设置。
  * 设置width:125px, 这个比任何屏幕都要小，所以不用自适应屏幕。

- 按钮设置一般最好48px*48px，因为要考虑到手指的宽度大约10mm,也就是40px. 保证元素间留有空闲，最少两个点击的目标间有40px。
  * nav, a, button {
	min-width: 48px;
	min-height:48px;
  }
  * 这种设置能够自适应屏幕（窗口？），采用width和height的设置无法适应屏幕大小。
  * eg. 
.nav a {
  text-decoration: none;
  color: #616161;
  padding: 1.5em; /*内边距等于a标签的1.5倍*/
}

- 响应式设计，从最小窗口开始考虑，它是一门艺术而非科学。

-----------------------
- 兼容不同的设备尺寸对html设置不同的样式表的方法  
- media设置不同的设备及其属性，调用不同的css样式表。
  * （1）第一种方式：link css，下面表示当屏幕像素小于500时使用的样式表  
<link rel="stylesheet" type="text/css" href="demo_media_print.css" media="screen and (min-width:500px)" />
<link rel="stylesheet" type="text/css" href="demo_media.css" /> media默认为all,表示所有设备
http://www.w3school.com.cn/html5/att_link_media.asp
  * （2）第二种方式：
@media screen and (min-width: 500px) {
	body { background-color: green; }
}
@import url("no.css") only screen and (min-width: 500px) /*import性能不好，所有不使用*/
调用css的方式：一种是linked css, 一种是@media方式。前者可以有很多小文件，很多http请求。后者文件会变大，http请求少。

- min-width是基于浏览器窗口大小，min-divice-width是基于屏幕大小。一般设备上使用min-width
- 浏览器窗口从小到大的变动叫做断点。 一个页面可以有多个断点。

## 网格布局
- https://developer.mozilla.org/en-US/docs/Web/CSS/CSS_Grid_Layout/Basic_Concepts_of_Grid_Layout
- flexbox 布局工具

## 响应式布局：大体流动模型，掉落列模型，活动布局模型，画布溢出模型
- column drop
- eg. 
.container{
	display: flex;
	flex-wrap: wrap;
}

.box{
	width: 100%;
}

- mostly fluid 放页面宽度到达一定宽度后，div元素的宽度不会再变大，页面两边有空白
- layout shifter 竖着布局， orders: -1
- off canvas 网页宽度溢出的部分有个按钮可以点开，例如上方的导航栏，和左右的内容。只有当页面一定大的时候才能自动显示。
- eg.
nav {
	width: 300px;
	height: 100%;
	position: absolute;
	transform: translate(-300px, 0); /*将导航栏移动出页面, 在左边-300px*/
	transition: transform 0.3s ease;
}

@media screen and (min-width: 500px) {
	nav { 
		position: relative;
		transform: translate(0,0);
	}
}

-----------------

## 响应式设计
### 1. 图片
- 每个页面的http文档大约右1.2M的图片，占据页面的65%。
- 响应式图片设计 这个有单独的视频课。

### 2. 表格
- 1.隐藏某些列（display: none） 
- 2.纵向的多列都变成横向的，没一行信息变成多行  https://codepen.io/team/css-tricks/pen/wXgJww?editors=1100
（1）块级显示 （2）thread, tr去除表格标题 （3）td （4）td 列的标题放在左边 content: attr(data-th) 应用到每个td元素
- 3.加入横向滚动条 div中加入样式 overflow-x: auto; width:100%;

### 3. 字
- 每行45-90个字符，根据字体有所区别。
- fron-size: 16px;
- line-height: 1.2em;

网站布局：
https://developer.mozilla.org/zh-CN/docs/learn/HTML/Introduction_to_HTML/%E6%96%87%E4%BB%B6%E5%92%8C%E7%BD%91%E7%AB%99%E7%BB%93%E6%9E%84


下周：
project2中 课程9的第11个， 课程10的第10个，project2 的项目

http://www.sublimelinter.com/en/latest/installation.html
http://pep8online.com/checkresult
