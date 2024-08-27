from flask_wtf import FlaskForm
from wtforms import(
    SelectField,
    StringField,
    SubmitField
)
from wtforms.validators import(
    DataRequired
)

class inputForm(FlaskForm):
    airline=SelectField(
        "Airline",
        choices={'SpiceJet','AirAsia','Vistara','GO_FIRST' ,'Indigo', 'Air_India'},
        validators=[DataRequired()]
    )
    Source=SelectField(
        "From",
        choices={'Delhi', 'Mumbai' ,'Bangalore' ,'Kolkata' ,'Hyderabad', 'Chennai'},
        validators=[DataRequired()]
    )
    departure=SelectField(
        "Departure Time",
        choices={'Evening', 'Early_Morning' ,'Morning' ,'Afternoon','Night' ,'Late_Night'},
        validators=[DataRequired()]
    )
    stops=SelectField(
        "Number of stops",
        choices={'zero', 'one' ,'two_or_more'},
        validators=[DataRequired()]
    )
    arrival=SelectField(
        "Arrival Time",
        choices={'Night','Morning' ,'Early_Morning', 'Afternoon', 'Evening', 'Late_Night'},
        validators=[DataRequired()]
    )
    destination=SelectField(
        "To",
        choices={'Mumbai' ,'Bangalore' ,'Kolkata', 'Hyderabad' ,'Chennai', 'Delhi'},
        validators=[DataRequired()]
    )
    coach=SelectField(
        "Class",
        choices={'Economy', 'Business'},
        validators=[DataRequired()]
    )
    duration=StringField(
        'Journey Time',
        validators=[DataRequired()]
    )
    daysLeft=StringField(
        "How many days to go",
        validators=[DataRequired()]
    )
    submit=SubmitField('Predict')
    
