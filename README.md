### Python Developer Assignment
Write an application in Python which meets following ‘Problem description’.
Show your programming skills as well as your problem-solving skills. Clean and readable code and a good design is important


###  Problem Description
- Allow user to enter string which will be encrypted by selected algorithm.
- You should also allow reversed mode
- Implement encryption to Morse code and decryption from Morse code
- Your solution should allow extension with another encryption and decryption algorithm (e.g Caesarcypher).


### Usage
Simple CLI allows you to choose between algorithms and decode/encode action. 
`python app.py [--alg=morse] [--action=encode] 'my super secret text'`

> As bonus all encoded text highlight by red color and decoded text is green :)

### Optional parameters
- `--help` gives you help about all parameters
- `--alg` -- choose one of encryption/decryption algorithms (setup to `morse` by default)
- `--action` -- `encrypt` or `decrypt` (setup to `encrypt` by default)

## Running tests
`python3 -m unittest` (or `python -m unittest discover` for Python 2)
