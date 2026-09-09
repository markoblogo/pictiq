# Parametric COLOR prototype

COLOR is a value-bearing protocol mechanism, not a lexical `red`, `blue`, or `green` icon. A rendered instance uses the canonical Pictiq frame and one large filled circle as the value field.

Conceptual machine form:

```json
{"type": "color", "value": "#ff0000"}
```

The same geometry can carry any requested color, such as `#ff0000`, `#264653`, or `#747b72`. This is the intentional exception to the normal monochrome rule because color itself is the payload. A grayscale reproduction cannot preserve hue; it can preserve only a luminance/lightness relationship, where sufficiently different values may remain distinguishable.

The prototype is not canonical lexicon vocabulary and has no ordinary icon ID. Use [`tools/render_color_param.py`](../tools/render_color_param.py) to produce deterministic demonstration SVGs and a grayscale comparison in `build/qa/`.
