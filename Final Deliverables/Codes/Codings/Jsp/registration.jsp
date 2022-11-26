<%@page language="java" contentType="text.html;charset=ISO-8859-1"
 pageEncoding="ISO-8859-1"%>
<%@page import="java.sql.*,java.util.*"%>
<%
String name=request.getParameter("name");
String email=request.getParameter("email");
String password=request.getParameter("password");
try
{
Class.forName("com.mysql.jdbc.Driver");
Connection conn = DriverManager.getConnection("jdbc:mysql://localhost:3306/fashion", "root", "root");
Statement st=conn.createStatement();
int i=st.executeUpdate("insert into registration(name, email, password)values('"+name+"','"+email+"','"+password+"')");
out.println("<a href='login.html'>Registered Successfully</a>");
}
catch(Exception e)
{
System.out.print(e);
e.printStackTrace();
}
%>