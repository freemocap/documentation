`# documentation

Documentation for FreeMoCap

Read the Docs badge - [![Documentation Status](https://readthedocs.org/projects/freemocap/badge/?version=latest)](https://freemocap.readthedocs.io/en/latest/?badge=latest)


 - This repository is connected to a static site at - https://freemocap.readthedocs.io
     - ReadTheDocs is a popular tool to host software documentation
 - Whenever there is a commit to the `main` branch of this repository, `read-the-docs` will attempt to build a new version of the documentation site from the markdown files in the `/docs/` folder using `mkdocs`
     - `mkdocs` is a static site generator that builds websites from markdown files, configured via the `mkdocs.yml` file in this repository
     - For more information on how this works, checkout the mkdocs website - https://mkdocs.org
     - Specifically, we are using the 'material mkdocs' theme, described here - https://squidfunk.github.io/mkdocs-material/

___
# Style Guide

This is a work in progress :)

The goal is to create a consistent style across all parts of the docs to create what I, Trent, am calling "semantic continuity" in how we communicate to our users. Semantic continuity means that the meaning of various symbols and text formatting is consistent across our documentation.
- This could be as small as making sure that there are periods at the end of every sentence, even in bullet points.
- Or it could be as big as making sure that [Admonitions](https://squidfunk.github.io/mkdocs-material/reference/admonitions/), or "call-outs", are used in the same way across the docs.

## [Admonitions](https://squidfunk.github.io/mkdocs-material/reference/admonitions/) - AKA Call-Outs
Our docs currently employ `6` types of Admonitions. The four which we have customized which can be found in `/stylesheets/extra.css`, and the other standard styles of admonitions can be found in [here](https://squidfunk.github.io/mkdocs-material/reference/admonitions/#supported-types).

Each of the Admonitions have a unique aesthetic and serve a specific purpose:

`tip-full-width`
- Description: Blueish box with white sparkle skelly icon. This is a custom Admonition.
- Purpose: Provide freemocap-specific tips, for example, in "How to process pre-recorded synchronized videos with `alpha` GUI", the `tip-full-width` helps folks who are trying to post-process videos they had recorded with using the `pre-alpha`.

![tip-full-width](https://user-images.githubusercontent.com/62706609/202797425-e0d0ec64-7752-4aeb-a76e-a39dd671be9f.png)
> Developer Note: `tip-full-width` should be renamed.

`take-note`
- Description: Greenish box with a dark green pencil icon. This is a custom Admonition.
- Purpose: Provide useful notes that are relevant to the page that the viewer is on. This call-out is important for helping folks stay on the ["happy path"](https://en.wikipedia.org/wiki/Happy_path) of getting the task they came here to do, done.

![take-note_admonition](https://user-images.githubusercontent.com/62706609/202797519-31d45917-568c-40f4-9978-a6f2a2205177.png)

`blender`
- Description: Creamsicle-orange box with black [Blender](https://www.google.com/search?client=firefox-b-1-d&q=blender) logo. This is a custom Admonition.
- Purpose: Provide information connecting freemocap to Blender. This could be linking to a Blender tutorial, or linking to the Blender download page. Blender is cool!

![blender_admonition](https://user-images.githubusercontent.com/62706609/202797532-8cf8f03b-14de-4725-9c5d-933a70329000.png)

`finished`
- Description: Bright-pink box with a white happy skull icon. This is a custom Admonition.
- Purpose: The purpose of this Admonition is to congratulate users for finishing a How-To or a Tutorial, and provide them with next steps.

![finished_admonition](https://user-images.githubusercontent.com/62706609/202797567-d03ec289-8e66-4577-b831-1cd4ab4f6374.png)

`info`
- Description: Bright blue box with a bright blue circle with the letter `i` cut out as the icon. This Admonition is one of the default call-outs from `Material for MkDocs`.
- Purpose: To provide the user with tangential, but interesting information that could be useful the the task at hand. If opened, this could easily lead the user down a rabbit hole; `info` admonitions should always be presented closed & openable by the user, implementing them in the `.md` files with `???` instead of the standard `!!!` for an open admonition.

![info_admonition](https://user-images.githubusercontent.com/62706609/202797755-e8bd7d78-5ddd-412a-8084-b0e5e20e9186.png)

`warning`
- Description: Bright orange box with an orange triangle with an `!` inside of it. This Admonition is one of the default call-outs from `Material for MkDocs`.
- Purpose: We use this call-out to clearly warn users of potential pitfalls. If this were a perfect software, we probably wouldn't have these. But it's not! And that's okay :) These call-outs will save us issue-posts.
- Styling note: the shown text for warnings should always being with `Warning:`, and be proceeded by a detailed explanation that clearly tells the user what to avoid, or make sure they do.

![warning_admonition](https://user-images.githubusercontent.com/62706609/202797732-7d7e8556-5d9e-4008-907e-bce50fb272c6.png)




