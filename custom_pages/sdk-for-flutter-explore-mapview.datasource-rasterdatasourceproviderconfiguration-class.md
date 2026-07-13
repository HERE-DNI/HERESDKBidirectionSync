---
title: "RasterDataSourceProviderConfiguration class - mapview.datasource library - Dart API"
slug: "sdk-for-flutter-explore-mapview.datasource-rasterdatasourceproviderconfiguration-class"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- RasterDataSourceProviderConfiguration-class.html -->
<div id="sdk-for-flutter-explore-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-explore-dartdoc-main-content" class="main-content" data-above-sidebar="mapview.datasource/mapview.datasource-library-sidebar.html" data-below-sidebar="mapview.datasource/RasterDataSourceProviderConfiguration-class-sidebar.html">

<div>

# <span class="kind-class">RasterDataSourceProviderConfiguration</span> class

</div>

<div class="section desc markdown">

Configuration of a data provider.

</div>

## Constructors

<span class="name"><a href="sdk-for-flutter-explore-mapview-datasource-rasterdatasourceproviderconfiguration-rasterdatasourceproviderconfiguration-default">RasterDataSourceProviderConfiguration.Default</a></span><span class="signature">(<span id="sdk-for-flutter-explore-Default-param-urlProvider" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-explore-mapview-datasource-tileurlprovidercallback">TileUrlProviderCallback</a></span> <span class="parameter-name">urlProvider</span>, </span><span id="sdk-for-flutter-explore-Default-param-tilingScheme" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-explore-mapview-datasource-tilingscheme">TilingScheme</a></span> <span class="parameter-name">tilingScheme</span>, </span><span id="sdk-for-flutter-explore-Default-param-storageLevels" class="parameter"><span class="type-annotation">List<span class="signature">\<<wbr></wbr><span class="type-parameter">int</span>\></span></span> <span class="parameter-name">storageLevels</span>, </span><span id="sdk-for-flutter-explore-Default-param-hasAlphaChannel" class="parameter"><span class="type-annotation">bool</span> <span class="parameter-name">hasAlphaChannel</span>, </span><span id="sdk-for-flutter-explore-Default-param-headers" class="parameter"><span class="type-annotation">Map<span class="signature">\<<wbr></wbr><span class="type-parameter">String</span>, <span class="type-parameter">String</span>\></span>?</span> <span class="parameter-name">headers</span></span>)</span>  
Creates a new instance.

<span class="name"><a href="sdk-for-flutter-explore-mapview-datasource-rasterdatasourceproviderconfiguration-rasterdatasourceproviderconfiguration-withdefaults">RasterDataSourceProviderConfiguration.withDefaults</a></span><span class="signature">(<span id="sdk-for-flutter-explore-withDefaults-param-urlProvider" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-explore-mapview-datasource-tileurlprovidercallback">TileUrlProviderCallback</a></span> <span class="parameter-name">urlProvider</span>, </span><span id="sdk-for-flutter-explore-withDefaults-param-tilingScheme" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-explore-mapview-datasource-tilingscheme">TilingScheme</a></span> <span class="parameter-name">tilingScheme</span>, </span><span id="sdk-for-flutter-explore-withDefaults-param-storageLevels" class="parameter"><span class="type-annotation">List<span class="signature">\<<wbr></wbr><span class="type-parameter">int</span>\></span></span> <span class="parameter-name">storageLevels</span></span>)</span>  
Creates a new instance.

## Properties

<span class="name"><a href="sdk-for-flutter-explore-mapview-datasource-rasterdatasourceproviderconfiguration-hasalphachannel">hasAlphaChannel</a></span> <span class="signature">↔ bool</span>  
A flag indicating whether the image content contains an alpha channel for transparency. Default value is `false`.

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

<span class="name"><a href="sdk-for-flutter-explore-mapview-datasource-rasterdatasourceproviderconfiguration-hashcode">hashCode</a></span> <span class="signature">→ int</span>  
The hash code for this object.

<div class="features">

<span class="feature">no setter</span><span class="feature">inherited</span>

</div>

<span class="name"><a href="sdk-for-flutter-explore-mapview-datasource-rasterdatasourceproviderconfiguration-headers">headers</a></span> <span class="signature">↔ Map<span class="signature">\<<wbr></wbr><span class="type-parameter">String</span>, <span class="type-parameter">String</span>\></span>?</span>  
The optional name-value pairs specifying HTTP headers that are passed with each tile request.

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

<span class="name"><a href="sdk-for-flutter-explore-mapview-datasource-rasterdatasourceproviderconfiguration-runtimetype">runtimeType</a></span> <span class="signature">→ Type</span>  
A representation of the runtime type of the object.

<div class="features">

<span class="feature">no setter</span><span class="feature">inherited</span>

</div>

<span class="name"><a href="sdk-for-flutter-explore-mapview-datasource-rasterdatasourceproviderconfiguration-storagelevels">storageLevels</a></span> <span class="signature">↔ List<span class="signature">\<<wbr></wbr><span class="type-parameter">int</span>\></span></span>  
The storage levels available for this data source. Supported range \[0, 31\]. At least one level must be available for this provider to be used as a source of data. At storage level zero, the whole world is represented by one tile. At storage level 1 the world is split in 2x2 tiles (or in 2x1 tiles, depending on the tiling scheme). The tiling process continues in this fashion until sufficient granularity has been achieved. In the XYZ addresing scheme for tiles, z value of the tile key coresponds to the storage level. Depending on the available storage levels and the given camera zoom level, the appropriate z value of the tile key will be determined.

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

<span class="name"><a href="sdk-for-flutter-explore-mapview-datasource-rasterdatasourceproviderconfiguration-tilingscheme">tilingScheme</a></span> <span class="signature">↔ <a href="sdk-for-flutter-explore-mapview-datasource-tilingscheme">TilingScheme</a></span>  
The tiling scheme used by this source.

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

<span class="name"><a href="sdk-for-flutter-explore-mapview-datasource-rasterdatasourceproviderconfiguration-urlprovider">urlProvider</a></span> <span class="signature">↔ <a href="sdk-for-flutter-explore-mapview-datasource-tileurlprovidercallback">TileUrlProviderCallback</a></span>  
Provides a function that generates URLs based on tile coordinates and storage level.

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

## Methods

<span class="name"><a href="sdk-for-flutter-explore-mapview-datasource-rasterdatasourceproviderconfiguration-nosuchmethod">noSuchMethod</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-explore-noSuchMethod-param-invocation" class="parameter"><span class="type-annotation">Invocation</span> <span class="parameter-name">invocation</span></span>) <span class="returntype parameter">→ dynamic</span> </span>  
Invoked when a nonexistent method or property is accessed.

<div class="features">

<span class="feature">inherited</span>

</div>

<span class="name"><a href="sdk-for-flutter-explore-mapview-datasource-rasterdatasourceproviderconfiguration-tostring">toString</a></span><span class="signature">(<wbr></wbr>) <span class="returntype parameter">→ String</span> </span>  
A string representation of this object.

<div class="features">

<span class="feature">inherited</span>

</div>

## Operators

<span class="name"><a href="sdk-for-flutter-explore-mapview-datasource-rasterdatasourceproviderconfiguration-operator_equals">operator ==</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-explore-param-other" class="parameter"><span class="type-annotation">Object</span> <span class="parameter-name">other</span></span>) <span class="returntype parameter">→ bool</span> </span>  
The equality operator.

<div class="features">

<span class="feature">inherited</span>

</div>

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>

</div>
`
}</HTMLBlock>
