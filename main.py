"""Entry point into pro-gen

"""
import time

from scripts import bio_server



server = bio_server.BioServer()


def main():
    for i in range(30):
        bio = server.fetch_new_bio()
        print "Profile %d >> " % i, bio
        time.sleep(0.6)

if __name__ == '__main__':
    main()
