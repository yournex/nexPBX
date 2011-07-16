import plugins

from django.http import HttpResponse, Http404

import logging
logger = logging.getLogger(__name__)

def add(req, **kw):
    serv_plug = plugins.getPlugins()
    if 'service' in kw and not kw['service']  in serv_plug :
        logger.error('Service %s is not exisit'%(kw['service']))
        raise Http404
    return serv_plug[kw['service']]['pyobject'].views.add(req, **kw)
