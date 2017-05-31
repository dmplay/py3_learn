import win32api
import win32con
import win32gui

def showBox():
    win32api.MessageBox(win32con.NULL, 'Python 你好！', '你好', win32con.MB_OK)

def search():
    classname = "MozillaWindowClass"
    titlename = "QQ"
    # 获取句柄
    hwnd = win32gui.FindWindow(None,titlename)
    # 获取窗口左上角和右下角坐标
    left, top, right, bottom = win32gui.GetWindowRect(hwnd)
    if left == -32000:
        win32gui.ShowWindow(hwnd,win32con.SW_SHOWNORMAL)
    left, top, right, bottom = win32gui.GetWindowRect(hwnd)
    # 获取某个句柄的类名和标题
    title = win32gui.GetWindowText(hwnd)
    clsname = win32gui.GetClassName(hwnd)

    # 获取父句柄hwnd类名为clsname的子句柄
    hwnd1 = win32gui.FindWindowEx(hwnd, None, clsname, None)

def get_child_windows(parent):
    '''     
    获得parent的所有子窗口句柄
     返回子窗口句柄列表
     '''
    if not parent:
        return
    hwndChildList = []
    win32gui.EnumChildWindows(parent, lambda hwnd, param: param.append(hwnd),  hwndChildList)
    return hwndChildList



if __name__=="__main__":
    search()