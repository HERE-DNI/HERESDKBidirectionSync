---
title: "WebsiteAddress constructor - WebsiteAddress - search library - Dart API"
slug: "sdk-for-flutter-explore-search-websiteaddress-websiteaddress"
---

<div id="sdk-for-flutter-explore-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-explore-dartdoc-main-content" class="main-content" data-above-sidebar="search/WebsiteAddress-class-sidebar.html" data-below-sidebar="">

<div>

# <span class="kind-constructor">WebsiteAddress</span> constructor

</div>

<div class="section multi-line-signature">

<span class="name">WebsiteAddress</span>(<wbr></wbr>

1.  <span id="sdk-for-flutter-explore-param-address" class="parameter"><span class="type-annotation">String</span> <span class="parameter-name">address</span>, </span>
2.  <span id="sdk-for-flutter-explore-param-categories" class="parameter"><span class="type-annotation">List<span class="signature">\<<wbr></wbr><span class="type-parameter"><a href="sdk-for-flutter-explore-search-placecategory-class">PlaceCategory</a></span>\></span></span> <span class="parameter-name">categories</span></span>

)

</div>

<div class="section desc markdown">

Creates a new instance.

- `address` The website address.
- `categories` Categories associated with website address. Note: In case <a href="sdk-for-flutter-explore-search-websiteaddress-categories">WebsiteAddress.categories</a> are not empty, then <a href="sdk-for-flutter-explore-search-websiteaddress-address">WebsiteAddress.address</a> should be used according to given categories. Otherwise, <a href="sdk-for-flutter-explore-search-websiteaddress-address">WebsiteAddress.address</a> is meant for general use.

</div>

## Implementation

``` dart
WebsiteAddress(this.address, this.categories);
```

</pre>

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas-left--> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>

