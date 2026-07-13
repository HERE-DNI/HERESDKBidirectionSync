---
title: "setBackgroundLocationAllowed method - LocationEngine class - location library - Dart API"
slug: "sdk-for-flutter-navigate-location-locationengine-setbackgroundlocationallowed"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- setBackgroundLocationAllowed.html -->
<div id="sdk-for-flutter-navigate-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-navigate-dartdoc-main-content" class="main-content" data-above-sidebar="location/LocationEngine-class-sidebar.html" data-below-sidebar="">

<div>

# <span class="kind-method">setBackgroundLocationAllowed</span> method

</div>

<div class="section multi-line-signature">

<span class="returntype"><a href="sdk-for-flutter-navigate-location-locationenginestatus">LocationEngineStatus</a></span> <span class="name">setBackgroundLocationAllowed</span>(<wbr></wbr>

1.  <span id="sdk-for-flutter-navigate-setBackgroundLocationAllowed-param-allowed" class="parameter"><span class="type-annotation">bool</span> <span class="parameter-name">allowed</span></span>

)

<div class="features">

<span class="feature">override</span>

</div>

</div>

<div class="section desc markdown">

On iOS devices this enables or disables application's background location updates. By default background location updates are enabled if application has background location capabilities. Set `allowed` to true to allow background location updates, or false to disable them. Returns <a href="sdk-for-flutter-navigate-location-locationenginestatus">LocationEngineStatus.ok</a> if call succeeds. <a href="sdk-for-flutter-navigate-location-locationenginestatus">LocationEngineStatus.notAllowed</a> if the application does not have background location capabilities enabled.

On Android devices this is not supported and <a href="sdk-for-flutter-navigate-location-locationenginestatus">LocationEngineStatus.notSupported</a> is returned.

</div>

## Implementation

``` dart
LocationEngineStatus setBackgroundLocationAllowed(bool allowed) {
  if (Platform.isIOS) {
    return _location.setBackgroundLocationAllowed(allowed);
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
