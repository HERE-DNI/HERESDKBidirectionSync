---
title: "onFeaturesNotAvailable method - LocationStatusListener class - location library - Dart API"
slug: "sdk-for-flutter-navigate-location-locationstatuslistener-onfeaturesnotavailable"
---

<div id="sdk-for-flutter-navigate-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-navigate-dartdoc-main-content" class="main-content" data-above-sidebar="location/LocationStatusListener-class-sidebar.html" data-below-sidebar="">

<div>

# <span class="kind-method">onFeaturesNotAvailable</span> abstract method

</div>

<div class="section multi-line-signature">

<span class="returntype">void</span> <span class="name">onFeaturesNotAvailable</span>(<wbr></wbr>

1.  <span id="sdk-for-flutter-navigate-onFeaturesNotAvailable-param-features" class="parameter"><span class="type-annotation">List<span class="signature">\<<wbr></wbr><span class="type-parameter"><a href="sdk-for-flutter-navigate-location-locationfeature">LocationFeature</a></span>\></span></span> <span class="parameter-name">features</span></span>

)

</div>

<div class="section desc markdown">

Called after start() if any requested location feature is not available for the application.

Typically all features are enabled by default, but in certain variants some features may be disabled, e.g. to reduce binary size. If a feature that you need is not available, contact your HERE representative for more information.

- `features` List of unavailable location features.

</div>

## Implementation

``` dart
void onFeaturesNotAvailable(List<LocationFeature> features);
```

</pre>

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas--> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>

