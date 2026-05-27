---
title: "Constructors"
slug: "sdk-for-flutter-explore-search-placefilter-class"
---

<HTMLBlock>
<div class="sdk-for-flutter">
<!-- PlaceFilter-class.html -->
<div class="doc-with-sidebar"><div class="sidebar-nav"><ol>
<li class="section-title"><a href="search/PlaceFilter-class.html#constructors">Constructors</a></li>
<li><a href="search/PlaceFilter/PlaceFilter.html">PlaceFilter</a></li>
<li class="section-title">
<a href="search/PlaceFilter-class.html#instance-properties">Properties</a>
</li>
<li><a href="search/PlaceFilter/ev.html">ev</a></li>
<li><a href="search/PlaceFilter/fuelTypes.html">fuelTypes</a></li>
<li><a href="search/PlaceFilter/hashCode.html">hashCode</a></li>
<li class="inherited"><a href="search/PlaceFilter/runtimeType.html">runtimeType</a></li>
<li><a href="search/PlaceFilter/truckClass.html">truckClass</a></li>
<li><a href="search/PlaceFilter/truckFuelTypes.html">truckFuelTypes</a></li>
<li class="section-title inherited"><a href="search/PlaceFilter-class.html#instance-methods">Methods</a></li>
<li class="inherited"><a href="search/PlaceFilter/noSuchMethod.html">noSuchMethod</a></li>
<li class="inherited"><a href="search/PlaceFilter/toString.html">toString</a></li>
<li class="section-title"><a href="search/PlaceFilter-class.html#operators">Operators</a></li>
<li><a href="search/PlaceFilter/operator_equals.html">operator ==</a></li>
</ol></div><div class="doc-content">
<div id="overlay-under-drawer"></div>
<header id="title">
menu
<ol class="breadcrumbs gt-separated dark hidden-xs">
<li><a href="../index.html">/sdk-for-flutter-explore</a></li>
<li><a href="../search/search-library.html">/sdk-for-flutter-explore-search-search-library</a></li>
<li class="self-crumb">PlaceFilter class</li>
</ol>
<div class="self-name">PlaceFilter</div>
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
<div class="main-content" data-above-sidebar="search/search-library-sidebar.html" data-below-sidebar="search/PlaceFilter-class-sidebar.html" id="dartdoc-main-content">
<div>
<h1>PlaceFilter class</h1></div>
<section class="desc markdown">
<p>The filter options to specify a place.</p>
<p>Consists of fuel, truck and EV options.</p>
</section>
<section class="summary offset-anchor" id="constructors">
<h2>Constructors</h2>
<dl class="constructor-summary-list">
<dt class="callable" id="PlaceFilter">
<a href="../search/PlaceFilter/PlaceFilter.html">/sdk-for-flutter-explore-search-placefilter-placefilter</a>()
</dt>
<dd>
</dd>
</dl>
</section>
<section class="summary offset-anchor" id="instance-properties">
<h2>Properties</h2>
<dl class="properties">
<dt class="property" id="ev">
<a href="../search/PlaceFilter/ev.html">/sdk-for-flutter-explore-search-placefilter-ev</a>
↔ <a href="../search/PlaceFilterEv-class.html">/sdk-for-flutter-explore-search-placefilterev-class</a>
</dt>
<dd>
  Constraints that are applicable on the places of category EV station.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property" id="fuelTypes">
<a href="../search/PlaceFilter/fuelTypes.html">/sdk-for-flutter-explore-search-placefilter-fueltypes</a>
↔ List&lt;<wbr/><a href="../transport/FuelType.html">/sdk-for-flutter-explore-transport-fueltype</a>&gt;
</dt>
<dd>
  The list of <a href="../transport/FuelType.html">/sdk-for-flutter-explore-transport-fueltype</a> elements that should be used to find only
