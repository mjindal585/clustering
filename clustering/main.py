# main.py
import scrapping
import preprocessing
import k_means
import hierarchical


def main():
    print("Starting run")
    scrapping.main()
    preprocessing.main()
    k_means.main()
    hierarchical.main()
    print("Run complete")


if __name__ == '__main__':
    main()
