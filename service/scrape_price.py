import os

from bs4 import BeautifulSoup
import requests
import argparse

from pipe import sort, select, Pipe


@Pipe
def join(iterable, sep):
    return sep.join(iterable)


def get_prices(pages):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/39.0.2171.95 Safari/537.36'}
    results = []
    for p in pages:
        resp = requests.get(p["url"], headers=headers)
        soup = BeautifulSoup(resp.text, features="html.parser")
        name = soup.select("div h2 a")[0].text
        price = float(soup.find("span", {"class": "green"}).text[1:])
        results.append({
            "url": p["url"],
            "size": p["size"],
            "price": price,
            "name": name
        })
    return results


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("output_file")
    args = parser.parse_args()
    from service.pages import pages
    prices = get_prices(pages)
    write_to_file(args.output_file, prices)


def write_to_file(output_file, prices):
    file_exists = os.path.isfile(output_file)
    with open(output_file, "a") as f:
        if not file_exists:
            f.write(",".join(sorted(prices[0].keys())) + "\n")
        for p in prices:
            sorted_values = list(p.items()) | sort() | select(lambda x: x[1])
            f.write((sorted_values | select(str) | join(",")) + "\n")


if __name__ == '__main__':
    main()