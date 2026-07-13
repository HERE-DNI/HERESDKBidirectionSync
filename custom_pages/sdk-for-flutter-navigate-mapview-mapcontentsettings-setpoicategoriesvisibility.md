---
title: "setPoiCategoriesVisibility method - MapContentSettings class - mapview library - Dart API"
slug: "sdk-for-flutter-navigate-mapview-mapcontentsettings-setpoicategoriesvisibility"
---

<div id="sdk-for-flutter-navigate-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-navigate-dartdoc-main-content" class="main-content" data-above-sidebar="mapview/MapContentSettings-class-sidebar.html" data-below-sidebar="">

<div>

# <span class="kind-method">setPoiCategoriesVisibility</span> static method

</div>

<div class="section multi-line-signature">

<span class="returntype">void</span> <span class="name">setPoiCategoriesVisibility</span>(<wbr></wbr>

1.  <span id="sdk-for-flutter-navigate-setPoiCategoriesVisibility-param-categoryIds" class="parameter"><span class="type-annotation">List<span class="signature">\<<wbr></wbr><span class="type-parameter">String</span>\></span></span> <span class="parameter-name">categoryIds</span>, </span>
2.  <span id="sdk-for-flutter-navigate-setPoiCategoriesVisibility-param-visibility" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-mapview-visibilitystate">VisibilityState</a></span> <span class="parameter-name">visibility</span></span>

)

</div>

<div class="section desc markdown">

Sets visibility for embedded carto POI categories (points of interest that are visible on the map, by default).

For HERE standard map schemes all available POI categories are visible by default for each selected map scheme. Note that not all POI categories are available for all map schemes.

Based on the given list of categories the number of shown carto POIs can be reduced. To find all possible POI category strings look into `here.sdk.search.PlaceCategory`. Note that it is enough to hide a main category like "100" (eat-and-drink) to also affect sub categories such as "100-1000" (eat-and-drink-restaurant) and "100-1100" (eat-and-drink-coffee-tea). To enable a sub category, also the related main categories need have the `VISIBLE` state.

The POI visibility is a property of the map data itself. Once set it will be applied to all HERE standard map schemes and the selected categories will remain even when switching a map scheme.

- `categoryIds` A list of POI categories that a visibility state is set for.

- `visibility` A selected visibility for specified POI categories.

</div>

## Implementation

``` dart
static void setPoiCategoriesVisibility(List<String> categoryIds, VisibilityState visibility) => $prototype.setPoiCategoriesVisibility(categoryIds, visibility);
```

</pre>

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas--> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>

