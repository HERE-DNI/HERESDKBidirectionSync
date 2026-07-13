---
title: "TextQuery.withArea constructor - TextQuery - search library - Dart API"
slug: "sdk-for-flutter-explore-search-textquery-textquery-witharea"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- TextQuery.withArea.html -->
<div id="sdk-for-flutter-explore-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-explore-dartdoc-main-content" class="main-content" data-above-sidebar="search/TextQuery-class-sidebar.html" data-below-sidebar="">

<div>

# <span class="kind-constructor">TextQuery.withArea</span> constructor

</div>

<div class="section multi-line-signature">

<span class="name">TextQuery.withArea</span>(<wbr></wbr>

1.  <span id="sdk-for-flutter-explore-withArea-param-query" class="parameter"><span class="type-annotation">String</span> <span class="parameter-name">query</span>, </span>
2.  <span id="sdk-for-flutter-explore-withArea-param-area" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-explore-search-textqueryarea-class">TextQueryArea</a></span> <span class="parameter-name">area</span></span>

)

</div>

<div class="section desc markdown">

Constructs a TextQuery from the provided text query and geographic area.

For Offline Search, search in a given `GeoBox`, `GeoCircle` or `GeoCorridor` restricts the results to only POIs.

- `query` Desired query to search.

- `area` Area which to provide the most relevant places.

</div>

## Implementation

``` dart
factory TextQuery.withArea(String query, TextQueryArea area) => $prototype.withArea(query, area);
```

</pre>

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas-left--> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>

</div>
`
}</HTMLBlock>
