from rest_framework import serializers
from api_app.models import Patient

class PatientSerializers(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Patient
        fields = ['patiend_id','last_name', 'first_name', 'blood']
        

# class DoctorSerializers(serializers.HyperlinkedModelSerializer):
#     patient = serializers.SerializerMethodField(read_only=True)

#     # project = ProjectSerializers(many=True)

#     class Meta:
#         model = Doctor
#         fields = ['doctor_id', 'doctor_name', 'patient']

#     # def get_project(self, obj):
#     #     task = Task.objects.filter(task_id=obj.task_id)
#     #     print(task)
#     #     project = Project.task.project_set.all()
#     #     print(project)
#     #     return obj.project.name

#     def get_patient(self, obj):
#         patient = {
#             'first_name': obj.patient.first_name,
#             'last_name': obj.patient.last_name,
#         }
#         return patient