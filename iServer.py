import ui, startserver
width, height = ui.get_screen_size()

URL = 'localhost'

view = ui.View()
webview = ui.WebView()
webview.width = width
webview.height = height
webview.load_url(URL)
webview.evaluate_javascript('window.location.href')
view.add_subview(webview)
view.present()
