import fire
import json
import sys
from util import CashFlow
from util import InvestmentProject


class Main(object):

    def present_value(self, amount, t, i):  # cuando tiene self es objeto
        flow = CashFlow(amount, t)
        print("The present value of cashflow{amount} in time {t} is {pv}.".format(amount=amount, t=t,
                                                                                  pv=flow.present_value(interest_rate=i)))\


    @staticmethod
    def describe_investment(filepath, hurdle_rate=None):
        investment_project = InvestmentProject.from_csv(filepath=filepath, hurdle_rate=hurdle_rate)
        description = investment_project.describe()
        print(json.dumps(description, indent=4))

    @staticmethod
    def plot_investment(filepath, save="", show=False):
        investment_project = InvestmentProject.from_csv(filepath=filepath)  # Inves... es una clase
        fig = investment_project.plot(show=show)
        if save:
            fig.savefig(save)

if __name__ == "__main__":
    fire.Fire(Main)