---
title: "excludeCategories property - CategoryQuery class - search library - Dart API"
slug: "sdk-for-flutter-explore-search-categoryquery-excludecategories"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- excludeCategories.html -->
<div id="sdk-for-flutter-explore-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-explore-dartdoc-main-content" class="main-content" data-above-sidebar="search/CategoryQuery-class-sidebar.html" data-below-sidebar="">

<div>

# <span class="kind-property">excludeCategories</span> property

</div>

<div class="section multi-line-signature">

List<span class="signature">\<<wbr></wbr><span class="type-parameter"><a href="sdk-for-flutter-explore-search-placecategory-class">PlaceCategory</a></span>\></span> <span class="name">excludeCategories</span>

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

</div>

<div class="section desc markdown">

List of categories and subcategories to be excluded. A place can be assigned multiple categories. If any of them is in `CategoryQuery.excludeCategories`, that place will not be included in the response, regardless of whether any of its assigned categories have been included in `CategoryQuery.categories`. In short, an exclusion will always win over an inclusion. This is especially useful for excluding specific subcategories from the main category.

</div>

## Implementation

``` dart
List<PlaceCategory> excludeCategories;
```

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas--> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>

</div>
`
}</HTMLBlock>
