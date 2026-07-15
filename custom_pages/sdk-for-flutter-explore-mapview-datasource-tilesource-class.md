---
title: "TileSource class - mapview.datasource library - Dart API"
slug: "sdk-for-flutter-explore-mapview-datasource-tilesource-class"
---

<div id="sdk-for-flutter-explore-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-explore-dartdoc-main-content" class="main-content" data-above-sidebar="mapview.datasource/mapview.datasource-library-sidebar.html" data-below-sidebar="mapview.datasource/TileSource-class-sidebar.html">

<div>

# <span class="kind-class">TileSource</span> class <a href="https://dart.dev/language/class-modifiers#abstract" class="feature feature-abstract" title="This type can not be directly constructed.">abstract</a>

</div>

<div class="section desc markdown">

A source of tiles.

The implementations must be thread-safe.

Note: This is a beta release of this feature, so there could be a few bugs and unexpected behavior. Related APIs may change for new releases without a deprecation process.

</div>

<div class="section">

Implementers  
- <a href="sdk-for-flutter-explore-mapview-datasource-linetilesource-class">LineTileSource</a>
- <a href="sdk-for-flutter-explore-mapview-datasource-pointtilesource-class">PointTileSource</a>
- <a href="sdk-for-flutter-explore-mapview-datasource-polygontilesource-class">PolygonTileSource</a>
- <a href="sdk-for-flutter-explore-mapview-datasource-rastertilesource-class">RasterTileSource</a>

</div>

## Constructors

<span class="name"><a href="sdk-for-flutter-explore-mapview-datasource-tilesource-tilesource">TileSource</a></span><span class="signature">(<span id="sdk-for-flutter-explore-param-getDataVersionLambda" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-explore-mapview-datasource-tilesourcedataversion-class">TileSourceDataVersion</a></span> <span class="parameter-name">getDataVersionLambda</span>(<span id="sdk-for-flutter-explore-param" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-explore-mapview-datasource-tilekey-class">TileKey</a></span></span>), </span><span id="sdk-for-flutter-explore-param-addListenerLambda" class="parameter"><span class="type-annotation">void</span> <span class="parameter-name">addListenerLambda</span>(<span id="sdk-for-flutter-explore-param" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-explore-mapview-datasource-tilesourcelistener-class">TileSourceListener</a></span></span>), </span><span id="sdk-for-flutter-explore-param-removeListenerLambda" class="parameter"><span class="type-annotation">void</span> <span class="parameter-name">removeListenerLambda</span>(<span id="sdk-for-flutter-explore-param" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-explore-mapview-datasource-tilesourcelistener-class">TileSourceListener</a></span></span>), </span><span id="sdk-for-flutter-explore-param-tilingSchemeGetLambda" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-explore-mapview-datasource-tilingscheme">TilingScheme</a></span> <span class="parameter-name">tilingSchemeGetLambda</span>(), </span><span id="sdk-for-flutter-explore-param-storageLevelsGetLambda" class="parameter"><span class="type-annotation">List<span class="signature">\<<wbr></wbr><span class="type-parameter">int</span>\></span></span> <span class="parameter-name">storageLevelsGetLambda</span>()</span>)</span>  
A source of tiles.

<div class="constructor-modifier features">

factory

</div>

## Properties

<span class="name"><a href="sdk-for-flutter-explore-mapview-datasource-tilesource-hashcode">hashCode</a></span> <span class="signature">→ int</span>  
The hash code for this object.

<div class="features">

<span class="feature">no setter</span><span class="feature">inherited</span>

</div>

<span class="name"><a href="sdk-for-flutter-explore-mapview-datasource-tilesource-runtimetype">runtimeType</a></span> <span class="signature">→ Type</span>  
A representation of the runtime type of the object.

<div class="features">

<span class="feature">no setter</span><span class="feature">inherited</span>

</div>

<span class="name"><a href="sdk-for-flutter-explore-mapview-datasource-tilesource-storagelevels">storageLevels</a></span> <span class="signature">→ List<span class="signature">\<<wbr></wbr><span class="type-parameter">int</span>\></span></span>  
The storage levels available for this data source. Supported range \[0, 31\]. At least one level must be available for this to be used as a source of data. Gets the storage levels available for this data source. Supported range \[0, 31\].

<div class="features">

<span class="feature">no setter</span>

</div>

<span class="name"><a href="sdk-for-flutter-explore-mapview-datasource-tilesource-tilingscheme">tilingScheme</a></span> <span class="signature">→ <a href="sdk-for-flutter-explore-mapview-datasource-tilingscheme">TilingScheme</a></span>  
The tiling scheme used by this source. Gets the tiling scheme used by this source.

<div class="features">

<span class="feature">no setter</span>

</div>

## Methods

<span class="name"><a href="sdk-for-flutter-explore-mapview-datasource-tilesource-addlistener">addListener</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-explore-addListener-param-listener" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-explore-mapview-datasource-tilesourcelistener-class">TileSourceListener</a></span> <span class="parameter-name">listener</span></span>) <span class="returntype parameter">→ void</span> </span>  
Adds a listener for receiving state notifications.

<span class="name"><a href="sdk-for-flutter-explore-mapview-datasource-tilesource-getdataversion">getDataVersion</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-explore-getDataVersion-param-tileKey" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-explore-mapview-datasource-tilekey-class">TileKey</a></span> <span class="parameter-name">tileKey</span></span>) <span class="returntype parameter">→ <a href="sdk-for-flutter-explore-mapview-datasource-tilesourcedataversion-class">TileSourceDataVersion</a></span> </span>  
Gets the current data version of a tile.

<span class="name"><a href="sdk-for-flutter-explore-mapview-datasource-tilesource-nosuchmethod">noSuchMethod</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-explore-noSuchMethod-param-invocation" class="parameter"><span class="type-annotation">Invocation</span> <span class="parameter-name">invocation</span></span>) <span class="returntype parameter">→ dynamic</span> </span>  
Invoked when a nonexistent method or property is accessed.

<div class="features">

<span class="feature">inherited</span>

</div>

<span class="name"><a href="sdk-for-flutter-explore-mapview-datasource-tilesource-removelistener">removeListener</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-explore-removeListener-param-listener" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-explore-mapview-datasource-tilesourcelistener-class">TileSourceListener</a></span> <span class="parameter-name">listener</span></span>) <span class="returntype parameter">→ void</span> </span>  
Removes a listener from receiving state notifications.

<span class="name"><a href="sdk-for-flutter-explore-mapview-datasource-tilesource-tostring">toString</a></span><span class="signature">(<wbr></wbr>) <span class="returntype parameter">→ String</span> </span>  
A string representation of this object.

<div class="features">

<span class="feature">inherited</span>

</div>

## Operators

<span class="name"><a href="sdk-for-flutter-explore-mapview-datasource-tilesource-operator_equals">operator ==</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-explore-param-other" class="parameter"><span class="type-annotation">Object</span> <span class="parameter-name">other</span></span>) <span class="returntype parameter">→ bool</span> </span>  
The equality operator.

<div class="features">

<span class="feature">inherited</span>

</div>

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>

