---
title: "Constructors"
slug: "sdk-for-flutter-explore-search-address-class"
---

<HTMLBlock>
<div class="sdk-for-flutter">
<!-- Address-class.html -->
<div class="doc-with-sidebar"><div class="sidebar-nav"><ol>
<li class="section-title"><a href="search/Address-class.html#constructors">Constructors</a></li>
<li><a href="search/Address/Address.html">Address</a></li>
<li class="section-title">
<a href="search/Address-class.html#instance-properties">Properties</a>
</li>
<li><a href="search/Address/addressText.html">addressText</a></li>
<li><a href="search/Address/block.html">block</a></li>
<li><a href="search/Address/city.html">city</a></li>
<li><a href="search/Address/country.html">country</a></li>
<li><a href="search/Address/countryCode.html">countryCode</a></li>
<li><a href="search/Address/county.html">county</a></li>
<li><a href="search/Address/district.html">district</a></li>
<li><a href="search/Address/hashCode.html">hashCode</a></li>
<li><a href="search/Address/houseNumOrName.html">houseNumOrName</a></li>
<li><a href="search/Address/postalCode.html">postalCode</a></li>
<li class="inherited"><a href="search/Address/runtimeType.html">runtimeType</a></li>
<li><a href="search/Address/state.html">state</a></li>
<li><a href="search/Address/stateCode.html">stateCode</a></li>
<li><a href="search/Address/street.html">street</a></li>
<li><a href="search/Address/subBlock.html">subBlock</a></li>
<li><a href="search/Address/subdistrict.html">subdistrict</a></li>
<li><a href="search/Address/type.html">type</a></li>
<li class="section-title inherited"><a href="search/Address-class.html#instance-methods">Methods</a></li>
<li class="inherited"><a href="search/Address/noSuchMethod.html">noSuchMethod</a></li>
<li class="inherited"><a href="search/Address/toString.html">toString</a></li>
<li class="section-title"><a href="search/Address-class.html#operators">Operators</a></li>
<li><a href="search/Address/operator_equals.html">operator ==</a></li>
</ol></div><div class="doc-content">
<div id="overlay-under-drawer"></div>
<header id="title">
menu
<ol class="breadcrumbs gt-separated dark hidden-xs">
<li><a href="../index.html">/sdk-for-flutter-explore</a></li>
<li><a href="../search/search-library.html">/sdk-for-flutter-explore-search-search-library</a></li>
<li class="self-crumb">Address class</li>
</ol>
<div class="self-name">Address</div>
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
<div class="main-content" data-above-sidebar="search/search-library-sidebar.html" data-below-sidebar="search/Address-class-sidebar.html" id="dartdoc-main-content">
<div>
<h1>Address class</h1></div>
<section class="desc markdown">
<p>Information about the address of a location.</p>
<p>Used in <a href="../search/Place/address.html">/sdk-for-flutter-explore-search-place-address</a>.</p>
<p>Note that while <code>OfflineSearchEngine.suggest</code> and <code>OfflineSearchEngine.suggestByText</code> set all available details,
<code>SearchEngine.suggest</code> and <code>SearchEngine.suggestByText</code> set only <a href="../search/Address/addressText.html">/sdk-for-flutter-explore-search-address-addresstext</a>.
Complete address details can be obtained by searching with <a href="../search/PlaceIdQuery-class.html">/sdk-for-flutter-explore-search-placeidquery-class</a>.</p>
</section>
<section class="summary offset-anchor" id="constructors">
<h2>Constructors</h2>
<dl class="constructor-summary-list">
<dt class="callable" id="Address">
<a href="../search/Address/Address.html">/sdk-for-flutter-explore-search-address-address</a>()
</dt>
<dd>
          Default constructor.
Note: Sets all the string values to "".
        </dd>
</dl>
</section>
<section class="summary offset-anchor" id="instance-properties">
<h2>Properties</h2>
<dl class="properties">
<dt class="property" id="addressText">
<a href="../search/Address/addressText.html">/sdk-for-flutter-explore-search-address-addresstext</a>
↔ String
</dt>
<dd>
  The text for the address, for example, "Secret Garden, 347 Lewis Ave, Brooklyn, NY 11233, United States".
Note: This String can be empty when no data is available.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property" id="block">
<a href="../search/Address/block.html">/sdk-for-flutter-explore-search-address-block</a>
↔ String
</dt>
<dd>
  The block number for the address. It is part of Japanese addressing system.
Note: This String can be empty when no data is available.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property" id="city">
<a href="../search/Address/city.html">/sdk-for-flutter-explore-search-address-city</a>
↔ String
</dt>
<dd>
  The city name for the address, for example, "Brooklyn".
Note: This String can be empty when no data is available.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property" id="country">
<a href="../search/Address/country.html">/sdk-for-flutter-explore-search-address-country</a>
↔ String
</dt>
<dd>
  The country name for the address, for example, "United States".
