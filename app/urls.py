# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.urls import path, re_path
from app import views
from .views import  Home, ProjectDetailView, show, edit, update, destroy

urlpatterns = [

    # The home page

    path('', Home.as_view(), name='home'),
    path('project_id=<pk>/', ProjectDetailView.as_view(), name='project_detail'),
    #path('timesheets/', timesheet_view, name = 'timesheet'),
    path('emp', views.emp),  
    path('show',show),  
    path('edit/<int:id>', edit),  
    path('update/<int:id>', update),  
    path('delete/<int:id>', destroy), 
    # Matches any html file
    re_path(r'^.*\.*', views.pages, name='pages'),

    
]
