import argparse
import base64
import sys


def encode(streaming=False):
    if streaming:
        for chunk in iter(lambda: sys.stdin.buffer.read(4096), b''):
            encoded = base64.a85encode(chunk)
            sys.stdout.buffer.write(encoded)
    else:
        data = sys.stdin.buffer.read()
        encoded = base64.a85encode(data)
        sys.stdout.buffer.write(encoded)


def decode(streaming=False):
    if streaming:
        for chunk in iter(lambda: sys.stdin.buffer.read(4096), b''):
            try:
                decoded = base64.a85decode(chunk)
                sys.stdout.buffer.write(decoded)
            except Exception as e:
                print(f"Decoding error: {e}", file=sys.stderr)
                sys.exit(1)
    else:
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
    parser.add_argument('--stream', action='store_true', help="Enable streaming mode (read in chunks)")
    args = parser.parse_args()

    if args.mode == 'encode':
        encode(streaming=args.stream)
    else:
        decode(streaming=args.stream)


if __name__ == "__main__":
    main()
