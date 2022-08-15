import webbrowser
import os 


webbrowser.open('https://www.youtube.com/')
""" 
Opens a web browser of your choice.
"""

# os.system("""osascript -e 'tell app "Slack" to open'""")
""" 
Has a terminal error.
Works, but does not open all applications in a window. Only opens in background. 
"""

os.system("""osascript -e 'tell application "Mission Control" to activate'""")
""" Opens any and all MacOS applications in the application folder. Will not bring already open applications to the foreground. """
