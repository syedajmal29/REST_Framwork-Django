import django_filters
from .models import Employee



class EmployeeFilter(django_filters.FilterSet):
    desigantion = django_filters.CharFilter(field_name='designation', lookup_expr='iexact')
    emp_name = django_filters.CharFilter(field_name='emp_name', lookup_expr='icontains')
    # id = django_filters.RangeFilter(field_name='id')
    id_min = django_filters.CharFilter(method='filter_by_id_range', label='from EMP ID')
    id_max = django_filters.CharFilter(method='filter_by_id_range', label='to EMP ID')


    class Meta:
        model = Employee
        fields = ['desigantion', 'emp_name','id_min' ,'id_max']  # 'id' is not included here because we are using custom method for range filtering]

    def filter_by_id_range(self, queryset, name, value):
        if name == 'id_min':
            return queryset.filter(emp_id__gte=value)
        elif name == 'id_max':
            return queryset.filter(emp_id__lte=value)
        return queryset

# This filter can be used in views to filter employees by designation and emp_name.    