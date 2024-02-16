# documentation

Documentation for FreeMoCap


 - This repository is connected to a static site at - https://freemocap.github.io/documentation
 - Whenever there is a commit to the `main` branch of this repository, a github action will attempt to build a new version of the documentation site from the markdown files in the `/docs/` folder using `mkdocs`
     - `mkdocs` is a static site generator that builds websites from markdown files, configured via the `mkdocs.yml` file in this repository
     - For more information on how this works, checkout the mkdocs website - https://mkdocs.org
     - Specifically, we are using the 'material mkdocs' theme, described here - https://squidfunk.github.io/mkdocs-material/

___

# Style Guide

This is a work in progress :) 

> `2024-02-15` We're currently in the process of switching from Material MkDocs to WriterSide for our documentation tool. To avoid confusion, we're deleting content from this README that specifically was tied to Material MkDocs, and will fill out our style guide in the future with information that is relevant to our doc style in WriterSide.

The goal is to create a consistent style across all parts of the docs to create what Trent is calling "semantic continuity" in how we communicate to our users. Semantic continuity means that the meaning of various symbols and text formatting is consistent across our documentation.
- This could be as small as making sure that there are periods at the end of every sentence, even in bullet points.
- Or it could be as big as making sure that admonitions or "call-outs", are used in the same way across the docs.





