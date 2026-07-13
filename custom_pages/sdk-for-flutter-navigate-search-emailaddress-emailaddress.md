---
title: "EmailAddress constructor - EmailAddress - search library - Dart API"
slug: "sdk-for-flutter-navigate-search-emailaddress-emailaddress"
---

<div id="sdk-for-flutter-navigate-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-navigate-dartdoc-main-content" class="main-content" data-above-sidebar="search/EmailAddress-class-sidebar.html" data-below-sidebar="">

<div>

# <span class="kind-constructor">EmailAddress</span> constructor

</div>

<div class="section multi-line-signature">

<span class="name">EmailAddress</span>(<wbr></wbr>

1.  <span id="sdk-for-flutter-navigate-param-address" class="parameter"><span class="type-annotation">String</span> <span class="parameter-name">address</span>, </span>
2.  <span id="sdk-for-flutter-navigate-param-categories" class="parameter"><span class="type-annotation">List<span class="signature">\<<wbr></wbr><span class="type-parameter"><a href="sdk-for-flutter-navigate-search-placecategory-class">PlaceCategory</a></span>\></span></span> <span class="parameter-name">categories</span></span>

)

</div>

<div class="section desc markdown">

Creates a new instance.

- `address` The email address.
- `categories` Categories associated with email address. Note: In case <a href="sdk-for-flutter-navigate-search-emailaddress-categories">EmailAddress.categories</a> are not empty, then <a href="sdk-for-flutter-navigate-search-emailaddress-address">EmailAddress.address</a> should be used according to given categories. Otherwise, <a href="sdk-for-flutter-navigate-search-emailaddress-address">EmailAddress.address</a> is meant for general use.

</div>

## Implementation

``` dart
EmailAddress(this.address, this.categories);
```

</pre>

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas-left--> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>

