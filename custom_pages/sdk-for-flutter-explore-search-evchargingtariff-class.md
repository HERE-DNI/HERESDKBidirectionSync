---
title: "Constructors"
slug: "sdk-for-flutter-explore-search-evchargingtariff-class"
---

<HTMLBlock>
<div class="sdk-for-flutter">
<!-- EVChargingTariff-class.html -->
<div class="doc-with-sidebar"><div class="sidebar-nav"><ol>
<li class="section-title"><a href="search/EVChargingTariff-class.html#constructors">Constructors</a></li>
<li><a href="search/EVChargingTariff/EVChargingTariff.html">EVChargingTariff</a></li>
<li class="section-title">
<a href="search/EVChargingTariff-class.html#instance-properties">Properties</a>
</li>
<li><a href="search/EVChargingTariff/currency.html">currency</a></li>
<li><a href="search/EVChargingTariff/elements.html">elements</a></li>
<li><a href="search/EVChargingTariff/hashCode.html">hashCode</a></li>
<li><a href="search/EVChargingTariff/name.html">name</a></li>
<li><a href="search/EVChargingTariff/partner.html">partner</a></li>
<li><a href="search/EVChargingTariff/partnerID.html">partnerID</a></li>
<li class="inherited"><a href="search/EVChargingTariff/runtimeType.html">runtimeType</a></li>
<li><a href="search/EVChargingTariff/type.html">type</a></li>
<li class="section-title inherited"><a href="search/EVChargingTariff-class.html#instance-methods">Methods</a></li>
<li class="inherited"><a href="search/EVChargingTariff/noSuchMethod.html">noSuchMethod</a></li>
<li class="inherited"><a href="search/EVChargingTariff/toString.html">toString</a></li>
<li class="section-title"><a href="search/EVChargingTariff-class.html#operators">Operators</a></li>
<li><a href="search/EVChargingTariff/operator_equals.html">operator ==</a></li>
</ol></div><div class="doc-content">
<div id="overlay-under-drawer"></div>
<header id="title">
menu
<ol class="breadcrumbs gt-separated dark hidden-xs">
<li><a href="../index.html">/sdk-for-flutter-explore</a></li>
<li><a href="../search/search-library.html">/sdk-for-flutter-explore-search-search-library</a></li>
<li class="self-crumb">EVChargingTariff class</li>
</ol>
<div class="self-name">EVChargingTariff</div>
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
<div class="main-content" data-above-sidebar="search/search-library-sidebar.html" data-below-sidebar="search/EVChargingTariff-class-sidebar.html" id="dartdoc-main-content">
<div>
<h1>EVChargingTariff class</h1></div>
<section class="desc markdown">
<p>Tariffs provide detailed pricing information for charging electric vehicles at a specific location.</p>
<p>Each tariff describes how costs are calculated based on various factors such as energy consumed,
time spent charging, and session duration.
Tariffs are typically associated with specific connectors or connector groups, and are only
included in the response when relevant data is available and requested.
<strong>Note:</strong> This is a beta release of this feature, so there could be a few bugs and unexpected behaviors.
Related APIs may change for new releases without a deprecation process.</p>
</section>
<section class="summary offset-anchor" id="constructors">
<h2>Constructors</h2>
<dl class="constructor-summary-list">
<dt class="callable" id="EVChargingTariff">
<a href="../search/EVChargingTariff/EVChargingTariff.html">/sdk-for-flutter-explore-search-evchargingtariff-evchargingtariff</a>()
</dt>
<dd>
</dd>
</dl>
</section>
<section class="summary offset-anchor" id="instance-properties">
<h2>Properties</h2>
<dl class="properties">
<dt class="property" id="currency">
<a href="../search/EVChargingTariff/currency.html">/sdk-for-flutter-explore-search-evchargingtariff-currency</a>
↔ String
</dt>
<dd>
  The currency in which the prices are given, represented by the ISO 4217 standard currency
code (e.g., EUR, DKK).
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property" id="elements">
<a href="../search/EVChargingTariff/elements.html">/sdk-for-flutter-explore-search-evchargingtariff-elements</a>
↔ List&lt;<wbr/><a href="../search/EVChargingTariffElement-class.html">/sdk-for-flutter-explore-search-evchargingtariffelement-class</a>&gt;
</dt>
<dd>
  Elements composing the tariff. Each element can have multiple components. When multiple elements
are present, the associated condition helps the client to select the element that matches the
charging session. If no condition matches, the element without any condition applies.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property" id="hashCode">
<a href="../search/EVChargingTariff/hashCode.html">/sdk-for-flutter-explore-search-evchargingtariff-hashcode</a>
→ int
</dt>
<dd>
  The hash code for this object.
  <div class="features">no setter</div>
</dd>
<dt class="property" id="name">
<a href="../search/EVChargingTariff/name.html">/sdk-for-flutter-explore-search-evchargingtariff-name</a>
↔ String?
</dt>
<dd>
  Name of the tariff. The name is not mandatory for ad-hoc tariffs, but may exist.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property" id="partner">
<a href="../search/EVChargingTariff/partner.html">/sdk-for-flutter-explore-search-evchargingtariff-partner</a>
↔ String
</dt>
<dd>
  Name of the partner providing the tariff, either the charge point operator or eMSP.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property" id="partnerID">
<a href="../search/EVChargingTariff/partnerID.html">/sdk-for-flutter-explore-search-evchargingtariff-partnerid</a>
↔ String
</dt>
<dd>
  A unique ID representing the partner.
The same id is used also in other parts of the API and other related HERE APIs.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property inherited" id="runtimeType">
<a href="../search/EVChargingTariff/runtimeType.html">/sdk-for-flutter-explore-search-evchargingtariff-runtimetype</a>
→ Type
</dt>
<dd class="inherited">
  A representation of the runtime type of the object.
  <div class="features">no setterinherited</div>
</dd>
<dt class="property" id="type">
<a href="../search/EVChargingTariff/type.html">/sdk-for-flutter-explore-search-evchargingtariff-type</a>
↔ <a href="../search/EVChargingTariffType.html">/sdk-for-flutter-explore-search-evchargingtarifftype</a>
</dt>
<dd>
  Indicates the pricing model.
  <div class="features">getter/setter pair</div>
</dd>
</dl>
</section>
<section class="summary offset-anchor inherited" id="instance-methods">
<h2>Methods</h2>
<dl class="callables">
<dt class="callable inherited" id="noSuchMethod">
<a href="../search/EVChargingTariff/noSuchMethod.html">/sdk-for-flutter-explore-search-evchargingtariff-nosuchmethod</a>(<wbr/>Invocation invocation)
    → dynamic

</dt>
<dd class="inherited">
  Invoked when a nonexistent method or property is accessed.
  <div class="features">inherited</div>
</dd>
<dt class="callable inherited" id="toString">
<a href="../search/EVChargingTariff/toString.html">/sdk-for-flutter-explore-search-evchargingtariff-tostring</a>(<wbr/>)
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
<a href="../search/EVChargingTariff/operator_equals.html">/sdk-for-flutter-explore-search-evchargingtariff-operator-equals</a>(<wbr/>Object other)
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
<li class="self-crumb">EVChargingTariff class</li>
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
