from django.shortcuts import render

# Create your views here.
def home(request):
	return render(request,'home.html',{})

def Addition(request):
	from random import randint
	num_1=randint(0,10)
	num_2=randint(0,10)
	if(request.method == "POST"):
		answer=request.POST['answer']
		old_num1=request.POST['old_num_1']
		old_num2=request.POST['old_num_2']
		if not answer:
			myAnswer="Hey! you forgot to fil out that form..."
			return render(request,'Addition.html',{'answer':answer,'myAnswer':myAnswer,'color':'warning','num_1':num_1,'num_2':num_2,})
		correct_answer=int(old_num1)+int(old_num2)
		if int(correct_answer)==int(answer) :
			myAnswer="Correct ! "+old_num1+" + "+old_num2+" is "+answer
			color="success"
		else:
			myAnswer="InCorrect ! "+old_num1+" + "+old_num2+" is not "+answer+", it is "+str(correct_answer)
			color="danger"

		return render(request,'Addition.html',{'answer':answer,'myAnswer':myAnswer,'num_1':num_1,'num_2':num_2,'color':color,})
	return render(request,'Addition.html',{'num_1':num_1,'num_2':num_2,})

def Subraction(request):
	from random import randint
	num_1=randint(0,10)
	num_2=randint(0,10)
	if(request.method == "POST"):
		answer=request.POST['answer']
		old_num1=request.POST['old_num_1']
		old_num2=request.POST['old_num_2']
		if not answer:
			myAnswer="Hey! you forgot to fil out that form..."
			return render(request,'Subraction.html',{'answer':answer,'myAnswer':myAnswer,'color':'warning','num_1':num_1,'num_2':num_2,})
		correct_answer=int(old_num1) - int(old_num2)
		if int(correct_answer)==int(answer) :
			myAnswer="Correct ! "+old_num1+" - "+old_num2+" is "+answer
			color="success"
		else:
			myAnswer="InCorrect ! "+old_num1+" - "+old_num2+" is not "+answer+", it is "+str(correct_answer)
			color="danger"
		return render(request,'Subraction.html',{'answer':answer,'myAnswer':myAnswer,'num_1':num_1,'num_2':num_2,'color':color,})
	return render(request,'Subraction.html',{'num_1':num_1,'num_2':num_2,})

def Multiplication(request):
	from random import randint
	num_1=randint(0,10)
	num_2=randint(0,10)
	if(request.method == "POST"):
		answer=request.POST['answer']
		old_num1=request.POST['old_num_1']
		old_num2=request.POST['old_num_2']
		if not answer:
			myAnswer="Hey! you forgot to fil out that form..."
			return render(request,'Multiplication.html',{'answer':answer,'myAnswer':myAnswer,'color':'warning','num_1':num_1,'num_2':num_2,})
		correct_answer=int(old_num1)*int(old_num2)
		if int(correct_answer)==int(answer) :
			myAnswer="Correct ! "+old_num1+" * "+old_num2+" is "+answer
			color="success"
		else:
			myAnswer="InCorrect ! "+old_num1+" * "+old_num2+" is not "+answer+", it is "+str(correct_answer)
			color="danger"

		return render(request,'Multiplication.html',{'answer':answer,'myAnswer':myAnswer,'num_1':num_1,'num_2':num_2,'color':color,})
	return render(request,'Multiplication.html',{'num_1':num_1,'num_2':num_2,})

def Division(request):
	from random import randint
	num_1=randint(0,10)
	num_2=randint(1,10)
	if(request.method == "POST"):
		answer=request.POST['answer']
		old_num1=request.POST['old_num_1']
		old_num2=request.POST['old_num_2']
		if not answer:
			myAnswer="Hey! you forgot to fil out that form..."
			return render(request,'Division.html',{'answer':answer,'myAnswer':myAnswer,'color':'warning','num_1':num_1,'num_2':num_2,})
		correct_answer=float(old_num1)/float(old_num2)
		if float(correct_answer)==float(answer) :
			myAnswer="Correct ! "+old_num1+" / "+old_num2+" is "+answer
			color="success"
		else:
			myAnswer="InCorrect ! "+old_num1+" / "+old_num2+" is not "+answer+", it is "+str(correct_answer)
			color="danger"

		return render(request,'Division.html',{'answer':answer,'myAnswer':myAnswer,'num_1':num_1,'num_2':num_2,'color':color,})
	return render(request,'Division.html',{'num_1':num_1,'num_2':num_2,})

