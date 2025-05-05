# Lib-version

`lib-version` is a version-aware Python library. It keeps track of its own version when requested.

## 📚 Table of Contents

- [Installation and Development](#-installationanddevelopment)
- [🛠 Requirements](#-requirements)
- [⚙️ GitHub Actions & CI/CD](#️-github-actions--cicd)

## [Installation and Development](#-installationanddevelopment)

To install the library, use the following command:

```bash
pip install .
```
To set up a development environment, install the optional build tools:

```bash
pip install -r requirements.txt
```

## [🛠 Requirements](#-requirements)

The library requires Python 3.10.

## [⚙️ GitHub Actions & CI/CD](#️-github-actions--cicd)
We use **GitHub Actions** to automate our entire CI/CD pipeline. Key aspects include:

- **Automated builds:** Every push to `main` and `develop` triggers the CI workflow to build the code.
- **Docker image publishing:** Our workflows build Docker images for both `app` and `model-service` and push them to GHCR under:
    - `ghcr.io/remla25-team17/app:<version>`
    - `ghcr.io/remla25-team17/model-service:<version>`
- **Versioning:** We use **GitVersion** to automate semantic versioning based on Git history and branch naming conventions. This ensures:
    - Stable releases for `main`
    - Pre-releases (e.g., `canary` tags) for `develop` and feature branches.
- **Release automation:** New releases are automatically published to GitHub Releases with changelogs and contributor lists, ensuring traceability.

## Contact

For any questions or issues, please contact the maintainers of the repository.