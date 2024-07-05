
# _*_coding: UTF-8_*_


import cgi

# 创建 FieldStorage 的实例化
form = cgi.FieldStorage()

# 获取数据
first_name = form.getvalue('first_name')
last_name  = form.getvalue('last_name')


print "Set-Cookie:UserID=XYZ;\r\n"
print "Set-Cookie:Password=XYZ123;\r\n"
print "Set-Cookie:Expires=Tuesday, 31-Dec-2007 23:12:40 GMT;\r\n"
print "Set-Cookie:Domain=www.w3cschool.cc;\r\n"
print "Set-Cookie:Path=/perl;\n"

print "Content-type:text/html\r\n\r\n"
print "<html>"
print "<head>"
print "<title>Hello - Second CGI Program</title>"
print "</head>"
print "<body>"
print "<h2>Hello %s %s</h2>" % (first_name, last_name)
print "</body>"
print "</html>"
