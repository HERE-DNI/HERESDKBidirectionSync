---
title: "PickedPlace constructor - PickedPlace - core library - Dart API"
slug: "sdk-for-flutter-explore-core-pickedplace-pickedplace"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- PickedPlace.html -->
<div id="sdk-for-flutter-explore-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-explore-dartdoc-main-content" class="main-content" data-above-sidebar="core/PickedPlace-class-sidebar.html" data-below-sidebar="">

<div>

# <span class="kind-constructor">PickedPlace</span> constructor

</div>

<div class="section multi-line-signature">

<span class="name">PickedPlace</span>(<wbr></wbr>

1.  <span id="sdk-for-flutter-explore-param-name" class="parameter"><span class="type-annotation">String</span> <span class="parameter-name">name</span>, </span>
2.  <span id="sdk-for-flutter-explore-param-coordinates" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-explore-core-geocoordinates-class">GeoCoordinates</a></span> <span class="parameter-name">coordinates</span>, </span>
3.  <span id="sdk-for-flutter-explore-param-placeCategoryId" class="parameter"><span class="type-annotation">String</span> <span class="parameter-name">placeCategoryId</span></span>

)

</div>

<div class="section desc markdown">

Creates a new instance.

- `name` The name of the POI localized in the currently selected map language.
- `coordinates` The geographic coordinates of the POI.
- `placeCategoryId` The place category ID of the POI. This is the same String value as `PlaceCategory.id` that can be obtained from the `SearchEngine` and the `OfflineSearchEngine`. Note that not all editions include the `OfflineSearchEngine`.

</div>

## Implementation

``` dart
PickedPlace(this.name, this.coordinates, this.placeCategoryId);
```

</pre>

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas-left--> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>

</div>
`
}</HTMLBlock>
