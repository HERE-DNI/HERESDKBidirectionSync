---
title: "hrn property - CatalogIdentifier class - core.engine library - Dart API"
slug: "sdk-for-flutter-explore-core-engine-catalogidentifier-hrn"
---

<div id="sdk-for-flutter-explore-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-explore-dartdoc-main-content" class="main-content" data-above-sidebar="core.engine/CatalogIdentifier-class-sidebar.html" data-below-sidebar="">

<div>

# <span class="kind-property">hrn</span> property

</div>

<div class="section multi-line-signature">

String <span class="name">hrn</span>

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

</div>

<div class="section desc markdown">

A HERE Resource Name (HRN) for this catalog. This is a unique string returned by the HERE platform when you add a new catalog to your project. For information about catalog creation process refer to <a href="https://www.here.com/docs/bundle/data-api-developer-guide/page/rest/creating-a-catalog.html">the Data API</a> By default, this field points to a default catalog on HERE platform, which contains data for the whole world excluding the region of Japan. Use <a href="sdk-for-flutter-explore-core-engine-catalogconfiguration-getdefault">CatalogConfiguration.getDefault</a> to get the default HRN value for use with the HERE platform.

</div>

## Implementation

``` dart
String hrn;
```

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas--> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>

