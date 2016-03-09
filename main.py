"""Progen entry point.

Main script to initiate biogenesis.
"""
import time

from scripts import bio_server


server = bio_server.BioServer()


def main():
    for i in range(50):
        bio = server.fetch_new_bio()
        print "Profile %d >> " % i, bio
        time.sleep(0.3)

if __name__ == '__main__':
    main()
