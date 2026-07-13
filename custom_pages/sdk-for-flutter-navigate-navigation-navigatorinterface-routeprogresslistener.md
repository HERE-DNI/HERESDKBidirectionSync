---
title: "routeProgressListener property - NavigatorInterface class - navigation library - Dart API"
slug: "sdk-for-flutter-navigate-navigation-navigatorinterface-routeprogresslistener"
---

<div id="sdk-for-flutter-navigate-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-navigate-dartdoc-main-content" class="main-content" data-above-sidebar="navigation/NavigatorInterface-class-sidebar.html" data-below-sidebar="">

<div>

# <span class="kind-property">routeProgressListener</span> property

</div>

<div id="sdk-for-flutter-navigate-getter" class="section">

<div class="section multi-line-signature">

<span class="returntype"><a href="sdk-for-flutter-navigate-navigation-routeprogresslistener-class">RouteProgressListener</a>?</span> <span class="name">routeProgressListener</span>

</div>

<div class="section desc markdown">

Object to receive notifications about navigation route progress. Route progress notifications only occurs if the route has been set. Setting `null` value to the listener will unset the listener. It returns `null` when no listener is set by an user. Gets the listener that notifies when a route progress change occurs.

</div>

## Implementation

``` dart
RouteProgressListener? get routeProgressListener;
```

</div>

<div id="sdk-for-flutter-navigate-setter" class="section">

<div class="section multi-line-signature">

<span class="returntype">void</span> <span class="name">routeProgressListener=</span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-navigate-routeProgressListener-param-value" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-navigation-routeprogresslistener-class">RouteProgressListener</a>?</span> <span class="parameter-name">value</span></span>)</span>

</div>

<div class="section desc markdown">

Object to receive notifications about navigation route progress. Route progress notifications only occurs if the route has been set. Setting `null` value to the listener will unset the listener. It returns `null` when no listener is set by an user. Sets the listener that notifies when a route progress change occurs.

</div>

## Implementation

``` dart
set routeProgressListener(RouteProgressListener? value);
```

</pre>

</div>

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas--> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>

