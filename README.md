![Python 3.6](https://img.shields.io/badge/python-3.6-brightgreen.svg)

# qualtrics-mailer
A package for importing contact lists and distributing pre-built surveys in Qualtrics

## Getting Started

1. Download this Repo
2. Prepare a csv file with your contact list using the [ExampleMailingList.csv](ExampleMailingList.csv)
3. 

### Prerequisites

This package requires Python 3.6 or greater, along with the modules specified in [requirements.txt](requirements.txt)

This package requires a paid Qualtrics account along with their Qualtrics API add-on. To purchase a Qualtrics account and/or an Qualtrics API add-on, please contact their sales team at: [Qualtrics Support](https://www.qualtrics.com/contact/)

## Running the tests

To use the provided functional and unit tests, follow the instructions in [tests/example_test_config.py](tests/example_test_config.py), and then run the tests as follows:
```
python -m unittest tests/functional_tests.py
```
and
```
python -m unittest tests/unit_tests.py
```

## License(s)
MIT License, See [LICENSE](LICENSE)

## Authors
* [ilankham](https://github.com/ilankham)
* [kaiichang](https://github.com/kaiichang)
