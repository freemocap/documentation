# Doc Page Templates

######## BEGIN `Starter` Template
# Starter

<!--Writerside adds this topic when you create a new documentation project.
You can use it as a sandbox to play with Writerside features, and remove it from the TOC when you don't need it anymore.-->

## Add new topics
You can create empty topics, or choose a template for different types of content that contains some boilerplate structure to help you get started:

![Create new topic options](new_topic_options.png){ width=290 }{border-effect=line}

## Write content
%product% supports two types of markup: Markdown and XML.
When you create a new help article, you can choose between two topic types, but this doesn't mean you have to stick to a single format.
You can author content in Markdown and extend it with semantic attributes or inject entire XML elements.

## Inject XML
For example, this is how you inject a procedure:

<procedure title="Inject a procedure" id="inject-a-procedure">
    <step>
        <p>Start typing and select a procedure type from the completion suggestions:</p>
        <img src="completion_procedure.png" alt="completion suggestions for procedure" border-effect="line"/>
    </step>
    <step>
        <p>Press <shortcut>Tab</shortcut> or <shortcut>Enter</shortcut> to insert the markup.</p>
    </step>
</procedure>

## Add interactive elements

### Tabs
To add switchable content, you can make use of tabs (inject them by starting to type `tab` on a new line):

<tabs>
    <tab title="Markdown">
        <code-block lang="plain text">![Alt Text](new_topic_options.png){ width=450 }</code-block>
    </tab>
    <tab title="Semantic markup">
        <code-block lang="xml">
            <![CDATA[<img src="new_topic_options.png" alt="Alt text" width="450px"/>]]></code-block>
    </tab>
</tabs>

### Collapsible blocks
Apart from injecting entire XML elements, you can use attributes to configure the behavior of certain elements.
For example, you can collapse a chapter that contains non-essential information:

#### Supplementary info {collapsible="true"}
Content under a collapsible header will be collapsed by default,
but you can modify the behavior by adding the following attribute:
`default-state="expanded"`

### Convert selection to XML
If you need to extend an element with more functions, you can convert selected content from Markdown to semantic markup.
For example, if you want to merge cells in a table, it's much easier to convert it to XML than do this in Markdown.
Position the caret anywhere in the table and press <shortcut>Alt+Enter</shortcut>:

<img src="convert_table_to_xml.png" alt="Convert table to XML" width="706" border-effect="line"/>

## Feedback and support
Please report any issues, usability improvements, or feature requests to our
<a href="https://youtrack.jetbrains.com/newIssue?project=WRS">YouTrack project</a>
(you will need to register).

