import pandas as pd
import ageGrade as ag

bq = pd.read_csv('data/bq-standards.csv')
bq = bq[bq['Gender'].isin(['M', 'F'])]
bq['Gender'] = bq['Gender'].replace({'M' : 'Men', 'F' : 'Women'})
bq = bq[~bq['Age Group'].isin(['Under 20', '20-24', '25-29'])]
bq['Age'] = bq['Age Group'].str[:2]
bq['Age'] = bq['Age'].astype(int)

bq['2020BQ'] = bq.apply(lambda x: ag.getAgeGradedTime(x['2020BQ'], x['Gender'], x['Age']), axis=1)
bq['2026BQ'] = bq.apply(lambda x: ag.getAgeGradedTime(x['2026BQ'], x['Gender'], x['Age']), axis=1)
print(bq)
bq.to_csv('output/Age Graded BQ.csv', index=False)
