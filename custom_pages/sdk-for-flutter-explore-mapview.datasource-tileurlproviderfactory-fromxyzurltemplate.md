---
title: "fromXyzUrlTemplate method - TileUrlProviderFactory class - mapview.datasource library - Dart API"
slug: "sdk-for-flutter-explore-mapview.datasource-tileurlproviderfactory-fromxyzurltemplate"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- fromXyzUrlTemplate.html -->
<div id="sdk-for-flutter-explore-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-explore-dartdoc-main-content" class="main-content" data-above-sidebar="mapview.datasource/TileUrlProviderFactory-class-sidebar.html" data-below-sidebar="">

<div>

# <span class="kind-method">fromXyzUrlTemplate</span> static method

</div>

<div class="section multi-line-signature">

<span class="returntype"><a href="sdk-for-flutter-explore-mapview-datasource-tileurlprovidercallback">TileUrlProviderCallback</a>?</span> <span class="name">fromXyzUrlTemplate</span>(<wbr></wbr>

1.  <span id="sdk-for-flutter-explore-fromXyzUrlTemplate-param-urlTemplate" class="parameter"><span class="type-annotation">String</span> <span class="parameter-name">urlTemplate</span></span>

)

</div>

<div class="section desc markdown">

Creates <a href="sdk-for-flutter-explore-mapview-datasource-tileurlprovidercallback">TileUrlProviderCallback</a> for the given URL template.

A url template should look like this 'https://TestRasterTileService.com/{z}/{x}/{y}/' here the z parameter is the storage level, x and y define the location of the tile. The valid range for X and Y is from 0 to 2^level − 1.

- `urlTemplate` The url template

Returns <a href="sdk-for-flutter-explore-mapview-datasource-tileurlprovidercallback">TileUrlProviderCallback?</a>. `null` if the provided template is not valid xyz url type.

</div>

## Implementation

``` dart
static TileUrlProviderCallback? fromXyzUrlTemplate(String urlTemplate) => $prototype.fromXyzUrlTemplate(urlTemplate);
```

</pre>

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas--> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>

</div>
`
}</HTMLBlock>
