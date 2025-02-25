from django.shortcuts import render
from django.http import JsonResponse
from .models import Portfolio
from django.contrib.auth.decorators import login_required
from django.core.files.storage import FileSystemStorage



def home_view(request):
    all_portfolio = Portfolio.objects.filter(user=request.user)
    return render(request,'home.html',{
        "portfolios":all_portfolio
    })

@login_required
def create_portfolio(request):
    if request.method == 'POST':

        print(request.POST)
        print(request.FILES)
        
        name = request.POST.get('p-name')
        full_name = request.POST.get('f-name')
        image = request.FILES.get('image')
        about_me = request.POST.get('about')
        title = request.POST.get('title')
        date_of_birth = request.POST.get('dob')
        email = request.POST.get('email')
        city = request.POST.get('city')
        phone = request.POST.get('phone')
        roles = request.POST.getlist('role')
        skills_names = request.POST.getlist('skill_name[]')
        skills_levels = request.POST.getlist('skill_level[]')
        education_degrees = request.POST.getlist('degree[]')
        education_years = request.POST.getlist('year[]')
        education_institutions = request.POST.getlist('college[]')
        
        socials = {
            "linkedin": request.POST.get('linkedin', ''),
            "github": request.POST.get('github', ''),
            "twitter": request.POST.get('twitter', ''),
            "instagram": request.POST.get('insta', '')
        }
        
        skills = {skills_names[i]: skills_levels[i] for i in range(len(skills_names))} if skills_names else {}
        education = {education_degrees[i]: {"year": education_years[i], "institution": education_institutions[i]} for i in range(len(education_degrees))} if education_degrees else {}
        
        
        portfolio = Portfolio(
            user=request.user,
            name=name,
            full_name=full_name,
            image=image,
            about_me=about_me,
            title=title,
            date_of_birth=date_of_birth,
            email=email,
            city=city,
            phone=phone,
            roles=roles,
            skills=skills,
            education=education,
            socials=socials
        )
        
        try:
            portfolio.save()
        except Exception as e:
            print(f"Error saving portfolio: {e}")  # Print error message
            return JsonResponse({"success": False, "message": str(e)}, status=400)
        
        return JsonResponse({"success": True, "message": "Portfolio created successfully!"})

    return render(request, 'create_portfolio.html')

def view_portfolio(request,id):
    return render(request,"portfolio-1.html",{
        'portfolio':Portfolio.objects.get(id=id)
    })