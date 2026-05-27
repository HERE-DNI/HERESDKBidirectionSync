---
title: "Constructors"
slug: "sdk-for-flutter-explore-search-evchargingtariffpricecomponent-class"
---

<HTMLBlock>
<div class="sdk-for-flutter">
<!-- EVChargingTariffPriceComponent-class.html -->
<div class="doc-with-sidebar"><div class="sidebar-nav"><ol>
<li class="section-title"><a href="search/EVChargingTariffPriceComponent-class.html#constructors">Constructors</a></li>
<li><a href="search/EVChargingTariffPriceComponent/EVChargingTariffPriceComponent.html">EVChargingTariffPriceComponent</a></li>
<li class="section-title">
<a href="search/EVChargingTariffPriceComponent-class.html#instance-properties">Properties</a>
</li>
<li><a href="search/EVChargingTariffPriceComponent/dimension.html">dimension</a></li>
<li><a href="search/EVChargingTariffPriceComponent/hashCode.html">hashCode</a></li>
<li><a href="search/EVChargingTariffPriceComponent/price.html">price</a></li>
<li class="inherited"><a href="search/EVChargingTariffPriceComponent/runtimeType.html">runtimeType</a></li>
<li><a href="search/EVChargingTariffPriceComponent/step.html">step</a></li>
<li><a href="search/EVChargingTariffPriceComponent/vat.html">vat</a></li>
<li class="section-title inherited"><a href="search/EVChargingTariffPriceComponent-class.html#instance-methods">Methods</a></li>
<li class="inherited"><a href="search/EVChargingTariffPriceComponent/noSuchMethod.html">noSuchMethod</a></li>
<li class="inherited"><a href="search/EVChargingTariffPriceComponent/toString.html">toString</a></li>
<li class="section-title"><a href="search/EVChargingTariffPriceComponent-class.html#operators">Operators</a></li>
<li><a href="search/EVChargingTariffPriceComponent/operator_equals.html">operator ==</a></li>
</ol></div><div class="doc-content">
<div id="overlay-under-drawer"></div>
<header id="title">
menu
<ol class="breadcrumbs gt-separated dark hidden-xs">
<li><a href="../index.html">/sdk-for-flutter-explore</a></li>
<li><a href="../search/search-library.html">/sdk-for-flutter-explore-search-search-library</a></li>
<li class="self-crumb">EVChargingTariffPriceComponent class</li>
</ol>
<div class="self-name">EVChargingTariffPriceComponent</div>
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
<div class="main-content" data-above-sidebar="search/search-library-sidebar.html" data-below-sidebar="search/EVChargingTariffPriceComponent-class-sidebar.html" id="dartdoc-main-content">
<div>
<h1>EVChargingTariffPriceComponent class</h1></div>
<section class="desc markdown">
<p>Represents the price component of an EV charging tariff.</p>
<p><strong>Note:</strong> This is a beta release of this feature, so there could be a few bugs and unexpected behaviors.
Related APIs may change for new releases without a deprecation process.</p>
</section>
<section class="summary offset-anchor" id="constructors">
<h2>Constructors</h2>
<dl class="constructor-summary-list">
<dt class="callable" id="EVChargingTariffPriceComponent">
<a href="../search/EVChargingTariffPriceComponent/EVChargingTariffPriceComponent.html">/sdk-for-flutter-explore-search-evchargingtariffpricecomponent-evchargingtariffpricecomponent</a>()
</dt>
<dd>
</dd>
</dl>
</section>
<section class="summary offset-anchor" id="instance-properties">
<h2>Properties</h2>
<dl class="properties">
<dt class="property" id="dimension">
<a href="../search/EVChargingTariffPriceComponent/dimension.html">/sdk-for-flutter-explore-search-evchargingtariffpricecomponent-dimension</a>
↔ <a href="../search/EVChargingTariffDimension.html">/sdk-for-flutter-explore-search-evchargingtariffdimension</a>
</dt>
<dd>
  The dimension or type of the price component.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property" id="hashCode">
<a href="../search/EVChargingTariffPriceComponent/hashCode.html">/sdk-for-flutter-explore-search-evchargingtariffpricecomponent-hashcode</a>
→ int
</dt>
<dd>
  The hash code for this object.
  <div class="features">no setter</div>
</dd>
<dt class="property" id="price">
<a href="../search/EVChargingTariffPriceComponent/price.html">/sdk-for-flutter-explore-search-evchargingtariffpricecomponent-price</a>
↔ double
</dt>
<dd>
  The price per unit, excluding VAT. The units are defined by the <a href="../search/EVChargingTariffPriceComponent/dimension.html">/sdk-for-flutter-explore-search-evchargingtariffpricecomponent-dimension</a>
<div class="features">getter/setter pair</div>
</dd>
<dt class="property inherited" id="runtimeType">
<a href="../search/EVChargingTariffPriceComponent/runtimeType.html">/sdk-for-flutter-explore-search-evchargingtariffpricecomponent-runtimetype</a>
→ Type
</dt>
<dd class="inherited">
  A representation of the runtime type of the object.
  <div class="features">no setterinherited</div>
</dd>
<dt class="property" id="step">
<a href="../search/EVChargingTariffPriceComponent/step.html">/sdk-for-flutter-explore-search-evchargingtariffpricecomponent-step</a>
↔ double?
</dt>
<dd>
  Dimension quantity used as a unit of billing. Present for all other dimensions except
<a href="../search/EVChargingTariffDimension.html">/sdk-for-flutter-explore-search-evchargingtariffdimension</a>. The customer is charged price for each full or partial
step of the dimension consumed. For <a href="../search/EVChargingTariffDimension.html">/sdk-for-flutter-explore-search-evchargingtariffdimension</a>, the step size unit
is 1 Wh, for <a href="../search/EVChargingTariffDimension.html">/sdk-for-flutter-explore-search-evchargingtariffdimension</a> and <a href="../search/EVChargingTariffDimension.html">/sdk-for-flutter-explore-search-evchargingtariffdimension</a>
it is 1 second. For example, if step is 300 for time, then time is billed in 5 minute steps, rounded upwards.
Similarly, if step is 100 for energy, then energy is billed in 100 Wh = 0.1 kWh steps.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property" id="vat">
<a href="../search/EVChargingTariffPriceComponent/vat.html">/sdk-for-flutter-explore-search-evchargingtariffpricecomponent-vat</a>
↔ double?
</dt>
<dd>
  The VAT percentage of the price component. If not present, no VAT is applicable.
  <div class="features">getter/setter pair</div>
</dd>
</dl>
</section>
<section class="summary offset-anchor inherited" id="instance-methods">
<h2>Methods</h2>
<dl class="callables">
<dt class="callable inherited" id="noSuchMethod">
<a href="../search/EVChargingTariffPriceComponent/noSuchMethod.html">/sdk-for-flutter-explore-search-evchargingtariffpricecomponent-nosuchmethod</a>(<wbr/>Invocation invocation)
    → dynamic

</dt>
<dd class="inherited">
  Invoked when a nonexistent method or property is accessed.
  <div class="features">inherited</div>
</dd>
<dt class="callable inherited" id="toString">
<a href="../search/EVChargingTariffPriceComponent/toString.html">/sdk-for-flutter-explore-search-evchargingtariffpricecomponent-tostring</a>(<wbr/>)
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
<a href="../search/EVChargingTariffPriceComponent/operator_equals.html">/sdk-for-flutter-explore-search-evchargingtariffpricecomponent-operator-equals</a>(<wbr/>Object other)
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
<li class="self-crumb">EVChargingTariffPriceComponent class</li>
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
