# documentation
Documentation for FreeMoCap

read the docs badge - [![Documentation Status](https://readthedocs.org/projects/freemocap/badge/?version=latest)](https://freemocap.readthedocs.io/en/latest/?badge=latest)


 - This repository is connected to a static site at - https://freemocap.readthedocs.io
     - ReadTheDocs is a popular tool to host software documentation
 - Whenever there is a commit to the `main` branch of this repository, `read-the-docs` will attempt to build a new version of the documentation site from the markdown files in the `/docs/` folder using `mkdocs`
     - `mkdocs` is a static site generator that builds websites from markdown files, configured via the `mkdocs.yml` file in this repository
     - For more information on how this works, checkout the mkdocs website - https://mkdocs.org
     - Specifically, we are using the 'material mkdocs' theme, described here - https://squidfunk.github.io/mkdocs-material/

test
