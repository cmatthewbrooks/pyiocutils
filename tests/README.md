# pyiocutils - Tests

## Usage

To run the test suite, use the [run_tests.py](run_tests.py) script.
```python
> python run_tests.py
```

To run an individual test method, build from this example:
```python
> python test_ioc.py TestIOC.test_is_domain
```

where:
+ test.ioc.py - is the individual test script
+ TestIOC - is the name of the test class which subclasses unittest.TestCase
+ test_is_domain - is a method of the test class

## Contents

+run_tests.py - the automated test suite; will run all tests 
+test_ioc.py - tests the ioc module
+test_iocfile.py - tests the iocfile module
+test_iocargs.py - tests the iocargs module
+data.py - some test data
+context.py - sets up the environment for easy imports
+iocfile.txt - an example ioc file for testing
