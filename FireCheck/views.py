from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.shortcuts import Http404,HttpResponseRedirect
from django.urls import reverse
# Create your views here.
#   from .data import building_data
from .models import *
from django.contrib.auth.models import User,Group
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth import authenticate, login, logout
def create(request):
    building_data()
    context= {
        "devices" : device.objects.all()
    }
    return render(request, "FireCheck/devicelist.html", context)
@login_required()
def index(request):
    context = {
        "buildings" : building.objects.all(),
        "devices" : device.objects.all(),
        "td" : device.objects.all().count(),
        "gd" : device.objects.filter(health='G').count(),
        "rd" : device.objects.filter(health='R').count(),
        "yd" : device.objects.filter(health='Y').count(),

    }
    return render(request, "FireCheck/index.html", context)
    #return render(request, "base.html", context)
@login_required()
def device_details(request, did):
    context= {
        "d" : device.objects.get(pk=did)
    }
    return render(request, "FireCheck/device_details.html", context)

@login_required()
def zone_details(request, zid):
    zo=zone.objects.get(pk=zid)
    context= {
        "z" : zone.objects.get(pk=zid),
        "d" : device.objects.filter(zone=zo),
        "dc":device.objects.filter(zone=zo).count(),
    }
    return render(request, "FireCheck/zone_details.html", context)
@login_required()
def building_details(request, bid):
    bo=building.objects.get(pk=bid)
    context= {
        "b" : building.objects.get(pk=bid),
        "d" : device.objects.filter(building=bo),
        "dc":device.objects.filter(building=bo).count(),
        "z" : zone.objects.filter(building=bo),
        "zc":zone.objects.filter(building=bo).count(),
        "p" : panel.objects.filter(building=bo),
        "pc":panel.objects.filter(building=bo).count(),
    }
    return render(request, "FireCheck/building_details.html", context)
@login_required()
def panel_details(request, pid):
    po=panel.objects.get(pk=pid)
    context= {
        "p" : panel.objects.get(pk=pid),
        "d" : device.objects.filter(panel=po),
        "dc":device.objects.filter(panel=po).count(),
        "z" : zone.objects.filter(panel=po),
        "zc":zone.objects.filter(panel=po).count(),
    }
    return render(request, "FireCheck/panel_details.html", context)



@login_required()
def device_list(request):
    context= {
        "devices" : device.objects.all()
    }
    return render(request, "FireCheck/device-list-table.html", context)

@login_required()
def red_device_list(request):
    context= {
        "devices" : device.objects.all().filter(health='R')
    }
    return render(request, "FireCheck/device-list-table.html", context)

@login_required()
def green_device_list(request):
    context= {
        "devices" : device.objects.all().filter(health='G')
    }
    return render(request, "FireCheck/device-list-table.html", context)

@login_required()
def yellow_device_list(request):
    context= {
        "devices" : device.objects.all().filter(health='Y')
    }
    return render(request, "FireCheck/device-list-table.html", context)

@login_required()
def building_list(request):
    context= {
        "buildings" : building.objects.all()
    }
    return render(request, "FireCheck/building-list.html", context)
@login_required()
def zone_list(request):
    context= {
        "zones" : zone.objects.all()
    }
    return render(request, "FireCheck/zonelist.html", context)
@login_required()
def panel_list(request):
    context= {
        "panels" : panel.objects.all()
    }
    return render(request, "FireCheck/panellist.html", context)
