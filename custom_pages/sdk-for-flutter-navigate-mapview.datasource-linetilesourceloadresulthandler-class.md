---
title: "LineTileSourceLoadResultHandler class - mapview.datasource library - Dart API"
slug: "sdk-for-flutter-navigate-mapview.datasource-linetilesourceloadresulthandler-class"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- LineTileSourceLoadResultHandler-class.html -->
<div id="sdk-for-flutter-navigate-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-navigate-dartdoc-main-content" class="main-content" data-above-sidebar="mapview.datasource/mapview.datasource-library-sidebar.html" data-below-sidebar="mapview.datasource/LineTileSourceLoadResultHandler-class-sidebar.html">

<div>

# <span class="kind-class">LineTileSourceLoadResultHandler</span> class <a href="https://dart.dev/language/class-modifiers#abstract" class="feature feature-abstract" title="This type can not be directly constructed.">abstract</a>

</div>

<div class="section desc markdown">

Result handler of a load tile request.

</div>

## Constructors

<span class="name"><a href="sdk-for-flutter-navigate-mapview-datasource-linetilesourceloadresulthandler-linetilesourceloadresulthandler">LineTileSourceLoadResultHandler</a></span><span class="signature">(<span id="sdk-for-flutter-navigate-param-loadedLambda" class="parameter"><span class="type-annotation">void</span> <span class="parameter-name">loadedLambda</span>(<span id="sdk-for-flutter-navigate-param" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-mapview-datasource-tilekey-class">TileKey</a></span>, </span><span id="sdk-for-flutter-navigate-param" class="parameter"><span class="type-annotation">List<span class="signature">\<<wbr></wbr><span class="type-parameter"><a href="sdk-for-flutter-navigate-mapview-datasource-linedata-class">LineData</a></span>\></span></span>, </span><span id="sdk-for-flutter-navigate-param" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-mapview-datasource-tilesourcetilemetadata-class">TileSourceTileMetadata</a></span></span>), </span><span id="sdk-for-flutter-navigate-param-failedLambda" class="parameter"><span class="type-annotation">void</span> <span class="parameter-name">failedLambda</span>(<span id="sdk-for-flutter-navigate-param" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-mapview-datasource-tilekey-class">TileKey</a></span></span>)</span>)</span>  
Result handler of a load tile request.

<div class="constructor-modifier features">

factory

</div>

## Properties

<span class="name"><a href="sdk-for-flutter-navigate-mapview-datasource-linetilesourceloadresulthandler-hashcode">hashCode</a></span> <span class="signature">→ int</span>  
The hash code for this object.

<div class="features">

<span class="feature">no setter</span><span class="feature">inherited</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-mapview-datasource-linetilesourceloadresulthandler-runtimetype">runtimeType</a></span> <span class="signature">→ Type</span>  
A representation of the runtime type of the object.

<div class="features">

<span class="feature">no setter</span><span class="feature">inherited</span>

</div>

## Methods

<span class="name"><a href="sdk-for-flutter-navigate-mapview-datasource-linetilesourceloadresulthandler-failed">failed</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-navigate-failed-param-tileKey" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-mapview-datasource-tilekey-class">TileKey</a></span> <span class="parameter-name">tileKey</span></span>) <span class="returntype parameter">→ void</span> </span>  
Called upon failed load tile request.

<span class="name"><a href="sdk-for-flutter-navigate-mapview-datasource-linetilesourceloadresulthandler-loaded">loaded</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-navigate-loaded-param-tileKey" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-mapview-datasource-tilekey-class">TileKey</a></span> <span class="parameter-name">tileKey</span>, </span><span id="sdk-for-flutter-navigate-loaded-param-data" class="parameter"><span class="type-annotation">List<span class="signature">\<<wbr></wbr><span class="type-parameter"><a href="sdk-for-flutter-navigate-mapview-datasource-linedata-class">LineData</a></span>\></span></span> <span class="parameter-name">data</span>, </span><span id="sdk-for-flutter-navigate-loaded-param-metadata" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-mapview-datasource-tilesourcetilemetadata-class">TileSourceTileMetadata</a></span> <span class="parameter-name">metadata</span></span>) <span class="returntype parameter">→ void</span> </span>  
Called upon successful load tile request.

<span class="name"><a href="sdk-for-flutter-navigate-mapview-datasource-linetilesourceloadresulthandler-nosuchmethod">noSuchMethod</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-navigate-noSuchMethod-param-invocation" class="parameter"><span class="type-annotation">Invocation</span> <span class="parameter-name">invocation</span></span>) <span class="returntype parameter">→ dynamic</span> </span>  
Invoked when a nonexistent method or property is accessed.

<div class="features">

<span class="feature">inherited</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-mapview-datasource-linetilesourceloadresulthandler-tostring">toString</a></span><span class="signature">(<wbr></wbr>) <span class="returntype parameter">→ String</span> </span>  
A string representation of this object.

<div class="features">

<span class="feature">inherited</span>

</div>

## Operators

<span class="name"><a href="sdk-for-flutter-navigate-mapview-datasource-linetilesourceloadresulthandler-operator_equals">operator ==</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-navigate-param-other" class="parameter"><span class="type-annotation">Object</span> <span class="parameter-name">other</span></span>) <span class="returntype parameter">→ bool</span> </span>  
The equality operator.

<div class="features">

<span class="feature">inherited</span>

</div>

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>

</div>
`
}</HTMLBlock>
