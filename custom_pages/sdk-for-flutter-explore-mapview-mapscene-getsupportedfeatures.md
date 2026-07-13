---
title: "getSupportedFeatures method - MapScene class - mapview library - Dart API"
slug: "sdk-for-flutter-explore-mapview-mapscene-getsupportedfeatures"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- getSupportedFeatures.html -->
<div id="sdk-for-flutter-explore-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-explore-dartdoc-main-content" class="main-content" data-above-sidebar="mapview/MapScene-class-sidebar.html" data-below-sidebar="">

<div>

# <span class="kind-method">getSupportedFeatures</span> abstract method

</div>

<div class="section multi-line-signature">

<span class="returntype">Map<span class="signature">\<<wbr></wbr><span class="type-parameter">String</span>, <span class="type-parameter">List<span class="signature">\<<wbr></wbr><span class="type-parameter">String</span>\></span></span>\></span></span> <span class="name">getSupportedFeatures</span>(<wbr></wbr>)

</div>

<div class="section desc markdown">

Gets features and all of their modes supported by the currently loaded scene configuration.

The key to the resulting map is the name of the feature and the value is a list of modes for that feature.

Result is empty if scene has not been loaded.

Returns `Map<String, List<String>>`. The map of supported features and all their modes.

</div>

## Implementation

``` dart
Map<String, List<String>> getSupportedFeatures();
```

</pre>

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas--> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>

</div>
`
}</HTMLBlock>
