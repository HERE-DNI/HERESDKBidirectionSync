---
title: "CategoryQueryArea class - search library - Dart API"
slug: "sdk-for-flutter-explore-search-categoryqueryarea-class"
---

<div id="sdk-for-flutter-explore-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-explore-dartdoc-main-content" class="main-content" data-above-sidebar="search/search-library-sidebar.html" data-below-sidebar="search/CategoryQueryArea-class-sidebar.html">

<div>

# <span class="kind-class">CategoryQueryArea</span> class

</div>

<div class="section desc markdown">

Area to perform search on.

</div>

<div class="section">

Annotations  
- @<a href="https://pub.dev/documentation/meta/1.17.0/meta/immutable-constant.html">immutable</a>

</div>

## Constructors

<span class="name"><a href="sdk-for-flutter-explore-search-categoryqueryarea-categoryqueryarea-withbox">CategoryQueryArea.withBox</a></span><span class="signature">(<span id="sdk-for-flutter-explore-withBox-param-areaCenter" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-explore-core-geocoordinates-class">GeoCoordinates</a></span> <span class="parameter-name">areaCenter</span>, </span><span id="sdk-for-flutter-explore-withBox-param-boxArea" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-explore-core-geobox-class">GeoBox</a></span> <span class="parameter-name">boxArea</span></span>)</span>  
Constructs a new instance of this class from provided parameters.

<div class="constructor-modifier features">

factory

</div>

<span class="name"><a href="sdk-for-flutter-explore-search-categoryqueryarea-categoryqueryarea-withcenter">CategoryQueryArea.withCenter</a></span><span class="signature">(<span id="sdk-for-flutter-explore-withCenter-param-areaCenter" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-explore-core-geocoordinates-class">GeoCoordinates</a></span> <span class="parameter-name">areaCenter</span></span>)</span>  
Constructs a new instance of this class from provided parameters.

<div class="constructor-modifier features">

factory

</div>

<span class="name"><a href="sdk-for-flutter-explore-search-categoryqueryarea-categoryqueryarea-withcircle">CategoryQueryArea.withCircle</a></span><span class="signature">(<span id="sdk-for-flutter-explore-withCircle-param-areaCenter" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-explore-core-geocoordinates-class">GeoCoordinates</a></span> <span class="parameter-name">areaCenter</span>, </span><span id="sdk-for-flutter-explore-withCircle-param-circleArea" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-explore-core-geocircle-class">GeoCircle</a></span> <span class="parameter-name">circleArea</span></span>)</span>  
Constructs a new instance of this class from provided parameters.

<div class="constructor-modifier features">

factory

</div>

<span class="name"><a href="sdk-for-flutter-explore-search-categoryqueryarea-categoryqueryarea-withcorridorandcenter">CategoryQueryArea.withCorridorAndCenter</a></span><span class="signature">(<span id="sdk-for-flutter-explore-withCorridorAndCenter-param-corridorArea" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-explore-core-geocorridor-class">GeoCorridor</a></span> <span class="parameter-name">corridorArea</span>, </span><span id="sdk-for-flutter-explore-withCorridorAndCenter-param-areaCenter" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-explore-core-geocoordinates-class">GeoCoordinates</a></span> <span class="parameter-name">areaCenter</span></span>)</span>  
Constructs a new instance of this class from provided parameters.

<div class="constructor-modifier features">

factory

</div>

## Properties

<span class="name"><a href="sdk-for-flutter-explore-search-categoryqueryarea-areacenter">areaCenter</a></span> <span class="signature">→ <a href="sdk-for-flutter-explore-core-geocoordinates-class">GeoCoordinates</a></span>  
Geographic coordinates of the center around which to provide the most relevant places.

<div class="features">

<span class="feature">final</span>

</div>

<span class="name"><a href="sdk-for-flutter-explore-search-categoryqueryarea-boxarea">boxArea</a></span> <span class="signature">→ <a href="sdk-for-flutter-explore-core-geobox-class">GeoBox</a>?</span>  
Geographic rectangle area in which to provide the most relevant places.

<div class="features">

<span class="feature">final</span>

</div>

<span class="name"><a href="sdk-for-flutter-explore-search-categoryqueryarea-circlearea">circleArea</a></span> <span class="signature">→ <a href="sdk-for-flutter-explore-core-geocircle-class">GeoCircle</a>?</span>  
Geographic circle area in which to provide the most relevant places.

<div class="features">

<span class="feature">final</span>

</div>

<span class="name"><a href="sdk-for-flutter-explore-search-categoryqueryarea-corridorarea">corridorArea</a></span> <span class="signature">→ <a href="sdk-for-flutter-explore-core-geocorridor-class">GeoCorridor</a>?</span>  
Geographic corridor area in which to provide the most relevant places. The contained polyline and half-width define the area that will be used in a search query.

<div class="features">

<span class="feature">final</span>

</div>

<span class="name"><a href="sdk-for-flutter-explore-search-categoryqueryarea-hashcode">hashCode</a></span> <span class="signature">→ int</span>  
The hash code for this object.

<div class="features">

<span class="feature">no setter</span>

</div>

<span class="name"><a href="sdk-for-flutter-explore-search-categoryqueryarea-runtimetype">runtimeType</a></span> <span class="signature">→ Type</span>  
A representation of the runtime type of the object.

<div class="features">

<span class="feature">no setter</span><span class="feature">inherited</span>

</div>

## Methods

<span class="name"><a href="sdk-for-flutter-explore-search-categoryqueryarea-nosuchmethod">noSuchMethod</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-explore-noSuchMethod-param-invocation" class="parameter"><span class="type-annotation">Invocation</span> <span class="parameter-name">invocation</span></span>) <span class="returntype parameter">→ dynamic</span> </span>  
Invoked when a nonexistent method or property is accessed.

<div class="features">

<span class="feature">inherited</span>

</div>

<span class="name"><a href="sdk-for-flutter-explore-search-categoryqueryarea-tostring">toString</a></span><span class="signature">(<wbr></wbr>) <span class="returntype parameter">→ String</span> </span>  
A string representation of this object.

<div class="features">

<span class="feature">inherited</span>

</div>

## Operators

<span class="name"><a href="sdk-for-flutter-explore-search-categoryqueryarea-operator_equals">operator ==</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-explore-param-other" class="parameter"><span class="type-annotation">Object</span> <span class="parameter-name">other</span></span>) <span class="returntype parameter">→ bool</span> </span>  
The equality operator.

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>

