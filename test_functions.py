from functions import add, substract, multiply
from functions import convert_farenheintToCelsius as f2c

def test_add():
  assert add(2,3) == 5
  assert add("space", "ship") == "spaceship"

#uncomment the following test in step 5

def test_substract():
  assert substract(2,3) == -1

def test_convert_farenheintToCelsius():
  assert f2c(32) == 0
  assert f2c(122) == pytest.approx(50)
  with pytest.raises(AssertionError):
    f2c(-600)