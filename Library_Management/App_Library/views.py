import csv
from django.shortcuts import render,redirect
from django.conf import settings
from .models import *
from django.http import HttpResponse, JsonResponse
import json
import traceback
from django.views.decorators.cache import cache_control
from django.views.decorators.csrf import csrf_exempt
from django.template.loader import render_to_string

def add_css_data_coutnry_state_city(request):
    print(settings.BASE_DIR)

    with open(f'{settings.BASE_DIR}/city.csv', 'r', encoding="utf8") as f:
        csvreader = csv.reader(f)
        header = next(csvreader)
        for row in csvreader:
            # add countries
            # print(row[0].strip(), row[1].strip(),row[2].strip())
            # CountryMaster.objects.create(shortname=row[1].strip(), country_name=row[2].strip(), phonecode=row[3].strip())

            # add state
            # print(row[0].strip(), row[1].strip(),row[2].strip())
            # StateMaster.objects.create(state_name=row[1].strip(), fk_country=row[2].strip())

            # add cites
            print(row[1].strip(), row[2].strip())
            try:
                state_object = StateMaster.objects.get(id=row[2].strip())
                CityMaster.objects.create(
                    city_name=row[1].strip(), fk_state=state_object)
            except:
                pass
    return HttpResponse('data added succesfully')


########  function for admin login #########

@csrf_exempt
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def Admin_Login(request):
    try:
        session_id = request.session.get('admin_user_id')
        if request.method =="POST": 
            data = json.loads(request.body.decode('utf-8'))
            username = data['admin_username']
            password = data['admin_password']
            
            if AdminMaster.objects.filter(username=username, password=password).exists():
                obj = AdminMaster.objects.get(username=username,password=password)
                request.session['admin_user_id'] = str(obj.id) #########creating session
                send_data = {"status": "1", "msg": "Login succesfull", "obj": obj.id}
            else:
                send_data = {"status": "0","msg": "Invalid Credential"}
        else:   
            if session_id:
                return redirect('Dasboard')
            else:
                return render(request, 'admin/admin_login.html')
    except:
        print(traceback.format_exc())
        send_data = {"status": "0", "msg": "Something Went Wrong"}
    return JsonResponse(send_data)




########### function for admin logout ##############

@csrf_exempt
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def Admin_logout(request):
    try:
        del request.session['admin_user_id']
        send_data = {"status":"1" ,"msg":"Admin Logout Successfully"}
    except:
        print(traceback.format_exc())
        send_data = {"status": "0", "msg": "Something Went Wrong",'error': traceback.format_exc()}
    return JsonResponse(send_data)




def Dasboard(request):
    return render(request,'dashboard.html')


@csrf_exempt
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def Employee_list(request):
    try:
        session_id = request.session.get('admin_user_id')
        if session_id:    
            Admin_obj=AdminMaster.objects.get(id=session_id)
            Empl_obj=EmployeeDetails.objects.all().order_by('-id')
            
            context={
                'Admin_obj':Admin_obj,
                'Emp_obj':Empl_obj
            }
            rendered = render_to_string('RTS_Files/employee_list_rts.html', context)
            return render(request, 'employee_list.html', {'rendered': rendered})
        else:    
            return redirect('Admin_Login')
    except:    
        print(traceback.format_exc())
    
########## Add Employee by admin ############
@csrf_exempt
def Add_employee_by_admin(request):
    try:
        if request.method == "POST":
            firstname = request.POST.get('firstname')
            lastname = request.POST.get('lastname')
            email = request.POST.get('email')
            username = request.POST.get('username')
            mobileno = request.POST.get('mobileno')
            birthdate = request.POST.get('birthdate')
            profilepic = request.FILES.get('profilepic')
            password = request.POST.get('password')
            
            EmployeeDetails.objects.create(first_name=firstname, last_name=lastname, email=email, username=username, date_of_birth=birthdate, mobile_no=mobileno, password=password,profile_image=profilepic)
            Emp_obj = EmployeeDetails.objects.all().order_by('-id')
            rendered = render_to_string('RTS_Files/employee_list_rts.html', {'Emp_obj': Emp_obj})

            send_data = {'status': '1','msg': 'Employee Added Successfully!', 'rendered': rendered}
        else:    
            send_data = {'status': '0', 'msg': 'Request Not Post'}
    except:
        send_data = {'status': '0', 'msg': 'Something Went Wrong'}
    return JsonResponse(send_data)

    
######### delete employee by admin ##########
@csrf_exempt
def delete_employee_by_admin(request):
    try:
        if request.method =="POST":
            data = json.loads(request.body.decode('utf-8'))
            emp_id = data['emp_id']
            EmployeeDetails.objects.get(id=emp_id).delete()
            Emp_obj=EmployeeDetails.objects.all().order_by('-id')
            
            rendered = render_to_string('RTS_Files/employee_list_rts.html', {'Emp_obj': Emp_obj})
            send_data = {'status': '1', 'msg': 'Employee deleted Successfully!', 'rendered': rendered}
        else:
            send_data = {'status': '0', 'msg': 'Request Not Post'}
    except:
        print(traceback.format_exc())
        send_data ={'status':0,'msg':'Something Went Wrong'}
    return JsonResponse(send_data)


def student_list(request):
    return render(request,'student_list.html')    




