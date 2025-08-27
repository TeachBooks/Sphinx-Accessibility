# Adding accessibility to Sphinx

Sphinx extension that provides accessibility features.

## Introduction

This Sphinx extension provides various accessibility features to enhance the usability of Sphinx-generated books. Features include:

- Support for dyslexic-friendly fonts
- High contrast mode

## Installation
To install the Sphinx-Accessibility extension, follow these steps:

**Step 1: Install the Package**

Install the `Sphinx-Accessibility` package using `pip`:
```
pip install sphinx-accessibility
```

**Step 2: Add to `requirements.txt`**

Make sure that the package is included in your project's `requirements.txt` to track the dependency:
```
sphinx-accessibility
```

**Step 3: Enable in `_config.yml`**

In your `_config.yml` file, add the extension to the list of Sphinx extra extensions:
```
sphinx: 
    extra_extensions:
        - sphinx_accessibility
```

## Features

### Accessibility Menu

The accessibility menu provides a centralized location for users to adjust various accessibility settings, including font size, contrast, and more. The icon for this menu is <svg width="1em" height="1em" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
<style>
    path {
        stroke: black;
    }
    path#head {
        fill: black;
    }
    @media (prefers-color-scheme: dark) {
      path {
        stroke: white;
      }
      path#head {
        fill: white;
      }
    }
  </style>
<path d="M12 22C17.5228 22 22 17.5228 22 12C22 6.47715 17.5228 2 12 2C6.47715 2 2 6.47715 2 12C2 17.5228 6.47715 22 12 22Z" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"/>
<path d="M7 9L12 10M17 9L12 10M12 10V13M12 13L10 18M12 13L14 18" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"/>
<path id="head" d="M12 7C11.7239 7 11.5 6.77614 11.5 6.5C11.5 6.22386 11.7239 6 12 6C12.2761 6 12.5 6.22386 12.5 6.5C12.5 6.77614 12.2761 7 12 7Z" stroke-width="2.0" stroke-linecap="round" stroke-linejoin="round"/>
</svg>.

### Support for dyslexic-friendly fonts

This feature allows users to switch to the dyslexic-friendly font [OpenDyslexic](https://opendyslexic.org/), improving readability for individuals with dyslexia. The font can be toggled on and off using the button <img src="svgs/Font.svg" style="height:1em;vertical-align:text-bottom;"> in the accessibility menu <img src="svgs/Accessibility.svg" style="height:1em;vertical-align:text-bottom;">.

### High contrast mode

This feature allows users to switch to a high contrast mode, improving visibility for individuals with visual impairments. The mode can be toggled on and off using the button <img src="svgs/Contrast.svg" style="height:1em;vertical-align:text-bottom;"> in the accessibility menu <img src="svgs/Accessibility.svg" style="height:1em;vertical-align:text-bottom;">.

The high-contrast mode tries to apply the following changes to the CSS:

- Change text and border colors to black in light-mode and white in dark-mode.
- Change background colors to white in light-mode and black in dark-mode.
- Makes all colors twice as intense.
- In dark-mode only: increases contrast with factor 1.5.

## Example

You can see how the accessibility features work in [this example book](https://teachbooks.io/TU-Delft-Theme-Example/).
