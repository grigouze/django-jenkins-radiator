# Create your views here.

import json

from django.shortcuts import render_to_response
from django.template import RequestContext
from django.conf import settings

from django.http import HttpResponse

from radiator.models import JenkinsCI

def index(request):
    """
        Return the view of jenkins jobs
    """

    return render_to_response('index.html', {'view': request.GET.get('view', \
                                '')}, context_instance=RequestContext(request))

def builds(request):
    """
        Return the json data of jenkins server
    """

    url = settings.JENKINS_URL
    view = request.GET.get('view') or settings.JENKINS_DEFAULT_URL
    timeout = settings.JENKINS_TIMEOUT

    jenkins = JenkinsCI(url=url, view=view, timeout=timeout)

    jobs = None
    result = None

    try:
        jobs = jenkins.get_all_jobs()
    except Exception, error:
        result = {'status': 'error', 'content': str(error.reason)}

    if not result:
        html = ''
        for job in jobs:
            blame = job['blame']
            if job['status'][0] in ('failed', 'unstable'):
                blame = "<br /><span class='blame'>%s</span>" % job['blame']

            html += "<li class = 'job " + " ".join(job['status']) + \
                    "'>%s%s</li>" % (job['name'], blame)

            result = {'status': 'ok', 'content': html}

    return HttpResponse(json.dumps(result))
