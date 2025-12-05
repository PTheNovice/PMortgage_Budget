"""
Mortgage Calculation =>> M = P[ (r * (1 + r) ^ n) / ((r * (1 + r) ^ n) - 1)] where r = monthly interest
rate, n = total lifetime payments, P = principal and M = mortgage amount

Next Steps to improve:
    Consolidate all Monthly payments into 1 function that returns multiple items - DONE
    Show the direct Principal and Interest
    Include Different Mortgage Term types
    Include Monthly, Yearly and Total Payments as well.
    Create function when receiving percentage for down_payment, property_taxes, pmi, 

"""

import pandas
import numpy
import matplotlib


class Mortgage:

    def __init__(self, principal, down_payment, interest_rate, property_taxes, pmi, insurance, hoa, loan_years, mortgage_frequency=12):
        """
        Init Mortgage Variables
        :param principal: Principal Loan Amount, float
        :param down_payment: Amount subtracted from the Principal, float
        :param interest_rate: Annual Interest Rate, float
        :param property_taxes: Annual Property Taxes, float
        :param pmi: Annual Premium Mortgage Insurance (usually included when down payment is less than 20%), float
        :param insurance: Annual Homeowners Insurance, float
        :param hoa: Homeowners Association fees, float
        :param loan_years: The total number of loan years, int
        :param mortgage_frequency: Only offering 2 payment options: monthly or bi-weekly payments, int
        """
        self.principal = principal
        self.down_payment = down_payment
        self.interest_rate = interest_rate
        self.property_taxes = property_taxes
        self.pmi = pmi
        self.insurance = insurance
        self.hoa = hoa
        self.loan_years = loan_years
        self.mortgage_frequency = mortgage_frequency

    def mortgage_calculation(self, ):
        """
        Calculation of the Property Mortgage
        :return: The Mortgage value
        """
        monthly_interest_rate_value = self.monthly_rate(self.interest_rate / 100, self.mortgage_frequency)
        n = self.total_num_of_payments(self.loan_years, self.mortgage_frequency)
        freq = ((1 + monthly_interest_rate_value) ** n)

        base_mortgage = (self.principal - self.down_payment) * ((monthly_interest_rate_value * freq) / (freq - 1))

        taxes = self.monthly_rate(self.property_taxes, self.mortgage_frequency)
        insurance = self.monthly_rate(self.insurance, self.mortgage_frequency)
        pmi = self.monthly_rate(self.pmi, self.mortgage_frequency)
        hoa = self.monthly_hoa(self.hoa, self.mortgage_frequency)

        mortgage = base_mortgage + taxes + insurance + pmi + hoa
        return mortgage

    def monthly_rate(self, rate: float, mortgage_frequency: int):
        """
        Used to deduce monthly rates
        :param rate:
        :param mortgage_frequency:
        :return: The Monthly interest rate
        """
        if mortgage_frequency == 24:
            return rate / 24
        else:
            return rate / 12

    def monthly_hoa(self, hoa, mortgage_frequency: int):
        """
        Monthly Premium Insurance
        :param hoa:
        :param mortgage_frequency:
        :return:
        """
        if mortgage_frequency == 24:
            return hoa / 2
        else:
            return hoa / 1

    def total_num_of_payments(self, loan_years, mortgage_frequency: int):
        """
        Total Number of Payments
        :param loan_years:
        :param mortgage_frequency:
        :return:
        """
        if mortgage_frequency == 24:
            return loan_years * 24
        else:
            return loan_years * 12


if __name__ == "__main__":
    mortgage = Mortgage(200000, 20000, 3.5, 4500, 1200, 2500, 0, 30)
    print(f' {mortgage.mortgage_calculation():.2f}')  # Works well!

    # P = float(input("What is your Principal?"))
    # D = float(input("What is your Down Payment (Dollar Amount)?"))  # need to update for percent or dollar amount
    # IR = float(input("What is your Annual Interest Rate(%)?"))
    # T = float(input("What are your Annual Property Taxes?"))
    # PMI = float(input("What is your Annual PMI?"))
    # I = float(input("What is your Annual Homeowners Insurance?"))
    # H = int(input("What is your monthly Homeowners Association Fee?"))
    # L = int(input("What is your total Loan Years?"))
    # F = int(input("What is your Mortgage Freq (Monthly[12] or Bi-Weekly[24])?")) # Re-word in terms of yearly payments
    # mortgage = Mortgage(P, D, IR, T, PMI, I, H, L, F)
    # print(f' {mortgage.mortgage_calculation():.2f}')  # Works well!
