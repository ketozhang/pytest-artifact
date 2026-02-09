# pytest-artifact

[![PyPI version](https://img.shields.io/pypi/v/pytest-artifact.svg)](https://pypi.org/project/pytest-artifact)
[![Python versions](https://img.shields.io/pypi/pyversions/pytest-artifact.svg)](https://pypi.org/project/pytest-artifact)
[![See Build Status on GitHub Actions](https://github.com/ketozhang/pytest-artifact/actions/workflows/main.yml/badge.svg)](https://github.com/ketozhang/pytest-artifact/actions/workflows/main.yml)

Pytest plugin for managing test artifacts

## Installation

You can install "pytest-artifact" via [pip](https://pypi.org/project/pip/) from [PyPI](https://pypi.org/project):

```bash
pip install pytest-artifact
```

## Usage

```py
import time
import matplotlib.pyplot as plt

def test_benchmark(artifacts):
    times = range(1, 101, 10)
    elapsed = []
    for t in times:
        start_time = time.perf_counter()

        sleep(t)

        end_time = time.perf_counter()
        elapsed.append(end_time - start_time)

    plt.scatter(times, elapsed)
    plt.savefig(artifacts.dir / 'benchmark.png')
```

## Contributing

Contributions are very welcome.

## License

Distributed under the terms of the [MIT](https://opensource.org/licenses/MIT) license, "pytest-artifact" is free and open source software

## Issues

If you encounter any problems, please [file an issue](https://github.com/ketozhang/pytest-artifact/issues) along with a detailed description.
