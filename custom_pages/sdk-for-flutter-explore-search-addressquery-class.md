---
title: "AddressQuery class - search library - Dart API"
slug: "sdk-for-flutter-explore-search-addressquery-class"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- AddressQuery-class.html -->
<div id="sdk-for-flutter-explore-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-explore-dartdoc-main-content" class="main-content" data-above-sidebar="search/search-library-sidebar.html" data-below-sidebar="search/AddressQuery-class-sidebar.html">

<div>

# <span class="kind-class">AddressQuery</span> class

</div>

<div class="section desc markdown">

The options to specify an address query.

A <a href="sdk-for-flutter-explore-search-addressquery-query">AddressQuery.query</a> can consist of parts of an address or full addresses, optionally comma separated. <a href="sdk-for-flutter-explore-search-addressquery-class">AddressQuery</a> should only be used to search for parts of the address, excluding the POI name. For example, "Invalidenstraße 116, Berlin, Germany" is appropriate, whereas "HERE, Invalidenstraße 116, Berlin, Germany" is not. To be able to include the POI name, use <a href="sdk-for-flutter-explore-search-textquery-class">TextQuery</a> instead. <a href="sdk-for-flutter-explore-search-searchoptions-languagecode">SearchOptions.languageCode</a> specifies the language of the <a href="sdk-for-flutter-explore-search-addressquery-query">AddressQuery.query</a> and determines the preferred language of the results.

</div>

<div class="section">

Annotations  
- @<a href="https://pub.dev/documentation/meta/1.17.0/meta/immutable-constant.html">immutable</a>

</div>

## Constructors

<span class="name"><a href="sdk-for-flutter-explore-search-addressquery-addressquery">AddressQuery</a></span><span class="signature">(<span id="sdk-for-flutter-explore-param-query" class="parameter"><span class="type-annotation">String</span> <span class="parameter-name">query</span></span>)</span>  
Constructs an AddressQuery from the provided text query.

<div class="constructor-modifier features">

factory

</div>

<span class="name"><a href="sdk-for-flutter-explore-search-addressquery-addressquery-withareacenter">AddressQuery.withAreaCenter</a></span><span class="signature">(<span id="sdk-for-flutter-explore-withAreaCenter-param-query" class="parameter"><span class="type-annotation">String</span> <span class="parameter-name">query</span>, </span><span id="sdk-for-flutter-explore-withAreaCenter-param-areaCenter" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-explore-core-geocoordinates-class">GeoCoordinates</a></span> <span class="parameter-name">areaCenter</span></span>)</span>  
Constructs an AddressQuery from the provided text query and geographical coordinates.

<div class="constructor-modifier features">

factory

</div>

<span class="name"><a href="sdk-for-flutter-explore-search-addressquery-addressquery-withareacenterincountries">AddressQuery.withAreaCenterInCountries</a></span><span class="signature">(<span id="sdk-for-flutter-explore-withAreaCenterInCountries-param-query" class="parameter"><span class="type-annotation">String</span> <span class="parameter-name">query</span>, </span><span id="sdk-for-flutter-explore-withAreaCenterInCountries-param-areaCenter" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-explore-core-geocoordinates-class">GeoCoordinates</a></span> <span class="parameter-name">areaCenter</span>, </span><span id="sdk-for-flutter-explore-withAreaCenterInCountries-param-countries" class="parameter"><span class="type-annotation">List<span class="signature">\<<wbr></wbr><span class="type-parameter"><a href="sdk-for-flutter-explore-core-countrycode">CountryCode</a></span>\></span></span> <span class="parameter-name">countries</span></span>)</span>  
Constructs an AddressQuery from the provided text query, geographical coordinates and the list of countries the query is applied in.

<div class="constructor-modifier features">

factory

</div>

## Properties

<span class="name"><a href="sdk-for-flutter-explore-search-addressquery-areacenter">areaCenter</a></span> <span class="signature">→ <a href="sdk-for-flutter-explore-core-geocoordinates-class">GeoCoordinates</a>?</span>  
Geographical coordinates of the center around which to provide the most relevant places. For Offline Search null value will result in <a href="sdk-for-flutter-explore-search-searcherror">SearchError.invalidArea</a>

<div class="features">

<span class="feature">final</span>

</div>

<span class="name"><a href="sdk-for-flutter-explore-search-addressquery-countries">countries</a></span> <span class="signature">→ List<span class="signature">\<<wbr></wbr><span class="type-parameter"><a href="sdk-for-flutter-explore-core-countrycode">CountryCode</a></span>\></span></span>  
A list of countries that the query is applied in. Not supported in `OfflineSearchEngine` (only available for the Navigate license).

<div class="features">

<span class="feature">final</span>

</div>

<span class="name"><a href="sdk-for-flutter-explore-search-addressquery-hashcode">hashCode</a></span> <span class="signature">→ int</span>  
The hash code for this object.

<div class="features">

<span class="feature">no setter</span>

</div>

<span class="name"><a href="sdk-for-flutter-explore-search-addressquery-query">query</a></span> <span class="signature">→ String</span>  
Desired address query to search.

<div class="features">

<span class="feature">final</span>

</div>

<span class="name"><a href="sdk-for-flutter-explore-search-addressquery-runtimetype">runtimeType</a></span> <span class="signature">→ Type</span>  
A representation of the runtime type of the object.

<div class="features">

<span class="feature">no setter</span><span class="feature">inherited</span>

</div>

## Methods

<span class="name"><a href="sdk-for-flutter-explore-search-addressquery-nosuchmethod">noSuchMethod</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-explore-noSuchMethod-param-invocation" class="parameter"><span class="type-annotation">Invocation</span> <span class="parameter-name">invocation</span></span>) <span class="returntype parameter">→ dynamic</span> </span>  
Invoked when a nonexistent method or property is accessed.

<div class="features">

<span class="feature">inherited</span>

</div>

<span class="name"><a href="sdk-for-flutter-explore-search-addressquery-tostring">toString</a></span><span class="signature">(<wbr></wbr>) <span class="returntype parameter">→ String</span> </span>  
A string representation of this object.

<div class="features">

<span class="feature">inherited</span>

</div>

## Operators

<span class="name"><a href="sdk-for-flutter-explore-search-addressquery-operator_equals">operator ==</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-explore-param-other" class="parameter"><span class="type-annotation">Object</span> <span class="parameter-name">other</span></span>) <span class="returntype parameter">→ bool</span> </span>  
The equality operator.

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>

</div>
`
}</HTMLBlock>
