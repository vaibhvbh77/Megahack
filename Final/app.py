from flask import Flask, render_template, request
import pcos_model
app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])


def basic():

    if request.method == 'POST':

        age = request.form['age']
        ChinHair = request.form['chinHair']
        CheeksHair = request.form['cheeksHair']
        upperLipHair = request.form['upperLipHair']
        betweenBreastHair = request.form['betweenBreastHair']
        armsHair = request.form['armsHair']
        innerThighHair= request.form['innerThighHair']
        exercise= request.form['exercise']
        eatOutside = request.form['eatOutside']
        Diagnosed = request.form['Diagnosed']
        Overweight = request.form['Overweight']
        Weightgain = request.form['Weightgain']
        Periods = request.form['Periods']
        Conceiving = request.form['Conceiving']
        AcneOrskinTag = request.form['AcneOrskinTag']
        HairThinning = request.form['HairThinning']
        DarkPatch = request.form['DarkPatch']
        Tiredness = request.form['Tiredness']
        MoodSwings = request.form['MoodSwings']
        CannedFood = request.form['CannedFood']
        City = request.form['City']
        
        if ChinHair == 5:
            ChinHair = 5
        elif ChinHair == 4:
            ChinHair = 4
        elif ChinHair == 3:
            ChinHair = 3
        elif ChinHair == 2:
            ChinHair = 2
        else:
            ChinHair = 1

        if CheeksHair == 5:
            CheeksHair = 5
        elif CheeksHair == 4:
            CheeksHair = 4
        elif CheeksHair == 3:
            CheeksHair = 3
        elif CheeksHair == 2:
            CheeksHair = 2
        else:
            CheeksHair = 1

        if upperLipHair == 5:
            upperLipHair = 5
        elif upperLipHair == 4:
            upperLipHair = 4
        elif upperLipHair == 3:
            upperLipHair = 3
        elif upperLipHair == 2:
            upperLipHair = 2
        else:
            upperLipHair = 1

        if betweenBreastHair == 5:
            betweenBreastHair = 5
        elif betweenBreastHair == 4:
            betweenBreastHair = 4
        elif betweenBreastHair == 3:
            betweenBreastHair = 3
        elif betweenBreastHair == 2:
            betweenBreastHair = 2
        else:
            betweenBreastHair = 1

        if armsHair == 5:
            armsHair = 5
        elif armsHair == 4:
            armsHair = 4
        elif armsHair == 3:
            armsHair = 3
        elif armsHair == 2:
            armsHair = 2
        else:
            armsHair = 1

        if innerThighHair == 5:
            innerThighHair = 5
        elif innerThighHair == 4:
            innerThighHair = 4
        elif innerThighHair == 3:
            innerThighHair = 3
        elif innerThighHair == 2:
            innerThighHair = 2
        else:
            innerThighHair = 1


        if exercise == 7:
            exercise = 7
        elif exercise == 6:
            exercise = 6
        elif exercise == 5:
            exercise = 5
        elif exercise == 4:
            exercise = 4
        elif exercise == 3:
            exercise = 3
        elif exercise == 2:
            exercise = 2
        else:
            exercise = 1

        if eatOutside == 1:
            eatOutside = 1
        else:
            eatOutside = 0

        if Diagnosed == 1:
            Diagnosed = 1
        else:
            Diagnosed = 0

        if Overweight == 1:
            Overweight = 1
        else:
            Overweight = 0

        if Weightgain == 1:
            Weightgain = 1
        else:
            Weightgain = 0

        if Periods == 1:
            Periods = 1
        else:
            Periods = 0

        if Conceiving == 1:
            Conceiving = 1
        else:
            Conceiving = 0

        if AcneOrskinTag == 1:
            AcneOrskinTag = 1
        else:
            AcneOrskinTag = 0

        if HairThinning == 1:
            HairThinning = 1
        else:
            HairThinning = 0

        if DarkPatch == 1:
            DarkPatch = 1
        else:
            DarkPatch = 0
        
        if Tiredness == 1:
            Tiredness = 1
        else:
            Tiredness = 0

        if MoodSwings == 1:
            MoodSwings = 1
        else:
            MoodSwings = 0

        if CannedFood == 1:
            CannedFood = 1
        else:
            CannedFood = 0

        if City == 1:
            City = 1
        else:
            City = 0
            
        value_to_be_predicted = [[
            age,
            ChinHair,
            CheeksHair,
            upperLipHair,
            betweenBreastHair,
            armsHair,
            innerThighHair,
            exercise,
            eatOutside,
            Diagnosed,
            Overweight,
            Weightgain,
            Periods,
            Conceiving,
            AcneOrskinTag,
            HairThinning,
            DarkPatch,
            Tiredness,
            MoodSwings,
            CannedFood,
            City
        ]]



        prediction_mechanism = pcos_model.training_model()
        prediction_value = prediction_mechanism.predict(value_to_be_predicted)

        POC_not_detected = 'You have no Polycystic ovary syndrome'
        POC_detected='You have Polycystic ovary syndrome ,Please consult with an specialist ' 
      


        if prediction_value == 0:
            return render_template('index.html', POC_not_detected=POC_not_detected)
        elif prediction_value == 1:
            return render_template('index.html', POC_detected=POC_detected)

    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)