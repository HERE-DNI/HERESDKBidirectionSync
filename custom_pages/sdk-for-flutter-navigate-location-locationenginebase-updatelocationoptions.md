---
title: "updateLocationOptions method - LocationEngineBase class - location library - Dart API"
slug: "sdk-for-flutter-navigate-location-locationenginebase-updatelocationoptions"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- updateLocationOptions.html -->
<div id="sdk-for-flutter-navigate-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-navigate-dartdoc-main-content" class="main-content" data-above-sidebar="location/LocationEngineBase-class-sidebar.html" data-below-sidebar="">

<div>

# <span class="kind-method">updateLocationOptions</span> abstract method

</div>

<div class="section multi-line-signature">

<span class="returntype"><a href="sdk-for-flutter-navigate-location-locationenginestatus">LocationEngineStatus</a></span> <span class="name">updateLocationOptions</span>(<wbr></wbr>

1.  <span id="sdk-for-flutter-navigate-updateLocationOptions-param-locationOptions" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-location-locationoptions-class">LocationOptions</a></span> <span class="parameter-name">locationOptions</span></span>

)

</div>

<div class="section desc markdown">

Reconfigures the location engine with desired <a href="sdk-for-flutter-navigate-location-locationoptions-class">LocationOptions</a>.

This method is a faster way to change location options for already started location engine, than calling <a href="sdk-for-flutter-navigate-location-locationenginebase-stop">LocationEngineBase.stop</a> and <a href="sdk-for-flutter-navigate-location-locationenginebase-startwithlocationoptions">LocationEngineBase.startWithLocationOptions</a> in sequence. Returns <a href="sdk-for-flutter-navigate-location-locationenginestatus">LocationEngineStatus.notReady</a>, if called for unstarted location engine. This method variant is not currently supported on iOS platforms. Returns <a href="sdk-for-flutter-navigate-location-locationenginestatus">LocationEngineStatus.notSupported</a> on platforms which this method variant is not supported.

- `locationOptions` Desired location options.

Returns <a href="sdk-for-flutter-navigate-location-locationenginestatus">LocationEngineStatus</a>. Engine status. Valid values are defined in <a href="sdk-for-flutter-navigate-location-locationenginestatus">LocationEngineStatus</a>

</div>

## Implementation

``` dart
LocationEngineStatus updateLocationOptions(LocationOptions locationOptions);
```

</pre>

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas--> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>

</div>
`
}</HTMLBlock>
