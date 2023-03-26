from django.urls import path
from design_project.views import design, ProjectDetail, shop, send_to_mail

app_name = 'design_project'


urlpatterns = [
    path('', design, name='design'),
    path('projects/<int:pk>/', ProjectDetail.as_view(), name='projects'),
    path('shops/', shop, name='shop'),
    path('answer/', send_to_mail, name='answer')
]
