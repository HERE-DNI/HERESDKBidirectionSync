---
title: "setLastKnownLocationPersistent method - LocationEngine class - location library - Dart API"
slug: "sdk-for-flutter-navigate-location-locationengine-setlastknownlocationpersistent"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- setLastKnownLocationPersistent.html -->
<div id="sdk-for-flutter-navigate-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-navigate-dartdoc-main-content" class="main-content" data-above-sidebar="location/LocationEngine-class-sidebar.html" data-below-sidebar="">

<div>

# <span class="kind-method">setLastKnownLocationPersistent</span> method

</div>

<div class="section multi-line-signature">

<span class="returntype"><a href="sdk-for-flutter-navigate-location-locationenginestatus">LocationEngineStatus</a></span> <span class="name">setLastKnownLocationPersistent</span>(<wbr></wbr>

1.  <span id="sdk-for-flutter-navigate-setLastKnownLocationPersistent-param-persistent" class="parameter"><span class="type-annotation">bool</span> <span class="parameter-name">persistent</span></span>

)

<div class="features">

<span class="feature">override</span>

</div>

</div>

<div class="section desc markdown">

On Android devices this enables or disables saving of last known location so that it persists across application sessions. By default persistent saving across sessions is enabled. Set `persistent` to true to enable last known location to persist across application sessions, or false to disable it. When calling this method then <a href="sdk-for-flutter-navigate-location-locationenginestatus">LocationEngineStatus.ok</a> is returned.

On iOS devices this is not supported and the value is stored, by default, across sessions. When calling this method then <a href="sdk-for-flutter-navigate-location-locationenginestatus">LocationEngineStatus.notSupported</a> is returned.

</div>

## Implementation

``` dart
LocationEngineStatus setLastKnownLocationPersistent(bool persistent)  {
  if (Platform.isAndroid) {
    return _location.setLastKnownLocationPersistent(persistent);
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
