---
title: "DesiredCatalog constructor - DesiredCatalog - core.engine library - Dart API"
slug: "sdk-for-flutter-explore-core-engine-desiredcatalog-desiredcatalog"
---

<div id="sdk-for-flutter-explore-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-explore-dartdoc-main-content" class="main-content" data-above-sidebar="core.engine/DesiredCatalog-class-sidebar.html" data-below-sidebar="">

<div>

# <span class="kind-constructor">DesiredCatalog</span> constructor

</div>

<div class="section multi-line-signature">

<span class="name">DesiredCatalog</span>(<wbr></wbr>

1.  <span id="sdk-for-flutter-explore-param-hrn" class="parameter"><span class="type-annotation">String</span> <span class="parameter-name">hrn</span>, </span>
2.  <span id="sdk-for-flutter-explore-param-version" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-explore-core-engine-catalogversionhint-class">CatalogVersionHint</a></span> <span class="parameter-name">version</span></span>

)

</div>

<div class="section desc markdown">

Creates a new instance.

- `hrn` A HERE Resource Name (HRN) for this catalog. This is a unique string returned by the HERE platform when you add a new catalog to your project. For more information, see <a href="sdk-for-flutter-explore-core-engine-catalogidentifier-hrn">CatalogIdentifier.hrn</a>

- `version` The version to use for this Catalog's data. You should use either <a href="sdk-for-flutter-explore-core-engine-catalogversionhint-specific">CatalogVersionHint.specific</a> to specify a specific version of the catalog or <a href="sdk-for-flutter-explore-core-engine-catalogversionhint-latestwithignoringcacheddata">CatalogVersionHint.latestWithIgnoringCachedData</a> to access the latest version of the catalog available on the HERE platform. Based on the value in this field, the HERE platform will determine the best version to use for this catalog or result in error logs if the desired version is not available.

</div>

## Implementation

``` dart
factory DesiredCatalog(String hrn, CatalogVersionHint version) => $prototype.make(hrn, version);
```

</pre>

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas-left--> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>

