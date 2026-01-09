# Python For The Lab

![Python For The Lab](theme/static/css/images/logo-red.svg)

This is the source code for the [Python For The Lab](https://www.pythonforthelab.com) website. It is built using [Pelican](https://getpelican.com/), a static site generator written in Python.

## About

Python For The Lab provides resources, courses, and books for scientists and engineers who want to learn how to use Python for controlling experiments and data analysis.

## Development

This project uses `uv` for dependency management.

### Setup

```bash
uv venv --python 3.13
uv pip install -r requirements.txt
```

### Build

To build the site locally:

```bash
uv run make
```

The output will be generated in the `output/` directory.

## Credits

Created by **Aquiles Carattino**.

## License

See the [LICENSE](LICENSE) file for more details.
