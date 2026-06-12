---
title: "MapPolygon class abstract"
slug: "sdk-for-flutter-explore-mapview-mappolygon-class"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- MapPolygon-class.html -->


<div>
<h1>MapPolygon class abstract</h1></div>

<p>A visual representation of a polygon on the map.</p>
<p>Can be used to visualize areas of all shapes
and sizes.</p>
<p>The geometry to be visualized is represented by an instance of <a href="/sdk-for-flutter-explore-core-geopolygon-class">GeoPolygon</a>.
To display circular areas (for example, a position accuracy indicator) use a GeoPolygon
created from a <a href="/sdk-for-flutter-explore-core-geocircle-class">GeoCircle</a> using <a href="/sdk-for-flutter-explore-core-geopolygon-geopolygon-withgeocircle">GeoPolygon.withGeoCircle</a>.</p>
<p>Note:</p>
<ul>
<li>The polygon shape should not cover more than half of the globe,
otherwise unexpected results may occur.</li>
<li>Polygons which are self-intersecting are not supported and may lead to render
artifacts.</li>
<li>The inner boundaries (holes) specified in the GeoPolygon are ignored.</li>
</ul>


<h2>Constructors</h2>
<ul><li><a href="/sdk-for-flutter-explore-mapview-mappolygon-mappolygon">MapPolygon</a></li><li><a href="/sdk-for-flutter-explore-mapview-mappolygon-mappolygon-withoutlinecolorandoutlinewidthinpixels">MapPolygon.withOutlineColorAndOutlineWidthInPixels</a></li></ul>


<h2>Properties</h2>
<ul><li><a href="/sdk-for-flutter-explore-mapview-mappolygon-draworder">drawOrder</a></li><li><a href="/sdk-for-flutter-explore-mapview-mappolygon-fillcolor">fillColor</a></li><li><a href="/sdk-for-flutter-explore-mapview-mappolygon-geometry">geometry</a></li><li><a href="/sdk-for-flutter-explore-mapview-mappolygon-hashcode">hashCode</a></li><li><a href="/sdk-for-flutter-explore-mapview-mappolygon-metadata">metadata</a></li><li><a href="/sdk-for-flutter-explore-mapview-mappolygon-outlinecolor">outlineColor</a></li><li><a href="/sdk-for-flutter-explore-mapview-mappolygon-outlinewidth">outlineWidth</a></li><li><a href="/sdk-for-flutter-explore-mapview-mappolygon-runtimetype">runtimeType</a></li><li><a href="/sdk-for-flutter-explore-mapview-mappolygon-visibilityranges">visibilityRanges</a></li></ul>


<h2>Methods</h2>
<ul><li><a href="/sdk-for-flutter-explore-mapview-mappolygon-nosuchmethod">noSuchMethod</a></li><li><a href="/sdk-for-flutter-explore-mapview-mappolygon-tostring">toString</a></li></ul>


<h2>Operators</h2>
<ul><li><a href="/sdk-for-flutter-explore-mapview-mappolygon-operator-equals">operator ==</a></li></ul>

 



</div>
`
}</HTMLBlock>
