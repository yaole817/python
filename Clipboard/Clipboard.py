import win32clipboard as w
import win32con

def getText():
	w.OpenClipboard()
	t = w.GetClipboardData(win32con.CF_UNICODETEXT)
	w.CloseClipboard()
	return t
def setText(txt):
	w.OpenClipboard()
	w.EmptyClipboard()
	w.SetClipboardData(win32con.CF_UNICODETEXT, txt)
	w.CloseClipboard()

if __name__ == '__main__':
	t = 122321312
	setText(str(t))
	print(getText())