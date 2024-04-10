# What my project does

My project generate simple, strong, memorable and easy-to-type passwords.

# Target audience

For anyone who need to get passwords easily.

# Comparison

Most passwords manager generate completely passwords with completely random characters that aren't very easy to memorize or tape.

Examples include [Dashlane](https://www.dashlane.com/features/password-generator), [Norton](https://my.norton.com/extspa/passwordmanager?path=pwd-gen), [Avast](https://www.avast.com/random-password-generator).

Or other like [Bitwarden](https://bitwarden.com/password-generator/) generate passwords that are not really fast-to-type.

The mine generate sth like `6Nixe#Becokace`  `0Qubyby+Pomafy` , or `7Zuxogu:Lebuwo` . I wanted to make a password generator that combines simplicity, security, memorability, and ease of type.

# Usage

You can install it with `pip install pwd-generator` and use the cli version:

```
pwd-gen

```

To use it in a python code

```python
import pwdgen
print(pwdgen.generate())
```

# Source code

The source code is on [github](https://github.com/RadoTheProgrammer/pwdgen)
