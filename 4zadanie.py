import sys

import utils


if __name__ == "main":

    args = sys.argv[1:]

    for code in args:
        conv = utils.currency_rates(code)
        if conv:
            cur = conv

            print(f"{cur}")