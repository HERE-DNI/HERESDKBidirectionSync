---
title: "Address class - search library - Dart API"
slug: "sdk-for-flutter-navigate-search-address-class"
---

<div id="sdk-for-flutter-navigate-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-navigate-dartdoc-main-content" class="main-content" data-above-sidebar="search/search-library-sidebar.html" data-below-sidebar="search/Address-class-sidebar.html">

<div>

# <span class="kind-class">Address</span> class

</div>

<div class="section desc markdown">

Information about the address of a location.

Used in <a href="sdk-for-flutter-navigate-search-place-address">Place.address</a>.

Note that while `OfflineSearchEngine.suggest` and `OfflineSearchEngine.suggestByText` set all available details, `SearchEngine.suggest` and `SearchEngine.suggestByText` set only <a href="sdk-for-flutter-navigate-search-address-addresstext">Address.addressText</a>. Complete address details can be obtained by searching with <a href="sdk-for-flutter-navigate-search-placeidquery-class">PlaceIdQuery</a>.

</div>

## Constructors

<span class="name"><a href="sdk-for-flutter-navigate-search-address-address">Address</a></span><span class="signature">()</span>  
Default constructor. Note: Sets all the string values to "".

## Properties

<span class="name"><a href="sdk-for-flutter-navigate-search-address-addresstext">addressText</a></span> <span class="signature">↔ String</span>  
The text for the address, for example, "Secret Garden, 347 Lewis Ave, Brooklyn, NY 11233, United States". Note: This String can be empty when no data is available.

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-search-address-block">block</a></span> <span class="signature">↔ String</span>  
The block number for the address. It is part of Japanese addressing system. Note: This String can be empty when no data is available.

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-search-address-city">city</a></span> <span class="signature">↔ String</span>  
The city name for the address, for example, "Brooklyn". Note: This String can be empty when no data is available.

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-search-address-country">country</a></span> <span class="signature">↔ String</span>  
The country name for the address, for example, "United States". Note: This String can be empty when no data is available.

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-search-address-countrycode">countryCode</a></span> <span class="signature">↔ String</span>  
An ISO-3166-1 (3-letter) country code for the address, for example, "USA". Note: This String can be empty when no data is available.

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-search-address-county">county</a></span> <span class="signature">↔ String</span>  
The county name for the address. It is a division of a state, typically a secondary-level administrative division of a country or equivalent, for example, "Kings". Note: This String can be empty when no data is available.

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-search-address-district">district</a></span> <span class="signature">↔ String</span>  
The district name for the address. It is a division of city, typically an administrative unit within a larger city or a customary name of a city's neighborhood, for example, "Bedford-Stuyvesant". Note: This String can be empty when no data is available.

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-search-address-hashcode">hashCode</a></span> <span class="signature">→ int</span>  
The hash code for this object.

<div class="features">

<span class="feature">no setter</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-search-address-housenumorname">houseNumOrName</a></span> <span class="signature">↔ String</span>  
The house name or number for the address, for example, "347". Note: This String can be empty when no data is available.

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-search-address-postalcode">postalCode</a></span> <span class="signature">↔ String</span>  
The postal code for the address. It is an alphanumeric string included in a postal address to facilitate mail sorting, known locally in various countries throughout the world as a postcode, post code, PIN or ZIP Code, for example, "11233". Note: This String can be empty when no data is available.

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-search-address-runtimetype">runtimeType</a></span> <span class="signature">→ Type</span>  
A representation of the runtime type of the object.

<div class="features">

<span class="feature">no setter</span><span class="feature">inherited</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-search-address-state">state</a></span> <span class="signature">↔ String</span>  
The state name for the address. It is the name of the state division of a country, for example, "New York". Note: This String can be empty when no data is available.

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-search-address-statecode">stateCode</a></span> <span class="signature">↔ String</span>  
The state code for the address. It is code/abbreviation of the state division of a country, for example, "NY". Note: This String can be empty when no data is available.

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-search-address-street">street</a></span> <span class="signature">↔ String</span>  
The street name for the address, for example, "Lewis Ave". Note: This String can be empty when no data is available.

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-search-address-subblock">subBlock</a></span> <span class="signature">↔ String</span>  
The sub-block number for the address. It is part of Japanese addressing system. Note: This String can be empty when no data is available.

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-search-address-subdistrict">subdistrict</a></span> <span class="signature">↔ String</span>  
The subdistrict name for the address. It is a subdivision of a district. Note: This String can be empty when no data is available.

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-search-address-type">type</a></span> <span class="signature">↔ <a href="sdk-for-flutter-navigate-search-addresstype">AddressType</a>?</span>  
Specifies the address type.

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

## Methods

<span class="name"><a href="sdk-for-flutter-navigate-search-address-nosuchmethod">noSuchMethod</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-navigate-noSuchMethod-param-invocation" class="parameter"><span class="type-annotation">Invocation</span> <span class="parameter-name">invocation</span></span>) <span class="returntype parameter">→ dynamic</span> </span>  
Invoked when a nonexistent method or property is accessed.

<div class="features">

<span class="feature">inherited</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-search-address-tostring">toString</a></span><span class="signature">(<wbr></wbr>) <span class="returntype parameter">→ String</span> </span>  
A string representation of this object.

<div class="features">

<span class="feature">inherited</span>

</div>

## Operators

<span class="name"><a href="sdk-for-flutter-navigate-search-address-operator_equals">operator ==</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-navigate-param-other" class="parameter"><span class="type-annotation">Object</span> <span class="parameter-name">other</span></span>) <span class="returntype parameter">→ bool</span> </span>  
The equality operator.

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>

