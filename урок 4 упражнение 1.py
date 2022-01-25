from sys import argv

script_name, produktivity, rate_per_hour, bonus = argv
print("Name of script: ", script_name)
print('Productivity, hours: ', produktivity)
print('Rate_per_hour: ', rate_per_hour)
print('Bonus: ', bonus)

print('Salary: ', int(produktivity) * int(rate_per_hour)) + int(bonus)