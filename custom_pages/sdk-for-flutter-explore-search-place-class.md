---
title: "Constructors"
slug: "sdk-for-flutter-explore-search-place-class"
---

<HTMLBlock>
<div class="sdk-for-flutter">
<!-- Place-class.html -->
<div class="doc-with-sidebar"><div class="sidebar-nav"><ol>
<li class="section-title"><a href="search/Place-class.html#constructors">Constructors</a></li>
<li><a href="search/Place/Place.html">Place</a></li>
<li class="section-title">
<a href="search/Place-class.html#instance-properties">Properties</a>
</li>
<li><a href="search/Place/accessPoints.html">accessPoints</a></li>
<li><a href="search/Place/address.html">address</a></li>
<li><a href="search/Place/areaType.html">areaType</a></li>
<li><a href="search/Place/boundingBox.html">boundingBox</a></li>
<li><a href="search/Place/details.html">details</a></li>
<li><a href="search/Place/distanceInMeters.html">distanceInMeters</a></li>
<li><a href="search/Place/geoCoordinates.html">geoCoordinates</a></li>
<li class="inherited"><a href="search/Place/hashCode.html">hashCode</a></li>
<li><a href="search/Place/id.html">id</a></li>
<li><a href="search/Place/isCoordinatesInterpolated.html">isCoordinatesInterpolated</a></li>
<li><a href="search/Place/placeType.html">placeType</a></li>
<li><a href="search/Place/politicalView.html">politicalView</a></li>
<li class="inherited"><a href="search/Place/runtimeType.html">runtimeType</a></li>
<li><a href="search/Place/title.html">title</a></li>
<li class="section-title"><a href="search/Place-class.html#instance-methods">Methods</a></li>
<li class="inherited"><a href="search/Place/noSuchMethod.html">noSuchMethod</a></li>
<li><a href="search/Place/serializeCompact.html">serializeCompact</a></li>
<li class="inherited"><a href="search/Place/toString.html">toString</a></li>
<li class="section-title inherited"><a href="search/Place-class.html#operators">Operators</a></li>
<li class="inherited"><a href="search/Place/operator_equals.html">operator ==</a></li>
<li class="section-title"><a href="search/Place-class.html#static-methods">Static methods</a></li>
<li><a href="search/Place/deserialize.html">deserialize</a></li>
</ol></div><div class="doc-content">
<div id="overlay-under-drawer"></div>
<header id="title">
menu
<ol class="breadcrumbs gt-separated dark hidden-xs">
<li><a href="../index.html">/sdk-for-flutter-explore</a></li>
<li><a href="../search/search-library.html">/sdk-for-flutter-explore-search-search-library</a></li>
<li class="self-crumb">Place class</li>
</ol>
<div class="self-name">Place</div>
<form class="search navbar-right" role="search">
<input autocomplete="off" class="form-control typeahead" disabled="" id="search-box" placeholder="Loading search..." type="text"/>
</form>
<div class="toggle" id="theme-button" title="Toggle brightness">
<label for="theme">
<input id="theme" type="checkbox" value="light-theme"/>

        dark_mode
      

        light_mode
      
</label>
</div>
</header>
<main>
<div class="main-content" data-above-sidebar="search/search-library-sidebar.html" data-below-sidebar="search/Place-class-sidebar.html" id="dartdoc-main-content">
<div>
<h1>Place class abstract</h1></div>
<section class="desc markdown">
<p>Represents a location object, such as a country, a city, a point of interest (POI) etc.</p>
</section>
<section class="summary offset-anchor" id="constructors">
<h2>Constructors</h2>
<dl class="constructor-summary-list">
<dt class="callable" id="Place">
<a href="../search/Place/Place.html">/sdk-for-flutter-explore-search-place-place</a>()
</dt>
<dd>
</dd>
</dl>
</section>
<section class="summary offset-anchor" id="instance-properties">
<h2>Properties</h2>
<dl class="properties">
<dt class="property" id="accessPoints">
<a href="../search/Place/accessPoints.html">/sdk-for-flutter-explore-search-place-accesspoints</a>
→ List&lt;<wbr/><a href="../core/GeoCoordinates-class.html">/sdk-for-flutter-explore-core-geocoordinates-class</a>&gt;
</dt>
<dd>
  The access points to the place, such as the points on a road or in a parking lot.
A place can have multiple access points. For example, a large warehouse can have
multiple entrances, while the center of the warehouse may not be directly reachable.
Note that access points are meant to be reachable by vehicles.
For routes it is recommended to navigate to one of the available access points (if any),
whereas the <code>sideOfStreetHint</code> should be set to the geographic coordinates of the place.
The list is empty when no access points are known or when the place is directly reachable.
A place can have multiple access points. For example, a large warehouse can have
multiple entrances, while the center of the warehouse may not be directly reachable.
Note that access points are meant to be reachable by vehicles.
For routes it is recommended to navigate to one of the available access points (if any),
whereas the <code>sideOfStreetHint</code> should be set to the geographic coordinates of the place.
The list is empty when no access points are known or when the place is directly reachable.
Gets the access points to the place, such as the points on a road or in a parking lot.
  <div class="features">no setter</div>
