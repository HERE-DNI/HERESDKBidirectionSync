---
title: "Map Marker Cluster"
slug: "sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-mapview-map-marker-cluster"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- index.html -->

<div class="root">



<div id="main">
<div class="main-content" data-page-type="classlike" id="content" pageids="API Reference::com.here.sdk.mapview/MapMarkerCluster///PointingToDeclaration//1617540583">
<div class="breadcrumbs">/sdk-for-flutter-explore//sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-mapview/MapMarkerCluster</div>
<div class="cover">
<h1 class="cover">Map<wbr/>Marker<wbr/>Cluster</h1>
<div class="platform-hinted" data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace">class /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-mapview-map-marker-cluster : /sdk-for-flutter-explore-a-p-i-reference-com-here-native-base</div><p class="paragraph">Groups map markers and enables their clustering to reduce visual clutter when there are many of them in a small area.</p><p class="paragraph">The markers that are close to each other are replaced by a single cluster marker. Cluster groups are generated based on geographical distance between objects, not based on screen space collision. Hence it is possible, that cluster markers can overlap.</p><p class="paragraph">The markers can be added to a cluster or to a scene, but not to both. To display the cluster on the map, add it to the scene using /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-mapview-map-scene-add-map-marker-cluster. The display of a cluster is only guaranteed in case its origin is within the viewport. At the moment, this is a known limitation that mostly affects clusters which are visually large and cover a sizeable part of the viewport.</p><p class="paragraph">Markers part of the cluster with opacity set to zero are still on the map and are considered for picking and clustering.</p></div></div>
</div>
<div class="tabbedcontent">
<div class="tabs-section" tabs-section="tabs-section"><button class="section-tab" data-active="" data-togglable="CONSTRUCTOR,TYPE,PROPERTY,FUNCTION">Members</button></div>
<div class="tabs-section-body">
<div data-togglable="CONSTRUCTOR">
<h2 class="">Constructors</h2>
<div class="table"><a anchor-label="MapMarkerCluster" data-filterable-set=":modules:dokkaHtml/release" data-name="-1684566432%2FConstructors%2F1617540583" id="-1684566432%2FConstructors%2F1617540583"></a>
<div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release" data-togglable="CONSTRUCTOR">
<div class="main-subrow keyValue">
<div class="">
<div>/sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-mapview-map-marker-cluster-map-marker-cluster</div>

<div class="copy-popup-wrapper">Link copied to clipboard</div>
</div>
<div>
<div class="title">
<div class="platform-hinted" data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace">constructor(imageStyle: /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-mapview-map-marker-cluster-image-style)</div><div class="brief"><p class="paragraph">Creates a new instance of a map marker cluster which is represented as an image.</p></div><div class="symbol monospace">constructor(imageStyle: /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-mapview-map-marker-cluster-image-style, counterStyle: /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-mapview-map-marker-cluster-counter-style)</div><div class="brief"><p class="paragraph">Creates a new instance of a map marker cluster which is represented as an image along with a counter showing how many markers are actually grouped under particular cluster icon.</p></div></div></div>
</div>
</div>
</div>
</div>
</div>
</div>
<div data-togglable="TYPE">
<h2 class="">Types</h2>
<div class="table"><a anchor-label="Companion" data-filterable-set=":modules:dokkaHtml/release" data-name="552349692%2FClasslikes%2F1617540583" id="552349692%2FClasslikes%2F1617540583"></a>
<div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
<div class="main-subrow keyValue">
<div class="">
<div>/sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-mapview-map-marker-cluster-companion</div>

<div class="copy-popup-wrapper">Link copied to clipboard</div>
</div>
<div>
<div class="title">
<div class="platform-hinted" data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace">object /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-mapview-map-marker-cluster-companion</div></div></div>
</div>
</div>
</div>
</div>
<a anchor-label="CounterStyle" data-filterable-set=":modules:dokkaHtml/release" data-name="1628063749%2FClasslikes%2F1617540583" id="1628063749%2FClasslikes%2F1617540583"></a>
<div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
<div class="main-subrow keyValue">
<div class="">
<div>/sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-mapview-map-marker-cluster-counter-style</div>

