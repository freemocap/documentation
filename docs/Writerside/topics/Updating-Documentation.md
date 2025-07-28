# Updating Documentation

* Our documentation uses [JetBrains Writerside](https://www.jetbrains.com/pycharm/) and lives at [https://freemocap.github.io/documentation/](https://freemocap.github.io/documentation/).
* PyCharm can be installed and updated using [JetBrains Toolbox](https://www.jetbrains.com/toolbox-app/).
* These instructions ensure a reliable workflow using that specific toolset.
* Because our documentation builds from a GitHub Actions that triggers from every commit, we require pull requests for all changes.  

> For more about our workflow, refer to [Contributing to the FreeMoCap Project](https://freemocap.github.io/documentation/contributing-index.html).

# If you **ARE NOT** a member of the FreeMoCap organization

1.  In PyCharm, install the Writerside plugin, restart PyCharm, then select the Writerside plugin in the left toolbar. 
2. Fork the repository and clone the forked repository's URL.
    * URL: https://github.com/[YOUR USERNAME]/documentation/
> For more information about forking, refer to [Fork a Repository](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/working-with-forks/fork-a-repo) on GitHub Docs.
4. Use the Writerside formatting style guide: [Markdown vs semantic markup - Writerside Documentation](https://www.jetbrains.com/help/writerside/markup-reference.html)
5. Once you've finished making your updates to documentation, submit a PR onto `main`.

# If you **ARE** a member of the FreeMoCap organization

1. In PyCharm, install the Writerside plugin, restart PyCharm, then select the Writerside plugin in the left toolbar. 
2. Select `Git` → `Clone` from the top menu.
    * URL: [https://github.com/freemocap/documentation/](https://github.com/freemocap/documentation/)
3. Create a branch. 
    * This can be done in PyCharm by clicking `main` in the top left and selecting `+ New Branch`.
4. Use the Writerside formatting style guide: [Markdown vs semantic markup - Writerside Documentation](https://www.jetbrains.com/help/writerside/markup-reference.html)
5. Once you've finished making your updates to documentation, submit a PR onto `main`.