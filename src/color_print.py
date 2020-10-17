from colorama import init, Fore, Back, Style
import time

class Colored(object):
    # 前景色:红色 背景色:默认
    def red(self, s):
        return Fore.RED + s + Fore.RESET

    # 前景色:绿色 背景色:默认
    def green(self, s):
        return Fore.GREEN + s + Fore.RESET

    # 前景色:黄色 背景色:默认
    def yellow(self, s):
        return Fore.YELLOW + s + Fore.RESET

    # 前景色:蓝色 背景色:默认
    def blue(self, s):
        return Fore.BLUE + s + Fore.RESET

    # 前景色:洋红色 背景色:默认
    def magenta(self, s):
        return Fore.MAGENTA + s + Fore.RESET

    # 前景色:青色 背景色:默认
    def cyan(self, s):
        return Fore.CYAN + s + Fore.RESET

    # 前景色:白色 背景色:默认
    def white(self, s):
        return Fore.WHITE + s + Fore.RESET

    # 前景色:黑色 背景色:默认
    def black(self, s):
        return Fore.BLACK

    # 前景色:白色 背景色:绿色
    def white_green(self, s):
        return Fore.WHITE + Back.GREEN + s + Fore.RESET + Back.RESET


color = Colored()


def print_flush(info):
    print(
        color.white("[")
        + color.blue(time.strftime("%H:%M:%S"))
        + color.white("]")
        + color.white("[")
        + color.green("INFO")
        + color.white("] ")
        + info, end="\r", flush=True
    )


def print_flush_two(info):
    print(
        "\r",
        color.white("[")
        + color.blue(time.strftime("%H:%M:%S"))
        + color.white("]")
        + color.white("[")
        + color.green("INFO")
        + color.white("] ")
        + info, end=""
    )


def print_info(info, target):
    print(
        color.cyan(time.strftime("%Y-%m-%d"))
        + ' '
        + color.cyan(time.strftime("%H:%M:%S"))
        + color.white(" [")
        + color.green("INFOR")
        + color.white("]")
        + color.white(' [')
        + color.cyan('target')
        + color.white(':')
        + color.yellow(target)
        + color.white('] - ')
        + color.green(info)
    )


def print_error(info, target):
    print(
        color.cyan(time.strftime("%Y-%m-%d"))
        + ' '
        + color.cyan(time.strftime("%H:%M:%S"))
        + color.white(" [")
        + color.red("ERROR")
        + color.white("]")
        + color.white(' [')
        + color.cyan('target')
        + color.white(':')
        + color.yellow(target)
        + color.white('] - ')
        + color.red(info)
    )


def print_warn(info, target):
    print(
        color.cyan(time.strftime("%Y-%m-%d"))
        + ' '
        + color.cyan(time.strftime("%H:%M:%S"))
        + color.white(" [")
        + color.magenta("WARNI")
        + color.white("]")
        + color.white(' [')
        + color.cyan('target')
        + color.white(':')
        + color.yellow(target)
        + color.white('] - ')
        + color.magenta(info)
    )
