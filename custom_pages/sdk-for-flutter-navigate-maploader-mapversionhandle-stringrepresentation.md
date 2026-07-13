---
title: "stringRepresentation method - MapVersionHandle class - maploader library - Dart API"
slug: "sdk-for-flutter-navigate-maploader-mapversionhandle-stringrepresentation"
---

<div id="sdk-for-flutter-navigate-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-navigate-dartdoc-main-content" class="main-content" data-above-sidebar="maploader/MapVersionHandle-class-sidebar.html" data-below-sidebar="">

<div>

# <span class="kind-method">stringRepresentation</span> abstract method

</div>

<div class="section multi-line-signature">

<span class="returntype">String</span> <span class="name">stringRepresentation</span>(<wbr></wbr>

1.  <span id="sdk-for-flutter-navigate-stringRepresentation-param-separator" class="parameter"><span class="type-annotation">String</span> <span class="parameter-name">separator</span></span>

)

</div>

<div class="section desc markdown">

Returns a string representation of the map version in the format "\[cache-version\]\[separator\]\[offline-maps-version\], \[japan-cache-version\]\[separator\]\[japan-offline-maps-version\]", which can be obtained via `sdk.maploader.MapUpdater`.

- `separator` Separator being used between elements of the map version. In case map version has single element to it, separator is not used. `none` token is used, when it is not possible to determine the version of the map.

Examples:

- separator=", " possible result is "8.10, 9.10"
- separator="." possible result is "8.10.9.10"
- separator="; " possible result is "8.10; 9.10"
- separator="; " possible result is "8.10"

Returns `String`. A string representation of the map version in the format

</div>

## Implementation

``` dart
String stringRepresentation(String separator);
```

</pre>

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas--> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>

