#include <iostream>
using namespace std;

#include <time.h>
#include <chrono>
#include <windows.h>

int main() {
    cout << "Hello, World!" << endl;
    // 当前时间戳，seconds since 1970-01-01
    while(true) {
        auto now = std::chrono::system_clock::now();
        //通过不同精度获取相差的毫秒数
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
        // 一天内有无定时重启过，0点时更新
        bool flag = false;
        if (time_tm->tm_hour == 0) {
            flag = false;
        }
        // 定时
        if (time_tm->tm_hour == 21 && time_tm->tm_min > 31 && time_tm->tm_min < 33) {
            flag = true;
            break; // 定时执行退出，可替换成定时执行任务
        }
    }
    cout << "程序退出~" << endl;
    return 0;
}
