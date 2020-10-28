import sys
sys.path.extend(__path__)

def name():
    return "Test plugin"

def description():
    return "test"

def version():
    return "0.1"

def qgisMinimumVersion():
    return "3.0"

def authorName():
    return u"Milosz Piglas"

def classFactory(iface):
    import main
    return main.Plugin(iface)
