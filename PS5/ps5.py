# -*- coding: utf-8 -*-
# Problem Set 5: Experimental Analysis
# Name: 
# Collaborators (discussion):
# Time:

import numpy
import matplotlib.pyplot as plt
import re

# cities in our weather data
CITIES = [
    'BOSTON',
    'SEATTLE',
    'SAN DIEGO',
    'PHILADELPHIA',
    'PHOENIX',
    'LAS VEGAS',
    'CHARLOTTE',
    'DALLAS',
    'BALTIMORE',
    'SAN JUAN',
    'LOS ANGELES',
    'MIAMI',
    'NEW ORLEANS',
    'ALBUQUERQUE',
    'PORTLAND',
    'SAN FRANCISCO',
    'TAMPA',
    'NEW YORK',
    'DETROIT',
    'ST LOUIS',
    'CHICAGO'
]

TRAINING_INTERVAL = range(1961, 2010)
TESTING_INTERVAL = range(2010, 2016)

"""
Begin helper code
"""
class Climate(object):
    """
    The collection of temperature records loaded from given csv file
    """
    def __init__(self, filename):
        """
        Initialize a Climate instance, which stores the temperature records
        loaded from a given csv file specified by filename.

        Args:
            filename: name of the csv file (str)
        """
        self.rawdata = {}

        f = open(filename, 'r')
        header = f.readline().strip().split(',')
        for line in f:
            items = line.strip().split(',')

            year = int(items[2][0:4])
            month = int(items[2][4:6])
            day = int(items[2][6:])

            city = items[header.index('CITY')]
            temperature = float(items[header.index('TEMP')])
            if city not in self.rawdata:
                self.rawdata[city] = {}
            if year not in self.rawdata[city]:
                self.rawdata[city][year] = {}
            if month not in self.rawdata[city][year]:
                self.rawdata[city][year][month] = {}
            self.rawdata[city][year][month][day] = temperature
            
        f.close()

    def get_yearly_temp(self, city, year):
        """
        Get the daily temperatures for the given year and city.

        Args:
            city: city name (str)
            year: the year to get the data for (int)

        Returns:
            a 1-d numpy array of daily temperatures for the specified year and
            city
        """
        temperatures = []
        assert city in self.rawdata, "provided city is not available"
        assert year in self.rawdata[city], "provided year is not available"
        for month in range(1, 13):
            for day in range(1, 32):
                if day in self.rawdata[city][year][month]:
                    temperatures.append(self.rawdata[city][year][month][day])
        return numpy.array(temperatures)

    def get_daily_temp(self, city, month, day, year):
        """
        Get the daily temperature for the given city and time (year + date).

        Args:
            city: city name (str)
            month: the month to get the data for (int, where January = 1,
                December = 12)
            day: the day to get the data for (int, where 1st day of month = 1)
            year: the year to get the data for (int)

        Returns:
            a float of the daily temperature for the specified time (year +
            date) and city
        """
        assert city in self.rawdata, "provided city is not available"
        assert year in self.rawdata[city], "provided year is not available"
        assert month in self.rawdata[city][year], "provided month is not available"
        assert day in self.rawdata[city][year][month], "provided day is not available"
        return self.rawdata[city][year][month][day]

def se_over_slope(x, y, estimated, model):
    """
    For a linear regression model, calculate the ratio of the standard error of
    this fitted curve's slope to the slope. The larger the absolute value of
    this ratio is, the more likely we have the upward/downward trend in this
    fitted curve by chance.
    
    Args:
        x: an 1-d numpy array with length N, representing the x-coordinates of
            the N sample points
        y: an 1-d numpy array with length N, representing the y-coordinates of
            the N sample points
        estimated: an 1-d numpy array of values estimated by a linear
            regression model
        model: a numpy array storing the coefficients of a linear regression
            model

    Returns:
        a float for the ratio of standard error of slope to slope
    """
    assert len(y) == len(estimated)
    assert len(x) == len(estimated)
    EE = ((estimated - y)**2).sum()
    var_x = ((x - x.mean())**2).sum()
    SE = numpy.sqrt(EE/(len(x)-2)/var_x)
    return SE/model[0]

"""
End helper code
"""

def generate_models(x, y, degs):
    """
    Generate regression models by fitting a polynomial for each degree in degs
    to points (x, y).

    Args:
        x: an 1-d numpy array with length N, representing the x-coordinates of
            the N sample points
        y: an 1-d numpy array with length N, representing the y-coordinates of
            the N sample points
        degs: a list of degrees of the fitting polynomial

    Returns:
        a list of numpy arrays, where each array is a 1-d array of coefficients
        that minimizes the squared error of the fitting polynomial
    """
    models = []
    for deg in degs:
        models.append(numpy.polyfit(x, y, deg))
    
    return models