Note: This String can be empty when no data is available.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property" id="countryCode">
<a href="../search/Address/countryCode.html">/sdk-for-flutter-explore-search-address-countrycode</a>
↔ String
</dt>
<dd>
  An ISO-3166-1 (3-letter) country code for the address, for example, "USA".
Note: This String can be empty when no data is available.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property" id="county">
<a href="../search/Address/county.html">/sdk-for-flutter-explore-search-address-county</a>
↔ String
</dt>
<dd>
  The county name for the address.
It is a division of a state, typically a secondary-level administrative division of a country or equivalent,
for example, "Kings".
Note: This String can be empty when no data is available.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property" id="district">
<a href="../search/Address/district.html">/sdk-for-flutter-explore-search-address-district</a>
↔ String
</dt>
<dd>
  The district name for the address.
It is a division of city, typically an administrative unit within a larger city or
a customary name of a city's neighborhood, for example, "Bedford-Stuyvesant".
Note: This String can be empty when no data is available.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property" id="hashCode">
<a href="../search/Address/hashCode.html">/sdk-for-flutter-explore-search-address-hashcode</a>
→ int
</dt>
<dd>
  The hash code for this object.
  <div class="features">no setter</div>
</dd>
<dt class="property" id="houseNumOrName">
<a href="../search/Address/houseNumOrName.html">/sdk-for-flutter-explore-search-address-housenumorname</a>
↔ String
</dt>
<dd>
  The house name or number for the address, for example, "347".
Note: This String can be empty when no data is available.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property" id="postalCode">
<a href="../search/Address/postalCode.html">/sdk-for-flutter-explore-search-address-postalcode</a>
↔ String
</dt>
<dd>
  The postal code for the address.
It is an alphanumeric string included in a postal address to facilitate mail sorting, known locally
in various countries throughout the world as a postcode, post code, PIN or ZIP Code, for example, "11233".
Note: This String can be empty when no data is available.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property inherited" id="runtimeType">
<a href="../search/Address/runtimeType.html">/sdk-for-flutter-explore-search-address-runtimetype</a>
→ Type
</dt>
<dd class="inherited">
  A representation of the runtime type of the object.
  <div class="features">no setterinherited</div>
</dd>
<dt class="property" id="state">
<a href="../search/Address/state.html">/sdk-for-flutter-explore-search-address-state</a>
↔ String
</dt>
<dd>
  The state name for the address.
It is the name of the state division of a country, for example, "New York".
Note: This String can be empty when no data is available.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property" id="stateCode">
<a href="../search/Address/stateCode.html">/sdk-for-flutter-explore-search-address-statecode</a>
↔ String
</dt>
<dd>
  The state code for the address.
It is code/abbreviation of the state division of a country, for example, "NY".
Note: This String can be empty when no data is available.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property" id="street">
<a href="../search/Address/street.html">/sdk-for-flutter-explore-search-address-street</a>
↔ String
</dt>
<dd>
  The street name for the address, for example, "Lewis Ave".
Note: This String can be empty when no data is available.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property" id="subBlock">
<a href="../search/Address/subBlock.html">/sdk-for-flutter-explore-search-address-subblock</a>
↔ String
</dt>
<dd>
  The sub-block number for the address. It is part of Japanese addressing system.
Note: This String can be empty when no data is available.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property" id="subdistrict">
<a href="../search/Address/subdistrict.html">/sdk-for-flutter-explore-search-address-subdistrict</a>
↔ String
</dt>
<dd>
  The subdistrict name for the address.
It is a subdivision of a district.
Note: This String can be empty when no data is available.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property" id="type">
<a href="../search/Address/type.html">/sdk-for-flutter-explore-search-address-type</a>
↔ <a href="../search/AddressType.html">/sdk-for-flutter-explore-search-addresstype</a>?
</dt>
<dd>
  Specifies the address type.
  <div class="features">getter/setter pair</div>
</dd>
</dl>
</section>
<section class="summary offset-anchor inherited" id="instance-methods">
<h2>Methods</h2>
<dl class="callables">
<dt class="callable inherited" id="noSuchMethod">
<a href="../search/Address/noSuchMethod.html">/sdk-for-flutter-explore-search-address-nosuchmethod</a>(<wbr/>Invocation invocation)
    → dynamic

</dt>
<dd class="inherited">
  Invoked when a nonexistent method or property is accessed.
  <div class="features">inherited</div>
</dd>
<dt class="callable inherited" id="toString">
<a href="../search/Address/toString.html">/sdk-for-flutter-explore-search-address-tostring</a>(<wbr/>)
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
<a href="../search/Address/operator_equals.html">/sdk-for-flutter-explore-search-address-operator-equals</a>(<wbr/>Object other)
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
<li class="self-crumb">Address class</li>
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
