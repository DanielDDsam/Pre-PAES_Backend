from api.models import *

# clean table
MathType.objects.filter().delete()
Question.objects.filter().delete()
Answer.objects.filter().delete()
# Users.objects.filter().delete()