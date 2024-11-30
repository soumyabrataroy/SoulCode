import streamlit as st
from datetime import datetime
from reportlab.pdfgen import canvas
from io import BytesIO
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph
from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import getSampleStyleSheet

# Create tabs
tab1, tab3, tab2 = st.tabs(["Individal analsis", "Compatibility Check","Analysis PDF generation"])


with tab1:
    
    st.title("Put DOB and unlock potential")

    # Define the minimum and maximum dates for the date picker
    min_date = datetime(1900, 1, 1)  # Minimum date (e.g., January 1, 1900)
    max_date = datetime(2100, 12, 31)  # Maximum date (e.g., December 31, 2100)

    # Create a date input widget with the specified date range
    selected_date = st.date_input("Select a date", value=datetime.today(), min_value=min_date, max_value=max_date)

    # Save the selected date in a variable
    date_variable = selected_date

    gender = st.selectbox("Select your gender:", ["Male", "Female"])

    # Display the selected date
    st.write(f"The selected date is: {date_variable}")
    # st.write(type(date_variable))

    # Optionally, convert it to a string or another format if needed
    date_string = date_variable.strftime("%d-%m-%Y")
    st.write(f"Formatted date: {date_string}")

    # Extracting the date value for further use
    day = date_variable.day
    month = date_variable.month
    year = date_variable.year

    mulank = sum(int(digit) for digit in str(day))
    month_sum = sum(int(digit) for digit in str(month))
    year_sum = sum(int(digit) for digit in str(year))
    date_month_year = mulank+month_sum+year_sum


    def total_sum(value):
        while len(str(value))>1:
            value = sum(int(digit) for digit in str(value))
        return value
    
    mulank = total_sum(mulank)
    bhagyank = total_sum(date_month_year)

    # Display the extracted day, month, and year
    st.write(f"Mulank: {mulank}, Bhagyank: {bhagyank}")

    # copying mulankand bhagyank
    mulank_ = mulank
    bhagyank_ = bhagyank

    # Compatibility of numbers:
    import pandas as pd



    # Standard luso grid
    std_grid = {
        'Lu So Grid':['Mental Plane','Heart Plane','Practical Plane'],
        'Vision Plane':[4,3,8],
        'Will Plane':[9,5,1],
        'Action Plane':[2,7,6]
    }

    # Creating a DataFrame from the dictionary
    luso_grid = pd.DataFrame(std_grid)

    # Displaying the DataFrame
    st.write(luso_grid)


    ######### Creating your luso grid ##########
    your_luso_grid = luso_grid.copy()
    your_luso_grid.iloc[:, 1:] = ''

    your_luso_grid_analysis = luso_grid.copy()
    your_luso_grid_analysis.iloc[:, 1:] = ''

    # adding day value
    for i in str(day):

        if i == '0':
            pass
        else:
            # Check if i is present and get its index
            index_of = luso_grid.isin([int(i)])
            # If you want to get the exact row and column index where i is located
            index_positions = index_of.stack().loc[lambda x: x].index.tolist()
            value = your_luso_grid.loc[index_positions[0][0], index_positions[0][1]]

            your_luso_grid.loc[index_positions[0][0], index_positions[0][1]] = str(value)+i
            your_luso_grid_analysis.loc[index_positions[0][0], index_positions[0][1]] = i

    # adding month value
    for i in str(month):

        if i == '0':
            pass
        else:
            # Check if i is present and get its index
            index_of = luso_grid.isin([int(i)])
            # If you want to get the exact row and column index where i is located
            index_positions = index_of.stack().loc[lambda x: x].index.tolist()
            value = your_luso_grid.loc[index_positions[0][0], index_positions[0][1]]

            your_luso_grid.loc[index_positions[0][0], index_positions[0][1]] = str(value)+i
            your_luso_grid_analysis.loc[index_positions[0][0], index_positions[0][1]] = i

    # adding year value
    for i in str(year):

        if i == '0':
            pass
        else:
            # Check if i is present and get its index
            index_of = luso_grid.isin([int(i)])
            # If you want to get the exact row and column index where i is located
            index_positions = index_of.stack().loc[lambda x: x].index.tolist()
            value = your_luso_grid.loc[index_positions[0][0], index_positions[0][1]]

            your_luso_grid.loc[index_positions[0][0], index_positions[0][1]] = str(value)+i
            your_luso_grid_analysis.loc[index_positions[0][0], index_positions[0][1]] = i

    # mulank 
    if len(str(day))==1 or str(day)=='10' or str(day)=='20' or str(day)=='30':
        pass
    else:
        index_of = luso_grid.isin([int(mulank)])
        # If you want to get the exact row and column index where i is located
        index_positions = index_of.stack().loc[lambda x: x].index.tolist()
        value = your_luso_grid.loc[index_positions[0][0], index_positions[0][1]]

        your_luso_grid.loc[index_positions[0][0], index_positions[0][1]] = str(value)+str(mulank)
        your_luso_grid_analysis.loc[index_positions[0][0], index_positions[0][1]] = str(mulank)

    # bhagyank

    index_of = luso_grid.isin([int(bhagyank)])
    # If you want to get the exact row and column index where i is located
    index_positions = index_of.stack().loc[lambda x: x].index.tolist()
    value = your_luso_grid.loc[index_positions[0][0], index_positions[0][1]]

    your_luso_grid.loc[index_positions[0][0], index_positions[0][1]] = str(value)+str(bhagyank)
    your_luso_grid_analysis.loc[index_positions[0][0], index_positions[0][1]] = str(bhagyank)

    st.write(your_luso_grid)
    st.write(your_luso_grid_analysis)


    # your luso grid analysis

    if ('4' in your_luso_grid_analysis.iloc[0, 1:].values) and ('9' in your_luso_grid_analysis.iloc[0, 1:].values) and ('2' in your_luso_grid_analysis.iloc[0, 1:].values):
        mind_plane = '1. Genius \n 2. Uses mind to come up with any decision \n 3. Logical person \n 4. Mind plane is 100% active \n 5. It is a blessing'
    elif ('4' in your_luso_grid_analysis.iloc[0, 1:].values) and ('9' in your_luso_grid_analysis.iloc[0, 1:].values):
         mind_plane = '1. Struggles with health (stress, leg problem, knee \n 2. Legal matter may happen'
    elif ('4' in your_luso_grid_analysis.iloc[0, 1:].values) and ('2' in your_luso_grid_analysis.iloc[0, 1:].values):
         mind_plane = '1. May involve in bad company \n 2. Get blame of others misbehaviour \n 3. An intelligent person \n 4. Family problems (elder sibling or mother)'
    elif ('9' in your_luso_grid_analysis.iloc[0, 1:].values) and ('2' in your_luso_grid_analysis.iloc[0, 1:].values):
         mind_plane = '1. Big helper of society \n 2. Bad with love relation (specially girls) \n 3. Support from powerful or elderly people \n 4. Spiritual person'
    elif ('4' in your_luso_grid_analysis.iloc[0, 1:].values):
         mind_plane = '1. Flexible in nature \n 2. Intelligent person \n 3. No grey area in life \n 4. Does not like manupulative people \n 5. Hardworking but may face struggling in early life'
    elif ('9' in your_luso_grid_analysis.iloc[0, 1:].values):
         mind_plane = '1. Religious Person \n 2. Artistic and short tempered \n 3. Donation lover \n 4. Thinks from the heart \n 5. Work for sociaty'
    elif ('2' in your_luso_grid_analysis.iloc[0, 1:].values):
         mind_plane = '1. Caring nature \n 2. Family oriented \n 3. Simple person \n 4. Take decisions considering the family in his/her mind.'
    else:
         mind_plane = 'mind plane is missing'

    if ('3' in your_luso_grid_analysis.iloc[1, 1:].values) and ('5' in your_luso_grid_analysis.iloc[1, 1:].values) and ('7' in your_luso_grid_analysis.iloc[1, 1:].values):
        heart_plane = '1. Satisfaction in life after 45 \n 2. Artistic \n 3. Good learner and education \n 4. Very emotional person \n 5. Golden heart'
    elif ('3' in your_luso_grid_analysis.iloc[1, 1:].values) and ('5' in your_luso_grid_analysis.iloc[1, 1:].values):
        heart_plane ='1. Rational behaviour \n 2. Lucky with money \n 3.Good communicator \n 4. Good for education business'
    elif ('5' in your_luso_grid_analysis.iloc[1, 1:].values) and ('7' in your_luso_grid_analysis.iloc[1, 1:].values):
        heart_plane ='1. Attractive personality \n 2. Business oriented \n 3. If 5 comes two times and 7 comes one time, people learn by themselves and start earning well'
    elif ('3' in your_luso_grid_analysis.iloc[1, 1:].values) and ('7' in your_luso_grid_analysis.iloc[1, 1:].values):
        heart_plane ='1. Lucky person \n 2. Skilled person \n 3. Good for occult science \n 4. Emotional person'
    elif ('3' in your_luso_grid_analysis.iloc[1, 1:].values):
        heart_plane ='1. Knowledge \n 2. Lezy \n 3. Quick Learner'
    elif ('5' in your_luso_grid_analysis.iloc[1, 1:].values):
        heart_plane ='1. Multiple experience in life \n 2. Enjoy life at fullest'
    elif ('7' in your_luso_grid_analysis.iloc[1, 1:].values):
        heart_plane ='1. Intuitive person \n 2. Researcher \n 3. Do not believe people easily \n 4. May face minimum two break-ups in life'
    else:
        heart_plane ='heart plane is missing. Emotion less.'

    if ('8' in your_luso_grid_analysis.iloc[2, 1:].values) and ('1' in your_luso_grid_analysis.iloc[2, 1:].values) and ('6' in your_luso_grid_analysis.iloc[2, 1:].values):
        practical_plane = 'It is 4th Raj jog \n 1. Very practical nature \n 2. Believing in meterialistic gains in life also gets them with time. Love luxury. \n 3. Romantic nature \n 4. Loves power and authority in job/business and in relationships'
    elif ('8' in your_luso_grid_analysis.iloc[2, 1:].values) and ('1' in your_luso_grid_analysis.iloc[2, 1:].values):
        practical_plane ='1. Image conscious \n 2. Agressive nature \n 3. May insult or accusation of a crime come into life once \n 4. Loves variety in career \n 5. His/her spouse may face frequent health issues \n 6. Loves being in authority'
    elif ('1' in your_luso_grid_analysis.iloc[2, 1:].values) and ('6' in your_luso_grid_analysis.iloc[2, 1:].values):
        practical_plane ='1. Not very good for marriage life \n 2. Luxury comes into life \n 3. Want to look groomed and rich'
    elif ('6' in your_luso_grid_analysis.iloc[2, 1:].values) and ('6' in your_luso_grid_analysis.iloc[2, 1:].values):
        practical_plane ='1. Money comes anyhow in life at a time of need \n 2. May face eyes related problems \n 3. May face genital related problems \n 4. Emotional person'
    elif ('8' in your_luso_grid_analysis.iloc[2, 1:].values):
        practical_plane ='1. Good money manager \n 2. Always speaks the truth and hates lier too much \n 3. Justice lover'
    elif ('1' in your_luso_grid_analysis.iloc[2, 1:].values):
        practical_plane ='1. Good in communication \n 2. Good memory and grasping power, 3. if one time: good in communication but bad in expression, if 2 times: good in communication and good in expression, if 3 times: 80% people very talkative and 20% people very introvert, if 4 times: when you speak creates some trouble'
    elif ('6' in your_luso_grid_analysis.iloc[2, 1:].values):
        practical_plane ='1. Family oriented \n 2. Loves luxury around him \n 3. Attractive personality \n 4. Art lover'
    else:
        practical_plane ='Practical plane is missing'

    if ('4' in your_luso_grid_analysis.iloc[0:, 1].values) and ('3' in your_luso_grid_analysis.iloc[0:, 1].values) and ('8' in your_luso_grid_analysis.iloc[0:, 1].values):
        vision_plane = '1. Strong thought process \n 2. Very good in brain related work \n 3. May gets airborn desease very easily \n 4. Good in practical planning of any work'
    elif ('4' in your_luso_grid_analysis.iloc[0:, 1].values) and ('3' in your_luso_grid_analysis.iloc[0:, 1].values):
        vision_plane = '1. Not very good for fame and art related work but give good results in technical fields \n 2. Person wants to be organised but can face irregularities in them \n 3. Intelligent person'
    elif ('3' in your_luso_grid_analysis.iloc[0:, 1].values) and ('8' in your_luso_grid_analysis.iloc[0:, 1].values):
        vision_plane = '1. Good for realestate and medical fields \n 2. Love to learn new things'
    elif ('4' in your_luso_grid_analysis.iloc[0:, 1].values) and ('8' in your_luso_grid_analysis.iloc[0:, 1].values):
        vision_plane = '1. Straight forward nature \n 2. Small friend circle \n 3. May take enemies with his tongue \n 4. Delayed success but not denied \n 5.Life can change 180 degrees if he/she continues to work hard'
    elif ('4' in your_luso_grid_analysis.iloc[0:, 1].values):
        vision_plane = '1. Flexible in nature \n 2. Intelligent person \n 3. No grey area in life \n 4. Does not like manupulative people \n 5. Hardworking but may face struggling in early life'
    elif ('3' in your_luso_grid_analysis.iloc[0:, 1].values):
        vision_plane = '1. Knowledge \n 2. Lezy \n 3. Quick Learner'
    elif ('8' in your_luso_grid_analysis.iloc[0:, 1].values):
        vision_plane = '1. Good money manager \n 2. Always speaks the truth and hates lier too much \n 3. Justice lover'
    else:
        vision_plane = 'vision plane is missing. A person may suggest something to others but people tend to overlook him'


    if ('9' in your_luso_grid_analysis.iloc[0:, 2].values) and ('5' in your_luso_grid_analysis.iloc[0:, 2].values) and ('1' in your_luso_grid_analysis.iloc[0:, 2].values):
        will_plane = 'It is 3rd Raj jog \n 1. Immense will power \n 2. May face difficulties in settling down till the age of 28 but after that they earn very well \n 3. Usually settles in 32 years \n 4. Many successful people have this number \n 5. Dominating personality \n 6. Fight back attitude'
    elif ('9' in your_luso_grid_analysis.iloc[0:, 2].values) and ('1' in your_luso_grid_analysis.iloc[0:, 2].values):
        will_plane = '1. Commanding nature \n 2. Leadership qualities \n 3. Respect is everything \n 4. May go for higher education.'
    elif ('9' in your_luso_grid_analysis.iloc[0:, 2].values) and ('5' in your_luso_grid_analysis.iloc[0:, 2].values):
        will_plane = '1. Kind hearted person \n 2. Strong will power \n 3. Manupulaters to get his work done. \n 4. Strong communication skills.'
    elif ('5' in your_luso_grid_analysis.iloc[0:, 2].values) and ('1' in your_luso_grid_analysis.iloc[0:, 2].values):
        will_plane = '1. Sharp minded person \n 2. Good business sense \n 3. good with father/ son but possibly one person shines at a time'
    elif ('9' in your_luso_grid_analysis.iloc[0:, 2].values):
        will_plane = '1. Religious Person \n 2. Artistic and short tempered \n 3. Donation lover \n 4. Thinks from the heart \n 5. Work for sociaty'
    elif ('5' in your_luso_grid_analysis.iloc[0:, 2].values):
        will_plane = '1. Multiple experience in life \n 2. Enjoy life at fullest'
    elif ('1' in your_luso_grid_analysis.iloc[0:, 2].values):
        will_plane = '1. Good in communication \n 2. Good memory and grasping power, \n3. if one time: good in communication but bad in expression, \nif 2 times: good in communication and good in expression, \nif 3 times: 80% people very talkative and 20% people very introvert, \nif 4 times: when you speak creates some trouble'
    else:
        will_plane = 'Will plane is missing. a person can lose hope in life easily. One or two failures can break his motivation for a long time.'


    if ('2' in your_luso_grid_analysis.iloc[0:, 3].values) and ('7' in your_luso_grid_analysis.iloc[0:, 3].values) and ('6' in your_luso_grid_analysis.iloc[0:, 3].values):
        action_plane = '1. Action takers (doers) \n 2. Quick decision maker \n 3. Good in sports \n 4. Opportunity grabber \n 5. If mental plane is missing he can not make decisions without proper thinking'
    elif ('2' in your_luso_grid_analysis.iloc[0:, 3].values) and ('7' in your_luso_grid_analysis.iloc[0:, 3].values):
        action_plane ='1. Caring nature \n 2. Spiritually inclined \n 3. Highly intitive \n 4. Sensitive \n 5. Good in occult scince \n 6. Money is not their priyority.'
    elif ('2' in your_luso_grid_analysis.iloc[0:, 3].values) and ('6' in your_luso_grid_analysis.iloc[0:, 3].values):
        action_plane ='1. Good looking \n 2. Caring nature \n 3. Art lover \n 4. Prone to water related diseases \n 5. Loves family too much (may become a hurdle in growth)'
    elif ('7' in your_luso_grid_analysis.iloc[0:, 3].values) and ('6' in your_luso_grid_analysis.iloc[0:, 3].values):
        action_plane ='1. Metal elements traits will be there \n 2. Attraction towards the opposite sex \n 3. Indulge in more than one love relationship \n 4. Chances of an extra marital affairs \n 5. Discipline'
    elif ('2' in your_luso_grid_analysis.iloc[0:, 2].values):
        action_plane ='1. Religious Person \n 2. Artistic and short tempered \n 3. Donation lover \n 4. Thinks from the heart \n 5. Work for sociaty'
    elif ('7' in your_luso_grid_analysis.iloc[0:, 2].values):
        action_plane ='1. Multiple experience in life \n 2. Enjoy life at fullest'
    elif ('6' in your_luso_grid_analysis.iloc[0:, 2].values):
        action_plane ='1. Good in communication \n 2. Good memory and grasping power, 3. if one time: good in communication but bad in expression, if 2 times: good in communication and good in expression, if 3 times: 80% people very talkative and 20% people very introvert, if 4 times: when you speak creates some trouble'
    else:
        action_plane ='Action plane is missing. Person may be lazy and have weak decision making power'


    if ('4' == your_luso_grid_analysis.iloc[0, 1]) and ('5' == your_luso_grid_analysis.iloc[1, 2]) and ('6' == your_luso_grid_analysis.iloc[2, 3]):
        raj_jog = 'You are have Golden Raj jog. 1. You will find all kinf of support very easily from friends and family \n 2. Everything will ve very easy for you. You get everything very easily'
    elif ('8' == your_luso_grid_analysis.iloc[2, 1]) and ('5' == your_luso_grid_analysis.iloc[1, 2]) and ('6' == your_luso_grid_analysis.iloc[0, 3]):
        raj_jog = 'You are have Silver Raj jog. 1. Any property related work best. You will have properties \n 2. Agreculture \n 3. Construction work is best for you.'
    else:
        raj_jog = ''

    analysis_report =  'Raj Jog:\n'+raj_jog+'\n\nMind Plane:\n'+mind_plane+'\n'+'\nHeart Plane:\n'+heart_plane+'\n'+'\nPractical Plane:\n'+practical_plane+'\n'+'\nVision Plane:\n'+vision_plane+'\n'+'\nWill Plane:\n'+will_plane+'\n'+'\nAction Plane:\n'+action_plane
    
    # st.write(gemini_response(analysis_report))
    st.write(analysis_report)

    # Creating a dictionary with sample data
    data = {
        'sn': [1, 2, 3, 4, 5, 6, 7, 8, 9],
        'role': ['king', 'queen', 'teacher (good)', 'mysterious (rahu)', 'prince','teacher (bad)','saint','judge','commander'],
        'friends': [[1,2,3,5,6,9],[1,2,3,5],[1,2,3,5,7],[1,5,7,6,4,8],[1,2,3,5,6],[1,5,6,7],[1,3,5,4,6],[5,3,6,7,4,8],[1,3,5]],
        'enemy':[[8],[8,4,9],[6],[2,9,4,8],[],[3],[],[1,2,4,8],[4,2]],
        'neutral':[[4,7],[7,6],[4,8,7,9],[3],[4,7,8,9],[2,4,8,9],[8,2,7,9],[9],[9,7,6,8]]
    }

    # Creating a DataFrame from the dictionary
    df = pd.DataFrame(data)

    # Displaying the DataFrame
    st.write(df)


    # Kua Number

    def kua_number(year, gender):
        if gender == 'Male':
            kua_number = 11 - total_sum(year)
            if kua_number == 5:
                kua_number = kua_number - 3
        else:
            kua_number = 4 + total_sum(year)
            if kua_number == 5:
                kua_number = kua_number + 3
        
        kua_number = total_sum(kua_number)
        return kua_number


    # Display Kua number
    kua_number_ = kua_number(year,gender)
    st.write(f"Kua Number: {kua_number_}")

    # Lucky Number 

    def lucky_number(m,v):

        all_numbers = [1,2,3,4,5,6,7,8,9]

        df.set_index('sn', inplace=True)
        values_to_remove_mulank = df.loc[m,'enemy']+df.loc[m,'neutral']
        values_to_remove_bhagyank = df.loc[v,'enemy']+df.loc[v,'neutral']
        values_to_remove = values_to_remove_mulank+values_to_remove_bhagyank
        filtered_list = [num for num in all_numbers if num not in values_to_remove]
        return filtered_list

    lucky_number_ = ', '.join([str(num) for num in lucky_number(mulank,bhagyank)])
    st.write("Lucky Numbers:",lucky_number_)


    # Creating a dictionary for mulank 1
    data = {
        'mulank': [1, 1, 1, 1, 1, 1, 1, 1, 1],
        'bhagyank': [1, 2, 3, 4, 5, 6, 7, 8, 9],
        'luck': [1, 0.8, 0.7, 0.7, 0.8, 0.75, 0.6, 0, 1],
        'remark': ['Administrative, Leadership','Any liquid related work','occult teaching or any education','Politics or share market','Finance or business related','Luxury or glamorous, It, finance','occult or teaching or meditation','delay success and hardwork','super successful and need to be fit ']
    }

    # Creating a DataFrame from the dictionary
    df_1 = pd.DataFrame(data)

    # Displaying the DataFrame
    st.write(df_1)

    # Creating a dictionary for mulank 2
    data = {
        'mulank': [2, 2, 2, 2, 2, 2, 2, 2, 2],
        'bhagyank': [1, 2, 3, 4, 5, 6, 7, 8, 9],
        'luck': [.9, 0.4, 0.5, 0.2, 0.6, 0.45, 0.45, 0, 0.2],
        'remark': ['Good at any job but partner required','low pressure, confuse, emotional, sensitive','Any healer related job like occult, spa, salon, crystal etc.','Struggle and depression','Finance, banking, property related','Creativity, Imagination, luxury','occult, consultant, confuse, curiosity','Married life problem, curiosity','marriage problem or job problem']
    }

    # Creating a DataFrame from the dictionary
    df_2 = pd.DataFrame(data)

    # Displaying the DataFrame
    st.write(df_2)

    # Creating a dictionary for mulank 3
    data = {
        'mulank': [3, 3, 3, 3, 3, 3, 3, 3, 3],
        'bhagyank': [1, 2, 3, 4, 5, 6, 7, 8, 9],
        'luck': [.7, 0.45, 0.6, 0.4, 0.6, 0, 0.8, 0.4, 0.8],
        'remark': ['Education, teaching, it, coder','liquid related work', 'Education, they have child like energy','Will be successful in a foreign land','Business of anything, edutech','Struggle, disappointment till age 25','Healing industry','Media, lawyer, printing','IT, Entertainment, Administrative']
    }

    # Creating a DataFrame from the dictionary
    df_3 = pd.DataFrame(data)

    # Displaying the DataFrame
    st.write(df_3)

    # Creating a dictionary for mulank 3
    data = {
        'mulank': [4, 4, 4, 4, 4, 4, 4, 4, 4],
        'bhagyank': [1, 2, 3, 4, 5, 6, 7, 8, 9],
        'luck': [.7, 0.4, 0.5, 0.3, 0.6, 0.6, 0.8, 0.2, 0.2],
        'remark': ['Speaker or leadership','Struggle, depression, reasoning', 'Sales, marketing, education eincrease','Lawer, low struggle','Revolutionary business but need solid team','Media, luxury related business','Successful in property related','Struggle','Accident, legal, low immune system']
    }

    # Creating a DataFrame from the dictionary
    df_4 = pd.DataFrame(data)

    # Displaying the DataFrame
    st.write(df_4)

    # Creating a dictionary for mulank 3
    data = {
        'mulank': [5, 5, 5, 5, 5, 5, 5, 5, 5],
        'bhagyank': [1, 2, 3, 4, 5, 6, 7, 8, 9],
        'luck': [.8, 0.7, 0.6, 0.4, 0.8, 0.9, 0.6, 0.6, 0.6],
        'remark': ['Successful property related','property related, emotional', 'communication related business or work','Sales and marketing head','Business risk taker, management','Travelling, investment','Finance, banking, insurance','After child birth property','Successful dealer, defence leated any work']
    }

    # Creating a DataFrame from the dictionary
    df_5 = pd.DataFrame(data)

    # Displaying the DataFrame
    st.write(df_5)

    # Creating a dictionary for mulank 3
    data = {
        'mulank': [6, 6, 6, 6, 6, 6, 6, 6, 6],
        'bhagyank': [1, 2, 3, 4, 5, 6, 7, 8, 9],
        'luck': [0.7, 0.4, 0, 0.6, 0.9, 0.8, 0.7, 0.6, 0.6],
        'remark': ['Luxury, administration, technical','sweet related work', 'Struggle in initial life','Media, caretaker, technical, jewellery','Travelling','Super successful, luxury','Sports, romantic nature','Best for low related, defence work','Scandals, controvertial, marriage related problem']
    }

    # Creating a DataFrame from the dictionary
    df_6 = pd.DataFrame(data)

    # Displaying the DataFrame
    st.write(df_6)

    # Creating a dictionary for mulank 3
    data = {
        'mulank': [7, 7, 7, 7, 7, 7, 7, 7, 7],
        'bhagyank': [1, 2, 3, 4, 5, 6, 7, 8, 9],
        'luck': [0.6, 0.4, 0.6, 0.6, 0.6, 0.8, 0.2, 0.2, 0.8],
        'remark': ['Best in occult, healer','Intuitive', 'Healing and Teaching','Successful','Business Healing','Sports','Marriage problem, disappointment','Occult','Teaching']
    }

    # Creating a DataFrame from the dictionary
    df_7 = pd.DataFrame(data)

    # Displaying the DataFrame
    st.write(df_7)

    # Creating a dictionary for mulank 3
    data = {
        'mulank': [8, 8, 8, 8, 8, 8, 8, 8, 8],
        'bhagyank': [1, 2, 3, 4, 5, 6, 7, 8, 9],
        'luck': [0, 0, 0.4, 0.2, 0.6, 0.6, 0.4, 0.2, 0.2],
        'remark': ['Slander, badnam, struggle but better in tech related industry','Health issue struggle', 'Law, printing business, electronic is good','Struggle need name correction','Realestate','Best law related','Confusion, struggle but success after 32 age','marriage and career problem','Defence army successful']
    }

    # Creating a DataFrame from the dictionary
    df_8 = pd.DataFrame(data)

    # Displaying the DataFrame
    st.write(df_8)

    # Creating a dictionary for mulank 3
    data = {
        'mulank': [9, 9, 9, 9, 9, 9, 9, 9, 9],
        'bhagyank': [1, 2, 3, 4, 5, 6, 7, 8, 9],
        'luck': [0.8, 0.2, 0.5, 0.3, 0.6, 0.4, 0.2, 0.4, 0.2],
        'remark': ['Successful need to be fit','struggle in marriage', 'Education, teaching','Health Issue, legal, bad friend issue','Successful in business, import export','Controvertial sexual, girl related','online Related work, intuition','Police, defence and army','Marriage problem, anger issue']
    }

    # Creating a DataFrame from the dictionary
    df_9 = pd.DataFrame(data)

    # Displaying the DataFrame
    st.write(df_9)


