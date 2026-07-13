---
title: "Place class - search library - Dart API"
slug: "sdk-for-flutter-explore-search-place-class"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- Place-class.html -->
<div id="sdk-for-flutter-explore-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-explore-dartdoc-main-content" class="main-content" data-above-sidebar="search/search-library-sidebar.html" data-below-sidebar="search/Place-class-sidebar.html">

<div>

# <span class="kind-class">Place</span> class <a href="https://dart.dev/language/class-modifiers#abstract" class="feature feature-abstract" title="This type can not be directly constructed.">abstract</a>

</div>

<div class="section desc markdown">

Represents a location object, such as a country, a city, a point of interest (POI) etc.

</div>

## Constructors

<span class="name"><a href="sdk-for-flutter-explore-search-place-place">Place</a></span><span class="signature">()</span>  

## Properties

<span class="name"><a href="sdk-for-flutter-explore-search-place-accesspoints">accessPoints</a></span> <span class="signature">→ List<span class="signature">\<<wbr></wbr><span class="type-parameter"><a href="sdk-for-flutter-explore-core-geocoordinates-class">GeoCoordinates</a></span>\></span></span>  
The access points to the place, such as the points on a road or in a parking lot. A place can have multiple access points. For example, a large warehouse can have multiple entrances, while the center of the warehouse may not be directly reachable. Note that access points are meant to be reachable by vehicles. For routes it is recommended to navigate to one of the available access points (if any), whereas the `sideOfStreetHint` should be set to the geographic coordinates of the place. The list is empty when no access points are known or when the place is directly reachable. A place can have multiple access points. For example, a large warehouse can have multiple entrances, while the center of the warehouse may not be directly reachable. Note that access points are meant to be reachable by vehicles. For routes it is recommended to navigate to one of the available access points (if any), whereas the `sideOfStreetHint` should be set to the geographic coordinates of the place. The list is empty when no access points are known or when the place is directly reachable. Gets the access points to the place, such as the points on a road or in a parking lot.

<div class="features">

<span class="feature">no setter</span>

</div>

<span class="name"><a href="sdk-for-flutter-explore-search-place-address">address</a></span> <span class="signature">→ <a href="sdk-for-flutter-explore-search-address-class">Address</a></span>  
The address of the place.

<div class="features">

<span class="feature">no setter</span>

</div>

<span class="name"><a href="sdk-for-flutter-explore-search-place-areatype">areaType</a></span> <span class="signature">→ <a href="sdk-for-flutter-explore-search-areatype">AreaType</a>?</span>  
The area type. It is available only when the <a href="sdk-for-flutter-explore-search-place-placetype">Place.placeType</a> is <a href="sdk-for-flutter-explore-search-placetype">PlaceType.area</a>. Gets the area type. It is available only when the <a href="sdk-for-flutter-explore-search-place-placetype">Place.placeType</a> is <a href="sdk-for-flutter-explore-search-placetype">PlaceType.area</a>.

<div class="features">

<span class="feature">no setter</span>

</div>

<span class="name"><a href="sdk-for-flutter-explore-search-place-boundingbox">boundingBox</a></span> <span class="signature">→ <a href="sdk-for-flutter-explore-core-geobox-class">GeoBox</a>?</span>  
The geographic coordinates of the map bounding box containing the place. Gets the geographic coordinates of the bounding box containing the place.

<div class="features">

<span class="feature">no setter</span>

</div>

<span class="name"><a href="sdk-for-flutter-explore-search-place-details">details</a></span> <span class="signature">→ <a href="sdk-for-flutter-explore-search-details-class">Details</a></span>  
The place's detailed information. Gets the place's detailed information.

<div class="features">

<span class="feature">no setter</span>

</div>

<span class="name"><a href="sdk-for-flutter-explore-search-place-distanceinmeters">distanceInMeters</a></span> <span class="signature">→ int?</span>  
The distance from the search center to the place in meters. Gets the distance from the search center to the place in meters.

<div class="features">

<span class="feature">no setter</span>

</div>

<span class="name"><a href="sdk-for-flutter-explore-search-place-geocoordinates">geoCoordinates</a></span> <span class="signature">→ <a href="sdk-for-flutter-explore-core-geocoordinates-class">GeoCoordinates</a>?</span>  
The geographic coordinates of the place. Can be `null` when retrieved from a suggestion's place property. Gets the geographic coordinates of the place.

<div class="features">

<span class="feature">no setter</span>

</div>

<span class="name"><a href="sdk-for-flutter-explore-search-place-hashcode">hashCode</a></span> <span class="signature">→ int</span>  
The hash code for this object.

<div class="features">

<span class="feature">no setter</span><span class="feature">inherited</span>

