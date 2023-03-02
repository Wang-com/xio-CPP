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
MYSQL* mysql; //mysql���� 

bool ConnectDatabase();
bool QueryDatabase(int&);


int main() {
    mysql = new MYSQL;
    ConnectDatabase();
    int timestamp = 0;
    time_t t;
    //��ָ��exe�ļ�
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
        timeinfo = localtime(&t);    // ת��
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
    //��ʼ��mysql  
    mysql_init(mysql);
    //����false������ʧ�ܣ�����true�����ӳɹ�
    if (!(mysql_real_connect(mysql, "localhost", "root", "123456", "xio", 0, NULL, 0))) //�м�ֱ����������û��������룬���ݿ������˿ںţ�����дĬ��0����3306�ȣ���������д�ɲ����ٴ���ȥ  
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
    MYSQL_RES* res; //����ṹ�������е�һ����ѯ�����  
    MYSQL_ROW column; //һ�������ݵ����Ͱ�ȫ(type-safe)�ı�ʾ����ʾ�����е���  
    char query[150]; //��ѯ��� 
    sprintf_s(query, "SELECT * FROM interrupt_cpp ORDER BY id DESC LIMIT 1"); //ִ�в�ѯ��䣬�����ǲ�ѯ���У�user�Ǳ��������ü����ţ���strcpyҲ����
    mysql_query(mysql, "set names gbk"); //���ñ����ʽ��SET NAMES GBKҲ�У�������cmd����������
    //����0 ��ѯ�ɹ�������1��ѯʧ��
    if (mysql_query(mysql, query))    //ִ��SQL���
    {
        printf("Query failed (%s)\n", mysql_error(mysql));
        return false;
    }
    else {
        //printf("query success\n");
    }
    //��ȡ�����  
    if (!(res = mysql_store_result(mysql)))   //���sql�������󷵻صĽ����  
    {
        printf("Couldn't get result from %s\n", mysql_error(mysql));
        return false;
    }
    //��ӡ��ȡ������  
    while (column = mysql_fetch_row(res))   //����֪�ֶ���������£���ȡ����ӡ��һ��  
    {
        times = atoi(column[1]);
    }
    mysql_free_result(res);
    return true;
}
