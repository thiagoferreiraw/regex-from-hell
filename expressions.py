import re


def validate_ip(text):
    pattern = r"^[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}$"
    return re.findall(pattern, text)


assert validate_ip("100.123.322.122")
assert validate_ip("10.0.0.1")
assert not validate_ip("100.c.322.a")
assert not validate_ip("a.8.8.8.8")
assert not validate_ip("100.1.322.b")
assert not validate_ip("100.1.322....b")
assert not validate_ip("100.1.322b123")


def validate_email(text):
    pattern = r"^[\w]{2,20}@[\w]{2,20}\.[\w]{2,20}$"
    return re.findall(pattern, text)


assert validate_email("Ola@das.com")
assert validate_email("Ola12313231@das.com")
# assert validate_email("Ola12313231@das.com.br") # this is broken
assert not validate_email("Ola12313231@")
assert not validate_email("Ola12313231@a.com")
assert not validate_email("Ola12313231@a.com")
assert not validate_email("[][][][][Ola12313231@a.com")
assert not validate_email("[][][][][Ola12313231@[][]$$$$[][].com")


def validate_hexadecimal(text):
    pattern = r"^[a-fA-F0-9]+$"
    return re.findall(pattern, text)


assert validate_hexadecimal("abcdef1234")
assert validate_hexadecimal("f")
assert validate_hexadecimal("f10")
assert not validate_hexadecimal("")
assert not validate_hexadecimal("z1")
assert not validate_hexadecimal("z")


def find_order_ids(text):
    # group () only what I want
    pattern = r"#{1}([a-fA-F0-9]{8})"
    return re.findall(pattern, text)


assert find_order_ids("my order is #ab3f22ea hehe") == ["ab3f22ea"]
assert find_order_ids("my order is #ab3f22ea hehe a random abc") == ["ab3f22ea"]
assert find_order_ids("my order is #ab3f22ea hehe a random abc ab3f22e2") == [
    "ab3f22ea"
]
assert find_order_ids("Many #abcd0987 , orders ##fdfd0000 ") == ["abcd0987", "fdfd0000"]
assert not find_order_ids("Many #abcx0987 , orders ##fdfx0000 ")


def get_html_tags(text):
    # [^>] Everthing less >
    pattern = r"<[^>]+>"
    return re.findall(pattern, text)


assert get_html_tags("<h1> hello world! </h1>") == ["<h1>", "</h1>"]


def get_html_tags_names_only(text):
    # ?! -> negative lookahead
    pattern = r"<(?!/)([^>]+)>"
    return re.findall(pattern, text)


result = get_html_tags_names_only("<h1> hello <span>xxxx</span>world! </h1>")
assert result == ["h1", "span"], result


def get_cpfs(text):
    pattern = r"\d{3}\.\d{3}\.\d{3}-\d{2}"
    return re.findall(pattern, text)


result = get_cpfs("My CPF is 142.444.222-99 hehe")
assert result == ["142.444.222-99"], result
