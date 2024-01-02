"""
    Module name :- tokenizer
    Method(s) :- tokenizer(target, prefix, suffix), get_request(url),
    get_url_list(url), infix_to_post_fix(expr)
"""

import requests


def tokenizer(target, prefix, suffix):
    """
    Generates list of tokens from text.

    Args:-
        target(str) :- A string of characters.
        prefix(str) :- Token must start with.
        suffix(str) :- Token must end with.

    Return
        List of tokens starts with prefix and end with suffix.
    """
    return [
        url[url.index(prefix) : url.index(suffix, url.index(prefix) + 1) + len(suffix)]
        for url in target.split()
    ]


def get_request(url):
    """
    Make an HTTP request to the url.

    Args:-
        url(str) :- URL to make call.

    Return:
        Response object's text.
    """
    response = requests.get(url, timeout=10)
    return response.text


def get_url_list(url):
    """
    Fetching links from the given url's source page.

    Args:-
        url(str):- URL to get source page.

    Return:
        List of url links in the source page.
    """
    url_list = []

    webpage_source = get_request(url=url)

    for target in webpage_source.split():
        if "href" in target and "http" in target:
            url = tokenizer(target=target, prefix="http", suffix='"')
            for link in url:
                url_list.append(link[:-1])

    return url_list


def infix_to_outfix(expr):
    """
    Postfix the given expression.

    Args:
        expr(str) :- Expression which is to be postfixed.

    Return
        Postfixed expression.
    """
    operators = []

    precedences = {"+": 1, "-": 1, "*": 2, "/": 2, "^": 3, "(": 4}

    postfix_expr = ""

    for ele in expr:
        if ele.isalnum():
            postfix_expr += ele
        elif ele == ")":
            while operator != "(":
                operator = operators.pop()
                if not operator == "(":
                    postfix_expr += operator
        else:
            if not operators:
                operators.append(ele)
            elif "(" in operators:
                operators.append(ele)
            elif precedences[ele] > precedences[operators[-1]]:
                operators.append(ele)
            else:
                while operators and precedences[ele] <= precedences[operators[-1]]:
                    operator = operators.pop()
                    if not operator == "(":
                        postfix_expr += operator
                operators.append(ele)

    for operator in reversed(operators):
        print(operator)
        postfix_expr += operator

    return postfix_expr


if __name__ == "__main__":
    print(get_url_list("https://enine.dev"))
