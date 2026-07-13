---
title: "routeNumberName property - RoadShieldIconProperties class - mapview library - Dart API"
slug: "sdk-for-flutter-navigate-mapview-roadshieldiconproperties-routenumbername"
---

<div id="sdk-for-flutter-navigate-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-navigate-dartdoc-main-content" class="main-content" data-above-sidebar="mapview/RoadShieldIconProperties-class-sidebar.html" data-below-sidebar="">

<div>

# <span class="kind-property">routeNumberName</span> property

</div>

<div class="section multi-line-signature">

String <span class="name">routeNumberName</span>

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

</div>

<div class="section desc markdown">

A string that is used to additionally determine the road shield's visual representation. In a routing context, the text can be taken from a `LocalizedRoadNumber`, which is available for each `Span` of a `Route` object. Typically, the string contains the number of a road, such as "E100". Internally, the text is parsed with a RegEx pattern and the results will be used along with other properties such as `routeType`, `countryCode` and `stateCode` to identify the visual representation of a road shield icon.

Note that the actual text which will be displayed on the road shield icon is set with <a href="sdk-for-flutter-navigate-mapview-roadshieldiconproperties-shieldtext">RoadShieldIconProperties.shieldText</a>. In order to determine the visuals of the icon, `countryCode`, `routeType` and eventually the `stateCode` is in most cases sufficient to determine the type of road shield. In this case an empty string should be passed.

**Note:** Texts that contain a `CardinalDirection` are currently not supported and may lead to unexpected results. See `LocalizedRoadNumber` for more details, it provides texts with and without a cardinal direction.

</div>

## Implementation

``` dart
String routeNumberName;
```

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas--> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>

