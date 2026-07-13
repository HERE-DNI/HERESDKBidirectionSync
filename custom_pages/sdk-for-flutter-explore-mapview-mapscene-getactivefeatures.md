---
title: "getActiveFeatures method - MapScene class - mapview library - Dart API"
slug: "sdk-for-flutter-explore-mapview-mapscene-getactivefeatures"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- getActiveFeatures.html -->
<div id="sdk-for-flutter-explore-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-explore-dartdoc-main-content" class="main-content" data-above-sidebar="mapview/MapScene-class-sidebar.html" data-below-sidebar="">

<div>

# <span class="kind-method">getActiveFeatures</span> abstract method

</div>

<div class="section multi-line-signature">

<span class="returntype">Map<span class="signature">\<<wbr></wbr><span class="type-parameter">String</span>, <span class="type-parameter">String</span>\></span></span> <span class="name">getActiveFeatures</span>(<wbr></wbr>)

</div>

<div class="section desc markdown">

Gets map features that are currently active.

Active features are features that are either enabled via a call to <a href="sdk-for-flutter-explore-mapview-mapscene-enablefeatures">MapScene.enableFeatures</a> or that are enabled by default in the scene.

The key to the resulting map is the name of the feature and the value is the active mode.

Result is empty if scene has not been loaded.

Returns `Map<String, String>`. The map of active features.

</div>

## Implementation

``` dart
Map<String, String> getActiveFeatures();
```

</pre>

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas--> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>

</div>
`
}</HTMLBlock>
