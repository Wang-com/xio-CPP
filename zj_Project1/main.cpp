#define _CRT_SECURE_NO_WARNINGS
#include <iostream>
#include <Windows.h>
#include <WinSock.h>
#include <mysql.h>
#include <string>
#include <time.h>
#include <chrono>

using namespace std;
#pragma comment(lib,"libmysql.lib")
#pragma comment(lib,"wsock32.lib")
MYSQL* mysql; //mysql����   

bool ConnectDatabase();
bool QueryDatabase(int&);
bool QueryDatabase2(int&);

int main() {
    int timestamp = 0;
    int yichangtime = 0;
    time_t t;
    time_t t2;

    mysql = new MYSQL;
    ConnectDatabase();
    //��ָ��exe�ļ�
    WinExec("C:\\Users\\hdu417\\Desktop\\Thread_Safe.bat", SW_SHOW);
    WinExec("C:\\Users\\hdu417\\Desktop\\yichangdetect.bat", SW_SHOW);
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
        //������
        cout << "time_diff: " << t - timestamp << endl;
        //cout << t << endl;
        //cout << timestamp << endl;
        timeinfo = localtime(&t);    // ת��
        strftime(buffer, sizeof(buffer), "Now is %Y/%m/%d %H:%M:%S", timeinfo);

        cout << buffer << endl;

        if (t - timestamp > 30) {
            system("taskkill /f /im python.exe");
            Sleep(1000);
            WinExec("C:\\Users\\hdu417\\Desktop\\Thread_Safe.bat", SW_SHOW);
            WinExec("C:\\Users\\hdu417\\Desktop\\yichangdetect.bat", SW_SHOW);
            Sleep(15000);
        }


        if (QueryDatabase2(yichangtime)) {
            //printf("select success\n");
            //cout << timestamp << endl;
        }
        else {
            yichangtime = 0;
        }
        time(&t2);
        
        struct tm* timeinfo2;
        char buffer2[128];
        //������
        cout << "time_diff: " << t2 - yichangtime << endl;
        //cout << t << endl;
        //cout << timestamp << endl;
        timeinfo2 = localtime(&t2);    // ת��
        strftime(buffer2, sizeof(buffer2), "Now is %Y/%m/%d %H:%M:%S", timeinfo2);

        cout << buffer2 << endl;

        if (t2 - yichangtime > 30) {
            system("taskkill /f /im python.exe");
            Sleep(1000);
            WinExec("C:\\Users\\hdu417\\Desktop\\Thread_Safe.bat", SW_SHOW);
            WinExec("C:\\Users\\hdu417\\Desktop\\yichangdetect.bat", SW_SHOW);
            Sleep(15000);
        }

        Sleep(5000);
        //delete mysql;
        //mysql = nullptr;
        timeinfo = nullptr;
        timeinfo2 = nullptr;

        /* 
        ��ʱ���� 
        */
        auto now = std::chrono::system_clock::now();
        //ͨ����ͬ���Ȼ�ȡ���ĺ�����
        uint64_t dis_millseconds = std::chrono::duration_cast<std::chrono::milliseconds>(now.time_since_epoch()).count()
            - std::chrono::duration_cast<std::chrono::seconds>(now.time_since_epoch()).count() * 1000;
        time_t tt = std::chrono::system_clock::to_time_t(now);
        auto time_tm = localtime(&tt);
        char strTime[25] = { 0 };
        sprintf(strTime, "%d-%02d-%02d %02d:%02d:%02d %03d", time_tm->tm_year + 1900,
            time_tm->tm_mon + 1, time_tm->tm_mday, time_tm->tm_hour,
            time_tm->tm_min, time_tm->tm_sec, (int)dis_millseconds);
        std::cout << strTime << std::endl;
        Sleep(2000);
        // һ�������޶�ʱ��������0��ʱ����
        bool flag = false;
        if (time_tm->tm_hour == 0) {
            flag = false;
        }
        // ��ʱ
        if (time_tm->tm_hour == 7 && time_tm->tm_min > 57 && time_tm->tm_min < 59) {
            flag = true;
            // break; // ��ʱִ���˳������滻�ɶ�ʱִ������
            system("taskkill /f /im python.exe");
            Sleep(1000);
            WinExec("C:\\Users\\hdu417\\Desktop\\Thread_Safe.bat", SW_SHOW);
            WinExec("C:\\Users\\hdu417\\Desktop\\yichangdetect.bat", SW_SHOW);
            Sleep(15000);
        }
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

bool QueryDatabase2(int& times) {
    MYSQL_RES* res; //����ṹ�������е�һ����ѯ�����  
    MYSQL_ROW column; //һ�������ݵ����Ͱ�ȫ(type-safe)�ı�ʾ����ʾ�����е���  
    char query[150]; //��ѯ��� 

    sprintf_s(query, "SELECT * FROM yichangdetect_cpp ORDER BY id DESC LIMIT 1"); //ִ�в�ѯ��䣬�����ǲ�ѯ���У�user�Ǳ��������ü����ţ���strcpyҲ����
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
