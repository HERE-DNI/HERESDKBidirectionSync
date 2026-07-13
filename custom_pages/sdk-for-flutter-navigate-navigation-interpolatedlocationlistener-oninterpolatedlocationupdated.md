---
title: "onInterpolatedLocationUpdated method - InterpolatedLocationListener class - navigation library - Dart API"
slug: "sdk-for-flutter-navigate-navigation-interpolatedlocationlistener-oninterpolatedlocationupdated"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- onInterpolatedLocationUpdated.html -->
<div id="sdk-for-flutter-navigate-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-navigate-dartdoc-main-content" class="main-content" data-above-sidebar="navigation/InterpolatedLocationListener-class-sidebar.html" data-below-sidebar="">

<div>

# <span class="kind-method">onInterpolatedLocationUpdated</span> abstract method

</div>

<div class="section multi-line-signature">

<span class="returntype">void</span> <span class="name">onInterpolatedLocationUpdated</span>(<wbr></wbr>

1.  <span id="sdk-for-flutter-navigate-onInterpolatedLocationUpdated-param-location" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-core-location-class">Location</a></span> <span class="parameter-name">location</span></span>

)

</div>

<div class="section desc markdown">

Called whenever a new interpolated location is calculated, usually several times per second.

The interpolated locations are only provided between <a href="sdk-for-flutter-navigate-navigation-visualnavigator-startrendering">VisualNavigator.startRendering</a> and <a href="sdk-for-flutter-navigate-navigation-visualnavigator-stoprendering">VisualNavigator.stopRendering</a> calls and the application is not running in the background.

- `location` The interpolated location.

</div>

## Implementation

``` dart
void onInterpolatedLocationUpdated(Location location);
```

</pre>

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas--> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>

</div>
`
}</HTMLBlock>