<div class="copy-popup-wrapper">Link copied to clipboard</div>
</div>
<div>
<div class="title">
<div class="platform-hinted" data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace">class /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-mapview-map-marker-cluster-counter-style</div><div class="brief"><p class="paragraph">Styling options for a marker cluster which is represented by the marker count as a text.</p></div></div></div>
</div>
</div>
</div>
</div>
<a anchor-label="Grouping" data-filterable-set=":modules:dokkaHtml/release" data-name="863245399%2FClasslikes%2F1617540583" id="863245399%2FClasslikes%2F1617540583"></a>
<div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
<div class="main-subrow keyValue">
<div class="">
<div>/sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-mapview-map-marker-cluster-grouping</div>

<div class="copy-popup-wrapper">Link copied to clipboard</div>
</div>
<div>
<div class="title">
<div class="platform-hinted" data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace">class /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-mapview-map-marker-cluster-grouping</div><div class="brief"><p class="paragraph">Represents a group of map markers belonging to a cluster.</p></div></div></div>
</div>
</div>
</div>
</div>
<a anchor-label="ImageStyle" data-filterable-set=":modules:dokkaHtml/release" data-name="441149796%2FClasslikes%2F1617540583" id="441149796%2FClasslikes%2F1617540583"></a>
<div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
<div class="main-subrow keyValue">
<div class="">
<div>/sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-mapview-map-marker-cluster-image-style</div>

<div class="copy-popup-wrapper">Link copied to clipboard</div>
</div>
<div>
<div class="title">
<div class="platform-hinted" data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace">class /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-mapview-map-marker-cluster-image-style</div><div class="brief"><p class="paragraph">This class specifies the visual appearance of a cluster marker.</p></div></div></div>
</div>
</div>
</div>
</div>
</div>
</div>
<div data-togglable="PROPERTY">
<h2 class="">Properties</h2>
<div class="table"><a anchor-label="markers" data-filterable-set=":modules:dokkaHtml/release" data-name="-1244957860%2FProperties%2F1617540583" id="-1244957860%2FProperties%2F1617540583"></a>
<div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
<div class="main-subrow keyValue">
<div class="">
<div>/sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-mapview-map-marker-cluster-markers</div>

<div class="copy-popup-wrapper">Link copied to clipboard</div>
</div>
<div>
<div class="title">
<div class="platform-hinted" data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace">val /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-mapview-map-marker-cluster-markers: <a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/-list/index.html">List</a>&lt;/sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-mapview-map-marker&gt;</div><div class="brief"><p class="paragraph">The list of map markers which currently belong to this cluster. Modifying the list has no effect on the marker cluster.</p></div></div></div>
</div>
</div>
</div>
</div>
<a anchor-label="opacity" data-filterable-set=":modules:dokkaHtml/release" data-name="-354986230%2FProperties%2F1617540583" id="-354986230%2FProperties%2F1617540583"></a>
<div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
<div class="main-subrow keyValue">
<div class="">
<div>/sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-mapview-map-marker-cluster-opacity</div>

<div class="copy-popup-wrapper">Link copied to clipboard</div>
</div>
<div>
<div class="title">
<div class="platform-hinted" data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace">var /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-mapview-map-marker-cluster-opacity: <a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-double/index.html">Double</a></div><div class="brief"><p class="paragraph">Opacity is the factor which is applied to the alpha channel of the image used for marker cluster.</p></div></div></div>
</div>
</div>
</div>
</div>
</div>
</div>
<div data-togglable="FUNCTION">
<h2 class="">Functions</h2>
<div class="table"><a anchor-label="addMapMarker" data-filterable-set=":modules:dokkaHtml/release" data-name="1758325836%2FFunctions%2F1617540583" id="1758325836%2FFunctions%2F1617540583"></a>
<div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
<div class="main-subrow keyValue">
<div class="">
<div>/sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-mapview-map-marker-cluster-add-map-marker</div>

