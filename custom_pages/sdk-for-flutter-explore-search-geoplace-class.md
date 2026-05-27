---
title: "Constructors"
slug: "sdk-for-flutter-explore-search-geoplace-class"
---

<HTMLBlock>
<div class="sdk-for-flutter">
<!-- GeoPlace-class.html -->
<div class="doc-with-sidebar"><div class="sidebar-nav"><ol>
<li class="section-title"><a href="search/GeoPlace-class.html#constructors">Constructors</a></li>
<li><a href="search/GeoPlace/GeoPlace.html">GeoPlace</a></li>
<li class="section-title">
<a href="search/GeoPlace-class.html#instance-properties">Properties</a>
</li>
<li><a href="search/GeoPlace/address.html">address</a></li>
<li><a href="search/GeoPlace/business.html">business</a></li>
<li><a href="search/GeoPlace/categories.html">categories</a></li>
<li><a href="search/GeoPlace/externalIDs.html">externalIDs</a></li>
<li><a href="search/GeoPlace/hashCode.html">hashCode</a></li>
<li><a href="search/GeoPlace/location.html">location</a></li>
<li class="inherited"><a href="search/GeoPlace/runtimeType.html">runtimeType</a></li>
<li><a href="search/GeoPlace/title.html">title</a></li>
<li><a href="search/GeoPlace/type.html">type</a></li>
<li><a href="search/GeoPlace/web.html">web</a></li>
<li class="section-title"><a href="search/GeoPlace-class.html#instance-methods">Methods</a></li>
<li><a href="search/GeoPlace/getID.html">getID</a></li>
<li><a href="search/GeoPlace/isMyPlace.html">isMyPlace</a></li>
<li class="inherited"><a href="search/GeoPlace/noSuchMethod.html">noSuchMethod</a></li>
<li class="inherited"><a href="search/GeoPlace/toString.html">toString</a></li>
<li class="section-title"><a href="search/GeoPlace-class.html#operators">Operators</a></li>
<li><a href="search/GeoPlace/operator_equals.html">operator ==</a></li>
<li class="section-title"><a href="search/GeoPlace-class.html#static-methods">Static methods</a></li>
<li><a href="search/GeoPlace/makeMyPlace.html">makeMyPlace</a></li>
</ol></div><div class="doc-content">
<div id="overlay-under-drawer"></div>
<header id="title">
menu
<ol class="breadcrumbs gt-separated dark hidden-xs">
<li><a href="../index.html">/sdk-for-flutter-explore</a></li>
<li><a href="../search/search-library.html">/sdk-for-flutter-explore-search-search-library</a></li>
<li class="self-crumb">GeoPlace class</li>
</ol>
<div class="self-name">GeoPlace</div>
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
<div class="main-content" data-above-sidebar="search/search-library-sidebar.html" data-below-sidebar="search/GeoPlace-class-sidebar.html" id="dartdoc-main-content">
<div>
<h1>GeoPlace class</h1></div>
<section class="desc markdown">
<p>GeoPlace struct represents a location object:
such as a country, a city, a point of interest (POI) etc.</p>
<p>It can be used for PersonalPlace creation, in order to provide search on custom places.</p>
</section>
<section class="summary offset-anchor" id="constructors">
<h2>Constructors</h2>
<dl class="constructor-summary-list">
<dt class="callable" id="GeoPlace">
<a href="../search/GeoPlace/GeoPlace.html">/sdk-for-flutter-explore-search-geoplace-geoplace</a>()
</dt>
<dd>
</dd>
</dl>
</section>
<section class="summary offset-anchor" id="instance-properties">
<h2>Properties</h2>
<dl class="properties">
<dt class="property" id="address">
<a href="../search/GeoPlace/address.html">/sdk-for-flutter-explore-search-geoplace-address</a>
↔ <a href="../search/Address-class.html">/sdk-for-flutter-explore-search-address-class</a>
</dt>
<dd>
  Address of the place
Note: Address can have default value when no data is available.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property" id="business">
<a href="../search/GeoPlace/business.html">/sdk-for-flutter-explore-search-geoplace-business</a>
↔ <a href="../search/BusinessDetails-class.html">/sdk-for-flutter-explore-search-businessdetails-class</a>
</dt>
<dd>
  Business details
Note: BusinessDetails can have default value when no data is available.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property" id="categories">
<a href="../search/GeoPlace/categories.html">/sdk-for-flutter-explore-search-geoplace-categories</a>
↔ List&lt;<wbr/><a href="../search/PlaceCategory-class.html">/sdk-for-flutter-explore-search-placecategory-class</a>&gt;
</dt>
<dd>
  List of corresponding categories
