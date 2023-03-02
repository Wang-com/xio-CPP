#define _CRT_SECURE_NO_WARNINGS
#include <iostream>
#include <Windows.h>
#include <WinSock.h>
#include <mysql.h>
#include <string>
#include <time.h>

using namespace std;
#pragma comment(lib,"libmysql.lib")
#pragma comment(lib,"wsock32.lib")
MYSQL* mysql; //mysql连接 

bool ConnectDatabase();
bool QueryDatabase(int&);


int main() {
    mysql = new MYSQL;
    ConnectDatabase();
    int timestamp = 0;
    time_t t;
    //打开指定exe文件
    WinExec("C:\\Users\\hdu41\\Desktop\\Thread_Safe.bat", SW_SHOW);
    Sleep(20000);
    while (true) {
        if (QueryDatabase(timestamp)) {
            //printf("select success\n");
            //cout << timestamp << endl;
        }
        else {
            timestamp = 0;
        }
        time(&t);
        struct tm* timeinfo;
        char buffer[128];
        //
        cout << t - timestamp << endl;
        //cout << t << endl;
        //cout << timestamp << endl;
        timeinfo = localtime(&t);    // 转换
        strftime(buffer, sizeof(buffer), "Now is %Y/%m/%d %H:%M:%S", timeinfo);

        cout << buffer << endl;

        if (t - timestamp > 30) {
            system("taskkill /f /im python.exe");
            Sleep(1000);
            WinExec("C:\\Users\\hdu41\\Desktop\\Thread_Safe.bat", SW_SHOW);
            Sleep(15000);
        }
        Sleep(5000);
        timeinfo = nullptr;
    }
    return 0;
}

bool ConnectDatabase() {
    //初始化mysql  
    mysql_init(mysql);
    //返回false则连接失败，返回true则连接成功
    if (!(mysql_real_connect(mysql, "localhost", "root", "123456", "xio", 0, NULL, 0))) //中间分别是主机，用户名，密码，数据库名，端口号（可以写默认0或者3306等），可以先写成参数再传进去  
    {
        printf("Error connecting to database:%s\n", mysql_error(mysql));
        return false;
    }
    else {
        printf("Connected...\n");
        return true;
    }
    return true;
}

bool QueryDatabase(int& times) {
    MYSQL_RES* res; //这个结构代表返回行的一个查询结果集  
    MYSQL_ROW column; //一个行数据的类型安全(type-safe)的表示，表示数据行的列  
    char query[150]; //查询语句 
    sprintf_s(query, "SELECT * FROM interrupt_cpp ORDER BY id DESC LIMIT 1"); //执行查询语句，这里是查询所有，user是表名，不用加引号，用strcpy也可以
    mysql_query(mysql, "set names gbk"); //设置编码格式（SET NAMES GBK也行），否则cmd下中文乱码
    //返回0 查询成功，返回1查询失败
    if (mysql_query(mysql, query))    //执行SQL语句
    {
        printf("Query failed (%s)\n", mysql_error(mysql));
        return false;
    }
    else {
        //printf("query success\n");
    }
    //获取结果集  
    if (!(res = mysql_store_result(mysql)))   //获得sql语句结束后返回的结果集  
    {
        printf("Couldn't get result from %s\n", mysql_error(mysql));
        return false;
    }
    //打印获取的数据  
    while (column = mysql_fetch_row(res))   //在已知字段数量情况下，获取并打印下一行  
    {
        times = atoi(column[1]);
    }
    mysql_free_result(res);
    return true;
}
