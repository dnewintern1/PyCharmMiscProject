import argparse

ap = argparse.ArgumentParser()

ap.add_argument("-n", "--number", required=True, help="The number you want to add")
ap.add_argument("-d", "--numbers", required=True, help="The number you want to add")
args = vars(ap.parse_args()) #converts the give value by the user to dictionaries

n = int(args['number'])
d = int(args['numbers'])
print('Addition of the two number is', n + d)
print('mul of the two number is', n * d)
print('subtract of the two number is', n - d)
print('divide of the two number is', n / d)

#building your own python scripts