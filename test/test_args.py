from args.args import Args


def test_parse_args():
    # given
    pattern = "l,p#,d*"
    values = ['True', '10', 'something']

    # when
    arg = Args(pattern, values)

    # then
    assert arg.get_bool('l')
    assert arg.get_int('p') == 10
    assert arg.get_string('d') == "something"
