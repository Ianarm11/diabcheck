from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SelectField, SubmitField
from wtforms.validators import DataRequired, Length

class DiabetesForm(FlaskForm):
    age = IntegerField('What is your age?', validators=[DataRequired(), Length(min=0, max=100)])
    gender = SelectField(u'What is your gender?', choices=[(1,'Male'),(0,'Female'),(0.5,'Other')])
    incUrination = SelectField(u'Have you experienced increased urniation?', choices=[(1,'Yes'),(0,'No')])
    incThirst = SelectField(u'Have you experienced increased thirst?', choices=[(1,'Yes'),(0,'No')])
    weightLoss = SelectField(u'Have you had any sudden weight loss?', choices=[(1,'Yes'),(0,'No')])
    limbWeakness = SelectField(u'Have you experienced any generalized or specific weakness in any of your limbs?', choices=[(1,'Yes'),(0,'No')])
    incHunger = SelectField(u'Have you experienced increased hunger (polyphagia)?', choices=[(1,'Yes'),(0,'No')])
    genitalThrush = SelectField(u'Have you suffered with genital thrush (yeast/candida infections)?', choices=[(1,'Yes'),(0,'No')])
    blurryVision = SelectField(u'Have you experienced visual blurring or difficulty seeing?', choices=[(1,'Yes'),(0,'No')])
    itching = SelectField(u'Have you experienced itching?', choices=[(1,'Yes'),(0,'No')])
    irritability = SelectField(u'Have you suffered from irritability?', choices=[(1,'Yes'),(0,'No')])
    woundOrInfections = SelectField(u'Have you experienced delayed wound healing or prolonged infections?', choices=[(1,'Yes'),(0,'No')])
    muscleParalysis = SelectField(u'Have you experienced any partial or mild muscle paralysis or inability to move like you used to (partial paresis)?', choices=[(1,'Yes'),(0,'No')])
    muscleStiffness = SelectField(u'Have you experienced any muscle stiffness?', choices=[(1,'Yes'),(0,'No')])
    hairLoss = SelectField(u'Have you experienced hair loss (alopecia)?', choices=[(1,'Yes'),(0,'No')])
    obese = SelectField(u'Are you obese?', choices=[(1,'Yes'),(0,'No')])
    submit = SubmitField('Get Results')
