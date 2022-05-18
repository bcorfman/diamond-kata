from main import diamond


def test_no_letter():
    assert diamond('') == ''

def test_single_letter():
    assert diamond('a') == 'A\n'

def test_b():
    assert diamond('b') == ' A\nB B\n A\n'

def test_c():
    assert diamond('C') == '  A\n B B\nC   C\n B B\n  A\n'
