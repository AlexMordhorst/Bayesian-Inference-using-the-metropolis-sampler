
import scipy.stats as stats

class Normal:
    def __init__(self, mu, sigma):
        self.mu = mu
        self.sigma = sigma
        self.dist = stats.norm(loc = mu, scale = sigma)

    def pdf(self,x):
        return self.dist.pdf(x)

    def logpdf(self,x):
        return self.dist.logpdf(x)

    def sample(self, n):
        return self.dist.rvs(n)


class Exponential:
    def __init__(self):
        self.dist = stats.expon()

    def logpdf(self,x):
        return self.dist.logpdf(x)