with tab2:
    st.title("Put DOB of you and your partner")

    # Define the minimum and maximum dates for the date picker
    min_date = datetime(1900, 1, 1)  # Minimum date (e.g., January 1, 1900)
    max_date = datetime(2100, 12, 31)  # Maximum date (e.g., December 31, 2100)

    # Create a date input widget with the specified date range
    first_person_date = st.date_input("Select first person date", value=datetime.today(), min_value=min_date, max_value=max_date)
    second_person_date = st.date_input("Select second person date", value=datetime.today(), min_value=min_date, max_value=max_date)


    # Save the selected date in a variable
    # date_variable = selected_date

    # gender = st.selectbox("Select your gender:", ["Male", "Female"])

    # Display the selected date
    st.write(f"First person selected date is: {first_person_date}")
    st.write(f"Second person selected date is: {second_person_date}")
    # st.write(type(date_variable))

    # Optionally, convert it to a string or another format if needed
    # date_string = date_variable.strftime("%d-%m-%Y")
    # st.write(f"Formatted date: {date_string}")

    # First person Luso grid
    # Extracting the date value for further use
    day = first_person_date.day
    month = first_person_date.month
    year = first_person_date.year

    mulank = sum(int(digit) for digit in str(day))
    month_sum = sum(int(digit) for digit in str(month))
    year_sum = sum(int(digit) for digit in str(year))
    date_month_year = mulank+month_sum+year_sum


    def total_sum(value):
        while len(str(value))>1:
            value = sum(int(digit) for digit in str(value))
        return value
    
    mulank = total_sum(mulank)
    bhagyank = total_sum(date_month_year)

    # Display the extracted day, month, and year
    st.write(f"Mulank: {mulank}, Bhagyank: {bhagyank}")

    # Compatibility of numbers:
    import pandas as pd



    # Standard luso grid
    std_grid = {
        'Lu So Grid':['Mental Plane','Heart Plane','Practical Plane'],
        'Vision Plane':[4,3,8],
        'Will Plane':[9,5,1],
        'Action Plane':[2,7,6]
    }

    # Creating a DataFrame from the dictionary
    luso_grid = pd.DataFrame(std_grid)

    # Displaying the DataFrame
    # st.write(luso_grid)


    ######### Creating your luso grid ##########
    your_luso_grid = luso_grid.copy()
    your_luso_grid.iloc[:, 1:] = ''

    your_luso_grid_analysis = luso_grid.copy()
    your_luso_grid_analysis.iloc[:, 1:] = ''

    # adding day value
    for i in str(day):

        if i == '0':
            pass
        else:
            # Check if i is present and get its index
            index_of = luso_grid.isin([int(i)])
            # If you want to get the exact row and column index where i is located
            index_positions = index_of.stack().loc[lambda x: x].index.tolist()
            value = your_luso_grid.loc[index_positions[0][0], index_positions[0][1]]

            your_luso_grid.loc[index_positions[0][0], index_positions[0][1]] = str(value)+i
            your_luso_grid_analysis.loc[index_positions[0][0], index_positions[0][1]] = i

    # adding month value
    for i in str(month):

        if i == '0':
            pass
        else:
            # Check if i is present and get its index
            index_of = luso_grid.isin([int(i)])
            # If you want to get the exact row and column index where i is located
            index_positions = index_of.stack().loc[lambda x: x].index.tolist()
            value = your_luso_grid.loc[index_positions[0][0], index_positions[0][1]]

            your_luso_grid.loc[index_positions[0][0], index_positions[0][1]] = str(value)+i
            your_luso_grid_analysis.loc[index_positions[0][0], index_positions[0][1]] = i

    # adding year value
    for i in str(year):

        if i == '0':
            pass
        else:
            # Check if i is present and get its index
            index_of = luso_grid.isin([int(i)])
            # If you want to get the exact row and column index where i is located
            index_positions = index_of.stack().loc[lambda x: x].index.tolist()
            value = your_luso_grid.loc[index_positions[0][0], index_positions[0][1]]

            your_luso_grid.loc[index_positions[0][0], index_positions[0][1]] = str(value)+i
            your_luso_grid_analysis.loc[index_positions[0][0], index_positions[0][1]] = i

    # mulank 
    if len(str(day))==1 or str(day)=='10' or str(day)=='20' or str(day)=='30':
        pass
    else:
        index_of = luso_grid.isin([int(mulank)])
        # If you want to get the exact row and column index where i is located
        index_positions = index_of.stack().loc[lambda x: x].index.tolist()
        value = your_luso_grid.loc[index_positions[0][0], index_positions[0][1]]

        your_luso_grid.loc[index_positions[0][0], index_positions[0][1]] = str(value)+str(mulank)
        your_luso_grid_analysis.loc[index_positions[0][0], index_positions[0][1]] = str(mulank)

    # bhagyank

    index_of = luso_grid.isin([int(bhagyank)])
    # If you want to get the exact row and column index where i is located
    index_positions = index_of.stack().loc[lambda x: x].index.tolist()
    value = your_luso_grid.loc[index_positions[0][0], index_positions[0][1]]

    your_luso_grid.loc[index_positions[0][0], index_positions[0][1]] = str(value)+str(bhagyank)
    your_luso_grid_analysis.loc[index_positions[0][0], index_positions[0][1]] = str(bhagyank)

    frst_your_luso_grid = your_luso_grid
    frst_your_luso_grid_analysis = your_luso_grid_analysis
    # st.write(frst_your_luso_grid)
    st.write(frst_your_luso_grid_analysis)




    ####################################### Second person Luso grid ################################
    # Extracting the date value for further use
    day = second_person_date.day
    month = second_person_date.month
    year = second_person_date.year

    mulank = sum(int(digit) for digit in str(day))
    month_sum = sum(int(digit) for digit in str(month))
    year_sum = sum(int(digit) for digit in str(year))
    date_month_year = mulank+month_sum+year_sum


    def total_sum(value):
        while len(str(value))>1:
            value = sum(int(digit) for digit in str(value))
        return value
    
    mulank = total_sum(mulank)
    bhagyank = total_sum(date_month_year)

    # Display the extracted day, month, and year
    st.write(f"Mulank: {mulank}, Bhagyank: {bhagyank}")

    # Compatibility of numbers:
    import pandas as pd



    # Standard luso grid
    std_grid = {
        'Lu So Grid':['Mental Plane','Heart Plane','Practical Plane'],
        'Vision Plane':[4,3,8],
        'Will Plane':[9,5,1],
        'Action Plane':[2,7,6]
    }

    # Creating a DataFrame from the dictionary
    luso_grid = pd.DataFrame(std_grid)

    # Displaying the DataFrame
    # st.write(luso_grid)


    ######### Creating your luso grid ##########
    your_luso_grid = luso_grid.copy()
    your_luso_grid.iloc[:, 1:] = ''

    your_luso_grid_analysis = luso_grid.copy()
    your_luso_grid_analysis.iloc[:, 1:] = ''

    # adding day value
    for i in str(day):

        if i == '0':
            pass
        else:
            # Check if i is present and get its index
            index_of = luso_grid.isin([int(i)])
            # If you want to get the exact row and column index where i is located
            index_positions = index_of.stack().loc[lambda x: x].index.tolist()
            value = your_luso_grid.loc[index_positions[0][0], index_positions[0][1]]

            your_luso_grid.loc[index_positions[0][0], index_positions[0][1]] = str(value)+i
            your_luso_grid_analysis.loc[index_positions[0][0], index_positions[0][1]] = i

    # adding month value
    for i in str(month):

        if i == '0':
            pass
        else:
            # Check if i is present and get its index
            index_of = luso_grid.isin([int(i)])
            # If you want to get the exact row and column index where i is located
            index_positions = index_of.stack().loc[lambda x: x].index.tolist()
            value = your_luso_grid.loc[index_positions[0][0], index_positions[0][1]]

            your_luso_grid.loc[index_positions[0][0], index_positions[0][1]] = str(value)+i
            your_luso_grid_analysis.loc[index_positions[0][0], index_positions[0][1]] = i

    # adding year value
    for i in str(year):

        if i == '0':
            pass
        else:
            # Check if i is present and get its index
            index_of = luso_grid.isin([int(i)])
            # If you want to get the exact row and column index where i is located
            index_positions = index_of.stack().loc[lambda x: x].index.tolist()
            value = your_luso_grid.loc[index_positions[0][0], index_positions[0][1]]

            your_luso_grid.loc[index_positions[0][0], index_positions[0][1]] = str(value)+i
            your_luso_grid_analysis.loc[index_positions[0][0], index_positions[0][1]] = i

    # mulank 
    if len(str(day))==1 or str(day)=='10' or str(day)=='20' or str(day)=='30':
        pass
    else:
        index_of = luso_grid.isin([int(mulank)])
        # If you want to get the exact row and column index where i is located
        index_positions = index_of.stack().loc[lambda x: x].index.tolist()
        value = your_luso_grid.loc[index_positions[0][0], index_positions[0][1]]

        your_luso_grid.loc[index_positions[0][0], index_positions[0][1]] = str(value)+str(mulank)
        your_luso_grid_analysis.loc[index_positions[0][0], index_positions[0][1]] = str(mulank)

    # bhagyank

    index_of = luso_grid.isin([int(bhagyank)])
    # If you want to get the exact row and column index where i is located
    index_positions = index_of.stack().loc[lambda x: x].index.tolist()
    value = your_luso_grid.loc[index_positions[0][0], index_positions[0][1]]

    your_luso_grid.loc[index_positions[0][0], index_positions[0][1]] = str(value)+str(bhagyank)
    your_luso_grid_analysis.loc[index_positions[0][0], index_positions[0][1]] = str(bhagyank)

    snd_your_luso_grid = your_luso_grid
    snd_your_luso_grid_analysis = your_luso_grid_analysis
    # st.write(snd_your_luso_grid)
    st.write(snd_your_luso_grid_analysis)




    result = frst_your_luso_grid_analysis + snd_your_luso_grid_analysis
    st.write(result)


