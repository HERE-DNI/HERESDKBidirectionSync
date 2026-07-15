---
title: "RasterDataSourceCacheConfiguration class - mapview.datasource library - Dart API"
slug: "sdk-for-flutter-explore-mapview-datasource-rasterdatasourcecacheconfiguration-class"
---

<div id="sdk-for-flutter-explore-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-explore-dartdoc-main-content" class="main-content" data-above-sidebar="mapview.datasource/mapview.datasource-library-sidebar.html" data-below-sidebar="mapview.datasource/RasterDataSourceCacheConfiguration-class-sidebar.html">

<div>

# <span class="kind-class">RasterDataSourceCacheConfiguration</span> class

</div>

<div class="section desc markdown">

Configuration of a local data cache.

</div>

## Constructors

<span class="name"><a href="sdk-for-flutter-explore-mapview-datasource-rasterdatasourcecacheconfiguration-rasterdatasourcecacheconfiguration">RasterDataSourceCacheConfiguration</a></span><span class="signature">(<span id="sdk-for-flutter-explore-param-path" class="parameter"><span class="type-annotation">String</span> <span class="parameter-name">path</span>, </span><span id="sdk-for-flutter-explore-param-diskSize" class="parameter"><span class="type-annotation">int</span> <span class="parameter-name">diskSize</span></span>)</span>  
Constructs a Cache object from the provided path and cache size.

<span class="name"><a href="sdk-for-flutter-explore-mapview-datasource-rasterdatasourcecacheconfiguration-rasterdatasourcecacheconfiguration-withdefaults">RasterDataSourceCacheConfiguration.withDefaults</a></span><span class="signature">(<span id="sdk-for-flutter-explore-withDefaults-param-path" class="parameter"><span class="type-annotation">String</span> <span class="parameter-name">path</span></span>)</span>  
Constructs a Cache object from the provided path and a default cache size of 32 MiB.

## Properties

<span class="name"><a href="sdk-for-flutter-explore-mapview-datasource-rasterdatasourcecacheconfiguration-disksize">diskSize</a></span> <span class="signature">↔ int</span>  
The maximum size to use on disk for the cache, in bytes. Default is 32 MiB. This cache is independent from the map cache as defined via `SDKOptions`. Its size is only limited by the total device storage capacity.

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

<span class="name"><a href="sdk-for-flutter-explore-mapview-datasource-rasterdatasourcecacheconfiguration-hashcode">hashCode</a></span> <span class="signature">→ int</span>  
The hash code for this object.

<div class="features">

<span class="feature">no setter</span><span class="feature">inherited</span>

</div>

<span class="name"><a href="sdk-for-flutter-explore-mapview-datasource-rasterdatasourcecacheconfiguration-path">path</a></span> <span class="signature">↔ String</span>  
The path to the directory to use for the cache. By default, the map gets initialized with a data path which can be fetched from `SDKOptions.cachePath`. The cache will be relative to this path, unless an absolute path is provided. The cache can be stored in an internal/external storage as long as the app has read/write permissions. Empty string means the data path will be used for caching. If the provided path, either as absolute path or as relative path is invalid, then caching will be disabled. There is no contraint regarding the existence of the path. If the path does not exist but is valid, it will be created.

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

<span class="name"><a href="sdk-for-flutter-explore-mapview-datasource-rasterdatasourcecacheconfiguration-runtimetype">runtimeType</a></span> <span class="signature">→ Type</span>  
A representation of the runtime type of the object.

<div class="features">

<span class="feature">no setter</span><span class="feature">inherited</span>

</div>

## Methods

<span class="name"><a href="sdk-for-flutter-explore-mapview-datasource-rasterdatasourcecacheconfiguration-nosuchmethod">noSuchMethod</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-explore-noSuchMethod-param-invocation" class="parameter"><span class="type-annotation">Invocation</span> <span class="parameter-name">invocation</span></span>) <span class="returntype parameter">→ dynamic</span> </span>  
Invoked when a nonexistent method or property is accessed.

<div class="features">

<span class="feature">inherited</span>

</div>

<span class="name"><a href="sdk-for-flutter-explore-mapview-datasource-rasterdatasourcecacheconfiguration-tostring">toString</a></span><span class="signature">(<wbr></wbr>) <span class="returntype parameter">→ String</span> </span>  
A string representation of this object.

<div class="features">

<span class="feature">inherited</span>

</div>

## Operators

<span class="name"><a href="sdk-for-flutter-explore-mapview-datasource-rasterdatasourcecacheconfiguration-operator_equals">operator ==</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-explore-param-other" class="parameter"><span class="type-annotation">Object</span> <span class="parameter-name">other</span></span>) <span class="returntype parameter">→ bool</span> </span>  
The equality operator.

<div class="features">

<span class="feature">inherited</span>

</div>

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>