<div class="copy-popup-wrapper">Link copied to clipboard</div>
</div>
<div>
<div class="title">
<div class="platform-hinted" data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace">external fun /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-mapview-map-marker-cluster-add-map-marker(marker: /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-mapview-map-marker)</div><div class="brief"><p class="paragraph">Adds a map marker to this cluster. Adding a marker which is already part of the cluster or which was already added to the map scene has no effect.</p></div></div></div>
</div>
</div>
</div>
</div>
<a anchor-label="addMapMarkers" data-filterable-set=":modules:dokkaHtml/release" data-name="1734396425%2FFunctions%2F1617540583" id="1734396425%2FFunctions%2F1617540583"></a>
<div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
<div class="main-subrow keyValue">
<div class="">
<div>/sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-mapview-map-marker-cluster-add-map-markers</div>

<div class="copy-popup-wrapper">Link copied to clipboard</div>
</div>
<div>
<div class="title">
<div class="platform-hinted" data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace">external fun /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-mapview-map-marker-cluster-add-map-markers(markers: <a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/-list/index.html">List</a>&lt;/sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-mapview-map-marker&gt;)</div><div class="brief"><p class="paragraph">Adds a list of map markers to this cluster.</p></div></div></div>
</div>
</div>
</div>
</div>
<a anchor-label="removeAllMapMarkers" data-filterable-set=":modules:dokkaHtml/release" data-name="-953271013%2FFunctions%2F1617540583" id="-953271013%2FFunctions%2F1617540583"></a>
<div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
<div class="main-subrow keyValue">
<div class="">
<div>/sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-mapview-map-marker-cluster-remove-all-map-markers</div>

<div class="copy-popup-wrapper">Link copied to clipboard</div>
</div>
<div>
<div class="title">
<div class="platform-hinted" data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace">external fun /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-mapview-map-marker-cluster-remove-all-map-markers()</div><div class="brief"><p class="paragraph">Removes all map markers from this cluster.</p></div></div></div>
</div>
</div>
</div>
</div>
<a anchor-label="removeMapMarker" data-filterable-set=":modules:dokkaHtml/release" data-name="-1003426017%2FFunctions%2F1617540583" id="-1003426017%2FFunctions%2F1617540583"></a>
<div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
<div class="main-subrow keyValue">
<div class="">
<div>/sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-mapview-map-marker-cluster-remove-map-marker</div>

<div class="copy-popup-wrapper">Link copied to clipboard</div>
</div>
<div>
<div class="title">
<div class="platform-hinted" data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace">external fun /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-mapview-map-marker-cluster-remove-map-marker(marker: /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-mapview-map-marker)</div><div class="brief"><p class="paragraph">Removes a map marker from this cluster.</p></div></div></div>
</div>
</div>
</div>
</div>
<a anchor-label="removeMapMarkers" data-filterable-set=":modules:dokkaHtml/release" data-name="1559632668%2FFunctions%2F1617540583" id="1559632668%2FFunctions%2F1617540583"></a>
<div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
<div class="main-subrow keyValue">
<div class="">
<div>/sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-mapview-map-marker-cluster-remove-map-markers</div>

<div class="copy-popup-wrapper">Link copied to clipboard</div>
</div>
<div>
<div class="title">
<div class="platform-hinted" data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace">external fun /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-mapview-map-marker-cluster-remove-map-markers(markers: <a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/-list/index.html">List</a>&lt;/sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-mapview-map-marker&gt;)</div><div class="brief"><p class="paragraph">Removes a list of map markers from this cluster.</p></div></div></div>
</div>
</div>
</div>
</div>
</div>
</div>
</div>
</div>
</div>
<div class="footer">
<a class="footer--button footer--button_go-to-top" href="#content" id="go-to-top-link"></a>
© 2026 Copyright

Generated by 
<a class="footer--link footer--link_external" href="https://github.com/Kotlin/dokka">
dokka
</a>

</div>
</div>

</div>

</div>
`
}</HTMLBlock>
