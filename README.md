# Regex from hell

Regex is a very useful tool for every programmer. It has many usages, being the most common input validation, searching for patterns in texts and url matching, among several other users.

This repo implements a few simple regular expressions with python for study purposes :) 

## Running tests

```
$ python3 expressions.py
```

## Available functions

## Sanity check: the validations bellow are experimental and therefore not meant for production use.

### validate_ip
```
>>> validate_ip("100.123.322.122")
["100.123.322.122"]
>>> validate_ip("100.123.322.122aaaa")
[]
```


### validate_email

```
>>> validate_email("olamundo@daaas.com")
["olamundo@daaas.com"]
>>> validate_email("olamundo@notvalid")
[]
```

### validate_hexadecimal

```
>>> validate_hexadecimal("abcdef1234")
["abcdef1234""]
>>> validate_hexadecimal("zzzz9999")
[]
```

### find_order_ids

```
>>> find_order_ids("my order is #ab3f22ea hehe")
["ab3f22ea"]
>>> find_order_ids("my order is #ab3f22ea and #fdfd0000 hehe")
["ab3f22ea", "fdfd0000"]
>>> find_order_ids("my order is #ab3f22XX hehe")
[]
```

### get_html_tags

```
>>> get_html_tags("<h1> hello world! </h1>")
["<h1>", "</h1>"]
```

### get_html_tags_names_only

```
>>> get_html_tags_names_only("<h1> hello <span>xxxx</span>world! </h1>")
["h1", "span"]
```

### get_cpfs

```
>>> get_cpfs("My CPF is 142.444.222-99 hehe")
["142.444.222-99"]
```

Huge thanks to @marcospb19 at Python Brazil 2019! 