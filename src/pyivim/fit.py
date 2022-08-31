class Fitting:
    """Class for Fit MRI-IVIM Images"""

    def __init__(self, data, bvalues, fit_method, threshold):
        self.data = data
        self.bvalues = bvalues
        self.fit_method = fit_method
        self.threshold = threshold

    def hello(self):
        print(self.data)
        print(self.bvalues)
        print(self.fit_method)
        return print("Hi")

    # Median Otsu

    def run(self):
        return print("Result Fitting")
