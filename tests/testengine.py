import main
from diff_message import displayDif

#import requests
#import colour
 
#r = requests.get('https://www.google.com')
#print (r.status_code)

#import os
#print(colour.red(os.getenv("REPL_OWNER")))
#print(os.getenv("REPL_SLUG"))

class TestAssertionError(Exception):
    def __init__(self, expected, actual):
        self.expected = expected
        self.actual = actual

class TestResult:

    def __init__(self, name, status, expected, actual):
        self.name= name
        self.status = status
        self.expected = str(expected) 
        self.actual = str(actual) 

    
    def toDict (self):
        return {"name" : self.name, "status": self.status, "expected": self.expected, "actual": self.actual}


class TestEngine:
    
    def __init__(self, label):
        self.success = 0
        self.fails = 0
        self.results = []
        self.label = label
    
    def setUp(self):
        print("\n\nRunning Tests.\n")

    def tearDown(self):
        print("Done.")

    def assertEqual(self, expected, actual, msg):
        if expected != actual:
            raise TestAssertionError(expected, actual)

    def assertDefExists (self, name):
        defs = dir(main)
        print("Checking Def exists:", name)
        if not(name in defs):
            exp = f"Expected to find def {name}."
            act = f"{name} not found."
            raise TestAssertionError(bytes(exp, 'utf-8'), bytes(act, 'utf-8'))


    def getTests (self):
        return []

    def runTest(self, fn):
        try:
            #run the test
            fn()

            #test didn't throw an exception, so OK.
            self.results.append(TestResult( fn.__name__, "passed", None, None).toDict())

        except TestAssertionError as err:
            #print(type(err), err)
            print()
            self.results.append(TestResult(
                fn.__name__, 
                "failed", 
                err.expected, 
                err.actual).toDict())
            displayDif(err.expected, err.actual)

        except NameError as err:
            self.results.append(TestResult(
                fn.__name__, 
                "failed", 
                err, 
                "").toDict())

    # Run all tests rather than halting at the first fail.
    def run(self):
        for test in self.getTests():
            self.runTest(test)

        return self.results


    