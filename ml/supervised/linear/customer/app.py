#frontend code here

from flask import Flask,render_template,request
import joblib

#getting model

#custmodel-lr
#customodel1-rf

model=joblib.load('custmodel.lb')

# Encoding dictionaries

dct1 = {
  'Personal Travel':1, 'Business travel':0
}
dct2= {
  'satisfied':1, 'neutral or dissatisfied':0
}

dict3 = {
  'Eco':2, 'Eco Plus':0, 'Business':1}

app=Flask(__name__)

@app.route("/",methods=['GET','POST'])
def index():

    if request.method=='POST':
         # Get form values
        tof = request.form.get("tot")
        classs = request.form.get("classs")
        satisfaction = request.form.get("satisfaction")

        # Print values (for debugging)
        tof_val = dct1.get(tof)
        satisfaction_val = dct2.get(satisfaction)
        classs_val = dict3.get(classs)



# Inflight entertainment', 'Baggage handling', 'Cleanliness',
#        'Departure Delay in Minutes', 'Arrival Delay in Minutes'],

# Numeric inputs from form
       
       
        inflight_entertainment = int(request.form.get("InflightEntertainment", 0))
        baggage_handling = int(request.form.get("BaggageHandling", 0))
        cleanliness = int(request.form.get("Cleanliness", 0))
        departure_delay = int(request.form.get("DepartureDelay", 0))
        arrival_delay = int(request.form.get("ArrivalDelay", 0))

        # Debug print
        print("Received Values:")
        print(tof_val, satisfaction_val, classs_val,
              inflight_entertainment, baggage_handling, cleanliness,
              departure_delay, arrival_delay)
        
        # training order
# (['Type of Travel', 'Class', 'satisfaction', 'Inflight entertainment',
#        'Baggage handling', 'Cleanliness', 'Departure Delay in Minutes',
#        'Arrival Delay in Minutes'],
#       dtype='object')
        # Pass all features to model (order must match training)
        features = [[
            tof_val, classs_val,  satisfaction_val,
            inflight_entertainment, baggage_handling, cleanliness,
            departure_delay, arrival_delay
        ]]

        # Predict
        prediction = model.predict(features)

        # Convert prediction to label
        if prediction[0] == 1:
            message = "Predicted: Loyal Customer ✅"
        else:
            message = "Predicted: Disloyal Customer ❌"

        return render_template("index.html", message=message)

    return render_template("index.html")

    


if __name__=='__main__':
    app.run(debug=True)