import click

from algorithms.morse_code import MorseCode
from algorithms.caesar_cipher import CaesarCiphers


# simplify color print with click
def print_red(msg):
    click.echo(click.style(msg, fg='red'))


def print_green(msg):
    click.echo(click.style(msg, fg='green'))


# available command line options
@click.command()
@click.option('--alg', default='morse',  help='Algorithm to work with')
@click.option('--action', default='encode',  help='decode or encode?')
@click.argument('msg')
def cli(alg, action, msg):
    """Encoding and Decoding CLI."""
    # Morse Code
    if alg == 'morse':
        morse = MorseCode()
        if action == 'encode':
            print_red(morse.encode(msg))
        elif action == 'decode':
            print_green(morse.decode(msg))
        else:
            print_red('wrong --action parameter, allowed: decode, encode')
    # Caesar Ciphers
    elif alg == 'caesar':
        caesar = CaesarCiphers()
        if action == 'encode':
            print_red(caesar.encode(msg))
        elif action == 'decode':
            print_green(caesar.decode(msg))
        else:
            print_red('wrong --action parameter, allowed: decode, encode')

    # add new algorithms here ..


if __name__ == '__main__':
    cli()
