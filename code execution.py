#!/usr/bin/env python
# coding: utf-8

# In[239]:


#Input data
data  =[{"Gender": "Male", "HeightCm":171, "WeightKg":96},
{ "Gender": "Male", "HeightCm": 161, "WeightKg":  47},
{ "Gender": "Male", "HeightCm": 170, "WeightKg": 80.5 },
{ "Gender": "Female", "HeightCm": 166.0, "WeightKg": 62},
{"Gender": "Female", "HeightCm": 150.0, "WeightKg": 90.99},
{"Gender": "Female", "HeightCm": 167.0, "WeightKg": 100},
{"Gender": "Female", "HeightCm": '@123', "WeightKg": 82},
{"Gender": "Female", "HeightCm": '@123', "WeightKg": 'ABC'},
{"Gender": "Female", "HeightCm": '$$$', "WeightKg": 'abc'},
{"Gender": "Female", "HeightCm": -132, "WeightKg": 'abc'},
{"Gender": "Female", "HeightCm": -132, "WeightKg": -58},
{"Gender": "Male", "HeightCm": 132, "WeightKg": -58},
{"Gender": "Male", "HeightCm": '1 32', "WeightKg": 58},
{"Gender": "Male", "HeightCm": 0, "WeightKg": 0},
{"Gender": "Male", "HeightCm": 0, "WeightKg": 0.7},
{"Gender": "Male", "HeightCm": 0.5, "WeightKg": 0.7},
{"Gender": "Male", "HeightCm": 0, "WeightKg": -10.4},
{"Gender": "Male", "HeightCm": 220, "WeightKg": '011 '}]

#Calculate bmi of a person and categorize it into bmi category and health risk
def bmi(weight, height):
    
    bmi_calc = {}
    
    #Checking the input is string or not
    if (isinstance(weight, str) == False) & (isinstance(height,str) == False):
        
        #Checking if the input is greater than 0 (positive)
        if (float(weight) > 0) & (float(height) > 0):
            
            bmi_calc['BMI'] = round(weight / (height/100)**2,1)

            if bmi_calc['BMI'] <= 18.4:
                bmi_calc['BMI Category'] = 'Underweight'
                bmi_calc['Health_risk'] = 'Malnutrition risk'
                
            elif bmi_calc['BMI'] <= 24.9:
                bmi_calc['BMI Category'] = 'Normal weight'
                bmi_calc['Health_risk'] = 'Low risk'
                
            elif bmi_calc['BMI'] <= 29.9:
                bmi_calc['BMI Category'] = 'Overweight'
                bmi_calc['Health_risk'] = 'Enhanced risk' 
                
            elif bmi_calc['BMI'] <= 34.9:
                bmi_calc['BMI Category'] = 'Moderately obese'
                bmi_calc['Health_risk'] = 'Medium risk'
                
            elif bmi_calc['BMI'] <= 39.9:
                bmi_calc['BMI Category'] = 'Severely obese'
                bmi_calc['Health_risk'] = 'High risk'
                
            else:
                bmi_calc['BMI Category'] = 'Very severely obese'
                bmi_calc['Health_risk'] = 'Very high risk'
             
        
        else:
            bmi_calc['BMI'] = 'Height / Weight not a valid number'
            bmi_calc['BMI Category'] = 'Height / Weight not a valid number'
            bmi_calc['Health_risk'] = 'Height / Weight not a valid number'

    else:
        bmi_calc['BMI'] = 'Height / Weight not a valid number'
        bmi_calc['BMI Category'] = 'Height / Weight not a valid number'
        bmi_calc['Health_risk'] = 'Height / Weight not a valid number'
    
   
    return bmi_calc

#Function call to calculate BMI and update data
[row.update(bmi(row["WeightKg"], row["HeightCm"])) for row in data]

print("Number of patients in BMI_catergory as Overweight are", len([row['BMI Category']  for row in data if row['BMI Category'] == 'Overweight']))


# In[ ]:




