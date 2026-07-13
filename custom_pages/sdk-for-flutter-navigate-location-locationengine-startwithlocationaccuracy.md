---
title: "startWithLocationAccuracy method - LocationEngine class - location library - Dart API"
slug: "sdk-for-flutter-navigate-location-locationengine-startwithlocationaccuracy"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- startWithLocationAccuracy.html -->
<div id="sdk-for-flutter-navigate-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-navigate-dartdoc-main-content" class="main-content" data-above-sidebar="location/LocationEngine-class-sidebar.html" data-below-sidebar="">

<div>

# <span class="kind-method">startWithLocationAccuracy</span> method

</div>

<div class="section multi-line-signature">

<span class="returntype"><a href="sdk-for-flutter-navigate-location-locationenginestatus">LocationEngineStatus</a></span> <span class="name">startWithLocationAccuracy</span>(<wbr></wbr>

1.  <span id="sdk-for-flutter-navigate-startWithLocationAccuracy-param-locationAccuracy" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-location-locationaccuracy">LocationAccuracy</a></span> <span class="parameter-name">locationAccuracy</span></span>

)

<div class="features">

<span class="feature">override</span>

</div>

</div>

<div class="section desc markdown">

Starts the location engine with desired <a href="sdk-for-flutter-navigate-location-locationaccuracy">LocationAccuracy</a>. Make sure to call either <a href="sdk-for-flutter-navigate-location-locationengine-confirmhereprivacynoticeinclusion">LocationEngine.confirmHEREPrivacyNoticeInclusion</a> or <a href="sdk-for-flutter-navigate-location-locationengine-confirmhereprivacynoticeexception">LocationEngine.confirmHEREPrivacyNoticeException</a> beforehand. Returns <a href="sdk-for-flutter-navigate-location-locationenginestatus">LocationEngineStatus.alreadyStarted</a> if <a href="sdk-for-flutter-navigate-location-locationengine-startwithlocationaccuracy">LocationEngine.startWithLocationAccuracy</a> or <a href="sdk-for-flutter-navigate-location-locationengine-startwithlocationoptions">LocationEngine.startWithLocationOptions</a> is called again without calling <a href="sdk-for-flutter-navigate-location-locationengine-stop">LocationEngine.stop</a> in between. See <a href="sdk-for-flutter-navigate-location-locationenginestatus">LocationEngineStatus</a> for other possible return values.

</div>

## Implementation

``` dart
LocationEngineStatus startWithLocationAccuracy(LocationAccuracy locationAccuracy) =>
    _location.startWithLocationAccuracy(locationAccuracy);
```

</pre>

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas--> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>

</div>
`
}</HTMLBlock>
