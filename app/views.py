from django.shortcuts import render

# Create your views here.
from app.models import *
from django.db.models import Q
def equijoin(request):
    EMPOBJECTS=Emp.objects.select_related('deptno').all()
    d={'EMPOBJECTS':EMPOBJECTS}
    return render(request,'equijoin.html',d)


def empsalgrade(request):
    #SO=SalGrade.objects.filter(grade=3)
    #EO=Emp.objects.filter(sal__range=(SO[0].losal,SO[0].hisal))
    SO=SalGrade.objects.filter(grade=4)
    EO=Emp.objects.filter(sal__range=(SO[0].losal,SO[0].hisal))
    SO=SalGrade.objects.filter(grade__in=(3,4))
    EO=Emp.objects.none()
    for sgo in SO:
        EO=EO|Emp.objects.filter(sal__range=(sgo.losal,sgo.hisal),ename__in=('BLAKE','KING'))
    d={'SO':SO,'EO':EO}
    return render(request,'empsalgrade.html',d)


def selfjoins(request):
    empmgrobjects=Emp.objects.select_related('mgr').all()
    
    empmgrobjects=Emp.objects.select_related('mgr').filter(sal=2500)
    
    empmgrobjects=Emp.objects.select_related('mgr').filter(mgr__ename='KING')
    d={'empmgrobjects':empmgrobjects}
    return render(request,'selfjoins.html',d)


def emp_mgr_dept(request):
    emd=Emp.objects.select_related('deptno','mgr').all()
    
    emd=Emp.objects.select_related('deptno','mgr').filter(deptno__dname='RESEARCH')
    emd=Emp.objects.select_related('deptno','mgr').filter(mgr__ename='BLAKE')
    emd=Emp.objects.select_related('deptno','mgr').filter(ename='MARTIN')
    emd=Emp.objects.select_related('deptno','mgr').all()
    emd=Emp.objects.select_related('deptno','mgr').filter(Q(deptno__dname='RESEARCH') | Q(mgr__ename='JOHNS'))
    
    d={'emd':emd}
    return render(request,'emp_mgr_dept.html',d)
