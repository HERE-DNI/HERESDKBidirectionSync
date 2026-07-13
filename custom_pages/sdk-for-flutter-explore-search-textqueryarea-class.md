---
title: "TextQueryArea class - search library - Dart API"
slug: "sdk-for-flutter-explore-search-textqueryarea-class"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- TextQueryArea-class.html -->
<div id="sdk-for-flutter-explore-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-explore-dartdoc-main-content" class="main-content" data-above-sidebar="search/search-library-sidebar.html" data-below-sidebar="search/TextQueryArea-class-sidebar.html">

<div>

# <span class="kind-class">TextQueryArea</span> class

</div>

<div class="section desc markdown">

Area to perform search on.

</div>

<div class="section">

Annotations  
- @<a href="https://pub.dev/documentation/meta/1.17.0/meta/immutable-constant.html">immutable</a>

</div>

## Constructors

<span class="name"><a href="sdk-for-flutter-explore-search-textqueryarea-textqueryarea-withbox">TextQueryArea.withBox</a></span><span class="signature">(<span id="sdk-for-flutter-explore-withBox-param-boxArea" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-explore-core-geobox-class">GeoBox</a></span> <span class="parameter-name">boxArea</span></span>)</span>  
Constructs a new instance of this class from provided parameters.

<div class="constructor-modifier features">

factory

</div>

<span class="name"><a href="sdk-for-flutter-explore-search-textqueryarea-textqueryarea-withcenter">TextQueryArea.withCenter</a></span><span class="signature">(<span id="sdk-for-flutter-explore-withCenter-param-areaCenter" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-explore-core-geocoordinates-class">GeoCoordinates</a></span> <span class="parameter-name">areaCenter</span></span>)</span>  
Constructs a new instance of this class from provided parameters.

<div class="constructor-modifier features">

factory

</div>

<span class="name"><a href="sdk-for-flutter-explore-search-textqueryarea-textqueryarea-withcircle">TextQueryArea.withCircle</a></span><span class="signature">(<span id="sdk-for-flutter-explore-withCircle-param-circleArea" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-explore-core-geocircle-class">GeoCircle</a></span> <span class="parameter-name">circleArea</span></span>)</span>  
Constructs a new instance of this class from provided parameters.

<div class="constructor-modifier features">

factory

</div>

<span class="name"><a href="sdk-for-flutter-explore-search-textqueryarea-textqueryarea-withcorridor">TextQueryArea.withCorridor</a></span><span class="signature">(<span id="sdk-for-flutter-explore-withCorridor-param-corridorArea" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-explore-core-geocorridor-class">GeoCorridor</a></span> <span class="parameter-name">corridorArea</span>, </span><span id="sdk-for-flutter-explore-withCorridor-param-areaCenter" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-explore-core-geocoordinates-class">GeoCoordinates</a></span> <span class="parameter-name">areaCenter</span></span>)</span>  
Constructs a new instance of this class from provided parameters.

<div class="constructor-modifier features">

factory

</div>

<span class="name"><a href="sdk-for-flutter-explore-search-textqueryarea-textqueryarea-withcountries">TextQueryArea.withCountries</a></span><span class="signature">(<span id="sdk-for-flutter-explore-withCountries-param-countries" class="parameter"><span class="type-annotation">List<span class="signature">\<<wbr></wbr><span class="type-parameter"><a href="sdk-for-flutter-explore-core-countrycode">CountryCode</a></span>\></span></span> <span class="parameter-name">countries</span>, </span><span id="sdk-for-flutter-explore-withCountries-param-areaCenter" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-explore-core-geocoordinates-class">GeoCoordinates</a></span> <span class="parameter-name">areaCenter</span></span>)</span>  
Constructs a new instance of this class from provided parameters.

<div class="constructor-modifier features">

factory

</div>

## Properties

<span class="name"><a href="sdk-for-flutter-explore-search-textqueryarea-areacenter">areaCenter</a></span> <span class="signature">→ <a href="sdk-for-flutter-explore-core-geocoordinates-class">GeoCoordinates</a>?</span>  
Geographic coordinates of the center around which to provide the most relevant places. For Offline Search, one of <a href="sdk-for-flutter-explore-search-textqueryarea-areacenter">TextQueryArea.areaCenter</a>, <a href="sdk-for-flutter-explore-search-textqueryarea-boxarea">TextQueryArea.boxArea</a> and <a href="sdk-for-flutter-explore-search-textqueryarea-circlearea">TextQueryArea.circleArea</a> has to be set, otherwise it will result in <a href="sdk-for-flutter-explore-search-searcherror">SearchError.invalidArea</a>.

<div class="features">

<span class="feature">final</span>

</div>

<span class="name"><a href="sdk-for-flutter-explore-search-textqueryarea-boxarea">boxArea</a></span> <span class="signature">→ <a href="sdk-for-flutter-explore-core-geobox-class">GeoBox</a>?</span>  
Geographic rectangle area in which to provide the most relevant places. For Offline Search, one of <a href="sdk-for-flutter-explore-search-textqueryarea-areacenter">TextQueryArea.areaCenter</a>, <a href="sdk-for-flutter-explore-search-textqueryarea-boxarea">TextQueryArea.boxArea</a> and <a href="sdk-for-flutter-explore-search-textqueryarea-circlearea">TextQueryArea.circleArea</a> has to be set, otherwise it will result in <a href="sdk-for-flutter-explore-search-searcherror">SearchError.invalidArea</a>. Also, for Offline Search, search in a given `GeoBox` restricts the results to only POIs.

<div class="features">

<span class="feature">final</span>

</div>

<span class="name"><a href="sdk-for-flutter-explore-search-textqueryarea-circlearea">circleArea</a></span> <span class="signature">→ <a href="sdk-for-flutter-explore-core-geocircle-class">GeoCircle</a>?</span>  
Geographic circle area in which to provide the most relevant places. For Offline Search, one of <a href="sdk-for-flutter-explore-search-textqueryarea-areacenter">TextQueryArea.areaCenter</a>, <a href="sdk-for-flutter-explore-search-textqueryarea-boxarea">TextQueryArea.boxArea</a> and <a href="sdk-for-flutter-explore-search-textqueryarea-circlearea">TextQueryArea.circleArea</a> has to be set, otherwise it will result in <a href="sdk-for-flutter-explore-search-searcherror">SearchError.invalidArea</a>. Also, for Offline Search, search in a given `GeoCircle` restricts the results to only POIs.

<div class="features">

<span class="feature">final</span>

</div>

<span class="name"><a href="sdk-for-flutter-explore-search-textqueryarea-corridorarea">corridorArea</a></span> <span class="signature">→ <a href="sdk-for-flutter-explore-core-geocorridor-class">GeoCorridor</a>?</span>  
Geographic corridor area in which to provide the most relevant places. The contained polyline and half-width define the area that will be used in a search query.

<div class="features">

<span class="feature">final</span>

</div>

<span class="name"><a href="sdk-for-flutter-explore-search-textqueryarea-countries">countries</a></span> <span class="signature">→ List<span class="signature">\<<wbr></wbr><span class="type-parameter"><a href="sdk-for-flutter-explore-core-countrycode">CountryCode</a></span>\></span></span>  
A list of countries that the query is applied in. Not supported in `OfflineSearchEngine` (which is only available for the Navigate license).

<div class="features">

<span class="feature">final</span>

</div>

<span class="name"><a href="sdk-for-flutter-explore-search-textqueryarea-hashcode">hashCode</a></span> <span class="signature">→ int</span>  
The hash code for this object.

<div class="features">

<span class="feature">no setter</span>

</div>

<span class="name"><a href="sdk-for-flutter-explore-search-textqueryarea-runtimetype">runtimeType</a></span> <span class="signature">→ Type</span>  
A representation of the runtime type of the object.

<div class="features">

<span class="feature">no setter</span><span class="feature">inherited</span>

</div>

## Methods

<span class="name"><a href="sdk-for-flutter-explore-search-textqueryarea-nosuchmethod">noSuchMethod</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-explore-noSuchMethod-param-invocation" class="parameter"><span class="type-annotation">Invocation</span> <span class="parameter-name">invocation</span></span>) <span class="returntype parameter">→ dynamic</span> </span>  
Invoked when a nonexistent method or property is accessed.

<div class="features">

<span class="feature">inherited</span>

</div>

<span class="name"><a href="sdk-for-flutter-explore-search-textqueryarea-tostring">toString</a></span><span class="signature">(<wbr></wbr>) <span class="returntype parameter">→ String</span> </span>  
A string representation of this object.

<div class="features">

<span class="feature">inherited</span>

</div>

## Operators

<span class="name"><a href="sdk-for-flutter-explore-search-textqueryarea-operator_equals">operator ==</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-explore-param-other" class="parameter"><span class="type-annotation">Object</span> <span class="parameter-name">other</span></span>) <span class="returntype parameter">→ bool</span> </span>  
The equality operator.

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>

</div>
`
}</HTMLBlock>