</dd>
<dt class="property" id="address">
<a href="../search/Place/address.html">/sdk-for-flutter-explore-search-place-address</a>
→ <a href="../search/Address-class.html">/sdk-for-flutter-explore-search-address-class</a>
</dt>
<dd>
  The address of the place.
  <div class="features">no setter</div>
</dd>
<dt class="property" id="areaType">
<a href="../search/Place/areaType.html">/sdk-for-flutter-explore-search-place-areatype</a>
→ <a href="../search/AreaType.html">/sdk-for-flutter-explore-search-areatype</a>?
</dt>
<dd>
  The area type. It is available only when the <a href="../search/Place/placeType.html">/sdk-for-flutter-explore-search-place-placetype</a> is <a href="../search/PlaceType.html">/sdk-for-flutter-explore-search-placetype</a>.
Gets the area type. It is available only when the <a href="../search/Place/placeType.html">/sdk-for-flutter-explore-search-place-placetype</a> is <a href="../search/PlaceType.html">/sdk-for-flutter-explore-search-placetype</a>.
  <div class="features">no setter</div>
</dd>
<dt class="property" id="boundingBox">
<a href="../search/Place/boundingBox.html">/sdk-for-flutter-explore-search-place-boundingbox</a>
→ <a href="../core/GeoBox-class.html">/sdk-for-flutter-explore-core-geobox-class</a>?
</dt>
<dd>
  The geographic coordinates of the map bounding box containing the place.
Gets the geographic coordinates of the bounding box containing the place.
  <div class="features">no setter</div>
</dd>
<dt class="property" id="details">
<a href="../search/Place/details.html">/sdk-for-flutter-explore-search-place-details</a>
→ <a href="../search/Details-class.html">/sdk-for-flutter-explore-search-details-class</a>
</dt>
<dd>
  The place's detailed information.
Gets the place's detailed information.
  <div class="features">no setter</div>
</dd>
<dt class="property" id="distanceInMeters">
<a href="../search/Place/distanceInMeters.html">/sdk-for-flutter-explore-search-place-distanceinmeters</a>
→ int?
</dt>
<dd>
  The distance from the search center to the place in meters.
Gets the distance from the search center to the place in meters.
  <div class="features">no setter</div>
</dd>
<dt class="property" id="geoCoordinates">
<a href="../search/Place/geoCoordinates.html">/sdk-for-flutter-explore-search-place-geocoordinates</a>
→ <a href="../core/GeoCoordinates-class.html">/sdk-for-flutter-explore-core-geocoordinates-class</a>?
</dt>
<dd>
  The geographic coordinates of the place.
Can be <code>null</code> when retrieved from a suggestion's place property.
Gets the geographic coordinates of the place.
  <div class="features">no setter</div>
</dd>
<dt class="property inherited" id="hashCode">
<a href="../search/Place/hashCode.html">/sdk-for-flutter-explore-search-place-hashcode</a>
→ int
</dt>
<dd class="inherited">
  The hash code for this object.
  <div class="features">no setterinherited</div>
</dd>
<dt class="property" id="id">
<a href="../search/Place/id.html">/sdk-for-flutter-explore-search-place-id</a>
→ String
</dt>
<dd>
  The unique id of this resource. It can be used to query further information.
When returned from <code>OfflineSearchEngine</code>, <code>id</code> is valid only for <code>Place</code> objects whose
<code>place_type</code> is <code>POI</code>. Otherwise, it is empty.
Gets the unique id of this resource. It can be used to query further information.
  <div class="features">no setter</div>
</dd>
<dt class="property" id="isCoordinatesInterpolated">
<a href="../search/Place/isCoordinatesInterpolated.html">/sdk-for-flutter-explore-search-place-iscoordinatesinterpolated</a>
→ bool
</dt>
<dd>
  A property that says whether the coordinates of the house number were interpolated or not.
This property is valid only for house number results retrieved using online search.
When false, it means <a href="../search/Place/geoCoordinates.html">/sdk-for-flutter-explore-search-place-geocoordinates</a> point to an accurate position of the house. Otherwise
coordinates are slightly less accurate, but are based on a highly optimized interpolation algorithm.
Gets the flag saying whether the coordinates of the house number were interpolated or not.
  <div class="features">no setter</div>
</dd>
<dt class="property" id="placeType">
<a href="../search/Place/placeType.html">/sdk-for-flutter-explore-search-place-placetype</a>
→ <a href="../search/PlaceType.html">/sdk-for-flutter-explore-search-placetype</a>
</dt>
<dd>
  The place type.