Note: This list can be empty when no data is available.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property" id="externalIDs">
<a href="../search/GeoPlace/externalIDs.html">/sdk-for-flutter-explore-search-geoplace-externalids</a>
↔ List&lt;<wbr/><a href="../core/ExternalID-class.html">/sdk-for-flutter-explore-core-externalid-class</a>&gt;
</dt>
<dd>
  Allows the client to set the id in their own system.
The list of supplier references to this place.
The references are provided by external suppliers and are only available to users with
valid contracts with said suppliers. If the user has no such contracts, the list is empty.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property" id="hashCode">
<a href="../search/GeoPlace/hashCode.html">/sdk-for-flutter-explore-search-geoplace-hashcode</a>
→ int
</dt>
<dd>
  The hash code for this object.
  <div class="features">no setter</div>
</dd>
<dt class="property" id="location">
<a href="../search/GeoPlace/location.html">/sdk-for-flutter-explore-search-geoplace-location</a>
↔ <a href="../search/LocationDetails-class.html">/sdk-for-flutter-explore-search-locationdetails-class</a>?
</dt>
<dd>
  Geographical details
Note: Can be <code>null</code> when retrieved from a suggestion's place property.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property inherited" id="runtimeType">
<a href="../search/GeoPlace/runtimeType.html">/sdk-for-flutter-explore-search-geoplace-runtimetype</a>
→ Type
</dt>
<dd class="inherited">
  A representation of the runtime type of the object.
  <div class="features">no setterinherited</div>
</dd>
<dt class="property" id="title">
<a href="../search/GeoPlace/title.html">/sdk-for-flutter-explore-search-geoplace-title</a>
↔ String
</dt>
<dd>
  The localized title for the resource.
Note: This String can be empty when no data is available.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property" id="type">
<a href="../search/GeoPlace/type.html">/sdk-for-flutter-explore-search-geoplace-type</a>
↔ <a href="../search/PlaceType.html">/sdk-for-flutter-explore-search-placetype</a>
</dt>
<dd>
  Specifies place type.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property" id="web">
<a href="../search/GeoPlace/web.html">/sdk-for-flutter-explore-search-geoplace-web</a>
↔ <a href="../search/WebDetails-class.html">/sdk-for-flutter-explore-search-webdetails-class</a>
</dt>
<dd>
  Contains info and direct web links to corresponding items.
Note: WebDetails can have default value when no data is available.
  <div class="features">getter/setter pair</div>
</dd>
</dl>
</section>
<section class="summary offset-anchor" id="instance-methods">
<h2>Methods</h2>
<dl class="callables">
<dt class="callable" id="getID">
<a href="../search/GeoPlace/getID.html">/sdk-for-flutter-explore-search-geoplace-getid</a>(<wbr/>)
    → String

</dt>
<dd>
  Allow the client to access GeoPlace id.
  

</dd>
<dt class="callable" id="isMyPlace">
<a href="../search/GeoPlace/isMyPlace.html">/sdk-for-flutter-explore-search-geoplace-ismyplace</a>(<wbr/>)
    → bool

</dt>
<dd>
  Allow the client to access info about is it my place or not.
  

</dd>
<dt class="callable inherited" id="noSuchMethod">
<a href="../search/GeoPlace/noSuchMethod.html">/sdk-for-flutter-explore-search-geoplace-nosuchmethod</a>(<wbr/>Invocation invocation)
    → dynamic

</dt>
<dd class="inherited">
  Invoked when a nonexistent method or property is accessed.
  <div class="features">inherited</div>
</dd>
<dt class="callable inherited" id="toString">
<a href="../search/GeoPlace/toString.html">/sdk-for-flutter-explore-search-geoplace-tostring</a>(<wbr/>)
    → String

</dt>
<dd class="inherited">
  A string representation of this object.
  <div class="features">inherited</div>
</dd>
</dl>
</section>
<section class="summary offset-anchor" id="operators">
<h2>Operators</h2>
<dl class="callables">
<dt class="callable" id="operator ==">
<a href="../search/GeoPlace/operator_equals.html">/sdk-for-flutter-explore-search-geoplace-operator-equals</a>(<wbr/>Object other)
    → bool

</dt>
<dd>
  The equality operator.
  

</dd>
</dl>
</section>
<section class="summary offset-anchor" id="static-methods">
<h2>Static Methods</h2>
<dl class="callables">
<dt class="callable" id="makeMyPlace">
<a href="../search/GeoPlace/makeMyPlace.html">/sdk-for-flutter-explore-search-geoplace-makemyplace</a>(<wbr/>String title, <a href="../core/GeoCoordinates-class.html">/sdk-for-flutter-explore-core-geocoordinates-class</a> coordinates)
    → <a href="../search/GeoPlace-class.html">/sdk-for-flutter-explore-search-geoplace-class</a>
</dt>
<dd>
  Creates a new instance of this class.
  

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
<li class="self-crumb">GeoPlace class</li>
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
