import math
import statistics as st
import matplotlib.pyplot as plt
from distributions.general_distribution import Distribution
# https://stackoverflow.com/questions/41816973/modulenotfounderror-what-does-it-mean-main-is-not-a-package


class Gaussian(Distribution):
    """
    Gaussian distribution class for calculating and
    visualizing a Gaussian distribution.

    Attributes:
       mean (float) representing the mean value of the distribution
       stdev (float) representing the standard deviation of the distribution
       data_list (list of floats) a list of floats extracted from the data file
    """
    def __init__(self, mu=0, sigma=1):
        super().__init__(mu, sigma)

    def calculate_mean(self):
        """
        Method to calculate the mean of the data set.

        Args:
           None

        Returns:
           float: mean of the data set
        """
        self.mean = st.mean(self.data)
        return self.mean

    def calculate_stdev(self, sample=True):
        """
        Method to calculate the standard deviation of the data set.

        Args:
           sample (bool): whether the data represents a sample or population

        Returns:
           float: standard deviation of the data set
        """
        if sample:
            self.stdev = st.stdev(self.data)
        else:
            self.stdev = st.pstdev(self.data)
        return self.stdev

    def read_data_file(self, file_name, sample=True):
        """
        Method to read in data from a txt file. The txt file should have
        one number (float) per line. The numbers are stored in the data attribute.
        After reading in the file, the mean and standard deviation are calculated

        Args:
            file_name (string): name of a file to read from
            sample (bool): whether the data represents a sample or population

        Returns:
            None
        """
        super().read_data_file(file_name)
        self.mean = self.calculate_mean()
        self.stdev = self.calculate_stdev(sample)

    def plot_histogram(self):
        """
        Method to output a histogram of the instance variable data using
        matplotlib pyplot library.

        Args:
            None

        Returns:
            None
        """
        if self.data:
            plt.hist(self.data)
            plt.title('Histogram of Data')
            plt.xlabel('data')
            plt.ylabel('count')
            plt.show()
        else:
            print("No data.")

    def pdf(self, x):
        """
        Probability density function calculator for the gaussian distribution.

        Args:
            x (float): point for calculating the probability density function
        Returns:
            float: probability density function output
        """
        mu = self.mean
        sigma = self.stdev
        variance = float(sigma) ** 2
        denom = (2 * math.pi * variance) ** .5
        num = math.exp(-(float(x) - float(mu)) ** 2 / (2 * variance))
        return num/denom
        # return (1.0 / (sigma * math.sqrt(2*math.pi))) * math.exp(-0.5*((x - mu) / sigma) ** 2)

    def plot_histogram_pdf(self, n_spaces=50):
        """
        Method to plot the normalized histogram of the data and a plot of the
        probability density function along the same range

        Args:
           n_spaces (int): number of data points

        Returns:
           list: x values for the pdf plot
           list: y values for the pdf plot
        """
        try:
            min_range = min(self.data)
            max_range = max(self.data)
        except ValueError:
            print("No data.")
            return

        # calculates the interval between x values
        interval = 1.0 * (max_range - min_range) / n_spaces

        x = []
        y = []

        # calculate the x values to visualize
        for i in range(n_spaces):
            tmp = min_range + interval * i
            x.append(tmp)
            y.append(self.pdf(tmp))

        # make the plots
        fig, axes = plt.subplots(2)
        fig.subplots_adjust(hspace=.5)
        axes[0].hist(self.data, density=True)
        axes[0].set_title('Normed Histogram of Data')
        axes[0].set_ylabel('Density')

        axes[1].plot(x, y)
        axes[1].set_title('Normal Distribution for \n Sample Mean and Sample Standard Deviation')
        axes[0].set_ylabel('Density')
        plt.show()

        return x, y

    def __add__(self, other):
        """
        Magic method to add together two Gaussian distributions

        Args:
            other (Gaussian): Gaussian instance

        Returns:
            Gaussian: Gaussian distribution
        """

        # create a new Gaussian object
        result = Gaussian()
        result.mean = self.mean + other.mean
        result.stdev = math.sqrt(self.stdev ** 2 + other.stdev ** 2)
        return result

    def __repr__(self):
        """
        Magic method to output the characteristics of the Gaussian instance

        Args:
            None

        Returns:
            string: characteristics of the Gaussian
        """
        return f"mean {self.mean}, standard deviation {self.stdev}"


def main():
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
    print(f"Gaussian Three probability density function for x=3: {gaussian_three.pdf(5)}")

    # add gaussian_one and gaussian_two together
    print('-'*25)
    print("Adding 2 gaussians:")
    print((gaussian_one + gaussian_two).__repr__())

    print('-'*25)
    gaussian_one.plot_histogram()           # No data.


if __name__ == '__main__':
    main()