the <a href="../search/FuelStation-class.html">/sdk-for-flutter-explore-search-fuelstation-class</a> search results that support all of them.
This filter is available to use with the <code>SearchEngine</code> and
<code>OfflineSearchEngine</code> (only available for the Navigate license), however <code>OfflineSearchEngine</code>
supports it only for <code>searchByText</code> and <code>searchByCategory</code> with allowed fuel types <code>DIESEL</code>, <code>LPG</code>,
<code>BIO_DIESEL</code>, <code>CNG</code>, <code>DIESEL_WITH_ADDITIVES</code>, <code>E10</code>, <code>E85</code>, <code>ETHANOL</code>, <code>ETHANOL_WITH_ADDITIVES</code>,
<code>GASOLINE</code>, <code>HYDROGEN</code>, <code>LNG</code>, <code>MIDGRADE</code>, <code>PREMIUM</code> and <code>REGULAR</code>.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property" id="hashCode">
<a href="../search/PlaceFilter/hashCode.html">/sdk-for-flutter-explore-search-placefilter-hashcode</a>
→ int
</dt>
<dd>
  The hash code for this object.
  <div class="features">no setter</div>
</dd>
<dt class="property inherited" id="runtimeType">
<a href="../search/PlaceFilter/runtimeType.html">/sdk-for-flutter-explore-search-placefilter-runtimetype</a>
→ Type
</dt>
<dd class="inherited">
  A representation of the runtime type of the object.
  <div class="features">no setterinherited</div>
</dd>
<dt class="property" id="truckClass">
<a href="../search/PlaceFilter/truckClass.html">/sdk-for-flutter-explore-search-placefilter-truckclass</a>
↔ <a href="../transport/TruckClass.html">/sdk-for-flutter-explore-transport-truckclass</a>?
</dt>
<dd>
  Should be used to find only the <a href="../search/FuelStation-class.html">/sdk-for-flutter-explore-search-fuelstation-class</a> search results with minimum supported <a href="../transport/TruckClass.html">/sdk-for-flutter-explore-transport-truckclass</a>.
This filter is only available to use with the <code>SearchEngine</code>.
The <code>OfflineSearchEngine</code> (only available for the Navigate license) does not apply this filter.
<a href="../transport/TruckClass.html">/sdk-for-flutter-explore-transport-truckclass</a> is not accepted in the filter.
Otherwise will result in <a href="../search/SearchError.html">/sdk-for-flutter-explore-search-searcherror</a>.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property" id="truckFuelTypes">
<a href="../search/PlaceFilter/truckFuelTypes.html">/sdk-for-flutter-explore-search-placefilter-truckfueltypes</a>
↔ List&lt;<wbr/><a href="../transport/TruckFuelType.html">/sdk-for-flutter-explore-transport-truckfueltype</a>&gt;
</dt>
<dd>
  The list of <a href="../transport/TruckFuelType.html">/sdk-for-flutter-explore-transport-truckfueltype</a> elements that should be used to find only
the <a href="../search/FuelStation-class.html">/sdk-for-flutter-explore-search-fuelstation-class</a> search results that support all of them.
Not supported for <code>suggestByText</code> in <code>OfflineSearchEngine</code> (only available for the Navigate license).
  <div class="features">getter/setter pair</div>
</dd>
</dl>
</section>
<section class="summary offset-anchor inherited" id="instance-methods">
<h2>Methods</h2>
<dl class="callables">
<dt class="callable inherited" id="noSuchMethod">
<a href="../search/PlaceFilter/noSuchMethod.html">/sdk-for-flutter-explore-search-placefilter-nosuchmethod</a>(<wbr/>Invocation invocation)
    → dynamic

</dt>
<dd class="inherited">
  Invoked when a nonexistent method or property is accessed.
  <div class="features">inherited</div>
</dd>
<dt class="callable inherited" id="toString">
<a href="../search/PlaceFilter/toString.html">/sdk-for-flutter-explore-search-placefilter-tostring</a>(<wbr/>)
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
<a href="../search/PlaceFilter/operator_equals.html">/sdk-for-flutter-explore-search-placefilter-operator-equals</a>(<wbr/>Object other)
    → bool

</dt>
<dd>
  The equality operator.
  

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
<li class="self-crumb">PlaceFilter class</li>
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
