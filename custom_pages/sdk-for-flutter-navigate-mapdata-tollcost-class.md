---
title: "TollCost class"
slug: "sdk-for-flutter-navigate-mapdata-tollcost-class"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- TollCost-class.html -->
<div class="doc-with-sidebar"><div class="sidebar-nav"><ol>
<li class="section-title"><a href="mapdata/TollCost-class.html#constructors">Constructors</a></li>
<li><a href="mapdata/TollCost/TollCost.html">TollCost</a></li>
<li class="section-title">
<a href="mapdata/TollCost-class.html#instance-properties">Properties</a>
</li>
<li><a href="mapdata/TollCost/currency.html">currency</a></li>
<li><a href="mapdata/TollCost/hashCode.html">hashCode</a></li>
<li><a href="mapdata/TollCost/isPriceCalculatedPerKilometer.html">isPriceCalculatedPerKilometer</a></li>
<li><a href="mapdata/TollCost/paymentMethods.html">paymentMethods</a></li>
<li><a href="mapdata/TollCost/price.html">price</a></li>
<li class="inherited"><a href="mapdata/TollCost/runtimeType.html">runtimeType</a></li>
<li><a href="mapdata/TollCost/transportSpecifications.html">transportSpecifications</a></li>
<li><a class="deprecated" href="mapdata/TollCost/vehicleProfiles.html">vehicleProfiles</a></li>
<li class="section-title inherited"><a href="mapdata/TollCost-class.html#instance-methods">Methods</a></li>
<li class="inherited"><a href="mapdata/TollCost/noSuchMethod.html">noSuchMethod</a></li>
<li class="inherited"><a href="mapdata/TollCost/toString.html">toString</a></li>
<li class="section-title"><a href="mapdata/TollCost-class.html#operators">Operators</a></li>
<li><a href="mapdata/TollCost/operator_equals.html">operator ==</a></li>
</ol></div><div class="doc-content">
<div id="overlay-under-drawer"></div>
<header id="title">
menu
<ol class="breadcrumbs gt-separated dark hidden-xs">
<li>/sdk-for-flutter-navigate</li>
<li>/sdk-for-flutter-navigate-mapdata-mapdata-library</li>
<li class="self-crumb">TollCost class</li>
</ol>
<div class="self-name">TollCost</div>
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
<div class="main-content" data-above-sidebar="mapdata/mapdata-library-sidebar.html" data-below-sidebar="mapdata/TollCost-class-sidebar.html" id="dartdoc-main-content">
<div>
<h1>TollCost class</h1></div>
<section class="desc markdown">
<p>Contains informations about the toll costs for a specific vehicle profile.</p>
</section>
<section class="summary offset-anchor" id="constructors">
<h2>Constructors</h2>
<dl class="constructor-summary-list">
<dt class="callable" id="TollCost">
/sdk-for-flutter-navigate-mapdata-tollcost-tollcost(String currency)
</dt>
<dd>
</dd>
</dl>
</section>
<section class="summary offset-anchor" id="instance-properties">
<h2>Properties</h2>
<dl class="properties">
<dt class="property" id="currency">
/sdk-for-flutter-navigate-mapdata-tollcost-currency
↔ String
</dt>
<dd>
  The currency in which the toll is to be paid in ISO 4217 format, e.g. "USD".
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property" id="hashCode">
/sdk-for-flutter-navigate-mapdata-tollcost-hashcode
→ int
</dt>
<dd>
  The hash code for this object.
  <div class="features">no setter</div>
</dd>
<dt class="property" id="isPriceCalculatedPerKilometer">
/sdk-for-flutter-navigate-mapdata-tollcost-ispricecalculatedperkilometer
↔ bool
</dt>
<dd>
  Indicates if the toll cost is based on the distance traveled. Defaults
to <code>false</code>.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property" id="paymentMethods">
/sdk-for-flutter-navigate-mapdata-tollcost-paymentmethods
↔ List&lt;<wbr/>/sdk-for-flutter-navigate-routing-paymentmethod&gt;
</dt>
<dd>
  The list of accepted payment methods like cash and credit card.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property" id="price">
/sdk-for-flutter-navigate-mapdata-tollcost-price
↔ double
</dt>
<dd>
  The amount of currency to be paid for the toll.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property inherited" id="runtimeType">
/sdk-for-flutter-navigate-mapdata-tollcost-runtimetype
→ Type
</dt>
<dd class="inherited">
  A representation of the runtime type of the object.
  <div class="features">no setterinherited</div>
</dd>
<dt class="property" id="transportSpecifications">
/sdk-for-flutter-navigate-mapdata-tollcost-transportspecifications
↔ List&lt;<wbr/>/sdk-for-flutter-navigate-transport-transportspecification-class&gt;
</dt>
<dd>
  List of transport specifications containing the vehicle characteristics for which the toll
cost applies.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property" id="vehicleProfiles">
/sdk-for-flutter-navigate-mapdata-tollcost-vehicleprofiles
↔ List&lt;<wbr/>/sdk-for-flutter-navigate-transport-vehicleprofile-class&gt;
</dt>
<dd>
  List of vehicle profile containing vehicle characteristics for which the toll cost applies.
  <div class="features">getter/setter pair</div>
</dd>
</dl>
</section>
<section class="summary offset-anchor inherited" id="instance-methods">
<h2>Methods</h2>
<dl class="callables">
<dt class="callable inherited" id="noSuchMethod">
/sdk-for-flutter-navigate-mapdata-tollcost-nosuchmethod(<wbr/>Invocation invocation)
    → dynamic

</dt>
<dd class="inherited">
  Invoked when a nonexistent method or property is accessed.
  <div class="features">inherited</div>
</dd>
<dt class="callable inherited" id="toString">
/sdk-for-flutter-navigate-mapdata-tollcost-tostring(<wbr/>)
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
/sdk-for-flutter-navigate-mapdata-tollcost-operator-equals(<wbr/>Object other)
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
<li>/sdk-for-flutter-navigate-mapdata-mapdata-library</li>
<li class="self-crumb">TollCost class</li>
</ol>
<h5>mapdata library</h5>
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
`
}</HTMLBlock>
