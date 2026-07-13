---
title: "PlaceFilter class - search library - Dart API"
slug: "sdk-for-flutter-navigate-search-placefilter-class"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- PlaceFilter-class.html -->
<div id="sdk-for-flutter-navigate-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-navigate-dartdoc-main-content" class="main-content" data-above-sidebar="search/search-library-sidebar.html" data-below-sidebar="search/PlaceFilter-class-sidebar.html">

<div>

# <span class="kind-class">PlaceFilter</span> class

</div>

<div class="section desc markdown">

The filter options to specify a place.

Consists of fuel, truck and EV options.

</div>

## Constructors

<span class="name"><a href="sdk-for-flutter-navigate-search-placefilter-placefilter">PlaceFilter</a></span><span class="signature">()</span>  

## Properties

<span class="name"><a href="sdk-for-flutter-navigate-search-placefilter-ev">ev</a></span> <span class="signature">↔ <a href="sdk-for-flutter-navigate-search-placefilterev-class">PlaceFilterEv</a></span>  
Constraints that are applicable on the places of category EV station.

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-search-placefilter-fueltypes">fuelTypes</a></span> <span class="signature">↔ List<span class="signature">\<<wbr></wbr><span class="type-parameter"><a href="sdk-for-flutter-navigate-transport-fueltype">FuelType</a></span>\></span></span>  
The list of <a href="sdk-for-flutter-navigate-transport-fueltype">FuelType</a> elements that should be used to find only the <a href="sdk-for-flutter-navigate-search-fuelstation-class">FuelStation</a> search results that support all of them. This filter is available to use with the `SearchEngine` and `OfflineSearchEngine` (only available for the Navigate license), however `OfflineSearchEngine` supports it only for `searchByText` and `searchByCategory` with allowed fuel types `DIESEL`, `LPG`, `BIO_DIESEL`, `CNG`, `DIESEL_WITH_ADDITIVES`, `E10`, `E85`, `ETHANOL`, `ETHANOL_WITH_ADDITIVES`, `GASOLINE`, `HYDROGEN`, `LNG`, `MIDGRADE`, `PREMIUM` and `REGULAR`.

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-search-placefilter-hashcode">hashCode</a></span> <span class="signature">→ int</span>  
The hash code for this object.

<div class="features">

<span class="feature">no setter</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-search-placefilter-runtimetype">runtimeType</a></span> <span class="signature">→ Type</span>  
A representation of the runtime type of the object.

<div class="features">

<span class="feature">no setter</span><span class="feature">inherited</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-search-placefilter-truckclass">truckClass</a></span> <span class="signature">↔ <a href="sdk-for-flutter-navigate-transport-truckclass">TruckClass</a>?</span>  
Should be used to find only the <a href="sdk-for-flutter-navigate-search-fuelstation-class">FuelStation</a> search results with minimum supported <a href="sdk-for-flutter-navigate-transport-truckclass">TruckClass</a>. This filter is only available to use with the `SearchEngine`. The `OfflineSearchEngine` (only available for the Navigate license) does not apply this filter. <a href="sdk-for-flutter-navigate-transport-truckclass">TruckClass.lightClass</a> is not accepted in the filter. Otherwise will result in <a href="sdk-for-flutter-navigate-search-searcherror">SearchError.invalidTruckClass</a>.

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-search-placefilter-truckfueltypes">truckFuelTypes</a></span> <span class="signature">↔ List<span class="signature">\<<wbr></wbr><span class="type-parameter"><a href="sdk-for-flutter-navigate-transport-truckfueltype">TruckFuelType</a></span>\></span></span>  
The list of <a href="sdk-for-flutter-navigate-transport-truckfueltype">TruckFuelType</a> elements that should be used to find only the <a href="sdk-for-flutter-navigate-search-fuelstation-class">FuelStation</a> search results that support all of them. Not supported for `suggestByText` in `OfflineSearchEngine` (only available for the Navigate license).

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

## Methods

<span class="name"><a href="sdk-for-flutter-navigate-search-placefilter-nosuchmethod">noSuchMethod</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-navigate-noSuchMethod-param-invocation" class="parameter"><span class="type-annotation">Invocation</span> <span class="parameter-name">invocation</span></span>) <span class="returntype parameter">→ dynamic</span> </span>  
Invoked when a nonexistent method or property is accessed.

<div class="features">

<span class="feature">inherited</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-search-placefilter-tostring">toString</a></span><span class="signature">(<wbr></wbr>) <span class="returntype parameter">→ String</span> </span>  
A string representation of this object.

<div class="features">

<span class="feature">inherited</span>

</div>

## Operators

<span class="name"><a href="sdk-for-flutter-navigate-search-placefilter-operator_equals">operator ==</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-navigate-param-other" class="parameter"><span class="type-annotation">Object</span> <span class="parameter-name">other</span></span>) <span class="returntype parameter">→ bool</span> </span>  
The equality operator.

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>

</div>
`
}</HTMLBlock>
