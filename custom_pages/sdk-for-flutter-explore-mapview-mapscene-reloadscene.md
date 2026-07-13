---
title: "reloadScene method - MapScene class - mapview library - Dart API"
slug: "sdk-for-flutter-explore-mapview-mapscene-reloadscene"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- reloadScene.html -->
<div id="sdk-for-flutter-explore-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-explore-dartdoc-main-content" class="main-content" data-above-sidebar="mapview/MapScene-class-sidebar.html" data-below-sidebar="">

<div>

# <span class="kind-method">reloadScene</span> abstract method

</div>

<div class="section multi-line-signature">

<span class="returntype">void</span> <span class="name">reloadScene</span>(<wbr></wbr>)

</div>

<div class="section desc markdown">

Asynchronously reloads the current map scene from file.

This skips any cached data used internally and reloads the scene including any changes made to the (custom) map styles in JSON.

`MapFeature` settings will be preserved.

Internal optimization checks will be skipped to ensure all custom style changes are loaded. Therefore, calling this method may take slightly longer than calling one of the

    loadScene(..)

overloads.
</p>

</div>

## Implementation

``` dart
void reloadScene();
```

</pre>

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas--> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>

</div>
`
}</HTMLBlock>
