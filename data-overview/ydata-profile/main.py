import pandas as pd
from ydata_profiling import ProfileReport

df = pd.read_excel('G:\Shared drives\Data and Research Team\Ad Hoc Requests\RCMG Test Data\Test File.xlsx',
                   skiprows=5, usecols=lambda x: x not in ['Unnamed: 0'])

profile = ProfileReport(df, config_file="lumata_config.yaml")

profile.to_file("Profile Report.html")

print("Profiling report generated and saved as 'Profiling Report.html'")


print('Hello team!!!')
