# pytest-artifacts

[![PyPI version](https://img.shields.io/pypi/v/pytest-artifacts.svg)](https://pypi.org/project/pytest-artifacts)
[![Python versions](https://img.shields.io/pypi/pyversions/pytest-artifacts.svg)](https://pypi.org/project/pytest-artifacts)
[![See Build Status on GitHub Actions](https://github.com/ketozhang/pytest-artifacts/actions/workflows/main.yml/badge.svg)](https://github.com/ketozhang/pytest-artifacts/actions/workflows/main.yml)

Pytest plugin for managing test artifacts

## Installation

You can install "pytest-artifacts"  from [PyPI](https://pypi.org/project):

```bash
pip install pytest-artifacts
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
Configurations may be set in `pyproject.toml` or `pytest.ini`. Some options can also be set via CLI (use `pytest --help`)

| Option | Type | Default | Description |
| --- | --- | --- | --- |
| `artifacts_dir` | str | `.artifacts/` | Directory to store test artifacts. Also settable via the `--artifacts-dir` CLI option, which takes precedence over the ini setting. |
| `artifacts_use_subdir_for_parametrize` | bool | `false` | When `True`, parametrized tests get a subdirectory per parameter ID (e.g. `.artifacts/test_foo/param_id/`). When `False`, all parameter variants share the same `.artifacts/test_foo/` directory and overwrite each other. |

```toml
# pyproject.toml
[tool.pytest.ini_options]
artifacts_dir = ".artifacts/"
artifacts_use_subdir_for_parametrize = false
```

```ini
# pytest.ini
[pytest]
artifacts_dir = .artifacts/
artifacts_use_subdir_for_parametrize = false
```

```sh
pytest --artifacts-dir .artifacts/ tests/
```

#### Parametrized test layout


```py
@pytest.mark.parametrize("x", [1, 2])
def test_foo(artifacts, x):
    with artifacts.open("out.txt", "w") as f:
        f.write(str(x))
```

With `artifacts_use_subdir_for_parametrize = false`:
```
.artifacts/
└── test_foo[1]/
    └── out.txt
└── test_foo[2]/
    └── out.txt
```

With `artifacts_use_subdir_for_parametrize = true`:
```
.artifacts/
└── test_foo/
    ├── 1/
    │   └── out.txt
    └── 2/
        └── out.txt
```

## Contributing

Contributions are very welcome.

## License

Distributed under the terms of the [MIT](https://opensource.org/licenses/MIT) license, "pytest-artifacts" is free and open source software

## Issues

If you encounter any problems, please [file an issue](https://github.com/ketozhang/pytest-artifacts/issues) along with a detailed description.
