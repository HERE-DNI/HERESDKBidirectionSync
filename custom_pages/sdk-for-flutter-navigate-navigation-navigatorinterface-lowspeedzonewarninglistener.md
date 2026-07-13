---
title: "lowSpeedZoneWarningListener property - NavigatorInterface class - navigation library - Dart API"
slug: "sdk-for-flutter-navigate-navigation-navigatorinterface-lowspeedzonewarninglistener"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- lowSpeedZoneWarningListener.html -->
<div id="sdk-for-flutter-navigate-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-navigate-dartdoc-main-content" class="main-content" data-above-sidebar="navigation/NavigatorInterface-class-sidebar.html" data-below-sidebar="">

<div>

# <span class="kind-property">lowSpeedZoneWarningListener</span> property

</div>

<div id="sdk-for-flutter-navigate-getter" class="section">

<div class="section multi-line-signature">

<span class="returntype"><a href="sdk-for-flutter-navigate-navigation-lowspeedzonewarninglistener-class">LowSpeedZoneWarningListener</a>?</span> <span class="name">lowSpeedZoneWarningListener</span>

</div>

<div class="section desc markdown">

Object to receive notifications about low speed zones on the current road. Low speed zone notifications are given regardless if a route is set. This listener is currently available *only* for Japan. Setting `null` value to the listener will unset the listener. It returns `null` when no listener is set by an user. Gets the listener to receive notifications about low speed zones on the current road.

</div>

## Implementation

``` dart
LowSpeedZoneWarningListener? get lowSpeedZoneWarningListener;
```

</div>

<div id="sdk-for-flutter-navigate-setter" class="section">

<div class="section multi-line-signature">

<span class="returntype">void</span> <span class="name">lowSpeedZoneWarningListener=</span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-navigate-lowSpeedZoneWarningListener-param-value" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-navigation-lowspeedzonewarninglistener-class">LowSpeedZoneWarningListener</a>?</span> <span class="parameter-name">value</span></span>)</span>

</div>

<div class="section desc markdown">

Object to receive notifications about low speed zones on the current road. Low speed zone notifications are given regardless if a route is set. This listener is currently available *only* for Japan. Setting `null` value to the listener will unset the listener. It returns `null` when no listener is set by an user. Sets the listener to receive notifications about low speed zones on the current road.

</div>

## Implementation

``` dart
set lowSpeedZoneWarningListener(LowSpeedZoneWarningListener? value);
```

</pre>

</div>

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas--> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>

</div>
`
}</HTMLBlock>
