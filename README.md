# 🛡️HashGuard

**Secure Local File Copy CLI Tool**

Verify file integrity with cryptographic hashes before and after copying.

---

## 🚀 Features

- Secure local file copy with integrity verification
- Supports multiple hash algorithms (e.g., SHA-256, MD5, BLAKE2)
- Optional verbose mode for printed output
- List available hashing algorithms with `--list-algorithms`
- Clean CLI built with `argparse`

---

## 📦 Installation

> 📌 **Coming soon on [PyPI](https://pypi.org/)!**

For now, clone the repo manually:

```
git clone https://github.com/PhoenixAnvil/hashguard.git
cd hashguard
python3 -m keyforge.cli source.txt destination.txt sha256
```

---

## 🛠 Usage

```
python3 -m hashguard.cli [source] [destination] [algorithm] [options]
```

Options:

| Flag                  | Description                                       |
|-----------------------|---------------------------------------------------|
| -l, --list-algorithms | List the available hashing algorithms             |
| -v, --verbose         | Show the verified hash and match status in output |

Example:

```
python3 -m hashguard.cli source.txt dest.txt sha256
```

---

## ✅ Tests

HashGuard is fully tested with pytest.

To run the test suite:

```
pytest
```

---

## 📂 Project Structure

```
hashguard/
├── cli.py # Command-line interface logic
├── copy.py # Core secure local file copy logic
tests/
├── __init__.py
├── test_cli.py
├── test_copy.py
```

---

## 🔥 A Product of The Forge

HashGuard is proudly crafted by PhoenixAnvil Labs — where tools aren’t just built…
they’re forged.

Learn more about our philosophy and DevOps workflow at:

➡️ https://phoenixanvilabs.dev

---

## 📬 Questions or Feedback?

We love hearing from the community!

> 📌 **Coming soon!**

### Mailing Lists

- 💬 Users: hashguard-users@phoenixanvilabs.dev
- 💻 Developers: hashguard-devel@phoenixanvilabs.dev

📣 Want updates about new releases?
Join the **HashGuard-Announce** mailing list!

- 📣 Announce: hashguard-announce@phoenixanvilabs.dev

### IRC Channels

---

## 📜 License

HashGuard is released under the MIT License — free for both personal and commercial use.

---
