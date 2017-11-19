[![Python 3.6](https://img.shields.io/badge/python-3.6-brightgreen.svg)](#prerequisites)  [![license](https://img.shields.io/badge/license-MIT%20License-blue.svg)](LICENSE)


# qualtrics-mailer
A package for distributing pre-built surveys in Qualtrics

## Getting Started

1. Download this repo or install from PyPI using
```
pip install qualtrics-mailer
```
2. Prepare a CSV file with your contact list using the  file [example_mailing_list.csv](qualtrics_mailer/example_mailing_list.csv) as a template; note that column headers must be formatted exactly as specified at [https://api.qualtrics.com/docs/update-contact](https://api.qualtrics.com/docs/update-contact).
3. Update [example_usage.py](qualtrics_mailer/example_usage.py) with a Qualtrics API token and object IDs.

Instructions for generating an API token can be found at
[https://www.qualtrics.com/support/integrations/api-integration/overview/](https://www.qualtrics.com/support/integrations/api-integration/overview/)

Instructions for finding Qualtrics objects ids can be found at
[https://api.qualtrics.com/docs/finding-qualtrics-ids](https://api.qualtrics.com/docs/finding-qualtrics-ids)

Additional documentation for the Qualtrics API can be found at [https://api.qualtrics.com/docs/overview](https://api.qualtrics.com/docs/overview)

### Prerequisites

This package requires Python 3.6 or greater, along with the Python modules specified in [requirements.txt](requirements.txt).

This package requires a paid Qualtrics account with API add-on. Details about purchasing a Qualtrics account and/or API add-on can obtained by contacting Qualtrics at [https://www.qualtrics.com/contact/](https://www.qualtrics.com/contact/)

## Running the tests

To run the provided functional and unit tests, follow the instructions in [tests/example_test_config.py](tests/example_test_config.py), and then run the tests from the root folder as follows:
```
python -m unittest tests/functional_tests.py
```
and
```
python -m unittest tests/unit_tests.py
```

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details MIT License

## Authors
* [ilankham](https://github.com/ilankham)
* [kaiichang](https://github.com/kaiichang)

## Disclaimer

This project is in no way affiliated with Qualtrics.
