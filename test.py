from epyk_mobile.interfaces.containers import WebView
from epyk_mobile.interfaces.text import TextView
from epyk_mobile.interfaces.android import View


test = View('my_web_view', '417dp', '0dp')
webView = WebView('test', '417dp', '0dp')
textView = TextView('textViewtest', '417dp', '0dp')
print(textView)
