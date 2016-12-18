# -*- coding: UTF-8 -*-

from tkinter import *

'''
功能描述：
'''

__author__ = 'Rolland'
MENU_ITEMS = ['开始', '选项', '抓取数据', '输出', '帮助']
# 菜单开始中的选项
MENU_FILE_ITEMS = ['初始化       ',
                   '退出         ']
# 菜单选项中的选项
MENU_OPTIONS_ITEMS = ['数据源              ',
                      '联赛                ',
                      '日期                ']
# 菜单抓取数据中的选项
MENU_RUN_ITEMS = ['抓取信息',
                  '抓取数据']
# 菜单输出中的选项
MENU_OUTPUT_ITEMS = ['打印数据',
                     '导出txt']
# 菜单 Help中的选项
MENU_HELP_ITEMS = ['关于                   ',
                   '帮助                   ']
# 关于信息
ABOUT_MESSAGE = '''
    Author       : Rolland Chen
    Author_email : rolland_chen@126.com
    Created      : 2016-11-12
    Version      : 0.1.1
'''

nmaxn = 1024
nminn = 0


def get_tk():
    """获取一个Tk对象"""
    return Tk()


def set_tk_title(tk, title):
    # 给窗口定义 title
    if title is not None and title != '':
        tk.title(title)
    else:
        tk.title('foot manager v1.0')


def set_tk_geometry(tk, size):
    """设置窗口大小，size的格式为：width x height,如：size = '200x100'."""
    if size is not None and size != '':
        tk.geometry(size)
    else:
        tk.geometry('800x600')


def get_menu(tk):
    """获取一个菜单条"""
    return Menu(tk)


def menu_start(menubar, root):
    """定义菜单 开始"""
    filemenu = Menu(menubar, tearoff=1)
    filemenu.add_command(label=MENU_FILE_ITEMS[
                         0], command=menu_event['init'])
    filemenu.add_command(label=MENU_FILE_ITEMS[1], command=root.destroy)
    menubar.add_cascade(label=MENU_ITEMS[0], menu=filemenu)


def menu_options(menubar):
    """定义菜单 选项"""
    options_menu = Menu(menubar, tearoff=1)
    options_menu.add_command(label=MENU_OPTIONS_ITEMS[
                             0], command=lambda: print(MENU_OPTIONS_ITEMS[0]))
    options_menu.add_separator()
    options_menu.add_command(label=MENU_OPTIONS_ITEMS[
                             1], command=lambda: print(MENU_OPTIONS_ITEMS[1]))
    options_menu.add_command(label=MENU_OPTIONS_ITEMS[
                             2], command=lambda: print(MENU_OPTIONS_ITEMS[2]))
    menubar.add_cascade(label=MENU_ITEMS[1], menu=options_menu)


def menu_run(menubar):
    """定义菜单 抓取"""
    run_menu = Menu(menubar, tearoff=1)
    run_menu.add_command(label=MENU_RUN_ITEMS[
                         0], command=menu_event['getInfo'])
    run_menu.add_command(label=MENU_RUN_ITEMS[
                         1], command=menu_event['getDatas'])

    menubar.add_cascade(label=MENU_ITEMS[2], menu=run_menu)


def menu_output(menubar):
    """定义菜单输出"""
    output_menu = Menu(menubar, tearoff=1)
    output_menu.add_command(label=MENU_OUTPUT_ITEMS[
                            0], command=lambda: print(MENU_OUTPUT_ITEMS[0]))
    output_menu.add_command(label=MENU_OUTPUT_ITEMS[
                            1], command=lambda: print(MENU_OUTPUT_ITEMS[1]))
    menubar.add_cascade(label=MENU_ITEMS[3], menu=output_menu)


def menu_help(menubar):
    """定义菜单Help"""
    help_menu = Menu(menubar, tearoff=1)
    help_menu.add_command(
        label=MENU_HELP_ITEMS[0],
        command=about_idel(menubar))
    help_menu.add_command(label=MENU_HELP_ITEMS[
                          1], command=lambda: print(MENU_HELP_ITEMS[1]))
    menubar.add_cascade(label=MENU_ITEMS[4], menu=help_menu)


def about_idel(r):
    """Help-About IDEL function"""
    label = Label(r, text=ABOUT_MESSAGE, fg='red')
    label.pack(side='top')


def init_menu_bar(root):
    # 获取菜单对象
    menubar = get_menu(root)
    '''初始化菜单条'''
    menu_start(menubar, root)  # file
    menu_options(menubar)  # edit
    menu_run(menubar)  # run
    menu_output(menubar)  # options
    menu_help(menubar)  # help
    return menubar


def initMenu(root):
    # 初始化菜单
    menubar = init_menu_bar(root)
    # 加载菜单配置
    root.config(menu=menubar)

    view_mode['menu'] = menubar


def initFrame(root):
    # 生成信息提示
    tipFrame = Frame(root, width=60, height=10, bd=3, bg='green')
    tipFrame.grid(column=0, row=0, columnspan=3, sticky=W)
    label_tips = Label(tipFrame)
    label_tips.grid()
    view_mode['tip'] = label_tips
    # 按钮组
    btnFrame = Frame(root, width=80, height=20)
    btnFrame.grid(column=0, row=1, sticky=W)
    startBtn = Button(btnFrame, text="开始初始化信息")
    startBtn.grid()
    startBtn["command"] = menu_event['getDatas']
    # 比赛列表
    lgFrame = Frame(root, width=10, height=100)
    lgFrame.grid(column=0, row=2)
    lgList = Listbox(lgFrame)
    view_mode['lglist'] = lgList
    # 输出信息
    outputFrame = Frame(root, width=90, height=90)
    outputFrame.grid(column=1, row=2)
    label_output = Text(outputFrame, width=100)
    label_output.grid()
    view_mode['output'] = label_output


def outPutText(type, vText):
    view_mode[type].config(view_mode[type], text=vText)

def outPutText2(text):
    view_mode['output'].delete(0.0,END)
    view_mode['output'].insert(0.0,text)


def viewMain(events):
    root = get_tk()
    global view_mode
    view_mode = {}
    global menu_event
    menu_event = {}
    menu_event.update(events)
    # 设置窗口大小
    set_tk_geometry(root, '')
    # 设置窗口 title
    set_tk_title(root, 'Soccer betting crawler')
    # 初始化菜单
    initMenu(root)
    # 初始化框架
    initFrame(root)
    return root
