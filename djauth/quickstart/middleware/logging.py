import json
from datetime import datetime
from django.conf import settings

class LoggingMiddleware(object):

    def prune_dict(self, cleandict):
        """ 
        Prune the things in the env that just serve to daze-and-confuse us
        """
        linux_env = ['LS_COLORS', 'RUN_MAIN', 'SCRIPT_NAME', 'LESSOPEN', 'COLORTERM', 
        'PS1', 'DISPLAY', 'PATH', 'SSH_AGENT_PID', 'LANG', 'TERM','SHELL', 
        'XDG_SESSION_PATH', 'XAUTHORITY', 'SHLVL', 'MANDATORY_PATH', 'WINDOWID',
        'XDG_RUNTIME_DIR', 'SSH_AUTH_SOCK', 'GDMSESSION','DEFAULTS_PATH',
        'XDG_SEAT_PATH', 'LESSCLOSE', 'DBUS_SESSION_BUS_ADDRESS', '_', 
        'DESKTOP_SESSION', 'UBUNTU_MENUPROXY', 'GTK_MODULES','XDG_DATA_DIRS',
        'XDG_CONFIG_DIRS', 'XDG_SESSION_COOKIE']

        virt_env = ['VIRTUALENVWRAPPER_LOG_DIR', 'WORKON_HOME','VIRTUAL_ENV',
        'VIRTUALENVWRAPPER_HOOK_DIR', 'VIRTUALENVWRAPPER_PROJECT_FILENAME']

        wsgi_env = [ 'wsgi.input','wsgi.multithread','wsgi.version','wsgi.multiprocess',
        'wsgi.run_once','wsgi.file_wrapper','wsgi.errors', 'wsgi.url_scheme']

        server_env = ['SERVER_SOFTWARE','HOME', 'DJANGO_SETTINGS_MODULE', 
        'GATEWAY_INTERFACE','OLDPWD', 'PWD' ]

        prune_em = linux_env + virt_env + wsgi_env + server_env

        for prune in prune_em:
            cleandict.pop(prune, None)

        for item in cleandict.keys():
            if cleandict[item] == "":
                cleandict.pop(item)

        return cleandict

    def process_request(self, request):
        """This is called every time a new request arrives in Django, but *before* 
        the url resolution is made.
         
        If this returns an HttpResponse -> nothing else is processed by django and 
           the HttpResponse is sent to client.
           
        If this returns None -> the request is passed along to the url resolver for 
           "normal" handling by Django 
        """
        enabled = getattr(settings, 'DEBUG', False)
        if not enabled:
            return None

        print "WARNING: this middleware is doing file-io and is expensive and unbounded."
        log_file = '/tmp/auth-testing.log'

        path = request.get_full_path()

        real_ip=""
        try:
            real_ip = request.META['HTTP_X_FORWARDED_FOR']
            # HTTP_X_FORWARDED_FOR can be a comma-separated list of IPs.
            real_ip = real_ip.split(",")[0]
            request.META['REMOTE_ADDR'] = real_ip
        except KeyError:
            pass

        log = open(log_file, 'a')
        log.write('----------- LoggingMiddleware: Request -----------\n')
        log.write('Date: %s\n' % datetime.now())
        log.write('IP: %s\n' % str(real_ip))
        log.write("%s: %s\n" % (request.method, str(path)))
        metadata = {k: str(v) for k, v in request.META.items()}
        metadata = self.prune_dict(metadata)
        log.write('---- request: headers ----\n')
        log.write(json.dumps(metadata, indent=4) + '\n')
        if len(request.COOKIES.items()) > 0:
            log.write('---- request: cookies ----\n')
            log.write(json.dumps({k: str(v) for k, v in request.COOKIES.items()}, indent=4) + '\n')
        log.write('-----------------------------------------\n')

        return None

    def process_response(self, request, response):
        enabled = getattr(settings, 'DEBUG', False)
        if not enabled:
            return response

        log_file = '/tmp/auth-testing.log'

    	path = request.get_full_path()

        log = open(log_file, 'a')
        log.write('----------- LoggingMiddleware: Response -----------\n')
        log.write("%s: %s\n" % (request.method, str(path)))
        log.write("%d: %s\n" % (response.status_code, response.status_text))
        log.write('---- respones: headers ---- \n')
        # In this context response.items is an array ot tuples.
        #import pdb; pdb.set_trace()
        metadata={}
        for tup in response.items():
            metadata[tup[0]]=tup[1]
        metadata = self.prune_dict(metadata)
        log.write(json.dumps(metadata, indent=4) + '\n')

        if len(response.cookies.items()) > 0:
            log.write('---- response: cookies ----\n')
            # I believe that response.cookies.items() is in the same format
            metadata={}
            for tup in response.cookies.items():
                metadata[tup[0]]=tup[1]
            metadata = self.prune_dict(metadata)
            log.write(json.dumps(metadata, indent=4) + '\n')

        log.write('---- response: content ----\n')
    	log.write(json.dumps(json.loads(response.content), indent=4) + '\n')
        log.write('-----------------------------------------\n')
        
        return response