def r_squared(y, estimated):
    """
    Calculate the R-squared error term.
    
    Args:
        y: 1-d numpy array with length N, representing the y-coordinates of the
            N sample points
        estimated: an 1-d numpy array of values estimated by the regression
            model

    Returns:
        a float for the R-squared error term
    """
    mean = numpy.mean(y)
    return (1 - sum((y - estimated) ** 2) / sum((y - mean) ** 2))


def evaluate_models_on_training(x, y, models):
    """
    For each regression model, compute the R-squared value for this model with the
    standard error over slope of a linear regression line (only if the model is
    linear), and plot the data along with the best fit curve.

    For the plots, you should plot data points (x,y) as blue dots and your best
    fit curve (aka model) as a red solid line. You should also label the axes
    of this figure appropriately and have a title reporting the following
    information:
        degree of your regression model,
        R-square of your model evaluated on the given data points,
        and SE/slope (if degree of this model is 1 -- see se_over_slope). 

    Args:
        x: an 1-d numpy array with length N, representing the x-coordinates of
            the N sample points
        y: an 1-d numpy array with length N, representing the y-coordinates of
            the N sample points
        models: a list containing the regression models you want to apply to
            your data. Each model is a numpy array storing the coefficients of
            a polynomial.

    Returns:
        None
    """
    for model in models:
        modelY = numpy.polyval(model, x)
        plt.plot(x, y, "bo", label = "Measured Points")
        plt.plot(x, modelY, "r-", label = "Model")
        r2 = r_squared(y, modelY)
        if len(model) == 2:
            plt.title(f'Degree of fit: {len(model) - 1} \n R2: {r2} \n Ratio of SE: {se_over_slope(x, y, modelY, model)}.')
        else:
            plt.title(f'Degree of fit: {len(model) - 1} \n R2: {r2}')
        plt.ylabel("Temperature")
        plt.xlabel("Year")
        plt.legend(loc = "best")
        plt.show()

def gen_cities_avg(climate, multi_cities, years):
    """
    Compute the average annual temperature over multiple cities.

    Args:
        climate: instance of Climate
        multi_cities: the names of cities we want to average over (list of str)
        years: the range of years of the yearly averaged temperature (list of
            int)

    Returns:
        a numpy 1-d array of floats with length = len(years). Each element in
        this array corresponds to the average annual temperature over the given
        cities for a given year.
    """
    avgTemp = []
    for year in years:
        temps = []
        for city in multi_cities:
            temps.append(climate.get_yearly_temp(city, year))
        temps = numpy.array(temps)
        avgTemp.append(temps.mean())
    return numpy.array(avgTemp)

def moving_average(y, window_length):
    """
    Compute the moving average of y with specified window length.

    Args:
        y: an 1-d numpy array with length N, representing the y-coordinates of
            the N sample points
        window_length: an integer indicating the window length for computing
            moving average

    Returns:
        an 1-d numpy array with the same length as y storing moving average of
        y-coordinates of the N sample points
    """
    moved_average = []
    y = numpy.array(y)
    for i in range(len(y)):
        if i < window_length:
            arr_slice = y[:(i + 1)]
            slice_average = arr_slice.sum() / arr_slice.size
            moved_average.append(slice_average)
        else:
            arr_slice = y[(i - window_length + 1):(i + 1)]
            slice_average = arr_slice.sum() / window_length
            moved_average.append(slice_average)
    moved_average = numpy.array(moved_average)
    return moved_average    

def rmse(y, estimated):
    """
    Calculate the root mean square error term.

    Args:
        y: an 1-d numpy array with length N, representing the y-coordinates of
            the N sample points
        estimated: an 1-d numpy array of values estimated by the regression
            model

    Returns:
        a float for the root mean square error term
    """
    return (sum((y - estimated) ** 2) / len(y)) ** 0.5

def gen_std_devs(climate, multi_cities, years):
    """
    For each year in years, compute the standard deviation over the averaged yearly
    temperatures for each city in multi_cities. 

    Args:
        climate: instance of Climate
        multi_cities: the names of cities we want to use in our std dev calculation (list of str)
        years: the range of years to calculate standard deviation for (list of int)

    Returns:
        a numpy 1-d array of floats with length = len(years). Each element in
        this array corresponds to the standard deviation of the average annual 
        city temperatures for the given cities in a given year.
    """
    stds = []
    for year in years:
        d365_info = numpy.zeros(365)
        d366_info = numpy.zeros(366)
        
        for city in multi_cities:
            if len(climate.get_yearly_temp(city, year)) == 365:
                d365_info += climate.get_yearly_temp(city, year)
            else:
                d366_info += climate.get_yearly_temp(city, year)
        if numpy.sum(d365_info) > numpy.sum(d366_info):
            d_info = d365_info
        else:
            d_info = d366_info

        d_info = d_info/len(multi_cities)
        mean = numpy.mean(d_info)
        
        variance = 0
        for value in d_info:
            variance += (value - mean)*(value - mean)
        stds.append(numpy.sqrt(variance/len(d_info)))
    return numpy.array(stds)    


