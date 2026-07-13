---
title: "specific method - CatalogVersionHint class - core.engine library - Dart API"
slug: "sdk-for-flutter-explore-core.engine-catalogversionhint-specific"
---

<div id="sdk-for-flutter-explore-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-explore-dartdoc-main-content" class="main-content" data-above-sidebar="core.engine/CatalogVersionHint-class-sidebar.html" data-below-sidebar="">

<div>

# <span class="kind-method">specific</span> static method

</div>

<div class="section multi-line-signature">

<span class="returntype"><a href="sdk-for-flutter-explore-core-engine-catalogversionhint-class">CatalogVersionHint</a></span> <span class="name">specific</span>(<wbr></wbr>

1.  <span id="sdk-for-flutter-explore-specific-param-version" class="parameter"><span class="type-annotation">int</span> <span class="parameter-name">version</span></span>

)

</div>

<div class="section desc markdown">

This static method is used when you are interested in a specific version of a catalog, that you want to specify manually.

To ensure proper functioning of this API, it is essential to clean the mutable and persistent storage.

- `version` An integer value indicating the version of catalog desired. If the desired version does not exist, the HERE platform will make the best effort to provide an appropriate version or result in error logs about invalid version.

Returns <a href="sdk-for-flutter-explore-core-engine-catalogversionhint-class">CatalogVersionHint</a>. Instance of <a href="sdk-for-flutter-explore-core-engine-catalogversionhint-class">CatalogVersionHint</a> with specified version.

</div>

## Implementation

``` dart
static CatalogVersionHint specific(int version) => $prototype.specific(version);
```

</pre>

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas--> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>

