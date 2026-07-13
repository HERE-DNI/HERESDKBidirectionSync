---
title: "excludeChains property - CategoryQuery class - search library - Dart API"
slug: "sdk-for-flutter-explore-search-categoryquery-excludechains"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- excludeChains.html -->
<div id="sdk-for-flutter-explore-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-explore-dartdoc-main-content" class="main-content" data-above-sidebar="search/CategoryQuery-class-sidebar.html" data-below-sidebar="">

<div>

# <span class="kind-property">excludeChains</span> property

</div>

<div class="section multi-line-signature">

List<span class="signature">\<<wbr></wbr><span class="type-parameter"><a href="sdk-for-flutter-explore-search-placechain-class">PlaceChain</a></span>\></span> <span class="name">excludeChains</span>

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

</div>

<div class="section desc markdown">

List of chains to be excluded. A place can be assigned multiple chains. If any of them is in `CategoryQuery.excludeChains`, that place will not be included in the response, regardless of whether any of its assigned chains have been included in `CategoryQuery.includeChains`. In short, an exclusion will always win over an inclusion.

</div>

## Implementation

``` dart
List<PlaceChain> excludeChains;
```

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas--> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>

</div>
`
}</HTMLBlock>
