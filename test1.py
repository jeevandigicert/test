import sqlite3
from flask import Flask, request

app = Flask(__name__)

@app.get("/user")
def user():
    name = request.args.get("name", "")
    con = sqlite3.connect("test.db")
    cur = con.cursor()
    cur.execute("SELECT * FROM users WHERE name = '" + name + "'")  # SQLi
    return str(cur.fetchall())
1:43
import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.Statement;
import java.sql.ResultSet;

public class VulnerableApp {

    public static void main(String[] args) throws Exception {
        String userInput = args[0]; // user controlled

        Connection conn = DriverManager.getConnection("jdbc:sqlite:test.db");
        Statement stmt = conn.createStatement();

        // 
 SQL Injection vulnerability
        String query = "SELECT * FROM users WHERE name = '" + userInput + "'";
        ResultSet rs = stmt.executeQuery(query);

        while (rs.next()) {
            System.out.println(rs.getString("name"));
        }

        conn.close();
    }
}
