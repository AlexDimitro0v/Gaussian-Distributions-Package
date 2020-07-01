import math
import matplotlib.pyplot as plt
from distributions.general_distribution import Distribution

# A binomial distribution is defined by two variables:
#   • the probability of getting a positive outcome
#   • the number of trials
#
# If you know these two values, you can calculate the mean and the standard deviation
#
# For example, if you flip a fair coin 25 times, p = 0.5 and n = 25
# You can then calculate the mean and standard deviation with the following formula:
#   • mean = p * n
#   • standard deviation = sqrt(n * p * (1 - p))
# https://www.youtube.com/watch?v=J8jNoF-K8E8


class Binomial(Distribution):
    """
    Binomial distribution class for calculating and visualizing a Binomial distribution.

    Attributes:
       p           (float) representing the probability of an event occurring
       n           (int) the total number of trials
       mean        (float) representing the mean value of the distribution
       stdev       (float) representing the standard deviation of the distribution
       data_list   (list of floats) a list of floats to be extracted from the data file
    """
    def __init__(self, prob=.5, size=0):
        self.p = prob
        self.n = size
        super().__init__(self.calculate_mean(), self.calculate_stdev())

    def calculate_mean(self):
        """
        Method to calculate the mean from p and n

        Args:
           None

        Returns:
           float: mean of the data set
        """
        self.mean = self.p*self.n
        return self.mean

    def calculate_stdev(self):
        """
        Method to calculate the standard deviation from p and n.

        Args:
           None

        Returns:
           float: standard deviation of the data set
        """
        self.stdev = math.sqrt(self.n * self.p * (1-self.p))
        return self.stdev

    def replace_stats_with_data(self):
        """
        Method to calculate p and n from the data set. The function updates the p and n variables of the object.

        Args:
           None
        Returns:
           float: the p value
           float: the n value
        """
        self.n = len(self.data)
        self.p = sum(self.data)/self.n      # the number of favourable outcomes divided by the total trials
        self.mean = self.calculate_mean()
        self.stdev = self.calculate_stdev()

        return self.p, self.n

        # The read_data_file() from the Generaldistribution class can read in a data file.
        # Because the Binomaildistribution class inherits from the Generaldistribution class,
        # you don't need to re-write this method.
        # However, the method doesn't update the mean or standard deviation of a distribution.
        # Hence we are going to write a method that calculates n, p, mean and stdv from a data set and then
        # updates the n, p, mean and stdev attributes.
        # A valid file to read data from would be in the form of a sequence (in lines) of
        # zeros and ones(favourable outcomes).

    def plot_bar(self):
        """
        Method to output a bar chart of the instance variable 'data' using matplotlib pyplot library.
        
        Args:
           None
        
        Returns:
           None
        """
        # Note: Histograms are used to show distributions of continuous variables
        # while bar charts are used to compare discrete variables.
        # Histograms plot quantitative data with ranges of the data grouped into bins or intervals
        # while bar charts plot categorical data.
        plt.bar(x=['0', '1'], height=[(1-self.p)*self.n, self.p*self.n])
        plt.title('Bar Chart of Data')
        plt.xlabel('outcome')
        plt.ylabel('count')
        plt.show()

    def pdf(self, k):
        # E.g. What is the probability that 4 out of 7 people would prefer Fanta instead of Cola randomly?
        # (e.g. with no preference, i.e. 0.5% change of picking Fanta)
        """Probability density function calculator for the binomial distribution.

        Args:
           k (float): point for calculating the probability density function

        Returns:
           float: probability density function output
        """
        a = math.factorial(self.n)/(math.factorial(k)*(math.factorial(self.n - k)))
        b = (self.p ** k) * math.pow(1 - self.p, self.n - k)
        return a*b

    def plot_bar_pdf(self):
        """
        Method to plot the pdf of the binomial distribution

        Args:
           None

        Returns:
           list: x values for the pdf plot
           list: y values for the pdf plot
        """

        x = []
        y = []

        # calculate the x values to visualize
        for i in range(self.n+1):
            x.append(i)
            y.append(self.pdf(i))

        # make the plots
        plt.bar(x, y)
        plt.title('Distribution of Outcomes')
        plt.ylabel('Probability')
        plt.xlabel('Outcome')

        plt.show()
        return x, y

    def __add__(self, other):
        """Function to add together two Binomial distributions with equal p (yes, I know...)

        Args:
            other (Binomial): Binomial instance

        Returns:
            Binomial: Binomial distribution
        """
        try:
            assert self.p == other.p, 'p values are not equal'
        except AssertionError:
            raise

        result = Binomial()
        result.n = self.n+other.n
        result.p = self.p
        result.calculate_mean()
        result.calculate_stdev()
        return result

    def __repr__(self):
        """
        Method to output the characteristics of the Binomial instance

        Args:
            None

        Returns:
            string: characteristics of the Binomial object
        """
        return f"mean {self.mean}, standard deviation {self.stdev}, p {self.p}, n {self.n}"


def main():
    #  For a binomial distribution with n trials and probability p,
    #  the probability density function calculates the likelihood of getting k positive outcomes.
    #  For example, if you flip a coin n = 60 times, with p = .5,
    #  what's the likelihood that the coin lands on heads 40 out of 60 times?
    binomial_one = Binomial(prob=0.5, size=60)
    print(binomial_one.pdf(40))


if __name__ == '__main__':
    main()
