from distributions.gaussian_distribution import Gaussian
from distributions.binomial_distribution import Binomial


def main_gaussian():
    # initialize two gaussian distributions
    gaussian_one = Gaussian(25, 3)
    gaussian_two = Gaussian(30, 4)

    # initialize a third gaussian distribution reading in a data file
    gaussian_three = Gaussian()
    gaussian_three.read_data_file('../numbers')     # calculates the mean and the stdev automatically

    # print out the mean and standard deviations
    print(f"Mean 1: {gaussian_one.mean}")
    print(f"Mean 2: {gaussian_two.mean}")

    print(f"Standard Deviation 1: {gaussian_one.stdev}")
    print(f"Standard Deviation 2: {gaussian_two.stdev}")

    print('-'*25)
    print("Gaussian 3:")
    print(f"Mean: {gaussian_three.mean}")
    print(f"Standard Deviation:{gaussian_three.stdev}")

    # plot histogram of gaussian three
    gaussian_three.plot_histogram()
    gaussian_three.plot_histogram_pdf()
    print(f"Gaussian Three probability density function for x=5: {gaussian_three.pdf(5)}")

    # add gaussian_one and gaussian_two together
    print('-'*25)
    print("Adding 2 gaussians:")
    print((gaussian_one + gaussian_two).__repr__())


def main_binomial():
    # initialize two binomial distributions
    binomial_one = Binomial(0.4, 20)
    binomial_two = Binomial(0.4, 60)

    # initialize a third binomial distribution reading in a data file
    binomial_three = Binomial()
    binomial_three.read_data_file('../numbers_binomial')

    # print out the 3 Binomials
    print("Binomial 1:")
    print(f"Total number of trials: {binomial_one.n}")
    print(f"Probability of an event occurring: {binomial_one.p}")
    print(f"Mean: {binomial_one.mean}")
    print(f"Standard Deviation: {binomial_one.stdev}")

    print('-'*25)
    print("Binomial 2:")
    print(f"Total number of trials: {binomial_two.n}")
    print(f"Probability of an event occurring: {binomial_two.p}")
    print(f"Mean: {binomial_two.mean}")
    print(f"Standard Deviation: {binomial_two.stdev}")

    print('-'*25)
    print("Binomial 3:")
    binomial_three.replace_stats_with_data()
    print(f"Total number of trials: {binomial_three.n}")
    print(f"Probability of an event occurring: {binomial_three.p}")
    print(f"Mean: {binomial_three.mean}")
    print(f"Standard Deviation:{binomial_three.stdev}")

    # plot histogram of binomial three
    print(f"Binomial three probability density function for x=5: {binomial_three.pdf(5)}")
    binomial_three.plot_bar()
    binomial_three.plot_bar_pdf()

    # add binomial_one and binomial_two together
    print('-'*25)
    print("Adding 2 binomials:")
    print((binomial_one + binomial_two).__repr__())


if __name__ == '__main__':
    main_binomial()
