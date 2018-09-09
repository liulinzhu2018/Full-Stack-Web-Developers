1. sql注入攻击
2. 脚本注入攻击
当网站的评论中，传入的JavaScript可能是攻击的脚本，所以一些网站不允许评论中使用JavaScript。
https://bleach.readthedocs.io/en/latest/
blench库，供python调用，能够确保html安全性。

postgresql
https://www.postgresql.org/docs/9.4/static/app-psql.html

sql表格标准化设计
1. 每一行的列数是相同的
2. 主键
3. 非key的列描述key，但不描述其他列
4. 行不会暗示行之前的关系

表之间的关系
reference
foreign key
self join
subquery子查询， 子查询的结果是一个表
https://www.postgresql.org/docs/9.4/static/sql-expressions.html#SQL-SYNTAX-SCALAR-SUBQUERIES
https://www.postgresql.org/docs/9.4/static/functions-subquery.html
https://www.postgresql.org/docs/9.4/static/sql-select.html#SQL-FROM

http://127.0.0.1:9079/browser/



https://pypi.org/project/pycodestyle/
pip install pycodestyle
pycodestyle -v C:\full-stack\4.Project-Logs-Analysis\fsnd-virtual-machine\FSND-Virtual-Machine\vagrant\forum\log_analysis.py


登陆数据库
-d 数据库名称
-U 用户名
psql -d forum -U postgres


windows网络重置方法
1.NETSH INT IP RESET
2.NETSH WINHTTP RESET PROXY
3.IPCONFIG /FLUSHDNS


1.创建news数据库
2.创建用户，CREATE USER vagrant WITH PASSWORD '920127';
3.创建role，create role vagrant LOGIN
4.执行newsdata.sql，psql -d news -f C:\full-stack\4.Project-Logs-Analysis\newsdata.sql -U vagrant


javascript
ECMAScript(ES5 or ES6)

打开web concole的方法： ctrl+shift+J

null 表示没有数据
var x = null;

undefined 缺少值
var x;
console.log(x);

NaN Not-A-Number, 表示计算出错

JavaScript takes the string "1", converts it to true, and compares it to the boolean true.
"1" == true
> Returns: true

"1" === 1     Returns: false // ===表示严格相等
0 === false   Returns: false
1 !== false   Returns: true  // !==严格不相等

"3" > 1    Returns: true // "3"隐式转换为3
true >= 0  Returns: true // true隐式转换为1


Here’s the list of all of the falsy values:
the Boolean value false
the null type
the undefined type
the number 0
the empty string ""
the odd value NaN (stands for "not a number", check out the NaN MDN article)
That's right, there are only six falsy values in all of JavaScript!

function fun(a)
{
	return a;
}

var catSays = function(max) 
{ 
  // code here 
};

匿名函数
