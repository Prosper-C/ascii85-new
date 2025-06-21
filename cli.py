import argparse
import base64
import sys


def encode():
    data = sys.stdin.buffer.read()
    encoded = base64.a85encode(data)
    sys.stdout.buffer.write(encoded)


def decode():
    data = sys.stdin.buffer.read()
    try:
        decoded = base64.a85decode(data)
        sys.stdout.buffer.write(decoded)
    except Exception as e:
        print(f"Decoding error: {e}", file=sys.stderr)
        sys.exit(1)


def main():
    parser = argparse.ArgumentParser(description="ASCII85 encoder/decoder")
    parser.add_argument('mode', choices=['encode', 'decode'], help="Mode: encode or decode")
    args = parser.parse_args()

    if args.mode == 'encode':
        encode()
    else:
        decode()


if __name__ == "__main__":
    main()