with tab3:

    def df_selection(m):
        if m == 1:
            return df_1
        elif m == 2:
            return df_2
        elif m == 3:
            return df_3
        elif m == 4:
            return df_4
        elif m == 5:
            return df_5
        elif m == 6:
            return df_6
        elif m == 7:
            return df_7
        elif m == 8:
            return df_8
        else:
            return df_9

    
    def create_pdf(text):
    # Create a PDF in memory
        buffer = BytesIO()
        doc = SimpleDocTemplate(buffer, pagesize=letter)

        # Define a basic style for the text
        styles = getSampleStyleSheet()
        style = styles["Normal"]  # Use the "Normal" paragraph style
        style.wordWrap = "LTR"

        # Split the input text into paragraphs based on line breaks
        paragraphs = [Paragraph(p, style) for p in text.split("\n") if p.strip()]

        # Build the PDF
        doc.build(paragraphs)
        buffer.seek(0)  # Reset buffer pointer to the beginning
        return buffer

    df_ = df_selection(mulank_)
    # st.write(df_)
    
    st.write(f'''             Lucky Numbers: {lucky_number_}
\nMulank: {mulank_}
\nBhagyank: {bhagyank_}
\nLuck: {round(df_[df_.iloc[:,1]==bhagyank_]['luck'].values[0]*100)}%
\nKua Number: {kua_number_}
\nOne Liner: {df_[df_.iloc[:,1]==bhagyank_]['remark'].values[0]}
\n{analysis_report}''')

    user_input = (f'''             Lucky Numbers: {lucky_number_}
\nMulank: {mulank_}
\nBhagyank: {bhagyank_}
\nLuck: {round(df_[df_.iloc[:,1]==bhagyank_]['luck'].values[0]*100)}%
\nKua Number: {kua_number_}
\nOne Liner: {df_[df_.iloc[:,1]==bhagyank_]['remark'].values[0]}
\n{analysis_report}''')


    if st.button("Generate PDF"):
        if user_input:
            pdf_file = create_pdf(user_input)
            st.success("PDF generated successfully!")
            st.text(pdf_file)

            # Provide a download link
            st.download_button(
                label="Download PDF",
                data=pdf_file,
                file_name="generated_text.pdf",
                mime="application/pdf",
            )
        else:
            st.error("Please enter some text before generating the PDF.")