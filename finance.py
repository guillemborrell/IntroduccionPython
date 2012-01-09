import urllib
import numpy
import datetime
import pylab

class yahoostock(object):
    """
    Wrapper class for Yahoo Finance chart data. The only mandatory
    argument is the signature of the stock as a string.
    
    Keyword arguments
    sdate -- Initial time for the data as datetime.date or datetime.datetime
    edate -- Final time for the data as datetime.date or datetime.datetime
    weekly -- If it is True gives weekly data
    monthly -- If it is True gives monthly data
    
    Example.
    IBM_stock = yahoostock('IBM',sdate=datetime.date(2011,1,30),weekly=True)
    """
    def __init__(self,symbol,**kwargs):
        self.symbol = symbol
        self.weekly = False
        self.monthly = False
        self.density = 'd'
        if kwargs.has_key('sdate'):
            self.sdate = True
            self.sd = kwargs['sdate'].day
            self.sm = kwargs['sdate'].month
            self.sy = kwargs['sdate'].year
        else:
            self.sdate = False
            
        if kwargs.has_key('edate'):
            self.edate = True
            self.ed = kwargs['edate'].day
            self.em = kwargs['edate'].month
            self.ey = kwargs['edate'].year
        else:
            self.edate = False
            
        if kwargs.has_key('weekly') and kwargs['weekly'] == True:
            self.density = 'w'
            
        if kwargs.has_key('monthly') and kwargs['monthly'] == True:
            self.monthly = 'm'
        
    def read(self):
        """Reads the data from Yahoo finance"""
        baseurl = 'http://ichart.yahoo.com/table.csv'
        url = baseurl+'?s='+self.symbol
        if self.sdate:
            url += '&a=%.2i'%(self.sm-1)
            url += '&b=%i'%(self.sd)
            url += '&c=%i'%(self.sy)
            
        if self.edate:
            url += '&d=%.2i'%(self.em-1)
            url += '&e=%i'%(self.ed)
            url += '&f=%i'%(self.ey)
            
        url += '&g=%s'%(self.density)

        #Check the converters argument out!
        #Thanks duck typing!
        try:
            self.data = numpy.loadtxt(urllib.urlopen(url),
                                      delimiter=',',
                                      skiprows=1,
                                      converters = {0: pylab.datestr2num})
            print "Read %i days."%self.data.shape[0]
        except IOError:
            print "No data retrieved. Probably no internet connection"
            self.data = None
                                  
        
    
    @property
    def date(self):
        """Date returned as a float"""
        return self.data[:,0]          
        
    @property
    def open(self):
        """Value at the beginning of the session"""
        return self.data[:,1]
        
    @property
    def high(self):
        """Highest value during the session"""
        return self.data[:,2]
        
    @property
    def low(self):
        """Lowest value during the session"""
        return self.data[:,3]
        
    @property
    def clse(self):
        """Value at the end of the session"""
        return self.data[:,4]
       
    @property
    def volume(self):
        """Volume traded during the sessino"""
        return self.data[:,5]
        
    @property
    def adj_close(self):
        """I Don't really know what this is"""
        return self.data[:,6]


if __name__ == '__main__':
    IBM_stock = yahoostock('IBM')
    IBM_stock.read()
