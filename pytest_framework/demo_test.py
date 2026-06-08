import pytest
@pytest.mark.smoke
@pytest.mark.xfail
def test_sample1():
    assert 1+1==2,"error"
    print("test1")
@pytest.mark.smoke
@pytest.mark.skip
def test_sample2():
    assert 1+1==3,"error"

    print("test2")
@pytest.mark.smoke
def test_sample3():
    print("test3")       

@pytest.mark.smoke
@pytest.mark.xfail
def test_sample4():
    assert 1+1!=2,"error"
    print("test4")    
@pytest.mark.re
@pytest.mark.parametrize("in1,in2,expected",[(1,2,5),(2,3,5),(4,5,9)])
def test_sample5(in1,in2,expected):
    assert in1+in2<=expected 
