# pytest-artifact

[![PyPI version](https://img.shields.io/pypi/v/pytest-artifact.svg)](https://pypi.org/project/pytest-artifact)
[![Python versions](https://img.shields.io/pypi/pyversions/pytest-artifact.svg)](https://pypi.org/project/pytest-artifact)
[![See Build Status on GitHub Actions](https://github.com/ketozhang/pytest-artifact/actions/workflows/main.yml/badge.svg)](https://github.com/ketozhang/pytest-artifact/actions/workflows/main.yml)

Pytest plugin for managing test artifacts

## Installation

You can install "pytest-artifact"  from [PyPI](https://pypi.org/project):

```bash
pip install pytest-artifact
```

## Usage
Attach the `artifacts` fixture to your pytest test case. The attribute `artifacts.dir` is a dedicated directory for the test case.

```py
import time
import matplotlib.pyplot as plt

def test_benchmark(artifacts):
    times = range(1, 101, 10)
    elapsed = []
    for t in times:
        start_time = time.perf_counter()

        time.sleep(t)

        end_time = time.perf_counter()
        elapsed.append(end_time - start_time)

    plt.scatter(times, elapsed)
    with artifacts.open('benchmark.png') as f:
        plt.savefig(f)
```

```
.artifacts/
└── test_benchmark/
    └── benchmark.png
```

The test case directory is named after the test path, function name, and if any, the test parameter ID.

### Configure
Configurations may be set in `pyproject.toml`, `pytest.ini`, or passed as command line options.

```toml
# pyproject.toml
[tool.pytest]
artifacts_dir = .artifacts/
```

```ini
# pytest.ini
[pytest]
artifacts_dir = .artifacts/
```

```sh
pytest --artifacts-dir .artifacts/ tests/
```

## Contributing

Contributions are very welcome.

## License

Distributed under the terms of the [MIT](https://opensource.org/licenses/MIT) license, "pytest-artifact" is free and open source software

## Issues

If you encounter any problems, please [file an issue](https://github.com/ketozhang/pytest-artifact/issues) along with a detailed description.
