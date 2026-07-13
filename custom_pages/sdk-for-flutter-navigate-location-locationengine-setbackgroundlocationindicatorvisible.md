---
title: "setBackgroundLocationIndicatorVisible method - LocationEngine class - location library - Dart API"
slug: "sdk-for-flutter-navigate-location-locationengine-setbackgroundlocationindicatorvisible"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- setBackgroundLocationIndicatorVisible.html -->
<div id="sdk-for-flutter-navigate-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-navigate-dartdoc-main-content" class="main-content" data-above-sidebar="location/LocationEngine-class-sidebar.html" data-below-sidebar="">

<div>

# <span class="kind-method">setBackgroundLocationIndicatorVisible</span> method

</div>

<div class="section multi-line-signature">

<span class="returntype"><a href="sdk-for-flutter-navigate-location-locationenginestatus">LocationEngineStatus</a></span> <span class="name">setBackgroundLocationIndicatorVisible</span>(<wbr></wbr>

1.  <span id="sdk-for-flutter-navigate-setBackgroundLocationIndicatorVisible-param-visible" class="parameter"><span class="type-annotation">bool</span> <span class="parameter-name">visible</span></span>

)

<div class="features">

<span class="feature">override</span>

</div>

</div>

<div class="section desc markdown">

On iOS devices this controls visibility of application's background location indicator. By default background location indicator is visible, if application has background location capabilities. Set `visible` to true to show background location indicator, or false to hide it. Returns <a href="sdk-for-flutter-navigate-location-locationenginestatus">LocationEngineStatus.ok</a> if call succeeds and <a href="sdk-for-flutter-navigate-location-locationenginestatus">LocationEngineStatus.notAllowed</a> if the application does not have background location capabilities enabled.

On Android devices this is not supported and <a href="sdk-for-flutter-navigate-location-locationenginestatus">LocationEngineStatus.notSupported</a> is returned.

</div>

## Implementation

``` dart
LocationEngineStatus setBackgroundLocationIndicatorVisible(bool visible) {
  if (Platform.isIOS) {
    return _location.setBackgroundLocationIndicatorVisible(visible);
  }
  return LocationEngineStatus.notSupported;
}
```

</pre>

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas--> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>

</div>
`
}</HTMLBlock>
