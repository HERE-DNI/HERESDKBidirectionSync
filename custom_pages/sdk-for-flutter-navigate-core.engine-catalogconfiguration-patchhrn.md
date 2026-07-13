---
title: "patchHrn property - CatalogConfiguration class - core.engine library - Dart API"
slug: "sdk-for-flutter-navigate-core.engine-catalogconfiguration-patchhrn"
---

<div id="sdk-for-flutter-navigate-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-navigate-dartdoc-main-content" class="main-content" data-above-sidebar="core.engine/CatalogConfiguration-class-sidebar.html" data-below-sidebar="">

<div>

# <span class="kind-property">patchHrn</span> property

</div>

<div class="section multi-line-signature">

String? <span class="name">patchHrn</span>

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

</div>

<div class="section desc markdown">

Some catalogs may have additional modifications to their data contained in an entirely separate catalog, called the patch catalog. This field indicates the HERE Resource Name (HRN) for the patch catalog. When this field is present, the catalog's data as referenced by <a href="sdk-for-flutter-navigate-core-engine-catalogconfiguration-catalog">CatalogConfiguration.catalog</a> is merged with data from the patch catalog. If this field is `null`, then incremental updates are disabled.

</div>

## Implementation

``` dart
String? patchHrn;
```

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas--> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>

