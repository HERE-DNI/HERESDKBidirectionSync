---
title: "getEnvironmentalZoneWarning method - WarningsRegistry class - warner library - Dart API"
slug: "sdk-for-flutter-navigate-warner-warningsregistry-getenvironmentalzonewarning"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- getEnvironmentalZoneWarning.html -->
<div id="sdk-for-flutter-navigate-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-navigate-dartdoc-main-content" class="main-content" data-above-sidebar="warner/WarningsRegistry-class-sidebar.html" data-below-sidebar="">

<div>

# <span class="kind-method">getEnvironmentalZoneWarning</span> abstract method

</div>

<div class="section multi-line-signature">

<span class="returntype"><a href="sdk-for-flutter-navigate-navigation-environmentalzonewarning-class">EnvironmentalZoneWarning</a>?</span> <span class="name">getEnvironmentalZoneWarning</span>(<wbr></wbr>

1.  <span id="sdk-for-flutter-navigate-getEnvironmentalZoneWarning-param-warning" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-warner-warning-class">Warning</a></span> <span class="parameter-name">warning</span></span>

)

</div>

<div class="section desc markdown">

Returns environmental zone warning corresponding to the given identifier.

- `warning` The identifier of the warning, as provided by `WarningListener.onWarning`. The `warning` uniquely identifies a single environmental zone warning within this registry and is used to retrieve its full metadata.

Returns <a href="sdk-for-flutter-navigate-navigation-environmentalzonewarning-class">EnvironmentalZoneWarning?</a>. The <a href="sdk-for-flutter-navigate-navigation-environmentalzonewarning-class">EnvironmentalZoneWarning</a> object associated with the provided `WarningsRegistry.getEnvironmentalZoneWarning.warning`, or `null` if no warning exists for the given `WarningsRegistry.getEnvironmentalZoneWarning.warning`. This object contains the full details and attributes of the corresponding warning.

</div>

## Implementation

``` dart
EnvironmentalZoneWarning? getEnvironmentalZoneWarning(Warning warning);
```

</pre>

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas--> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>

</div>
`
}</HTMLBlock>
