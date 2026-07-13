---
title: "text property - EventText class - navigation library - Dart API"
slug: "sdk-for-flutter-navigate-navigation-eventtext-text"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- text.html -->
<div id="sdk-for-flutter-navigate-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-navigate-dartdoc-main-content" class="main-content" data-above-sidebar="navigation/EventText-class-sidebar.html" data-below-sidebar="">

<div>

# <span class="kind-property">text</span> property

</div>

<div class="section multi-line-signature">

String <span class="name">text</span>

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

</div>

<div class="section desc markdown">

The text notification instruction. The text is formatted and localized as specified via <a href="sdk-for-flutter-navigate-routing-routetextoptions-class">RouteTextOptions</a>.

**Note:** During navigation, the text will be always empty when the <a href="sdk-for-flutter-navigate-routing-maneuver-class">Maneuver</a> is taken from the `Navigator` or `VisualNavigator` instance via the provided index. The text instruction that can be accessed from the <a href="sdk-for-flutter-navigate-routing-route-class">Route</a> instance is meant as preview and it is not necessarily matching the more comprehensive maneuver information you can access during navigation. This information can be enhanced with real-time `ManeuverNotifications` texts that can be used for spoken text notifications during a trip.

</div>

## Implementation

``` dart
String text;
```

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas--> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>

</div>
`
}</HTMLBlock>
