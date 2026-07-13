---
title: "RoadShieldIconProperties constructor - RoadShieldIconProperties - mapview library - Dart API"
slug: "sdk-for-flutter-explore-mapview-roadshieldiconproperties-roadshieldiconproperties"
---

<div id="sdk-for-flutter-explore-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-explore-dartdoc-main-content" class="main-content" data-above-sidebar="mapview/RoadShieldIconProperties-class-sidebar.html" data-below-sidebar="">

<div>

# <span class="kind-constructor">RoadShieldIconProperties</span> constructor

</div>

<div class="section multi-line-signature">

<span class="name">RoadShieldIconProperties</span>(<wbr></wbr>

1.  <span id="sdk-for-flutter-explore-param-routeType" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-explore-core-routetype">RouteType</a></span> <span class="parameter-name">routeType</span>, </span>
2.  <span id="sdk-for-flutter-explore-param-countryCode" class="parameter"><span class="type-annotation">String</span> <span class="parameter-name">countryCode</span>, </span>
3.  <span id="sdk-for-flutter-explore-param-stateCode" class="parameter"><span class="type-annotation">String</span> <span class="parameter-name">stateCode</span>, </span>
4.  <span id="sdk-for-flutter-explore-param-routeNumberName" class="parameter"><span class="type-annotation">String</span> <span class="parameter-name">routeNumberName</span>, </span>
5.  <span id="sdk-for-flutter-explore-param-shieldText" class="parameter"><span class="type-annotation">String</span> <span class="parameter-name">shieldText</span>, </span>

)

</div>

<div class="section desc markdown">

Creates a new instance.

- `routeType` The type of route indicating the significance of the road in a range from 0 to 6. A value of 1 stands for the most major route and 6 the most minor, with 0 being of unknown type.
- `countryCode` The country code in ISO-3166-1 alpha-3 format, which will determine the type of road shield.
- `stateCode` The state code for the road. It's a 2-letter code in ISO 3166-2 format. For example the ones listed for US on this page <https://en.wikipedia.org/wiki/ISO_3166-2:US>. The code "AL" is for Alabama. Another example is the code for autonomous communities listed on <https://en.wikipedia.org/wiki/ISO_3166-2:ES>. Can be empty if not required for the particular country.
- `routeNumberName` A string that is used to additionally determine the road shield's visual representation. In a routing context, the text can be taken from a `LocalizedRoadNumber`, which is available for each `Span` of a `Route` object. Typically, the string contains the number of a road, such as "E100". Internally, the text is parsed with a RegEx pattern and the results will be used along with other properties such as `routeType`, `countryCode` and `stateCode` to identify the visual representation of a road shield icon.

Note that the actual text which will be displayed on the road shield icon is set with <a href="sdk-for-flutter-explore-mapview-roadshieldiconproperties-shieldtext">RoadShieldIconProperties.shieldText</a>. In order to determine the visuals of the icon, `countryCode`, `routeType` and eventually the `stateCode` is in most cases sufficient to determine the type of road shield. In this case an empty string should be passed.

**Note:** Texts that contain a `CardinalDirection` are currently not supported and may lead to unexpected results. See `LocalizedRoadNumber` for more details, it provides texts with and without a cardinal direction.

- `shieldText` The text of the road-shield. This is the text which is displayed on the road-shield in reality. It will be in the output road-shield icon.

</div>

## Implementation

``` dart
RoadShieldIconProperties(this.routeType, this.countryCode, this.stateCode, this.routeNumberName, this.shieldText);
```

</pre>

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas-left--> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>