def evaluate_models_on_testing(x, y, models):
    """
    For each regression model, compute the RMSE for this model and plot the
    test data along with the model’s estimation.

    For the plots, you should plot data points (x,y) as blue dots and your best
    fit curve (aka model) as a red solid line. You should also label the axes
    of this figure appropriately and have a title reporting the following
    information:
        degree of your regression model,
        RMSE of your model evaluated on the given data points. 

    Args:
        x: an 1-d numpy array with length N, representing the x-coordinates of
            the N sample points
        y: an 1-d numpy array with length N, representing the y-coordinates of
            the N sample points
        models: a list containing the regression models you want to apply to
            your data. Each model is a numpy array storing the coefficients of
            a polynomial.

    Returns:
        None
    """
    for model in models:
        modelY = numpy.polyval(model, x)
        plt.plot(x, y, "b.", label = "Measured Points")
        plt.plot(x, modelY, "r-", label = "Model")
        RMSE = rmse(y, modelY)
        plt.title(f'Degree of fit: {len(model) - 1} \n RMSE: {RMSE}')
        plt.ylabel("Temperature")
        plt.xlabel("Year")
        plt.legend(loc = "best")
        plt.show()

if __name__ == '__main__':

    # Part A.4
    # data = Climate("data.csv")
    # dailyTemp = []
    # for year in TRAINING_INTERVAL:
    #     temp = data.get_daily_temp("NEW YORK", 1, 10, year)
    #     dailyTemp.append(temp)
    # dailyTemp = numpy.array(dailyTemp)
    # TRAINING_INTERVAL = numpy.array(TRAINING_INTERVAL)
    # degree = [1]
    # models = generate_models(TRAINING_INTERVAL, dailyTemp, degree)
    # evaluate_models_on_training(TRAINING_INTERVAL, dailyTemp, models)

    # data = Climate("data.csv")
    # annualTemp = []
    # for year in TRAINING_INTERVAL:
    #     temp = data.get_yearly_temp("NEW YORK", year)
    #     annualTemp.append(temp)
    # annualTemp = numpy.array(annualTemp, dtype=object)
    # TRAINING_INTERVAL = numpy.array(TRAINING_INTERVAL)
    # degree = [1]
    # models = generate_models(TRAINING_INTERVAL, annualTemp, degree)
    # evaluate_models_on_training(TRAINING_INTERVAL, annualTemp, models)  

    # Part B
    data = Climate("data.csv")
    citiesAVG = gen_cities_avg(data, CITIES, TRAINING_INTERVAL)
    TRAINING_INTERVAL = numpy.array(TRAINING_INTERVAL)
    degree = [1]
    models = generate_models(TRAINING_INTERVAL, citiesAVG, degree)
    evaluate_models_on_training(TRAINING_INTERVAL, citiesAVG, models)

    # Part C
    data = Climate("data.csv")
    TRAINING_INTERVAL = numpy.array(TRAINING_INTERVAL)
    cityData = gen_cities_avg(data, CITIES, TRAINING_INTERVAL)
    movingAVG = moving_average(cityData, 5)
    degree = [1]
    models = generate_models(TRAINING_INTERVAL, movingAVG, degree)
    evaluate_models_on_training(TRAINING_INTERVAL, cityData, models)

    # Part D.2.I
    data = Climate("data.csv")
    citiesAVG = gen_cities_avg(data, CITIES, TRAINING_INTERVAL)
    TRAINING_INTERVAL = numpy.array(TRAINING_INTERVAL)
    degree = [1, 2, 20]
    models = generate_models(TRAINING_INTERVAL, citiesAVG, degree)
    evaluate_models_on_training(TRAINING_INTERVAL, citiesAVG, models)
    # Part D.2.II
    # Comment the evaluate_models_on_training above for using this part
    citiesAVG_testing = gen_cities_avg(data, CITIES, TESTING_INTERVAL)
    TESTING_INTERVAL = numpy.array(TESTING_INTERVAL)
    models_testing = generate_models(TESTING_INTERVAL, citiesAVG_testing, degree)
    evaluate_models_on_testing(TESTING_INTERVAL, citiesAVG_testing, models_testing)

    # Part E
    data = Climate("data.csv")
    stdDev = gen_std_devs(data, CITIES, TRAINING_INTERVAL)
    movingAVG = moving_average(stdDev, 5)
    degree =[1]
    TRAINING_INTERVAL = numpy.array(TRAINING_INTERVAL)
    models = generate_models(stdDev, TRAINING_INTERVAL, degree)
    evaluate_models_on_training(stdDev, TRAINING_INTERVAL, models)
