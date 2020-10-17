import requests
import pool
import argparse
import subprocess

from src.dir_scan import *
from src.color_print import *

if __name__ == '__main__':
    msg = '''
▓█████▄  ██▓ ██▀███    ██████  ▄████▄   ▄▄▄       ███▄    █ 
▒██▀ ██▌▓██▒▓██ ▒ ██▒▒██    ▒ ▒██▀ ▀█  ▒████▄     ██ ▀█   █ 
░██   █▌▒██▒▓██ ░▄█ ▒░ ▓██▄   ▒▓█    ▄ ▒██  ▀█▄  ▓██  ▀█ ██▒
░▓█▄   ▌░██░▒██▀▀█▄    ▒   ██▒▒▓▓▄ ▄██▒░██▄▄▄▄██ ▓██▒  ▐▌██▒
░▒████▓ ░██░░██▓ ▒██▒▒██████▒▒▒ ▓███▀ ░ ▓█   ▓██▒▒██░   ▓██░
 ▒▒▓  ▒ ░▓  ░ ▒▓ ░▒▓░▒ ▒▓▒ ▒ ░░ ░▒ ▒  ░ ▒▒   ▓▒█░░ ▒░   ▒ ▒ 
 ░ ▒  ▒  ▒ ░  ░▒ ░ ▒░░ ░▒  ░ ░  ░  ▒     ▒   ▒▒ ░░ ░░   ░ ▒░
 ░ ░  ░  ▒ ░  ░░   ░ ░  ░  ░  ░          ░   ▒      ░   ░ ░ 
   ░     ░     ░           ░  ░ ░            ░  ░         ░ 
 ░                            ░                             
    '''
    print(color.green(msg))
    print(color.green('[Version: 0.1]'))
    print(color.green('Build [2020-10-05] [Windows/x64]'))
    print(color.green('Edit Version: python3.7.9'))
    parser = argparse.ArgumentParser(usage="python3 dirscan.py -h", prog='dirscan')
    parser.add_argument('-u', '--url', help='指定目标url', required=True, type=str)
    parser.add_argument('-t', '--threads', help="线程数量", type=int)
    parser.add_argument('-e', '--ele', help="文件类型", type=str)
    parser.add_argument('-c', '--cookie', help='指定扫描cookie', type=str)
    args = parser.parse_args()
    URL = args.url
    THREADS = args.threads
    ELE = args.ele
    COOKIE = args.cookie
    if URL == None:
        rsp = subprocess.Popen(['python3', 'infoscaner.py', '-h'])
        output, error = rsp.communicate()
        print(output)
    elif URL != None and THREADS == None and ELE == None and COOKIE == None:
        print_info('默认扫描后台目录', URL)
        dir_scan(url=URL, threads=10, dirtype='all', cookie=None)
    elif URL != None and THREADS == None and ELE == None and COOKIE != None:
        print_info('默认扫描后台目录', URL)
        dir_scan(url=URL, threads=10, dirtype='all', cookie=COOKIE)
    elif URL != None and THREADS == None and ELE != None and COOKIE == None:
        print_info('指定文件类型扫描后台目录', URL)
        dir_scan(url=URL, threads=10, dirtype=ELE, cookie=None)
    elif URL != None and THREADS == None and ELE != None and COOKIE != None:
        print_info('指定文件类型扫描后台目录', URL)
        print_info('使用cookie' + color.yellow(COOKIE), URL)
        dir_scan(url=URL, threads=10, dirtype=ELE, cookie=COOKIE)
    elif URL != None and THREADS != None and ELE != None and COOKIE == None:
        print_info('指定文件类型扫描后台目录', URL)
        dir_scan(url=URL, threads=THREADS, dirtype=ELE, cookie=None)
    elif URL != None and THREADS != None and ELE != None and COOKIE != None:
        print_info('指定文件类型扫描后台目录', URL)
        print_info('使用cookie' + color.yellow(COOKIE), URL)
        dir_scan(url=URL, threads=THREADS, dirtype=ELE, cookie=COOKIE)
    elif URL != None and THREADS != None and ELE == None and COOKIE == None:
        print_info('扫描全部后台目录', URL)
        dir_scan(url=URL, threads=THREADS, dirtype='all', cookie=None)
    elif URL != None and THREADS != None and ELE == None and COOKIE != None:
        print_info('扫描全部后台目录', URL)
        print_info('使用cookie' + color.yellow(COOKIE), URL)
        dir_scan(url=URL, threads=THREADS, dirtype='all', cookie=COOKIE)
    else:
        print_error('参数有误', URL)