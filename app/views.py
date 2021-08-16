# -*- encoding: utf-8 -*-
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from django.template import loader
from django.http import HttpResponse
from django import template
from projects.models import Project, Phase
from profiles.models import Profile
from timesheets.models import Timesheet
from workflow.models import Document, Submission, Status
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView, DetailView
from django.db.models import Sum, Count, DurationField, ExpressionWrapper, F, Min, Max, Q, When

@login_required(login_url="/login/")
def index(request):
    
    context = {}
    context['segment'] = 'index'

    html_template = loader.get_template( 'index.html' )
    return HttpResponse(html_template.render(context, request))

@login_required(login_url="/login/")
def pages(request):
    context = {}
    # All resource paths end in .html.
    # Pick out the html file name from the url. And load that template.
    try:
        
        load_template      = request.path.split('/')[-1]
        context['segment'] = load_template
        
        html_template = loader.get_template( load_template )
        return HttpResponse(html_template.render(context, request))
        
    except template.TemplateDoesNotExist:

        html_template = loader.get_template( 'page-404.html' )
        return HttpResponse(html_template.render(context, request))

    except:
    
        html_template = loader.get_template( 'page-500.html' )
        return HttpResponse(html_template.render(context, request))





class Home(LoginRequiredMixin, TemplateView):
    template_name = 'index.html'

    #getting the project:
    def get_object(self):
        pk = self.kwargs.get('project_id')
        return pk
    #getting the project phases:
    def get_context_data(self, **kwargs):
        context = super(Home, self).get_context_data(**kwargs)
        projects = Project.objects.all()
        phases = Phase.objects.all()
        timesheets = Timesheet.objects.filter(phase__project=self.get_object())
        context["timesheets"] = timesheets
        context["phases"] = phases
        context["projects"] = projects
        context['projects_stats'] = Project.objects.all().aggregate(total_value = (Sum('value')), total_projects = (Count('id')), total_design_value = (Sum('design_value_prelims')))
        context['phase_stats'] = Phase.objects.all().aggregate(max_deadline = (Max('design_end')), min_deadline = (Min('design_start')))

        print(projects)
        return context





class ProjectDetailView(LoginRequiredMixin,DetailView):
    context_object_name = 'project_details'
    model = Project
    template_name = 'project-detail.html'

    def get_object(self):
        pk = self.kwargs['pk']
        return pk

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        projects = Project.objects.all()
        project = get_object_or_404(Project, pk=self.kwargs['pk'])
        status_a = Status.objects.filter(submission__document__phase__project=self.get_object(), status=0, active=True)
        context['project'] = project
        context["projects"] = projects
        context['phases'] = Phase.objects.filter(project_id=self.get_object())
        context['timesheets'] = Timesheet.objects.filter(phase__project=self.get_object())
        context['documents'] = Document.objects.filter(phase__project=self.get_object())
        context['submissions'] = Submission.objects.filter(document__phase__project=self.get_object())
        context['statuses'] = Status.objects.filter(submission__document__phase__project=self.get_object())
        context['time_distribution'] = Timesheet.objects.filter(phase__project=self.get_object()).aggregate(
            tot_survey_time = Sum('time_spent', filter=Q(activity=0)),
            tot_int_meet_time = Sum('time_spent', filter=Q(activity=1)),
            tot_ext_meet_time = Sum('time_spent', filter=Q(activity=2)),
            tot_ts_time = Sum('time_spent', filter=Q(activity=3)),
            tot_ga_time = Sum('time_spent', filter=Q(activity=4)),
            tot_fab_time = Sum('time_spent', filter=Q(activity=5)),
            tot_amendments_time = Sum('time_spent', filter=Q(activity=6)),
            tot_ab_time = Sum('time_spent', filter=Q(activity=7)),
            tot_time_spent = Sum('time_spent'),
            
            tot_survey_spent = Sum('time_spent', filter=Q(activity=0))*project.hourly_rate,
            tot_int_meet_spent = Sum('time_spent', filter=Q(activity=1))*project.hourly_rate,
            tot_ext_meet_spent = Sum('time_spent', filter=Q(activity=2))*project.hourly_rate,
            tot_ts_spent = Sum('time_spent', filter=Q(activity=3))*project.hourly_rate,
            tot_ga_spent = Sum('time_spent', filter=Q(activity=4))*project.hourly_rate,
            tot_fab_spent = Sum('time_spent', filter=Q(activity=5))*project.hourly_rate,
            tot_amendments_spent = Sum('time_spent', filter=Q(activity=6))*project.hourly_rate,
            tot_ab_spent = Sum('time_spent', filter=Q(activity=7))*project.hourly_rate,
            tot_spent = Sum('time_spent')*project.hourly_rate

            )

        context['documents_status'] = Status.objects.filter(submission__document__phase__project=self.get_object()).order_by('-phase.pk').aggregate(
            status_a = Count('status', filter=Q(status=0, active = True)),
            status_b = Count('status', filter=Q(status=1, active = True)),
            status_c = Count('status', filter=Q(status=2, active = True))               
            )
        print(context)
        
        return context


from django.shortcuts import render
from django.forms import inlineformset_factory
from timesheets.models import Timesheet
from profiles.models import Profile
from django import forms

# Create your views here.
#def timesheet_view(request):
    #user_id = request.user.id
    #projects = Project.objects.all()
 #   phases = Phase.objects.all().order_by('-id')[:10]
 #   TimesheetFormset = inlineformset_factory(Phase, Timesheet, fields = '__all__', extra = 1)

    #formset = TimesheetFormset(instance=forms.phases)

  #  context = {
  #      'formset': formset
  #      }
  #  print(context)
  #  return render(request, 'timesheets/add.html', context)
from projects.forms.forms import ProjectForm  


def emp(request):  
    if request.method == "POST":  
        form = ProjectForm(request.POST)  
        if form.is_valid():  
            try:  
                form.save()  
                return redirect('/show')  
            except:  
                pass  
    else:  
        form = ProjectForm()  
    return render(request,'project-crud/add-project.html',{'form':form})  
def show(request):  
    projects = Project.objects.all()  
    return render(request,"project-crud/show-project.html",{'projects':projects})  
def edit(request, id):  
    project = Project.objects.get(id=id)  
    return render(request,'edit.html', {'project':project})  
def update(request, id):  
    project = Project.objects.get(id=id)  
    form = ProjectForm(request.POST, instance = project)  
    if form.is_valid():  
        form.save()  
        return redirect("/show")  
    return render(request, 'edit.html', {'project':project})  
def destroy(request, id):  
    project = Project.objects.get(id=id)  
    project.delete()  
    return redirect("/show")  