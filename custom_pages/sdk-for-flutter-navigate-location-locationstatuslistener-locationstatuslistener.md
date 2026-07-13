---
title: "LocationStatusListener constructor - LocationStatusListener - location library - Dart API"
slug: "sdk-for-flutter-navigate-location-locationstatuslistener-locationstatuslistener"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- LocationStatusListener.html -->
<div id="sdk-for-flutter-navigate-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-navigate-dartdoc-main-content" class="main-content" data-above-sidebar="location/LocationStatusListener-class-sidebar.html" data-below-sidebar="">

<div>

# <span class="kind-constructor">LocationStatusListener</span> constructor

</div>

<div class="section multi-line-signature">

<span class="name">LocationStatusListener</span>(<wbr></wbr>

1.  <span id="sdk-for-flutter-navigate-param-onStatusChangedLambda" class="parameter"><span class="type-annotation">void</span> <span class="parameter-name">onStatusChangedLambda</span>(</span>
    1.  <span id="sdk-for-flutter-navigate-param" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-location-locationenginestatus">LocationEngineStatus</a></span></span>

    ), </span>
2.  <span id="sdk-for-flutter-navigate-param-onFeaturesNotAvailableLambda" class="parameter"><span class="type-annotation">void</span> <span class="parameter-name">onFeaturesNotAvailableLambda</span>(</span>
    1.  <span id="sdk-for-flutter-navigate-param" class="parameter"><span class="type-annotation">List<span class="signature">\<<wbr></wbr><span class="type-parameter"><a href="sdk-for-flutter-navigate-location-locationfeature">LocationFeature</a></span>\></span></span></span>

    )</span>

)

</div>

<div class="section desc markdown">

Abstract class for listening the LocationEngine status updates.

</div>

## Implementation

``` dart
factory LocationStatusListener(
  void Function(LocationEngineStatus) onStatusChangedLambda,
  void Function(List<LocationFeature>) onFeaturesNotAvailableLambda,

) => LocationStatusListener$Lambdas(
  onStatusChangedLambda,
  onFeaturesNotAvailableLambda,

);
```

</pre>

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas-left--> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>

</div>
`
}</HTMLBlock>
