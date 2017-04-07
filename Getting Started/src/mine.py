import argparse
p=argparse.ArgumentParser()
p.add_argument('--foo',nargs='?',const='abc', default='other')
p.add_argument('bar')
args = p.parse_args()
print(args)