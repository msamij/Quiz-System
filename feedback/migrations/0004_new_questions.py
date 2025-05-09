from django.db import migrations


def load_questions(apps, schema_editor):
    Question = apps.get_model('feedback', 'Question')
    questions = [
        "What is the correct syntax for declaring an html tag?",
        "Which of the following tag is used to write CSS in HTML file?",
        "Which of the following tag is used to link an external CSS file in HTML?",
        "What is the largest heading tag in HTML?",
        "Which of the following tag is used to create a container (a parent) for other HTML elements?",
        "Which of the following tag is a block level element in HTML?",
        "Which of the following tag is an inline level element in HTML?",
        "Which of the following is true about block level elements?",
        "Which property is used in CSS to change the text color of HTML element?",
        "Which property is used in CSS to change the font size of HTML element?",
        "Which one of the following is called a universal selector in CSS?",
        "Which of the following is the correct syntax for selecting an element in CSS using a class?",
        "Which of the following is the correct syntax for selecting an element in CSS using an id?",
        "Which CSS property is used to add an image to HTML element using CSS?",
        "Which CSS property is used for alignment of text?",
        "Which CSS property is used to create space outside of an element?"
    ]
    for q in questions:
        Question.objects.create(question_text=q)


class Migration(migrations.Migration):

    dependencies = [
        ('feedback', '0003_rename_studentanswers_studentanswer'),
    ]

    operations = [
        migrations.RunPython(load_questions),
    ]
