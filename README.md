# svgtoscode

`svgtoscode` converts SVGs to S-code.

## What is S-code?

Several times I've been working on a project that needs *almost* SVGs, but with a few differences:

- only paths and polygons
- only straight paths; Bezier curves can be "dithered" down to many straight segments

To make it as easy to parse as possible, I wanted to output something similar to G-code, which is why I named my version S-code (the S stands for stupid).