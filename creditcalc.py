import argparse
import math


def incorrect_parameters():
    print("Incorrect Parameters.")
    return 1


parser = argparse.ArgumentParser(description="Loan calculator")

parser.add_argument("--type", choices=["annuity", "diff"], help="Choose whether you want to calculate \
                    annuity or differentiated payments. You must choose one of the options")
parser.add_argument("--payment", help="Monthly payment")
parser.add_argument("--principal", help="The loan principal amount")
parser.add_argument("--periods", help="Number of months needed to repay loan")
parser.add_argument(
    "--interest", help="Annual interest rate without a percent sign")

args = parser.parse_args()
parameters = [args.type, args.payment,
              args.principal, args. periods, args.interest]
n = 0
flag = 0

for parameter in parameters:
    if parameter is None:
        n += 1
if n > 1:
    flag = incorrect_parameters()
if args.payment:
    monthly_payment = float(args.payment)
    if monthly_payment < 0:
        if flag == 0:
            flag = incorrect_parameters()
if args.principal:
    loan_principal = int(args.principal)
    if loan_principal < 0:
        if flag == 0:
            flag = incorrect_parameters()
if args.periods:
    number_of_periods = int(args.periods)
    if number_of_periods < 0:
        if flag == 0:
            flag = incorrect_parameters()
if args.interest:
    i = float(args.interest) / 1200
    if i < 0:
        if flag == 0:
            flag = incorrect_parameters()
else:
    if flag == 0:
        flag = incorrect_parameters()

if flag == 0:
    over_payment = 0
    if args.type == "diff":
        for month in range(number_of_periods):
            diff_payment = math.ceil(loan_principal / number_of_periods + i
                                     * (loan_principal - loan_principal * month / number_of_periods))
            over_payment += diff_payment
            print(f"Month {month + 1}: payment is {diff_payment}")
        print(f"\nOverpayment = {int(over_payment - loan_principal)}")

    if args.type == "annuity":
        if args.periods is None:
            number_of_periods = math.ceil(
                math.log((monthly_payment / (monthly_payment - i * loan_principal)), 1 + i))
            if number_of_periods % 12 == 0:
                if number_of_periods // 12 == 1:
                    print("It will take 1 year to repay this loan!")
                else:
                    print(
                        f"It will take {number_of_periods // 12} years to repay this loan!")
            elif number_of_periods / 12 < 1:
                print(
                    f"It will take {number_of_periods % 12} months to repay this loan!")
            else:
                print(f"It will take {int(number_of_periods // 12)} years and "
                      f"{number_of_periods % 12} months to repay this loan!")
            print(
                f"Overpayment = {int(monthly_payment * number_of_periods - loan_principal)}")

        if args.payment is None:
            monthly_payment = math.ceil(loan_principal * i * pow(1 + i, number_of_periods)
                                        / (pow(1 + i, number_of_periods) - 1))
            print(f"Your annuity payment = {monthly_payment}!")
            print(
                f"Overpayment = {int(monthly_payment * number_of_periods - loan_principal)}")

        if args.principal is None:
            loan_principal = math.floor(monthly_payment
                                        / ((i * pow(1 + i, number_of_periods)) / (pow(1 + i, number_of_periods) - 1)))
            print(f"Your loan principal = {loan_principal}!")
            print(
                f"Overpayment = {int(monthly_payment * number_of_periods - loan_principal)}")
