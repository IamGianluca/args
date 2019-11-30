import pytest

from args.args import Args


@pytest.mark.parametrize(
    "pattern,in_,expected", [("l", ["True"], True), ("l", ["False"], False),]
)
def test_get_bool(pattern, in_, expected):
    # when
    arg = Args(pattern, in_)

    # then
    assert arg.get_bool("l") == expected


@pytest.mark.parametrize(
    "pattern,in_,expected", [("p#", ["99999"], 99999), ("p#", ["0"], 0),]
)
def test_get_int(pattern, in_, expected):
    # when
    arg = Args(pattern, in_)

    # then
    assert arg.get_int("p") == expected


@pytest.mark.parametrize(
    "pattern,in_,expected",
    [("a*.", ["99999"], "99999"), ("a*.", ["True"], "True"),],
)
def test_get_str(pattern, in_, expected):
    # when
    arg = Args(pattern, in_)

    # then
    assert arg.get_str("a") == expected
