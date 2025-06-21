import base64
import subprocess
import sys


def run_cli(mode, input_bytes):
    proc = subprocess.Popen(
        [sys.executable, 'cli.py', mode],
        stdin=subprocess.PIPE,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE
    )
    out, err = proc.communicate(input=input_bytes)
    return proc.returncode, out, err


def test_encode_decode():
    data = b"Hello, world!"
    retcode, encoded, _ = run_cli('encode', data)
    assert retcode == 0
    assert encoded == base64.a85encode(data)

    retcode, decoded, _ = run_cli('decode', encoded)
    assert retcode == 0
    assert decoded == data


def test_decode_invalid():
    retcode, _, err = run_cli('decode', b"invalid!!@@@")
    assert retcode != 0
    assert b"error" in err.lower()