Gets the place type.
  <div class="features">no setter</div>
</dd>
<dt class="property" id="politicalView">
<a href="../search/Place/politicalView.html">/sdk-for-flutter-explore-search-place-politicalview</a>
→ String?
</dt>
<dd>
  The geopolitical view, defined as a three letter country code, each disputed territory has international and alternative views.
Populated when the geopolitical view parameter is set in the <a href="../core.engine/SDKOptions-class.html">/sdk-for-flutter-explore-core-engine-sdkoptions-class</a>
and passed to <a href="../core.engine/SDKNativeEngine-class.html">/sdk-for-flutter-explore-core-engine-sdknativeengine-class</a> on instantiation,
but only if it is an alternative view.
For more details refer to <a href="../core.engine/SDKOptions-class.html">/sdk-for-flutter-explore-core-engine-sdkoptions-class</a>.
Gets the geopolitical view, defined as a three letter country code, each disputed territory has international and alternative views.
  <div class="features">no setter</div>
</dd>
<dt class="property inherited" id="runtimeType">
<a href="../search/Place/runtimeType.html">/sdk-for-flutter-explore-search-place-runtimetype</a>
→ Type
</dt>
<dd class="inherited">
  A representation of the runtime type of the object.
  <div class="features">no setterinherited</div>
</dd>
<dt class="property" id="title">
<a href="../search/Place/title.html">/sdk-for-flutter-explore-search-place-title</a>
→ String
</dt>
<dd>
  The localized title for the resource.
Gets the localized title for the resource.
  <div class="features">no setter</div>
</dd>
</dl>
</section>
<section class="summary offset-anchor" id="instance-methods">
<h2>Methods</h2>
<dl class="callables">
<dt class="callable inherited" id="noSuchMethod">
<a href="../search/Place/noSuchMethod.html">/sdk-for-flutter-explore-search-place-nosuchmethod</a>(<wbr/>Invocation invocation)
    → dynamic

</dt>
<dd class="inherited">
  Invoked when a nonexistent method or property is accessed.
  <div class="features">inherited</div>
</dd>
<dt class="callable" id="serializeCompact">
<a href="../search/Place/serializeCompact.html">/sdk-for-flutter-explore-search-place-serializecompact</a>(<wbr/>)
    → String

</dt>
<dd>
  Serializes <a href="../search/Place-class.html">/sdk-for-flutter-explore-search-place-class</a> to persist or transfer.
  

</dd>
<dt class="callable inherited" id="toString">
<a href="../search/Place/toString.html">/sdk-for-flutter-explore-search-place-tostring</a>(<wbr/>)
    → String

</dt>
<dd class="inherited">
  A string representation of this object.
  <div class="features">inherited</div>
</dd>
</dl>
</section>
<section class="summary offset-anchor inherited" id="operators">
<h2>Operators</h2>
<dl class="callables">
<dt class="callable inherited" id="operator ==">
<a href="../search/Place/operator_equals.html">/sdk-for-flutter-explore-search-place-operator-equals</a>(<wbr/>Object other)
    → bool

</dt>
<dd class="inherited">
  The equality operator.
  <div class="features">inherited</div>
</dd>
</dl>
</section>
<section class="summary offset-anchor" id="static-methods">
<h2>Static Methods</h2>
<dl class="callables">
<dt class="callable" id="deserialize">
<a href="../search/Place/deserialize.html">/sdk-for-flutter-explore-search-place-deserialize</a>(<wbr/>String serializedPlace)
    → <a href="../search/Place-class.html">/sdk-for-flutter-explore-search-place-class</a>
</dt>
<dd>
  Returns a <a href="../search/Place-class.html">/sdk-for-flutter-explore-search-place-class</a> created from serialized string.
  

</dd>
</dl>
</section>
</div>
<div class="sidebar sidebar-offcanvas-left" id="dartdoc-sidebar-left">
<header class="hidden-l" id="header-search-sidebar">
<form class="search-sidebar" role="search">
<input autocomplete="off" class="form-control typeahead" disabled="" id="search-sidebar" placeholder="Loading search..." type="text"/>
</form>
</header>
<ol class="breadcrumbs gt-separated dark hidden-l" id="sidebar-nav">
<li><a href="../index.html">/sdk-for-flutter-explore</a></li>
<li><a href="../search/search-library.html">/sdk-for-flutter-explore-search-search-library</a></li>
<li class="self-crumb">Place class</li>
</ol>
<h5>search library</h5>
<div id="dartdoc-sidebar-left-content"></div>
</div>
<div class="sidebar sidebar-offcanvas-right" id="dartdoc-sidebar-right">
</div>
</main>
<footer>

    here_sdk
      4.26.0
  
</footer>
</div></div>
</div>
</HTMLBlock>
