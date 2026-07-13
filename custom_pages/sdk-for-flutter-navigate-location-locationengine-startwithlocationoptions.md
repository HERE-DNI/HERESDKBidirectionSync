---
title: "startWithLocationOptions method - LocationEngine class - location library - Dart API"
slug: "sdk-for-flutter-navigate-location-locationengine-startwithlocationoptions"
---

<div id="sdk-for-flutter-navigate-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-navigate-dartdoc-main-content" class="main-content" data-above-sidebar="location/LocationEngine-class-sidebar.html" data-below-sidebar="">

<div>

# <span class="kind-method">startWithLocationOptions</span> method

</div>

<div class="section multi-line-signature">

<span class="returntype"><a href="sdk-for-flutter-navigate-location-locationenginestatus">LocationEngineStatus</a></span> <span class="name">startWithLocationOptions</span>(<wbr></wbr>

1.  <span id="sdk-for-flutter-navigate-startWithLocationOptions-param-locationOptions" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-location-locationoptions-class">LocationOptions</a></span> <span class="parameter-name">locationOptions</span></span>

)

<div class="features">

<span class="feature">override</span>

</div>

</div>

<div class="section desc markdown">

On Android devices starts the location engine with desired <a href="sdk-for-flutter-navigate-location-locationoptions-class">LocationOptions</a>. Make sure to call either <a href="sdk-for-flutter-navigate-location-locationengine-confirmhereprivacynoticeinclusion">LocationEngine.confirmHEREPrivacyNoticeInclusion</a> or <a href="sdk-for-flutter-navigate-location-locationengine-confirmhereprivacynoticeexception">LocationEngine.confirmHEREPrivacyNoticeException</a> beforehand. Returns <a href="sdk-for-flutter-navigate-location-locationenginestatus">LocationEngineStatus.alreadyStarted</a> if <a href="sdk-for-flutter-navigate-location-locationengine-startwithlocationaccuracy">LocationEngine.startWithLocationAccuracy</a> or <a href="sdk-for-flutter-navigate-location-locationengine-startwithlocationoptions">LocationEngine.startWithLocationOptions</a> is called again without calling <a href="sdk-for-flutter-navigate-location-locationengine-stop">LocationEngine.stop</a> in between. See <a href="sdk-for-flutter-navigate-location-locationenginestatus">LocationEngineStatus</a> for other possible return values.

On iOS devices this is not supported and <a href="sdk-for-flutter-navigate-location-locationenginestatus">LocationEngineStatus.notSupported</a> is returned.

</div>

## Implementation

``` dart
LocationEngineStatus startWithLocationOptions(LocationOptions locationOptions) =>
    _location.startWithLocationOptions(locationOptions);
```

</pre>

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas--> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>

