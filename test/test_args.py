import pytest

from args.args import Args


@pytest.mark.parametrize(
    "bool_str,bool_bool", [("True", True), ("False", False),]
)
def test_parse_args(bool_str, bool_bool):
    # given
    pattern = "l"
    values = [
        bool_str,
    ]

    # when
    arg = Args(pattern, values)

    # then
    assert arg.get_bool("l") == bool_bool
