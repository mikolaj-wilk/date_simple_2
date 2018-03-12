import date_simple as ds
import datetime 

def test_get_date_object(date=None):
    today_date_object = ds.get_date_object()
    assert today_date_object == datetime.date(today)
    assert isintance(today_date_object, datetime.date)
    x_date_object = ds.get_date_object(date='2018-02-26')
    assert x_date_object == datetime.date('2018-02-26')
    assert isinstance(x_date_object, datetime.date)

def test_get_date_string(date_object=None):
    datestr1 = ds.get_date_string()
    assert datestr1 == str(datetime.date(today))
    assert isinstance(datestr1, str)
    datestr2 = ds.get_date_string(date_object=dateobj2)
    assert datestr2 == dateobj2.strftime('%Y-%m-%d')
    assert isinstance(datestr2, str)

def test_bad_date(date=None):
    with pytest.raises(ValueError):
        ds.get_date_object(date='2018-0226')
    with pytest.raises(TypeError):
        ds.get_date_object(date=57)

def test_nondatetype(date_object=None):
    with pytest.raises(TypeError):
        ds.get_date_object(date=57)





