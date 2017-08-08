# svgtoscode

`svgtoscode` converts SVGs to S-code.

## What is S-code?

Several times I've been working on a project that needs *almost* SVGs, but with a few differences:

- only paths and polygons
- only straight paths; Bezier curves can be "dithered" down to many straight segments
- stupid simple line-based parsing

I wanted to output something similar to G-code, which is why I named my version S-code (the S stands for stupid).

## Usage

    svg2scode original.svg > out.scode  # outputs to stdout

## Example

S-code looks like [this](https://gist.github.com/milkey-mouse/10139c21f24e2940b7eeba48ee1536b7).

There's no spec because I will probably change it as soon as a project needs another property from the SVGs ¯\\_(ツ)_/¯
