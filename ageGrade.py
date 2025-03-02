import pandas as pd
import utils

standards = pd.read_csv('data/age-standards.csv')
factors = pd.read_csv('data/age-factors.csv')

### Accepts a time in seconds or HH:MM:SS and returns the age graded time
### Defaults to 2025 age factors, but can specify 2010, 2015, 2020, or 2025
def getAgeGradedTime(time, gender, age, year='2025', format='string'):
    if isinstance(time, str):
        time = utils.timeToSeconds(time)

    if gender.upper() in ['M', 'MEN']:
        gender = 'Men'
    elif gender.upper() in ['W', 'F', 'WOMEN', 'FEMALE']:
        gender = 'Women'

    if age < 20:
        age = 20
    elif age > 79:
        age = 79
    
    factor = factors.loc[(factors['Gender'] == gender) & (factors['Age'] == age)].iloc[0][year]
    ageGradedTime = time * factor
    return utils.secondsToTime(ageGradedTime) if format == 'string' else int(ageGradedTime)

### Accepts a time in seconds or HH:MM:SS and returns the age grade percentile
### Defaults to 2025 age factors, but can specify 2010, 2015, 2020, or 2025
def getAgeGrade(time, gender, age, year='2025'):
    if isinstance(time, str):
        time = utils.timeToSeconds(time)

    if gender.upper() in ['M', 'MEN']:
        gender = 'Men'
    elif gender.upper() in ['W', 'F', 'WOMEN', 'FEMALE']:
        gender = 'Women'

    if age < 20:
        age = 20
    elif age > 79:
        age = 79
    
    time = getAgeGradedTime(time, gender, age, year, format='time')
    print(utils.secondsToTime(time))
    standard = standards.loc[standards['Gender'] == gender].iloc[0][year]

    ageGrade = (standard / time) * 100
    return ageGrade
