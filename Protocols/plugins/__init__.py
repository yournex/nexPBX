import yaml

__plugin_configs = None


def getConfig(config_dir=None):
    """Load Protocols config from yaml file"""
    if config_dir == None:
        from nexPBX import settings
        config_dir = settings.NEXPBX_ETC
    try :
        config_file = open("%s/plugins.yml"%config_dir)
        y =yaml.load(config_file)
        return y['Protocols']
    except :
        raise

def getPlugins(config_dir=None):
    """Return plugins, load them if it's not loaded"""
    global __plugin_configs
    if __plugin_configs == None:
        return loadPlugins(config_dir)
    return __plugin_configs

def loadPlugins(config_dir=None):
    """load plugins"""
    global __plugin_configs
    ret_plugin = {}
    try :
        __plugin_configs = getConfig(config_dir)
        for proto in __plugin_configs :
            try :
                fromlist = ["views", "models"]
                #try to load plugin directly and get __doc__ value from that
                if proto['package'].rfind(".") != -1:
                    fromlist.append(proto['package'][proto['package'].rfind(".")+1:])
                pkg = __import__(proto['package'], fromlist=fromlist)
                proto['description']       = pkg.__doc__
                proto['installed_version'] = pkg.__version__
                proto['installed']         = True
                proto['pyobject']          = pkg
            except :
                proto['installed'] = False
                proto['enable']    = True
                proto['pyobject']  = None

            ret_plugin[proto['name']] = proto
        return ret_plugin
    except :
        raise


def getPluginsAsTuple(config_dir):
    """Return package names in this plugin as tuple
    It's usefull for using in INSTALLED_APPS
    """
    plugins_as_tuple = ()
    plugins = getConfig(config_dir)
    for proto in plugins :
        try :
            __import__(proto['package'])
            plugins_as_tuple = plugins_as_tuple + (proto['package'],)
        except :
            pass
    return plugins_as_tuple

