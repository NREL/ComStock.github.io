# ComStock.github.io

## Markdown Notes

### Highlight Callout Box 

To add a "highlight" box (blue callout box), add the following line directly before the text that you want to appear in the box. 

```
{: .highlight }
This is the text that you want to appear in the box. Dont add a blank line before the text.
```

If you want multiple paragraphs in the callout box, add `>` in front of each line:

```
{: .highlight }
> Hello
>
> This is a multi-paragraph
>
> box!
```

If you want the callout box to have a title, just use `{: .highlight-title }` instead. The first `>` line will be used as the title.

### Warning Callout box

To add a "warning" box (orange callout box), add the following line directly before the text that you want to appear in the box.

```
{: .warning }
This is the text that you want to appear in the box
```

If you want the callout box to have a title, just use `{: .warning-title }` instead. The first `>` line will be used as the title.

### Collapsible Section

Below is an example of a collapsible section.  The section is wrapped with `<details></details> tags`.  The `<summary></summary>` section contains the title of the section, which will be visible when the section is both collapsed or expanded.  The hidden section follows. If the section should be open by default, include the word `open` in the `<details>` tag. If the section should be collapsed by default, do not include the word `open`.

```
<details open markdown="block">
  <summary>
    A collapsed section Title
  </summary>
  This is some text that will be revealed when the section is expanded
</details>
```