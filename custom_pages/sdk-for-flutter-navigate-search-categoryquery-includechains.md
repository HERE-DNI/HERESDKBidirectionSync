---
title: "includeChains property - CategoryQuery class - search library - Dart API"
slug: "sdk-for-flutter-navigate-search-categoryquery-includechains"
---

<div id="sdk-for-flutter-navigate-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-navigate-dartdoc-main-content" class="main-content" data-above-sidebar="search/CategoryQuery-class-sidebar.html" data-below-sidebar="">

<div>

# <span class="kind-property">includeChains</span> property

</div>

<div class="section multi-line-signature">

List<span class="signature">\<<wbr></wbr><span class="type-parameter"><a href="sdk-for-flutter-navigate-search-placechain-class">PlaceChain</a></span>\></span> <span class="name">includeChains</span>

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

</div>

<div class="section desc markdown">

List of chains to be included. A place can be assigned multiple chains. If any of them is in `CategoryQuery.includeChains`, but none are in `CategoryQuery.excludeChains`, that place will be included in the response.

</div>

## Implementation

``` dart
List<PlaceChain> includeChains;
```

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas--> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>

