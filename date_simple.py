import datetime
# Hello I hacked your file
def get_date_object(date=None):
    if date == None:
	    return datetime.date.today()
    else:
        try:
            new_date = datetime.datetime.strptime(date, '%Y-%m-%d').date()
            return new_date
        except ValueError: 
            raise ValueError('Date is a bad date')
        except TypeError:
            raise TypeError('Not string type')

def get_date_string(date_object=None):
    if date_object == None:
        return str(datetime.date.today())
    else:
        try: 
            date_string = date_object.strftime('%Y-%m-%d')
            return date_string 
except (TypeError, AttributeError):
            raise TypeError('Not a datetime.date object type')
