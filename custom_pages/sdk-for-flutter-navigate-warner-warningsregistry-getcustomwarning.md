---
title: "getCustomWarning method - WarningsRegistry class - warner library - Dart API"
slug: "sdk-for-flutter-navigate-warner-warningsregistry-getcustomwarning"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- getCustomWarning.html -->
<div id="sdk-for-flutter-navigate-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-navigate-dartdoc-main-content" class="main-content" data-above-sidebar="warner/WarningsRegistry-class-sidebar.html" data-below-sidebar="">

<div>

# <span class="kind-method">getCustomWarning</span> abstract method

</div>

<div class="section multi-line-signature">

<span class="returntype"><a href="sdk-for-flutter-navigate-warner-customwarning-class">CustomWarning</a>?</span> <span class="name">getCustomWarning</span>(<wbr></wbr>

1.  <span id="sdk-for-flutter-navigate-getCustomWarning-param-warning" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-warner-warning-class">Warning</a></span> <span class="parameter-name">warning</span></span>

)

</div>

<div class="section desc markdown">

Returns additional data associated with the given custom warning.

The provided `WarningsRegistry.getCustomWarning.warning` identifies a specific custom warning instance by its base warning information and custom warning type. This information is used to resolve the corresponding entry in the warning registry and retrieve any additional, type-specific data associated with the warning.

- `warning` The <a href="sdk-for-flutter-navigate-warner-warning-class">Warning</a> instance identifying the custom warning for which additional data should be retrieved.

Returns <a href="sdk-for-flutter-navigate-warner-customwarning-class">CustomWarning?</a>. The `CustomWarning` associated with the given `WarningsRegistry.getCustomWarning.warning`, or `null` if no additional data exists for this warning. The returned object contains the payload with type-specific details and attributes of the corresponding warning.

**Note:** This is a beta release of this feature, so there could be a few bugs and unexpected behaviors. Related APIs may change for new releases without a deprecation process.

</div>

## Implementation

``` dart
CustomWarning? getCustomWarning(Warning warning);
```

</pre>

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas--> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>

</div>
`
}</HTMLBlock>
