"""Entry point into pro-gen

"""
import time

from scripts import generator



generator = generator.Generator()


def main():
    for i in range(20):
        bio = generator.create_new_bio()
        print "Profile %d >> " % i, bio
        time.sleep(1)

if __name__ == '__main__':
    main()
