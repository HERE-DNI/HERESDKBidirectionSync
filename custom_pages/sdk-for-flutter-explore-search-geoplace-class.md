---
title: "GeoPlace class - search library - Dart API"
slug: "sdk-for-flutter-explore-search-geoplace-class"
---

<div id="sdk-for-flutter-explore-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-explore-dartdoc-main-content" class="main-content" data-above-sidebar="search/search-library-sidebar.html" data-below-sidebar="search/GeoPlace-class-sidebar.html">

<div>

# <span class="kind-class">GeoPlace</span> class

</div>

<div class="section desc markdown">

GeoPlace struct represents a location object: such as a country, a city, a point of interest (POI) etc.

It can be used for PersonalPlace creation, in order to provide search on custom places.

</div>

## Constructors

<span class="name"><a href="sdk-for-flutter-explore-search-geoplace-geoplace">GeoPlace</a></span><span class="signature">()</span>  

## Properties

<span class="name"><a href="sdk-for-flutter-explore-search-geoplace-address">address</a></span> <span class="signature">↔ <a href="sdk-for-flutter-explore-search-address-class">Address</a></span>  
Address of the place Note: Address can have default value when no data is available.

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

<span class="name"><a href="sdk-for-flutter-explore-search-geoplace-business">business</a></span> <span class="signature">↔ <a href="sdk-for-flutter-explore-search-businessdetails-class">BusinessDetails</a></span>  
Business details Note: BusinessDetails can have default value when no data is available.

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

<span class="name"><a href="sdk-for-flutter-explore-search-geoplace-categories">categories</a></span> <span class="signature">↔ List<span class="signature">\<<wbr></wbr><span class="type-parameter"><a href="sdk-for-flutter-explore-search-placecategory-class">PlaceCategory</a></span>\></span></span>  
List of corresponding categories Note: This list can be empty when no data is available.

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

<span class="name"><a href="sdk-for-flutter-explore-search-geoplace-externalids">externalIDs</a></span> <span class="signature">↔ List<span class="signature">\<<wbr></wbr><span class="type-parameter"><a href="sdk-for-flutter-explore-core-externalid-class">ExternalID</a></span>\></span></span>  
Allows the client to set the id in their own system. The list of supplier references to this place. The references are provided by external suppliers and are only available to users with valid contracts with said suppliers. If the user has no such contracts, the list is empty.

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

<span class="name"><a href="sdk-for-flutter-explore-search-geoplace-hashcode">hashCode</a></span> <span class="signature">→ int</span>  
The hash code for this object.

<div class="features">

<span class="feature">no setter</span>

</div>

<span class="name"><a href="sdk-for-flutter-explore-search-geoplace-location">location</a></span> <span class="signature">↔ <a href="sdk-for-flutter-explore-search-locationdetails-class">LocationDetails</a>?</span>  
Geographical details Note: Can be `null` when retrieved from a suggestion's place property.

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

<span class="name"><a href="sdk-for-flutter-explore-search-geoplace-runtimetype">runtimeType</a></span> <span class="signature">→ Type</span>  
A representation of the runtime type of the object.

<div class="features">

<span class="feature">no setter</span><span class="feature">inherited</span>

</div>

<span class="name"><a href="sdk-for-flutter-explore-search-geoplace-title">title</a></span> <span class="signature">↔ String</span>  
The localized title for the resource. Note: This String can be empty when no data is available.

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

<span class="name"><a href="sdk-for-flutter-explore-search-geoplace-type">type</a></span> <span class="signature">↔ <a href="sdk-for-flutter-explore-search-placetype">PlaceType</a></span>  
Specifies place type.

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

<span class="name"><a href="sdk-for-flutter-explore-search-geoplace-web">web</a></span> <span class="signature">↔ <a href="sdk-for-flutter-explore-search-webdetails-class">WebDetails</a></span>  
Contains info and direct web links to corresponding items. Note: WebDetails can have default value when no data is available.

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

## Methods

<span class="name"><a href="sdk-for-flutter-explore-search-geoplace-getid">getID</a></span><span class="signature">(<wbr></wbr>) <span class="returntype parameter">→ String</span> </span>  
Allow the client to access GeoPlace id.

<span class="name"><a href="sdk-for-flutter-explore-search-geoplace-ismyplace">isMyPlace</a></span><span class="signature">(<wbr></wbr>) <span class="returntype parameter">→ bool</span> </span>  
Allow the client to access info about is it my place or not.

<span class="name"><a href="sdk-for-flutter-explore-search-geoplace-nosuchmethod">noSuchMethod</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-explore-noSuchMethod-param-invocation" class="parameter"><span class="type-annotation">Invocation</span> <span class="parameter-name">invocation</span></span>) <span class="returntype parameter">→ dynamic</span> </span>  
Invoked when a nonexistent method or property is accessed.

<div class="features">

<span class="feature">inherited</span>

</div>

<span class="name"><a href="sdk-for-flutter-explore-search-geoplace-tostring">toString</a></span><span class="signature">(<wbr></wbr>) <span class="returntype parameter">→ String</span> </span>  
A string representation of this object.

<div class="features">

<span class="feature">inherited</span>

</div>

## Operators

<span class="name"><a href="sdk-for-flutter-explore-search-geoplace-operator_equals">operator ==</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-explore-param-other" class="parameter"><span class="type-annotation">Object</span> <span class="parameter-name">other</span></span>) <span class="returntype parameter">→ bool</span> </span>  
The equality operator.

## Static Methods

<span class="name"><a href="sdk-for-flutter-explore-search-geoplace-makemyplace">makeMyPlace</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-explore-makeMyPlace-param-title" class="parameter"><span class="type-annotation">String</span> <span class="parameter-name">title</span>, </span><span id="sdk-for-flutter-explore-makeMyPlace-param-coordinates" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-explore-core-geocoordinates-class">GeoCoordinates</a></span> <span class="parameter-name">coordinates</span></span>) <span class="returntype parameter">→ <a href="sdk-for-flutter-explore-search-geoplace-class">GeoPlace</a></span> </span>  
Creates a new instance of this class.

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>

