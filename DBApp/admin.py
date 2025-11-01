from django.contrib import admin
from . models import Employee,Department,Employee_dup
# Register your models here.
class EmpAdmin(admin.ModelAdmin):
    list_display=['empno','empname','salary','department','grade']
    def grade(self,obj):
        if obj.salary>40000:
            return 'high'
        elif obj.salary>20000:
            return 'medium'
        else:
            return 'low'
    list_editable=['empname','salary','department']
    list_filter=['salary','department']
    ordering=['-empno']
class deptAdmin(admin.ModelAdmin):
    list_display=['deptno','deptname']
admin.site.register(Employee,EmpAdmin)
admin.site.register(Department,deptAdmin)
admin.site.register(Employee_dup,EmpAdmin)