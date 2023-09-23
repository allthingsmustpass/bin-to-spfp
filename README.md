# decimal to spfp converter

this repository contains a Python script for converting decimal numbers to IEEE 754 single-precision floating-point representation. it also supports negative numbers 

- [ ] currently working on handle fractional parts of decimal numbers.

## Installation

1. clone this repository to your local machine using the following command:

```bash
git clone https://github.com/allthingsmustpass/bin-to-spfp.git
```
2. Run the script by executing the following command:

```bash
python floating_point_converter.py
```

## Usage

1. When you run the script, it will prompt you to enter a decimal number. it can be positive (eg. 23) or negative (eg. -12).
2. it will display the sign bit, exponent, and mantissa of the resulting floating-point representation.
3. the script will also provide intermediate steps, such as converting decimal to binary and adjusting the exponent.
    1. it contains some functions for one's complement and two's complement.

## License

this project is licensed under the MIT License - see the [MIT](https://choosealicense.com/licenses/mit/) file for details.