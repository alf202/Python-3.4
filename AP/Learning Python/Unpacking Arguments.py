def health_calculator(age, apples_ate, cigs_smoked):
    answer = (100 - age) + (apples_ate * 3.5) - (cigs_smoked * 2)
    print(answer)

alfies_data = [13, 20, 0]

health_calculator(*alfies_data)
