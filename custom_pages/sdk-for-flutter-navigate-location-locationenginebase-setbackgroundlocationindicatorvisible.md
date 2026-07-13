---
title: "setBackgroundLocationIndicatorVisible method - LocationEngineBase class - location library - Dart API"
slug: "sdk-for-flutter-navigate-location-locationenginebase-setbackgroundlocationindicatorvisible"
---

<div id="sdk-for-flutter-navigate-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-navigate-dartdoc-main-content" class="main-content" data-above-sidebar="location/LocationEngineBase-class-sidebar.html" data-below-sidebar="">

<div>

# <span class="kind-method">setBackgroundLocationIndicatorVisible</span> abstract method

</div>

<div class="section multi-line-signature">

<span class="returntype"><a href="sdk-for-flutter-navigate-location-locationenginestatus">LocationEngineStatus</a></span> <span class="name">setBackgroundLocationIndicatorVisible</span>(<wbr></wbr>

1.  <span id="sdk-for-flutter-navigate-setBackgroundLocationIndicatorVisible-param-visible" class="parameter"><span class="type-annotation">bool</span> <span class="parameter-name">visible</span></span>

)

</div>

<div class="section desc markdown">

Controls visibility of application's background location indicator.

By default background location indicator is visible, if application has background location capabilities.

- `visible` Set to `true` to show background location indicator, or `false` to hide it.

Returns <a href="sdk-for-flutter-navigate-location-locationenginestatus">LocationEngineStatus</a>. <a href="sdk-for-flutter-navigate-location-locationenginestatus">LocationEngineStatus.ok</a> if call succeeds. <a href="sdk-for-flutter-navigate-location-locationenginestatus">LocationEngineStatus.notAllowed</a> if the application does not have background location capabilities enabled. <a href="sdk-for-flutter-navigate-location-locationenginestatus">LocationEngineStatus.notSupported</a> on platforms which do not support controlling of background location indicator visibility.

</div>

## Implementation

``` dart
LocationEngineStatus setBackgroundLocationIndicatorVisible(bool visible);
```

</pre>

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas--> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>

