---
title: "startWithLocationAccuracy method - LocationEngineBase class - location library - Dart API"
slug: "sdk-for-flutter-navigate-location-locationenginebase-startwithlocationaccuracy"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- startWithLocationAccuracy.html -->
<div id="sdk-for-flutter-navigate-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-navigate-dartdoc-main-content" class="main-content" data-above-sidebar="location/LocationEngineBase-class-sidebar.html" data-below-sidebar="">

<div>

# <span class="kind-method">startWithLocationAccuracy</span> abstract method

</div>

<div class="section multi-line-signature">

<span class="returntype"><a href="sdk-for-flutter-navigate-location-locationenginestatus">LocationEngineStatus</a></span> <span class="name">startWithLocationAccuracy</span>(<wbr></wbr>

1.  <span id="sdk-for-flutter-navigate-startWithLocationAccuracy-param-locationAccuracy" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-location-locationaccuracy">LocationAccuracy</a></span> <span class="parameter-name">locationAccuracy</span></span>

)

</div>

<div class="section desc markdown">

Starts the location engine with desired <a href="sdk-for-flutter-navigate-location-locationaccuracy">LocationAccuracy</a>.

Returns <a href="sdk-for-flutter-navigate-location-locationenginestatus">LocationEngineStatus.alreadyStarted</a>, if <a href="sdk-for-flutter-navigate-location-locationenginebase-startwithlocationoptions">LocationEngineBase.startWithLocationOptions</a> is called again without <a href="sdk-for-flutter-navigate-location-locationenginebase-stop">LocationEngineBase.stop</a> in between. Make sure to call either <a href="sdk-for-flutter-navigate-location-locationenginebase-confirmhereprivacynoticeinclusion">LocationEngineBase.confirmHEREPrivacyNoticeInclusion</a> or <a href="sdk-for-flutter-navigate-location-locationenginebase-confirmhereprivacynoticeexception">LocationEngineBase.confirmHEREPrivacyNoticeException</a> beforehand.

- `locationAccuracy` Desired location accuracy. Requested accuracy is not guaranteed.

Returns <a href="sdk-for-flutter-navigate-location-locationenginestatus">LocationEngineStatus</a>. Engine status. Valid values are defined in <a href="sdk-for-flutter-navigate-location-locationenginestatus">LocationEngineStatus</a>

</div>

## Implementation

``` dart
LocationEngineStatus startWithLocationAccuracy(LocationAccuracy locationAccuracy);
```

</pre>

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas--> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>

</div>
`
}</HTMLBlock>