You are welcome to join our
<a href="https://jb.gg/WRS_Slack">public Slack workspace</a>.
Before you do, please read our [Code of conduct](https://plugins.jetbrains.com/plugin/20158-writerside/docs/writerside-code-of-conduct.html).
We assume that you’ve read and acknowledged it before joining.

You can also always email us at [writerside@jetbrains.com](mailto:writerside@jetbrains.com).

<seealso>
    <category ref="wrs">
        <a href="https://plugins.jetbrains.com/plugin/20158-writerside/docs/markup-reference.html">Markup reference</a>
        <a href="https://plugins.jetbrains.com/plugin/20158-writerside/docs/manage-table-of-contents.html">Reorder topics in the TOC</a>
        <a href="https://plugins.jetbrains.com/plugin/20158-writerside/docs/local-build.html">Build and publish</a>
        <a href="https://plugins.jetbrains.com/plugin/20158-writerside/docs/configure-search.html">Configure Search</a>
    </category>
</seealso>
######## END `Starter` Template

######## Begin `Overview` Template
# Overview

Overview articles give background information and provide context to a particular subject.
Their goal is to explain a concept, not to teach or give instructions.

## What is product/service/concept

Provide some background and context, explain choices and alternatives.

## Glossary

A definition list or a glossary:

First Term
: This is the definition of the first term.

Second Term
: This is the definition of the second term.
######## END `Overview` Template

######## BEGIN `How To` Template
# `How to` Template

A How-to article is an action-oriented type of document.
It explains how to perform a specific task or solve a problem, and usually contains a sequence of steps.
Start with a short introductory paragraph that explains what users will accomplish by following this procedure,
what they need to perform it for, or define the target audience of the doc.

> **Highlight important information**
>
> You can change the element to *tip* or *warning* by renaming the style attribute below.
>
{style="note"}

## Before you start

It is good practice to list the prerequisites that are required or recommended.

Make sure that:
- First prerequisite
- Second prerequisite

## How to perform a task

Some introductory information.

1. Step with a code block

   ```bash
    run this --that
   ```

2. Step with a [link](https://www.jetbrains.com)

3. Step with a list.
   - List item
   - List item
   - List item

######## END `How To` Template


######## BEGIN `Section Starting Page` Tempate
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE topic
        SYSTEM "https://resources.jetbrains.com/writerside/1.0/xhtml-entities.dtd">
<topic xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
       xsi:noNamespaceSchemaLocation="https://resources.jetbrains.com/writerside/1.0/topic.v2.xsd"
       title="Section Starting Page" id="Section-Starting-Page">

<!--    A section combines multiple topics dedicated to a specific subject.
            Add a starting page to provide an overview of the topics in the section.
            Start with two topics you want to promote in the <spotlight> group,
            several important topics in the <primary> group (for example, where to start),
            several less important topics in the <secondary> group (for example, more advanced topics),
            and optionally add any other relevant topics in the <misc> group as cards and lists of links
            (maybe related topics from other sections).
            Only the spotlight section is limited to two topics.
            For other groups, try to keep the number between 2 and 6, but you can add more if necessary.-->

    <section-starting-page>
        <title>Section starting page title</title>
        <description>
            Add an introductory paragraph: explain what this section is about in 2-3 short sentences.
        </description>

        <!--    Add up to 2 topics that you want to promote. Use the "type" attribute to select an icon.    -->
        <spotlight>
            <a href="" type="account" summary="This overrides the card summary of the topic">Custom card title</a>
            <a href="" type="search" summary="This overrides the card summary of the topic">Another custom title</a>
        </spotlight>

        <!--    Add several topics that are most important for this section.    -->
        <primary>
            <title>Get started</title>
            <a href=""/>
            <a href="" summary="With a custom card summary"/>
            <a href="">Custom card title</a>
            <a href="" summary="With a custom card summary">Custom card title</a>
        </primary>

        <!--    Add several topics that are less important or are relevant only for advanced/experienced users.    -->
        <secondary>
            <title>Explore advanced features</title>
            <a href=""/>
            <a href="" summary="With a custom card summary"/>
            <a href="">Custom card title</a>
            <a href="" summary="With a custom card summary">Custom card title</a>
        </secondary>

        <!--    Optionally add additional cards and links to topics that are not in this section but may be relevant.    -->
        <misc>
            <cards>
                <title>Other relevant topics as wide cards</title>
                <a href=""/>
                <a href="" summary="With a custom card summary"/>
                <a href="">Custom card title</a>
                <a href="" summary="With a custom card summary">Custom card title</a>
            </cards>

            <cards narrow="true">
                <title>Other relevant topics as narrow cards</title>
                <a href=""/>
                <a href=""/>
                <a href="" summary="With a custom card summary"/>
                <a href="">Custom card title</a>
                <a href="">Custom card title</a>
                <a href="" summary="With a custom card summary">Custom card title</a>
            </cards>

            <links>
                <group>
                    <title>Other related topics as links</title>
                    <a href=""/>
                    <a href="" summary="With a custom card summary"/>
                    <a href="">Custom card title</a>
                    <a href="" summary="With a custom card summary">Custom card title</a>
                </group>
                <group>
                    <title>Two in a row</title>
                    <a href=""/>
                    <a href="" summary="With a custom card summary"/>
                    <a href="">Custom card title</a>
                    <a href="" summary="With a custom card summary">Custom card title</a>
                </group>
            </links>

            <links narrow="true">
                <group>
                    <title>More related topics</title>
                    <a href=""/>
                    <a href="" summary="With a custom card summary"/>
                    <a href="">Custom card title</a>
                    <a href="" summary="With a custom card summary">Custom card title</a>
                </group>
                <group>
                    <title>Three in a row</title>
                    <a href=""/>
                    <a href=""/>
                    <a href="">Custom card title</a>
                    <a href="">Custom card title</a>
                </group>
                <group>
                    <title>Each group is narrow</title>
                    <a href=""/>
                    <a href=""/>
                    <a href="">Custom card title</a>
                    <a href="">Custom card title</a>
                </group>
            </links>
        </misc>
    </section-starting-page>

</topic>
######## END `Section Starting Page` Tempate