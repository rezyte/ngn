from django.shortcuts import render, redirect


def view_score(request):

	return render(request, 'view-score.html')

def single_page_cd(request):

	return render(request, 'single-page-cd.html')

def final_page(request):

	return render(request, "final-page.html")


def main_page(request):
	if request.method == "POST":
		username = request.POST.get("gthyreyrytr")
		password = request.POST.get("hrhryhrjhjh")
		if username == "980070152" and password == "0020392354":
			return redirect("main:view_score")
		else:
			pass
	return render(request, "index.html")


def verify(request):
	if request.method == "POST":
		username = request.POST.get("gthyreyrytr")
		password = request.POST.get("hrhryhrjhjh")
		if username == "980070152" and password == "0020392354":
			return redirect("main:view_score")
	return render(request,"view-score.html")
