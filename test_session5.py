# -*- coding: utf-8 -*-
import pytest
import string
import inspect
import re
import session5
import math
import sys
from io import StringIO

def test_indentations():
    ''' Returns pass if used four spaces for each level of syntactically \
    significant indenting.'''
    lines = inspect.getsource(session5)
    spaces = re.findall('\n +.', lines)
    for space in spaces:
        assert len(space) % 4 == 2, "Your script contains misplaced indentations"
        assert len(re.sub(r'[^ ]', '', space)) % 4 == 0, "Your code indentation does not follow PEP8 guidelines"

def test_function_name_had_cap_letter():
    functions = inspect.getmembers(session5, inspect.isfunction)
    for function in functions:  
        assert len(re.findall('([A-Z])', function[0])) == 0, "You have used Capital letter(s) in your function names"

TestData_TC01_01 = [(-1,0,2),
                    (1,-1,2),
                    (1,1,-2),
                    (1,1,0) 
                    ]

@pytest.mark.parametrize("test_data",TestData_TC01_01)
def test_TC01_01_ValueError_squared_power_list(test_data):
    with pytest.raises(ValueError):
        session5.squared_power_list(*test_data)

TestData_TC01_02 =[([2],[2]),
                   ([2,1,1],[2]),
                   ([2,0,1],[1,2]),
                   ([2,0,3],[1,2,4,8])]
@pytest.mark.parametrize("test_data,expected",TestData_TC01_02)
def test_TC01_02_Output_squared_power_list(test_data,expected):
    assert session5.squared_power_list(*test_data) == expected

TestData_TC02_01 = [('x',4),
                    (5,'x'),
                    (5,4.1)]

@pytest.mark.parametrize("test_data",TestData_TC02_01)
def test_TC02_01_TypeError_polygon_area(test_data):
    with pytest.raises(TypeError):
        session5.polygon_area(*test_data)

TestData_TC02_02 = [(0,4),
                    (-1,4),
                    (2,1),
                    (2,7)]

@pytest.mark.parametrize("test_data",TestData_TC02_02)
def test_TC02_02_ValueError_polygon_area(test_data):
    with pytest.raises(ValueError):
        session5.polygon_area(*test_data)

TestData_TC02_03 = [([3,3],3.9),
                    ([4.45,4],19.80),
                    ([4,5],27.53),
                    ([5,6],64.95)]

@pytest.mark.parametrize("test_data,expected",TestData_TC02_03)
def test_TC02_03_Output_polygon_area(test_data,expected):
        assert math.isclose(session5.polygon_area(*test_data),expected,rel_tol=1e-2)

TestData_TC03_01 = [('x',3),
                    (5,5),
                    (5,'deg C')]

@pytest.mark.parametrize("test_data",TestData_TC03_01)
def test_TC03_01_TypeError_temp_converter(test_data):
        with pytest.raises(TypeError):
            session5.temp_converter(*test_data)

TestData_TC03_02 = [([0,'c'],32),
                    ([0,'C'],32),
                    ([32,'f'],0),
                    ([32,'F'],0),
                    ([-40,'f'],-40),
                    ([-40,'c'],-40)]

@pytest.mark.parametrize("test_data,expected",TestData_TC03_02)
def test_TC03_02_Output_temp_converter(test_data,expected):
        assert math.isclose(session5.temp_converter(*test_data),expected,rel_tol=1e-2)

TestData_TC04_01 = [('x','m','s'),
                    (-1,'m','s'),
                    (10,'lightyear','s'),
                    (10,'s','m'),
                    (10,5,'s'),
                    (10,'km',5)]

@pytest.mark.parametrize("test_data",TestData_TC04_01)
def test_TC04_01_ValueError_speed_converter(test_data):
        with pytest.raises(ValueError):
            session5.speed_converter(*test_data)

TestData_TC04_02 = [([10,'m','s'],2.77),
                    ([10,'miles','hr'],6.21)]

@pytest.mark.parametrize("test_data,expected",TestData_TC04_02)
def test_TC04_02_ValueError_speed_converter(test_data,expected):
        assert math.isclose(session5.speed_converter(*test_data),expected,rel_tol=1e-2)

TestData_TC04_02 = [([10,'m','s'],2.77),
                    ([10,'miles','hr'],6.21)]

@pytest.mark.parametrize("test_data,expected",TestData_TC04_02)
def test_TC04_02_ValueError_speed_converter(test_data,expected):
        assert math.isclose(session5.speed_converter(*test_data),expected,rel_tol=1e-2)

result=StringIO()
test_str="This is test string"
TestData_TC05_01 = [([print,'123456','abcd',test_str],{'repetitions':2,'file':result},'123456 abcd This is test string'),
                    ([print,'123456','abcd',test_str],{'repetitions':2,'sep':'-','file':result},'123456-abcd-This is test string'),
                    ([print,'123456','abcd',test_str],{'repetitions':2,'sep':'-','end':'***','file':result},'123456-abcd-This is test string***')]

@pytest.mark.parametrize("arg,kwarg,expected",TestData_TC05_01)
def test_TC05_01_time_it_print(arg,kwarg,expected):
        print('',file=result)  
        session5.time_it(*arg,**kwarg)
        assert expected in result.getvalue()

TestData_TC06_01 =[([session5.squared_power_list,2,0,3],{'UnitTest':True,'repetitions':1},[1,2,4,8]),
                   ([session5.squared_power_list],{'UnitTest':True,'base':2,'exp_strt':0,'exp_end':3,'repetitions':1},[1,2,4,8])]
@pytest.mark.parametrize("arg,kwarg,expected",TestData_TC06_01,ids=["squared_power_list_Pos_arg","squared_power_list_kwarg"])
def test_TC06_01_time_it(arg,kwarg,expected):
    assert session5.time_it(*arg,**kwarg) == expected

TC06_02_IDs = ["polygon_area_Pos_arg","polygon_area_kwarg",
            "temp_converter_Pos_arg","temp_converter_kwarg",
            "speed_converter_Pos_arg","speed_converter_kwarg"]

TestData_TC06_02 =[([session5.polygon_area,3,3],{'UnitTest':True,'repetitions':1},3.9),
                   ([session5.polygon_area],{'UnitTest':True,'length':3,'sides':3,'repetitions':1},3.9),
                   ([session5.temp_converter,0,'c'],{'UnitTest':True,'repetitions':1},32),
                   ([session5.temp_converter],{'UnitTest':True,'temp':0,'scale':'c','repetitions':1},32),
                   ([session5.speed_converter,10,'m','s'],{'UnitTest':True,'repetitions':1},2.77),
                   ([session5.speed_converter],{'UnitTest':True,'speed':10,'dist':'m','time':'s','repetitions':1},2.77)]

@pytest.mark.parametrize("arg,kwarg,expected",TestData_TC06_02,ids=TC06_02_IDs)
def test_TC06_02_time_it(arg,kwarg,expected):
    assert math.isclose(session5.time_it(*arg,**kwarg),expected,rel_tol=1e-2)