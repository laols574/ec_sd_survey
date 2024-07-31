import pandas as pd

f = open("prolific_ids.txt")
f = f.readlines()
prolific_ids = [line.strip() for line in f]

qualtrics_results = pd.read_csv("qualtrics_export.csv")
prolific_results = pd.read_csv("prolific_export.csv")

qualtrics_results = qualtrics_results[qualtrics_results['PROLIFIC_PID'].isin(prolific_ids)]
prolific_results = prolific_results[prolific_results['PROLIFIC_PID'].isin(prolific_ids)]

merged_df = pd.merge(qualtrics_results, prolific_results, on='PROLIFIC_PID', how='inner')

merged_df.to_csv("merged_survey_results.csv", index=False)
