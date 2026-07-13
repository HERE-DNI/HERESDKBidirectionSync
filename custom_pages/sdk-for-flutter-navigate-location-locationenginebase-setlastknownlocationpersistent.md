---
title: "setLastKnownLocationPersistent method - LocationEngineBase class - location library - Dart API"
slug: "sdk-for-flutter-navigate-location-locationenginebase-setlastknownlocationpersistent"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- setLastKnownLocationPersistent.html -->
<div id="sdk-for-flutter-navigate-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-navigate-dartdoc-main-content" class="main-content" data-above-sidebar="location/LocationEngineBase-class-sidebar.html" data-below-sidebar="">

<div>

# <span class="kind-method">setLastKnownLocationPersistent</span> abstract method

</div>

<div class="section multi-line-signature">

<span class="returntype"><a href="sdk-for-flutter-navigate-location-locationenginestatus">LocationEngineStatus</a></span> <span class="name">setLastKnownLocationPersistent</span>(<wbr></wbr>

1.  <span id="sdk-for-flutter-navigate-setLastKnownLocationPersistent-param-persistent" class="parameter"><span class="type-annotation">bool</span> <span class="parameter-name">persistent</span></span>

)

</div>

<div class="section desc markdown">

Enables or disables saving of last known location so that it persists between application sessions.

Defaults to enabled.

- `persistent` Set to `true` to enable last known location to be saved persistently, or `false` to disable it.

Returns <a href="sdk-for-flutter-navigate-location-locationenginestatus">LocationEngineStatus</a>. <a href="sdk-for-flutter-navigate-location-locationenginestatus">LocationEngineStatus.ok</a> if call succeeds. <a href="sdk-for-flutter-navigate-location-locationenginestatus">LocationEngineStatus.notSupported</a> on platforms which do not support controlling of last known location saving.

</div>

## Implementation

``` dart
LocationEngineStatus setLastKnownLocationPersistent(bool persistent);
```

</pre>

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas--> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>

</div>
`
}</HTMLBlock>
