# Pre-registered coding rules

## Success by comparison

| Test | Exact | Practically correct | Partial | Incorrect |
|---|---|---|---|---|
| Quantity | Says 3. | Clearly expects three units. | — | 2, 4, several, unknown or another quantity. |
| Availability | Asks whether water is available/possessed. | Would provide water or state availability. | Recognizes water plus a question but not availability. | Unrelated message. |
| Location | Asks where the toilet is. | Indicates/shows toilet location. | Recognizes toilet plus question but cannot state requested information. | Unrelated message. |

## Error taxonomy

`VISUAL_RECOGNITION_ERROR`, `QUANTITY_DECODING_ERROR`, `QUESTION_NOT_RECOGNIZED`, `QUESTION_SCOPE_ERROR`, `AVAILABILITY_NOT_RECOVERED`, `LOCATION_NOT_RECOVERED`, `OVER_SPECIFICATION`, `UNDER_SPECIFICATION`, `CONTEXTUALLY_CORRECT`, `EXACTLY_CORRECT`, `PRACTICALLY_SUCCESSFUL_BUT_SEMANTICALLY_INEXACT`, `NO_INTERPRETATION`, `HALLUCINATED_RELATION`.

Code practical success separately from exact semantic recovery. A verbal answer may include several codes. Do not infer success from confidence alone.