</div>

<span class="name"><a href="sdk-for-flutter-explore-search-place-id">id</a></span> <span class="signature">→ String</span>  
The unique id of this resource. It can be used to query further information. When returned from `OfflineSearchEngine`, `id` is valid only for `Place` objects whose `place_type` is `POI`. Otherwise, it is empty. Gets the unique id of this resource. It can be used to query further information.

<div class="features">

<span class="feature">no setter</span>

</div>

<span class="name"><a href="sdk-for-flutter-explore-search-place-iscoordinatesinterpolated">isCoordinatesInterpolated</a></span> <span class="signature">→ bool</span>  
A property that says whether the coordinates of the house number were interpolated or not. This property is valid only for house number results retrieved using online search. When false, it means <a href="sdk-for-flutter-explore-search-place-geocoordinates">Place.geoCoordinates</a> point to an accurate position of the house. Otherwise coordinates are slightly less accurate, but are based on a highly optimized interpolation algorithm. Gets the flag saying whether the coordinates of the house number were interpolated or not.

<div class="features">

<span class="feature">no setter</span>

</div>

<span class="name"><a href="sdk-for-flutter-explore-search-place-placetype">placeType</a></span> <span class="signature">→ <a href="sdk-for-flutter-explore-search-placetype">PlaceType</a></span>  
The place type. Gets the place type.

<div class="features">

<span class="feature">no setter</span>

</div>

<span class="name"><a href="sdk-for-flutter-explore-search-place-politicalview">politicalView</a></span> <span class="signature">→ String?</span>  
The geopolitical view, defined as a three letter country code, each disputed territory has international and alternative views. Populated when the geopolitical view parameter is set in the <a href="sdk-for-flutter-explore-core-engine-sdkoptions-class">SDKOptions</a> and passed to <a href="sdk-for-flutter-explore-core-engine-sdknativeengine-class">SDKNativeEngine</a> on instantiation, but only if it is an alternative view. For more details refer to <a href="sdk-for-flutter-explore-core-engine-sdkoptions-class">SDKOptions</a>. Gets the geopolitical view, defined as a three letter country code, each disputed territory has international and alternative views.

<div class="features">

<span class="feature">no setter</span>

</div>

<span class="name"><a href="sdk-for-flutter-explore-search-place-runtimetype">runtimeType</a></span> <span class="signature">→ Type</span>  
A representation of the runtime type of the object.

<div class="features">

<span class="feature">no setter</span><span class="feature">inherited</span>

</div>

<span class="name"><a href="sdk-for-flutter-explore-search-place-title">title</a></span> <span class="signature">→ String</span>  
The localized title for the resource. Gets the localized title for the resource.

<div class="features">

<span class="feature">no setter</span>

</div>

## Methods

<span class="name"><a href="sdk-for-flutter-explore-search-place-nosuchmethod">noSuchMethod</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-explore-noSuchMethod-param-invocation" class="parameter"><span class="type-annotation">Invocation</span> <span class="parameter-name">invocation</span></span>) <span class="returntype parameter">→ dynamic</span> </span>  
Invoked when a nonexistent method or property is accessed.

<div class="features">

<span class="feature">inherited</span>

</div>

<span class="name"><a href="sdk-for-flutter-explore-search-place-serializecompact">serializeCompact</a></span><span class="signature">(<wbr></wbr>) <span class="returntype parameter">→ String</span> </span>  
Serializes <a href="sdk-for-flutter-explore-search-place-class">Place</a> to persist or transfer.

<span class="name"><a href="sdk-for-flutter-explore-search-place-tostring">toString</a></span><span class="signature">(<wbr></wbr>) <span class="returntype parameter">→ String</span> </span>  
A string representation of this object.

<div class="features">

<span class="feature">inherited</span>

</div>

## Operators

<span class="name"><a href="sdk-for-flutter-explore-search-place-operator_equals">operator ==</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-explore-param-other" class="parameter"><span class="type-annotation">Object</span> <span class="parameter-name">other</span></span>) <span class="returntype parameter">→ bool</span> </span>  
The equality operator.

<div class="features">

<span class="feature">inherited</span>

</div>

## Static Methods

<span class="name"><a href="sdk-for-flutter-explore-search-place-deserialize">deserialize</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-explore-deserialize-param-serializedPlace" class="parameter"><span class="type-annotation">String</span> <span class="parameter-name">serializedPlace</span></span>) <span class="returntype parameter">→ <a href="sdk-for-flutter-explore-search-place-class">Place</a></span> </span>  
Returns a <a href="sdk-for-flutter-explore-search-place-class">Place</a> created from serialized string.

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>

</div>
`
}</HTMLBlock>
