---
title: "borderCrossingWarningListener property - NavigatorInterface class - navigation library - Dart API"
slug: "sdk-for-flutter-navigate-navigation-navigatorinterface-bordercrossingwarninglistener"
---

<div id="sdk-for-flutter-navigate-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-navigate-dartdoc-main-content" class="main-content" data-above-sidebar="navigation/NavigatorInterface-class-sidebar.html" data-below-sidebar="">

<div>

# <span class="kind-property">borderCrossingWarningListener</span> property

</div>

<div id="sdk-for-flutter-navigate-getter" class="section">

<div class="section multi-line-signature">

<span class="returntype"><a href="sdk-for-flutter-navigate-navigation-bordercrossingwarninglistener-class">BorderCrossingWarningListener</a>?</span> <span class="name">borderCrossingWarningListener</span>

</div>

<div class="section desc markdown">

Object to receive notifications about border crossings on the current road. Border crossing notifications are given only if a route is present. Setting `null` value to the listener will unset the listener. It returns `null` when no listener is set by an user. Gets the listener to receive notifications about border crossings on the current road.

</div>

## Implementation

``` dart
BorderCrossingWarningListener? get borderCrossingWarningListener;
```

</div>

<div id="sdk-for-flutter-navigate-setter" class="section">

<div class="section multi-line-signature">

<span class="returntype">void</span> <span class="name">borderCrossingWarningListener=</span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-navigate-borderCrossingWarningListener-param-value" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-navigation-bordercrossingwarninglistener-class">BorderCrossingWarningListener</a>?</span> <span class="parameter-name">value</span></span>)</span>

</div>

<div class="section desc markdown">

Object to receive notifications about border crossings on the current road. Border crossing notifications are given only if a route is present. Setting `null` value to the listener will unset the listener. It returns `null` when no listener is set by an user. Sets the listener to receive notifications about border crossings on the current road.

</div>

## Implementation

``` dart
set borderCrossingWarningListener(BorderCrossingWarningListener? value);
```

</pre>

</div>

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas--> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>

