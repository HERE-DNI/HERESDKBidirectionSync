---
title: "TileGeoBoundsCalculator class - mapview.datasource library - Dart API"
slug: "sdk-for-flutter-explore-mapview-datasource-tilegeoboundscalculator-class"
---

<div id="sdk-for-flutter-explore-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-explore-dartdoc-main-content" class="main-content" data-above-sidebar="mapview.datasource/mapview.datasource-library-sidebar.html" data-below-sidebar="mapview.datasource/TileGeoBoundsCalculator-class-sidebar.html">

<div>

# <span class="kind-class">TileGeoBoundsCalculator</span> class <a href="https://dart.dev/language/class-modifiers#abstract" class="feature feature-abstract" title="This type can not be directly constructed.">abstract</a>

</div>

<div class="section desc markdown">

A calculator of geodetic bounds for tiles identified by keys generated in a particular tiling scheme (<a href="sdk-for-flutter-explore-mapview-datasource-tilingscheme">TilingScheme</a>).

Note: This is a beta release of this feature, so there could be a few bugs and unexpected behavior. Related APIs may change for new releases without a deprecation process.

</div>

## Constructors

<span class="name"><a href="sdk-for-flutter-explore-mapview-datasource-tilegeoboundscalculator-tilegeoboundscalculator">TileGeoBoundsCalculator</a></span><span class="signature">(<span id="sdk-for-flutter-explore-param-tilingScheme" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-explore-mapview-datasource-tilingscheme">TilingScheme</a></span> <span class="parameter-name">tilingScheme</span></span>)</span>  
Creates an instance of <a href="sdk-for-flutter-explore-mapview-datasource-tilegeoboundscalculator-class">TileGeoBoundsCalculator</a>.

<div class="constructor-modifier features">

factory

</div>

## Properties

<span class="name"><a href="sdk-for-flutter-explore-mapview-datasource-tilegeoboundscalculator-hashcode">hashCode</a></span> <span class="signature">→ int</span>  
The hash code for this object.

<div class="features">

<span class="feature">no setter</span><span class="feature">inherited</span>

</div>

<span class="name"><a href="sdk-for-flutter-explore-mapview-datasource-tilegeoboundscalculator-runtimetype">runtimeType</a></span> <span class="signature">→ Type</span>  
A representation of the runtime type of the object.

<div class="features">

<span class="feature">no setter</span><span class="feature">inherited</span>

</div>

## Methods

<span class="name"><a href="sdk-for-flutter-explore-mapview-datasource-tilegeoboundscalculator-boundsof">boundsOf</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-explore-boundsOf-param-tileKey" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-explore-mapview-datasource-tilekey-class">TileKey</a></span> <span class="parameter-name">tileKey</span></span>) <span class="returntype parameter">→ <a href="sdk-for-flutter-explore-core-geobox-class">GeoBox</a></span> </span>  
Computes the geodetic bounds (as <a href="sdk-for-flutter-explore-core-geobox-class">GeoBox</a>) for a tile identified by <a href="sdk-for-flutter-explore-mapview-datasource-tilekey-class">TileKey</a>.

<span class="name"><a href="sdk-for-flutter-explore-mapview-datasource-tilegeoboundscalculator-nosuchmethod">noSuchMethod</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-explore-noSuchMethod-param-invocation" class="parameter"><span class="type-annotation">Invocation</span> <span class="parameter-name">invocation</span></span>) <span class="returntype parameter">→ dynamic</span> </span>  
Invoked when a nonexistent method or property is accessed.

<div class="features">

<span class="feature">inherited</span>

</div>

<span class="name"><a href="sdk-for-flutter-explore-mapview-datasource-tilegeoboundscalculator-tostring">toString</a></span><span class="signature">(<wbr></wbr>) <span class="returntype parameter">→ String</span> </span>  
A string representation of this object.

<div class="features">

<span class="feature">inherited</span>

</div>

## Operators

<span class="name"><a href="sdk-for-flutter-explore-mapview-datasource-tilegeoboundscalculator-operator_equals">operator ==</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-explore-param-other" class="parameter"><span class="type-annotation">Object</span> <span class="parameter-name">other</span></span>) <span class="returntype parameter">→ bool</span> </span>  
The equality operator.

<div class="features">

<span class="feature">inherited</span>

</div>

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>

