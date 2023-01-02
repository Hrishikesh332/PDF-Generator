from django.shortcuts import render
from django.http import FileResponse
import io
from reportlab.pdfgen import canvas
from reportlab.lib.units import inch
from reportlab.lib.pagesizes import letter

def pdf_gen(request):
    b=io.BytesIO()
    c=canvas.Canvas(b, pagesize=letter, bottomup=0)
    textob=c.beginText()
    textob.setTextOrigin(inch, inch)
    textob.setFont("Helvetica", 14)

    lines=[
        "Line 1",
        "Line 2",
        "Line 3"
    ]

    for line in lines:
        textob.textLine(line)

    c.drawText(textob)
    c.showPage()
    c.save()
    b.seek(0)

    return FileResponse(b, as_attachment=True, filename="new.pdf")


def report_gen(request):
    openai.api_key= API_KEY
    if request.POST["query"]:
            ques=str(request.POST["query"])
            print(ques)

            answer = openai.Completion.create(
            model="text-davinci-003",
            prompt=f"Generate a report on the following topic: {ques}\n A:",
            temperature=0,
            max_tokens=100,
            top_p=1,
            frequency_penalty=0,
            presence_penalty=0,
            stop=["\n"]
            )
            print(answer.choices[0].text)
        #return HttpResponse(answer.choices[0].text)
    return render(request, 'pdfapp/index.html',{'result1':answer.choices[0].text})
