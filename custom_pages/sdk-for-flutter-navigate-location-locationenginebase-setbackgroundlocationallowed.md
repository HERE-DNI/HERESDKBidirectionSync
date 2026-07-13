---
title: "setBackgroundLocationAllowed method - LocationEngineBase class - location library - Dart API"
slug: "sdk-for-flutter-navigate-location-locationenginebase-setbackgroundlocationallowed"
---

<div id="sdk-for-flutter-navigate-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-navigate-dartdoc-main-content" class="main-content" data-above-sidebar="location/LocationEngineBase-class-sidebar.html" data-below-sidebar="">

<div>

# <span class="kind-method">setBackgroundLocationAllowed</span> abstract method

</div>

<div class="section multi-line-signature">

<span class="returntype"><a href="sdk-for-flutter-navigate-location-locationenginestatus">LocationEngineStatus</a></span> <span class="name">setBackgroundLocationAllowed</span>(<wbr></wbr>

1.  <span id="sdk-for-flutter-navigate-setBackgroundLocationAllowed-param-allowed" class="parameter"><span class="type-annotation">bool</span> <span class="parameter-name">allowed</span></span>

)

</div>

<div class="section desc markdown">

Enables or disables background location updates for an application.

Defaults to `false`.

- `allowed` Set to `true` to allow background location updates, or `false` to disable them.

Returns <a href="sdk-for-flutter-navigate-location-locationenginestatus">LocationEngineStatus</a>. <a href="sdk-for-flutter-navigate-location-locationenginestatus">LocationEngineStatus.ok</a> if call succeeds. <a href="sdk-for-flutter-navigate-location-locationenginestatus">LocationEngineStatus.notAllowed</a> if the application does not have background location capabilities enabled. <a href="sdk-for-flutter-navigate-location-locationenginestatus">LocationEngineStatus.notSupported</a> on platforms which do not support controlling of background location modes.

</div>

## Implementation

``` dart
LocationEngineStatus setBackgroundLocationAllowed(bool allowed);
```

</pre>

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas--> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>

