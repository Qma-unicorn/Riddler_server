from django.shortcuts import redirect

import os
import openpyxl

from .models import *

def IndexView(request):
    def add(sheet):
        slay = 1
        missAnswer = False
        missQuestion = False
        while True:
            block = sheet['A' + str(slay)].value
            content = sheet['B' + str(slay)].value
            if block:
                if block == 'quiz':
                    slay += 1
                    block = sheet['A' + str(slay)].value
                    if block == 'description':
                        quizDesc = sheet['B' + str(slay)].value
                        if not Quiz.objects.filter(name=content).first():
                            quiz = Quiz(name=content, desc=quizDesc)
                            quiz.save()
                        else:
                            missQuestion = True
                    else:
                        break

                elif block == 'question' and not missQuestion:
                    if not Question.objects.filter(content = content, quiz = quiz).first():
                        question = Question(content = content, quiz = quiz)
                        question.save()
                    else:
                        missAnswer = True
                elif block == 'endquestion' and not missQuestion:
                    missAnswer = False
                elif 'answer' in block and not missAnswer and not missQuestion:
                    correct = block.split(',')[1].strip()
                    if not Answer.objects.filter(content = content, question = question, correct = correct).first():
                        answer = Answer(content = content, correct = correct, question = question)
                        answer.save()
                elif block == 'endquizes':
                    break
                slay += 1
            else:
                break

    if request.user.is_authenticated:
        path = os.getcwd() + '/Loader/tests/'
        with os.scandir(path) as files:
            for file in files:
                if file.is_file() and file.name.split(".")[-1] == 'xlsx':
                    fileSource = os.path.join(path, file.name)
                    wb = openpyxl.load_workbook(fileSource)
                    for sheet_name in wb.get_sheet_names():
                        sheet = wb.get_sheet_by_name(sheet_name)
                        add(sheet)
        return redirect('/admin')