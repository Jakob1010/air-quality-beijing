import pandas as pd
import matplotlib.pyplot as plt


def main():
    df = pd.read_csv("data/credit.csv")
    df.describe()

    # checking status vs class
    df.groupby(['checking_status', 'class'])['checking_status'].count().unstack('class').fillna(0).plot(kind='bar', stacked='true', rot=0)
    plt.savefig("plots/credit/checking_status.png")

    # duration vs class
    df[['duration', 'class']].groupby('class').boxplot()
    plt.savefig("plots/credit/duration.png")

    # credit history vs class
    df.groupby(['credit_history', 'class'])['credit_history'].count().unstack('class').fillna(0).plot(kind='bar', stacked='true', figsize=(12, 6), rot=0)
    plt.savefig("plots/credit/credit_history.png")

    # purpose vs class
    df.groupby(['purpose', 'class'])['purpose'].count().unstack('class').fillna(0).plot(kind='bar', stacked='true', figsize=(15, 5), rot=0)
    plt.savefig("plots/credit/purpose.png")

    # credit amount vs class
    df[['credit_amount', 'class']].groupby('class').boxplot()
    plt.savefig("plots/credit/credit_amount.png")

    # saving status vs class
    df.groupby(['savings_status', 'class'])['savings_status'].count().unstack('class').fillna(0).plot(kind='bar', stacked='true', figsize=(12, 4), rot=0)
    plt.savefig("plots/credit/savings_status.png")

    # employment vs class
    df.groupby(['employment', 'class'])['employment'].count().unstack('class').fillna(0).plot(kind='bar', stacked='true', figsize=(12, 4), rot=0)
    plt.savefig("plots/credit/employment.png")

    # installment commitment vs class
    df[['installment_commitment', 'class']].groupby('class').boxplot()
    plt.savefig("plots/credit/installment_commitment.png")

    # personal status vs class
    df.groupby(['personal_status', 'class'])['personal_status'].count().unstack('class').fillna(0).plot(kind='bar', stacked='true', figsize=(12, 4), rot=0)
    plt.savefig("plots/credit/personal_status.png")

    # other parties vs class
    df.groupby(['other_parties', 'class'])['other_parties'].count().unstack('class').fillna(0).plot(kind='bar', stacked='true', figsize=(12, 4), rot=0)
    plt.savefig("plots/credit/other_parties.png")

    # residence since vs class
    df[['residence_since', 'class']].groupby('class').boxplot()
    plt.savefig("plots/credit/residence_since.png")

    # property magnitude vs class
    df.groupby(['property_magnitude', 'class'])['property_magnitude'].count().unstack('class').fillna(0).plot(kind='bar', stacked='true', figsize=(12, 4), rot=0)
    plt.savefig("plots/credit/property_magnitude.png")

    # age vs class
    df[['age', 'class']].groupby('class').boxplot()
    plt.savefig("plots/credit/age.png")

    # other payment plans vs class
    df.groupby(['other_payment_plans', 'class'])['other_payment_plans'].count().unstack('class').fillna(0).plot(kind='bar', stacked='true', figsize=(12, 4), rot=0)
    plt.savefig("plots/credit/other_payment_plans.png")

    # housing vs class
    df.groupby(['housing', 'class'])['housing'].count().unstack('class').fillna(0).plot(kind='bar', stacked='true', figsize=(12, 4), rot=0)
    plt.savefig("plots/credit/housing.png")

    # existing credits vs class
    df[['existing_credits', 'class']].groupby('class').boxplot()
    plt.savefig("plots/credit/existing_credits.png")

    # job vs class
    df.groupby(['job', 'class'])['job'].count().unstack('class').fillna(0).plot(kind='bar', stacked='true', rot=0)
    plt.savefig("plots/credit/job.png")

    # number of dependents vs class
    df[['num_dependents', 'class']].groupby('class').boxplot()
    plt.savefig("plots/credit/num_dependents.png")

    # own telephone vs class
    df.groupby(['own_telephone', 'class'])['own_telephone'].count().unstack('class').fillna(0).plot(kind='bar', stacked='true', rot=0)
    plt.savefig("plots/credit/own_telephone.png")

    # foreign worker vs class
    df.groupby(['foreign_worker', 'class'])['foreign_worker'].count().unstack('class').fillna(0).plot(kind='bar', stacked='true', rot=0)
    plt.savefig("plots/credit/foreign_worker.png")

    # show all plots
    #plt.show()


if __name__ == '__main__':
    main()
