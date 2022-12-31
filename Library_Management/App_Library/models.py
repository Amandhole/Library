from django.db import models

# Create your models here.



    
# class CountryMaster(models.Model):
#     country_name = models.CharField(max_length = 50,null=True, blank=True)
#     country_code = models.CharField(max_length = 20,null=True, blank=True)
#     country_image = models.ImageField(upload_to ='CountryImage/', null=True, blank=True)
#     currency_name = models.CharField(max_length = 20,null=True, blank=True)
#     currency_code = models.CharField(max_length = 20,null=True, blank=True)
#     country_status = models.BooleanField(default=False)


class CountryMaster(models.Model):
    shortname = models.CharField(max_length=50, null=True, blank=True)
    country_name = models.CharField(max_length=50, null=True, blank=True)
    phonecode = models.CharField(max_length=100, null=True, blank=True)

    # def __str__(self):
    #     return self.country_name


class StateMaster(models.Model):
    state_name = models.CharField(max_length=50, null=True, blank=True)
    fk_country = models.ForeignKey(CountryMaster, on_delete=models.CASCADE, null=True, blank=True,)

    # def __str__(self):
    #     return self.state_name


class CityMaster(models.Model):
    city_name = models.CharField(max_length=50, null=True, blank=True)
    fk_state = models.ForeignKey(StateMaster, on_delete=models.CASCADE, null=True, blank=True,)

    # def __str__(self):
    #     return self.city_name


class AdminMaster(models.Model):
    name = models.CharField(max_length=50, null=True, blank=True)
    username = models.CharField(max_length=100, null=True, blank=True)
    password = models.CharField(max_length=100, null=True, blank=True)

    

class EmployeeDetails(models.Model):
    first_name = models.CharField(max_length=50, null=True, blank=True)
    last_name = models.CharField(max_length=50, null=True, blank=True)
    email = models.EmailField(max_length=50, null=True, blank=True)
    username = models.CharField(max_length=100, null=True, blank=True)
    date_of_birth = models.DateTimeField(max_length=50, null=True, blank=True)
    mobile_no = models.CharField(max_length=50, null=True, blank=True)
    password = models.CharField(max_length=100, null=True, blank=True)
    profile_image = models.ImageField(upload_to ='ProfileImage/', null=True, blank=True)

