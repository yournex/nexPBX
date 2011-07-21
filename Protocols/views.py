import plugins

from django.http import HttpResponse, Http404

import logging
logger = logging.getLogger(__name__)

def add(req, **kw):
    serv_plug = plugins.getPlugins()
    if serv_plug == None or 'protocol' in kw  and not kw['protocol']  in serv_plug :
        logger.error('Protocol %s is not exisit'%(kw['protocol']))
        raise Http404
    return serv_plug[kw['protocol']]['pyobject'].views.add(req, **kw)
