from django.shortcuts import render,redirect,get_object_or_404
from .forms import QuestionForm,ChoiceForm
from .models import Question,Choice
from django.views.decorators.http import require_POST
from django.contrib.auth.decorators import login_required

# Create your views here.

def index(request):
    # Question의 모든 정보를 questions에 넣는다.
    questions = Question.objects.all()
    return render(request, 'questions/index.html', {'questions': questions})

@login_required
def create(request):
    # 1. 사용자가 데이터를 입력하기 위해서 GET요청(폼을 요청)
    # 6. 사용자가 데이터를 입력하고 POST요청
    # 12. 사용자가 올바른 데이터를 입력하고 POST요청

    # 7. POST method로 들어오기 떄문에 if문 실행
    # 13. POST method로 들어오기 떄문에 if문 실행
    if request.method=="POST":
        # 8.사용자의 데이터를 모델폼에 입력
        # 14.사용자의 데이터를 모델폼에 입력
        form = QuestionForm(request.POST)
        # 9. 데이터가 올바른지 검증
        # 15. 데이터가 올바른지 검증
        if form.is_valid():
            # 16. 데이터 저장
            form.save()
            # 17. 저장 후 index.html로 이동
            return redirect('questions:index')
    # 2. GET mothod로 들어오기 때문에 else문 실행
    else:
        # QuestionForm에 사용자가 입력한 것을 출력하여 form에 저장
        # 3. 사용자에게 빈 폼을 보여주기 위해서 모델폼을 인스턴스화 한 후 form변수에 저장
        form = QuestionForm()
    # 4. dict로 만들기
    # 10. 검증을 통과하지 못했을 경우 -> 올바른 데이터는 남기고 다시 폼 보여주기
    context = {
        'form':form,
    }
    #5. form.html보여주기
    #11. form.html 보여주기
    return render(request, 'questions/form.html', context)


def detail(request, id):

    #오브젝트를 가져오거나 404를 보내거나
    question = get_object_or_404(Question, id=id)
    choice_form = ChoiceForm()

    choices = question.choice_set.all()
    total_1 = choices.filter(pick=1).count()
    total_2 = choices.filter(pick=2).count()

    if total_1+total_2 == 0:
        persent_1 = 0
        persent_2 = 0
    else:
        persent_1 = total_1/(total_1+total_2) *100
        persent_2 = total_2/(total_1+total_2) *100

    context = {
        'question': question,
        'choice_form':choice_form,
        'persent_1':persent_1,
        'persent_2':persent_2,
    }
    return render(request, 'questions/detail.html', context)

def update(request, id):
    # 기존에 있던 정보를 가져옴
    question = get_object_or_404(Question, id=id)
    if request.method == "POST":
        #기존의 정보와 새로운 정보 다 필요하다.
        #기존의정보 instance=question
        form = QuestionForm(request.POST, instance=question)
        if form.is_valid():
            form.save()
            return redirect('questions:detail', id)
    else:
        # 수정버튼을 누르면 기존의 정보를 들고 와야한다.
        form = QuestionForm(instance=question)

    context = {
        'form':form,
    }
    return render(request, 'questions/form.html', context)

def delete(request,id):
    if request.method == 'POST':
        get_object_or_404(Question, id=id).delete()
        return redirect('questions:index')
    else:
        return redirect('questions:detail',id)

@require_POST
def choice_create(request,id):
    question = get_object_or_404(Question, id=id)
    choice_form = ChoiceForm(request.POST)
    if choice_form.is_valid():
        choice = choice_form.save(commit=False)
        choice.question = question
        choice.save()
    return redirect('questions:detail',id)

# 주소창에 직접입력했을 때(get방식들어올때) 405에러를 띄운다. require_POST
@require_POST
def choice_delete(request,question_id,choice_id):
    choice = get_object_or_404(Choice, id=choice_id)
    choice.delete()
    return redirect('questions:detail', question_id)