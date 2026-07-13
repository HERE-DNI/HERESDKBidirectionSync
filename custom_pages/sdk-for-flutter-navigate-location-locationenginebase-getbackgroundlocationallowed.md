---
title: "getBackgroundLocationAllowed method - LocationEngineBase class - location library - Dart API"
slug: "sdk-for-flutter-navigate-location-locationenginebase-getbackgroundlocationallowed"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- getBackgroundLocationAllowed.html -->
<div id="sdk-for-flutter-navigate-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-navigate-dartdoc-main-content" class="main-content" data-above-sidebar="location/LocationEngineBase-class-sidebar.html" data-below-sidebar="">

<div>

# <span class="kind-method">getBackgroundLocationAllowed</span> abstract method

</div>

<div class="section multi-line-signature">

<span class="returntype">bool</span> <span class="name">getBackgroundLocationAllowed</span>(<wbr></wbr>)

</div>

<div class="section desc markdown">

Check if application's background location updates are enabled.

Returns `false` on platforms which do not support controlling of background location modes using <a href="sdk-for-flutter-navigate-location-locationenginebase-setbackgroundlocationallowed">LocationEngineBase.setBackgroundLocationAllowed</a> method.

Returns `bool`. `True` if background location updates are allowed, `false` otherwise.

</div>

## Implementation

``` dart
bool getBackgroundLocationAllowed();
```

</pre>

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas--> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>

</div>
`
}</HTMLBlock>
