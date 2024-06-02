from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

project_list = [
    {
        "id": 1,
        "title": "The first Project is great",
        "description": "Fully functional ecommerce website",
    },
    {
        "id": 2,
        "title": "The second Project is not too bad",
        "description": "Fully functional Insurance trading website",
    },
    {
        "id": 3,
        "title": "The first Project is a masterpiece",
        "description": "Fully functional fintech website",
    },
]


def project(request, project_id):
    current_project = None
    for proj in project_list:
        if str(proj["id"]) == str(project_id):
            current_project = proj
            break
    return render(request, 'projects/single-project.html', {'project': current_project})


def projects(request):
    page = "projects"
    number = 100
    return render(request, 'projects/projects.html', {'page': page, 'number': number, 'projects': project_list})
