---
title: "TilingScheme enum - mapview.datasource library - Dart API"
slug: "sdk-for-flutter-explore-mapview.datasource-tilingscheme"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- TilingScheme.html -->
<div id="sdk-for-flutter-explore-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-explore-dartdoc-main-content" class="main-content" data-above-sidebar="mapview.datasource/mapview.datasource-library-sidebar.html" data-below-sidebar="mapview.datasource/TilingScheme-enum-sidebar.html">

<div>

# <span class="kind-enum">TilingScheme</span> enum

</div>

<div class="section desc markdown">

List of available data tiling schemes.

X axis has the origin at -180 longitude and is increasing in east direction. Y axis has the origin at max latitude and is increasing in south direction. For half quad tree schemes, only the uppper half of the tree is used.

</div>

## Values

<span class="name">halfQuadTreeIdentity</span> <span class="signature">→ const <a href="sdk-for-flutter-explore-mapview-datasource-tilingscheme">TilingScheme</a></span>  
A tiling scheme that splits 0-th level tile into 2 equal-sized subtiles and all other level tiles into 4 equal-sized subtiles.

<span class="name">halfQuadTreeMercator</span> <span class="signature">→ const <a href="sdk-for-flutter-explore-mapview-datasource-tilingscheme">TilingScheme</a></span>  
A tiling scheme that splits 0-th level tile into 2 equal-sized subtiles and all other level tiles into 4 equal-sized subtiles. The coordinates of the tile's corners are transformed through the web-mercator projection.

<span class="name">halfQuadTreeEquirectangular</span> <span class="signature">→ const <a href="sdk-for-flutter-explore-mapview-datasource-tilingscheme">TilingScheme</a></span>  
A tiling scheme that splits 0-th level tile into 2 equal-sized subtiles and all other level tiles into 4 equal-sized subtiles. The coordinates of the tile's corners are transformed through the equirectangular (plate carree) projection.

<span class="name">quadTreeIdentity</span> <span class="signature">→ const <a href="sdk-for-flutter-explore-mapview-datasource-tilingscheme">TilingScheme</a></span>  
A tiling scheme that splits each level tile into 4 equal-sized subtiles.

<span class="name">quadTreeMercator</span> <span class="signature">→ const <a href="sdk-for-flutter-explore-mapview-datasource-tilingscheme">TilingScheme</a></span>  
A tiling scheme that splits each level tile into 4 equal-sized subtiles. The coordinates of the tile's corners are transformed through the web-mercator projection.

<span class="name">quadTreeEquirectangular</span> <span class="signature">→ const <a href="sdk-for-flutter-explore-mapview-datasource-tilingscheme">TilingScheme</a></span>  
A tiling scheme that splits each level tile into 4 equal-sized subtiles. The coordinates of the tile's corners are transformed through the equirectangular (plate carree) projection.

## Properties

<span class="name"><a href="sdk-for-flutter-explore-mapview-datasource-tilingscheme-hashcode">hashCode</a></span> <span class="signature">→ int</span>  
The hash code for this object.

<div class="features">

<span class="feature">no setter</span><span class="feature">inherited</span>

</div>

<span class="name"><a href="sdk-for-flutter-explore-mapview-datasource-tilingscheme-index">index</a></span> <span class="signature">→ int</span>  
A numeric identifier for the enumerated value.

<div class="features">

<span class="feature">no setter</span><span class="feature">inherited</span>

</div>

<span class="name"><a href="sdk-for-flutter-explore-mapview-datasource-tilingscheme-runtimetype">runtimeType</a></span> <span class="signature">→ Type</span>  
A representation of the runtime type of the object.

<div class="features">

<span class="feature">no setter</span><span class="feature">inherited</span>

</div>

## Methods

<span class="name"><a href="sdk-for-flutter-explore-mapview-datasource-tilingscheme-nosuchmethod">noSuchMethod</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-explore-noSuchMethod-param-invocation" class="parameter"><span class="type-annotation">Invocation</span> <span class="parameter-name">invocation</span></span>) <span class="returntype parameter">→ dynamic</span> </span>  
Invoked when a nonexistent method or property is accessed.

<div class="features">

<span class="feature">inherited</span>

</div>

<span class="name"><a href="sdk-for-flutter-explore-mapview-datasource-tilingscheme-tostring">toString</a></span><span class="signature">(<wbr></wbr>) <span class="returntype parameter">→ String</span> </span>  
A string representation of this object.

<div class="features">

<span class="feature">inherited</span>

</div>

## Operators

<span class="name"><a href="sdk-for-flutter-explore-mapview-datasource-tilingscheme-operator_equals">operator ==</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-explore-param-other" class="parameter"><span class="type-annotation">Object</span> <span class="parameter-name">other</span></span>) <span class="returntype parameter">→ bool</span> </span>  
The equality operator.

<div class="features">

<span class="feature">inherited</span>

</div>

## Constants

<span class="name"><a href="sdk-for-flutter-explore-mapview-datasource-tilingscheme-values-constant">values</a></span> <span class="signature">→ const List<span class="signature">\<<wbr></wbr><span class="type-parameter"><a href="sdk-for-flutter-explore-mapview-datasource-tilingscheme">TilingScheme</a></span>\></span></span>  
A constant List of the values in this enum, in order of their declaration.

</div>

<!-- /.main-content --> <!-- /.sidebar-offcanvas --> <span class="no-break"> here_sdk 4.26.0 </span>

</div>
`
}</HTMLBlock>
