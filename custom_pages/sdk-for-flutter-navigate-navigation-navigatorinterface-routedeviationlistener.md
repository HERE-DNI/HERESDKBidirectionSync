---
title: "routeDeviationListener property - NavigatorInterface class - navigation library - Dart API"
slug: "sdk-for-flutter-navigate-navigation-navigatorinterface-routedeviationlistener"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- routeDeviationListener.html -->
<div id="sdk-for-flutter-navigate-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-navigate-dartdoc-main-content" class="main-content" data-above-sidebar="navigation/NavigatorInterface-class-sidebar.html" data-below-sidebar="">

<div>

# <span class="kind-property">routeDeviationListener</span> property

</div>

<div id="sdk-for-flutter-navigate-getter" class="section">

<div class="section multi-line-signature">

<span class="returntype"><a href="sdk-for-flutter-navigate-navigation-routedeviationlistener-class">RouteDeviationListener</a>?</span> <span class="name">routeDeviationListener</span>

</div>

<div class="section desc markdown">

Object to receive notifications about deviations from the route if any occurs. Route deviation notifications only occurs if a route has been set. Setting `null` value to the listener will unset the listener. It returns `null` when no listener is set by an user. Gets the listener that notifies when deviation from the route is observed.

</div>

## Implementation

``` dart
RouteDeviationListener? get routeDeviationListener;
```

</div>

<div id="sdk-for-flutter-navigate-setter" class="section">

<div class="section multi-line-signature">

<span class="returntype">void</span> <span class="name">routeDeviationListener=</span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-navigate-routeDeviationListener-param-value" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-navigation-routedeviationlistener-class">RouteDeviationListener</a>?</span> <span class="parameter-name">value</span></span>)</span>

</div>

<div class="section desc markdown">

Object to receive notifications about deviations from the route if any occurs. Route deviation notifications only occurs if a route has been set. Setting `null` value to the listener will unset the listener. It returns `null` when no listener is set by an user. Sets the listener that notifies when deviation from the route is observed.

</div>

## Implementation

``` dart
set routeDeviationListener(RouteDeviationListener? value);
```

</pre>

</div>

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas--> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>

</div>
`
}</HTMLBlock>
