---
title: "Untitled"
slug: "sdk-for-flutter-navigate-search-placefilter-class"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- PlaceFilter-class.html -->

<div id="overlay-under-drawer"></div>
<header id="title">
menu
<ol class="breadcrumbs gt-separated dark hidden-xs">
<li>/sdk-for-flutter-navigate</li>
<li>/sdk-for-flutter-navigate-search-search-library</li>
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
/sdk-for-flutter-navigate-search-placefilter-placefilter()
</dt>
<dd>
</dd>
</dl>
</section>
<section class="summary offset-anchor" id="instance-properties">
<h2>Properties</h2>
<dl class="properties">
<dt class="property" id="ev">
/sdk-for-flutter-navigate-search-placefilter-ev
↔ /sdk-for-flutter-navigate-search-placefilterev-class
</dt>
<dd>
  Constraints that are applicable on the places of category EV station.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property" id="fuelTypes">
/sdk-for-flutter-navigate-search-placefilter-fueltypes
↔ List&lt;<wbr/>/sdk-for-flutter-navigate-transport-fueltype&gt;
</dt>
<dd>
  The list of /sdk-for-flutter-navigate-transport-fueltype elements that should be used to find only
the /sdk-for-flutter-navigate-search-fuelstation-class search results that support all of them.
This filter is available to use with the <code>SearchEngine</code> and
<code>OfflineSearchEngine</code> (only available for the Navigate license), however <code>OfflineSearchEngine</code>
supports it only for <code>searchByText</code> and <code>searchByCategory</code> with allowed fuel types <code>DIESEL</code>, <code>LPG</code>,
<code>BIO_DIESEL</code>, <code>CNG</code>, <code>DIESEL_WITH_ADDITIVES</code>, <code>E10</code>, <code>E85</code>, <code>ETHANOL</code>, <code>ETHANOL_WITH_ADDITIVES</code>,
<code>GASOLINE</code>, <code>HYDROGEN</code>, <code>LNG</code>, <code>MIDGRADE</code>, <code>PREMIUM</code> and <code>REGULAR</code>.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property" id="hashCode">
/sdk-for-flutter-navigate-search-placefilter-hashcode
→ int
</dt>
<dd>
  The hash code for this object.
  <div class="features">no setter</div>
</dd>
<dt class="property inherited" id="runtimeType">
/sdk-for-flutter-navigate-search-placefilter-runtimetype
→ Type
</dt>
<dd class="inherited">
  A representation of the runtime type of the object.
  <div class="features">no setterinherited</div>
</dd>
<dt class="property" id="truckClass">
/sdk-for-flutter-navigate-search-placefilter-truckclass
↔ /sdk-for-flutter-navigate-transport-truckclass?
</dt>
<dd>
  Should be used to find only the /sdk-for-flutter-navigate-search-fuelstation-class search results with minimum supported /sdk-for-flutter-navigate-transport-truckclass.
This filter is only available to use with the <code>SearchEngine</code>.
The <code>OfflineSearchEngine</code> (only available for the Navigate license) does not apply this filter.
/sdk-for-flutter-navigate-transport-truckclass is not accepted in the filter.
Otherwise will result in /sdk-for-flutter-navigate-search-searcherror.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property" id="truckFuelTypes">
/sdk-for-flutter-navigate-search-placefilter-truckfueltypes
↔ List&lt;<wbr/>/sdk-for-flutter-navigate-transport-truckfueltype&gt;
</dt>
<dd>
  The list of /sdk-for-flutter-navigate-transport-truckfueltype elements that should be used to find only
the /sdk-for-flutter-navigate-search-fuelstation-class search results that support all of them.
Not supported for <code>suggestByText</code> in <code>OfflineSearchEngine</code> (only available for the Navigate license).
  <div class="features">getter/setter pair</div>
</dd>
</dl>
</section>
<section class="summary offset-anchor inherited" id="instance-methods">
<h2>Methods</h2>
<dl class="callables">
<dt class="callable inherited" id="noSuchMethod">
/sdk-for-flutter-navigate-search-placefilter-nosuchmethod(<wbr/>Invocation invocation)
    → dynamic

</dt>
<dd class="inherited">
  Invoked when a nonexistent method or property is accessed.
  <div class="features">inherited</div>
</dd>
<dt class="callable inherited" id="toString">
/sdk-for-flutter-navigate-search-placefilter-tostring(<wbr/>)
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
/sdk-for-flutter-navigate-search-placefilter-operator-equals(<wbr/>Object other)
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
<li>/sdk-for-flutter-navigate</li>
<li>/sdk-for-flutter-navigate-search-search-library</li>
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



</div>
`
}</HTMLBlock>
