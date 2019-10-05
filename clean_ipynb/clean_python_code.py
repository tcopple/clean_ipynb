from re import sub
from subprocess import PIPE, Popen


def clean_python_code(code):

    code_ = sub("^%", "#cleaning...%", code, flags="m")

    completed_process = Popen(
        ("echo", code_), stdout=PIPE, stderr=PIPE, universal_newlines=True
    )

    completed_process = Popen(
        ("isort", "-"),
        stdin=completed_process.stdout,
        stdout=PIPE,
        stderr=PIPE,
        universal_newlines=True,
    )

    completed_process = Popen(
        ("black", "-"),
        stdin=completed_process.stdout,
        stdout=PIPE,
        stderr=PIPE,
        universal_newlines=True,
    )

    clean_code = sub(
        "^#cleaning...%", "%", completed_process.communicate()[0].strip(), flags="m"
    )

    return clean_code
