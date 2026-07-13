---
title: "PlaceCategory constructor - PlaceCategory - search library - Dart API"
slug: "sdk-for-flutter-navigate-search-placecategory-placecategory"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- PlaceCategory.html -->
<div id="sdk-for-flutter-navigate-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-navigate-dartdoc-main-content" class="main-content" data-above-sidebar="search/PlaceCategory-class-sidebar.html" data-below-sidebar="">

<div>

# <span class="kind-constructor">PlaceCategory</span> constructor

</div>

<div class="section multi-line-signature">

<span class="name">PlaceCategory</span>(<wbr></wbr>

1.  <span id="sdk-for-flutter-navigate-param-id" class="parameter"><span class="type-annotation">String</span> <span class="parameter-name">id</span></span>

)

</div>

<div class="section desc markdown">

Creates a new instance of this class.

- `id` Place category ID. The HERE places category system provides three levels of granularity:

1.  Level 1 represents high level groupings, such as "Eat and drink". Their IDs take the form "xxx", for example "100".
2.  Level 2 represents logical sub-groups or domains, such as "Eat and Drink / Restaurant". Their IDs take the form "xxx-xxxx", for example "100-1000".
3.  Level 3 provides the greatest level of granularity about place categorization, such as "Eat and Drink / Restaurant / Casual Dining". Their IDs take the form "xxx-xxxx-xxxx", for example "100-1000-0001". The category ID can be provided as one of the predefined values, such as <a href="sdk-for-flutter-navigate-search-placecategory-eatanddrinkrestaurant">PlaceCategory.eatAndDrinkRestaurant</a> or as a literal string that matches one of the category IDs defined by the HERE Search service. Only level 1 and 2 category IDs are predefined. The complete list of supported category IDs, including level 3, can be found online: <https://www.here.com/docs/bundle/geocoding-and-search-api-v7-api-reference/page/index.html>.

</div>

## Implementation

``` dart
factory PlaceCategory(String id) => $prototype.make(id);
```

</pre>

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas-left--> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>

</div>
`
}</HTMLBlock>
