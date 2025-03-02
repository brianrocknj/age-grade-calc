import pandas as pd
import utils

standards = pd.read_csv('data/age-standards.csv')
factors = pd.read_csv('data/age-factors.csv')
percentiles = pd.read_csv('data/percentiles-2024.csv')

### Accepts a time in seconds or HH:MM:SS and returns the age graded time
### Defaults to 2025 age factors, but can specify 2010, 2015, 2020, or 2025
def getAgeGradedTime(time, gender, age, year='2025', format='string'):
    if isinstance(time, str):
        time = utils.timeToSeconds(time)

    if gender.upper() in ['M', 'MEN', 'MAN', 'MALE']:
        gender = 'Men'
    elif gender.upper() in ['W', 'F', 'WOMEN', 'WOMAN', 'FEMALE']:
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

    if gender.upper() in ['M', 'MEN', 'MAN', 'MALE']:
        gender = 'Men'
    elif gender.upper() in ['W', 'F', 'WOMEN', 'WOMAN', 'FEMALE']:
        gender = 'Women'

    if age < 20:
        age = 20
    elif age > 79:
        age = 79
    
    time = getAgeGradedTime(time, gender, age, year, format='time')
    standard = standards.loc[standards['Gender'] == gender].iloc[0][year]

    ageGrade = (standard / time) * 100
    return round(ageGrade, 1)

def getPercentile(time, gender, age, year='2025'):
    if isinstance(time, str):
        time = utils.timeToSeconds(time)

    if gender.upper() in ['M', 'MEN', 'MAN', 'MALE']:
        gender = 'Men'
    elif gender.upper() in ['W', 'F', 'WOMEN', 'WOMAN', 'FEMALE']:
        gender = 'Women'

    age = int(age)
    if age < 20:
        age = 20
    elif age > 79:
        age = 79

    ageGroup = utils.getAgeGroup(age)

    perc = percentiles[(percentiles['Gender'] == gender) & (percentiles[ageGroup] > time)]['Percentile'].max()
    return perc

