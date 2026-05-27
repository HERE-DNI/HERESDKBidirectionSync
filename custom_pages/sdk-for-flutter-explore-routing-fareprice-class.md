---
title: "Constructors"
slug: "sdk-for-flutter-explore-routing-fareprice-class"
---

<HTMLBlock>
<div class="sdk-for-flutter">
<!-- FarePrice-class.html -->
<div class="doc-with-sidebar"><div class="sidebar-nav"><ol>
<li class="section-title"><a href="routing/FarePrice-class.html#constructors">Constructors</a></li>
<li><a href="routing/FarePrice/FarePrice.html">FarePrice</a></li>
<li class="section-title">
<a href="routing/FarePrice-class.html#instance-properties">Properties</a>
</li>
<li><a href="routing/FarePrice/currency.html">currency</a></li>
<li><a href="routing/FarePrice/estimated.html">estimated</a></li>
<li><a href="routing/FarePrice/hashCode.html">hashCode</a></li>
<li><a href="routing/FarePrice/maximum.html">maximum</a></li>
<li><a href="routing/FarePrice/minimum.html">minimum</a></li>
<li class="inherited"><a href="routing/FarePrice/runtimeType.html">runtimeType</a></li>
<li><a href="routing/FarePrice/type.html">type</a></li>
<li><a href="routing/FarePrice/validityPeriod.html">validityPeriod</a></li>
<li class="section-title inherited"><a href="routing/FarePrice-class.html#instance-methods">Methods</a></li>
<li class="inherited"><a href="routing/FarePrice/noSuchMethod.html">noSuchMethod</a></li>
<li class="inherited"><a href="routing/FarePrice/toString.html">toString</a></li>
<li class="section-title"><a href="routing/FarePrice-class.html#operators">Operators</a></li>
<li><a href="routing/FarePrice/operator_equals.html">operator ==</a></li>
</ol></div><div class="doc-content">
<div id="overlay-under-drawer"></div>
<header id="title">
menu
<ol class="breadcrumbs gt-separated dark hidden-xs">
<li><a href="../index.html">/sdk-for-flutter-explore</a></li>
<li><a href="../routing/routing-library.html">/sdk-for-flutter-explore-routing-routing-library</a></li>
<li class="self-crumb">FarePrice class</li>
</ol>
<div class="self-name">FarePrice</div>
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
<div class="main-content" data-above-sidebar="routing/routing-library-sidebar.html" data-below-sidebar="routing/FarePrice-class-sidebar.html" id="dartdoc-main-content">
<div>
<h1>FarePrice class</h1></div>
<section class="desc markdown">
<p>Price of a fare.</p>
</section>
<section class="summary offset-anchor" id="constructors">
<h2>Constructors</h2>
<dl class="constructor-summary-list">
<dt class="callable" id="FarePrice">
<a href="../routing/FarePrice/FarePrice.html">/sdk-for-flutter-explore-routing-fareprice-fareprice</a>()
</dt>
<dd>
</dd>
</dl>
</section>
<section class="summary offset-anchor" id="instance-properties">
<h2>Properties</h2>
<dl class="properties">
<dt class="property" id="currency">
<a href="../routing/FarePrice/currency.html">/sdk-for-flutter-explore-routing-fareprice-currency</a>
↔ String
</dt>
<dd>
  Local currency of the price compliant to ISO 4217. For example, "GBP" for the British pound sterling.
Defaults to "EUR" string.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property" id="estimated">
<a href="../routing/FarePrice/estimated.html">/sdk-for-flutter-explore-routing-fareprice-estimated</a>
↔ bool
</dt>
<dd>
<code>True</code> when the fare price is estimated based on best guess and the actual price may differ.
Defaults to <code>false</code>.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property" id="hashCode">
<a href="../routing/FarePrice/hashCode.html">/sdk-for-flutter-explore-routing-fareprice-hashcode</a>
→ int
</dt>
<dd>
  The hash code for this object.
  <div class="features">no setter</div>
</dd>
<dt class="property" id="maximum">
<a href="../routing/FarePrice/maximum.html">/sdk-for-flutter-explore-routing-fareprice-maximum</a>
↔ double
</dt>
<dd>
  Maximum price when the price is of <a href="../routing/FarePriceType.html">/sdk-for-flutter-explore-routing-farepricetype</a> type. Otherwise, it is
equal to <a href="../routing/FarePrice/minimum.html">/sdk-for-flutter-explore-routing-fareprice-minimum</a>.
Defaults to 0.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property" id="minimum">
<a href="../routing/FarePrice/minimum.html">/sdk-for-flutter-explore-routing-fareprice-minimum</a>
↔ double
</dt>
<dd>
  Minimum price when the price is of <a href="../routing/FarePriceType.html">/sdk-for-flutter-explore-routing-farepricetype</a> type. Otherwise, it is
equal to <a href="../routing/FarePrice/maximum.html">/sdk-for-flutter-explore-routing-fareprice-maximum</a>.
Defaults to 0.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property inherited" id="runtimeType">
<a href="../routing/FarePrice/runtimeType.html">/sdk-for-flutter-explore-routing-fareprice-runtimetype</a>
→ Type
</dt>
<dd class="inherited">
  A representation of the runtime type of the object.
  <div class="features">no setterinherited</div>
</dd>
<dt class="property" id="type">
<a href="../routing/FarePrice/type.html">/sdk-for-flutter-explore-routing-fareprice-type</a>
↔ <a href="../routing/FarePriceType.html">/sdk-for-flutter-explore-routing-farepricetype</a>
</dt>
<dd>
  Type of price represented by this object.
Defaults to <a href="../routing/FarePriceType.html">/sdk-for-flutter-explore-routing-farepricetype</a>.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property" id="validityPeriod">
<a href="../routing/FarePrice/validityPeriod.html">/sdk-for-flutter-explore-routing-fareprice-validityperiod</a>
↔ Duration?
</dt>
<dd>
  When set, the price is paid for a specific duration.
  <div class="features">getter/setter pair</div>
</dd>
</dl>
</section>
<section class="summary offset-anchor inherited" id="instance-methods">
<h2>Methods</h2>
<dl class="callables">
<dt class="callable inherited" id="noSuchMethod">
<a href="../routing/FarePrice/noSuchMethod.html">/sdk-for-flutter-explore-routing-fareprice-nosuchmethod</a>(<wbr/>Invocation invocation)
    → dynamic

</dt>
<dd class="inherited">
  Invoked when a nonexistent method or property is accessed.
  <div class="features">inherited</div>
</dd>
<dt class="callable inherited" id="toString">
<a href="../routing/FarePrice/toString.html">/sdk-for-flutter-explore-routing-fareprice-tostring</a>(<wbr/>)
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
<a href="../routing/FarePrice/operator_equals.html">/sdk-for-flutter-explore-routing-fareprice-operator-equals</a>(<wbr/>Object other)
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
<li><a href="../routing/routing-library.html">/sdk-for-flutter-explore-routing-routing-library</a></li>
<li class="self-crumb">FarePrice class</li>
</ol>
<h5>routing library</h5>
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
