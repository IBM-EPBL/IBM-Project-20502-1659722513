<%@page language="java" contentType="text.html;charset=ISO-8859-1"
 pageEncoding="ISO-8859-1"%>
<%@page import="java.sql.*,java.util.*"%>
<%
String name = request.getParameter("name");
session.putValue("name", name);
String password = request.getParameter("password");
Class.forName("com.mysql.jdbc.Driver");
java.sql.Connection con = DriverManager.getConnection("jdbc:mysql://localhost:3306/fashion", "root", "root");
Statement st = con.createStatement();
ResultSet rs = st.executeQuery("select * from admin where name='" + name + "' and password='" + password + "'");
try{
 rs.next();
 if (rs.getString("password").equals(password) && rs.getString("name").equals(name)) {
  out.println("<a href='admin_dashboard.html'>Welcome Admin</a>");
 } else {
  out.println("Invalid password or username.");
 }
} catch (Exception e) {
 e.printStackTrace();
}
%>