---
title: "EVChargingTariffElement class"
slug: "sdk-for-flutter-explore-search-evchargingtariffelement-class"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- EVChargingTariffElement-class.html -->
<div class="doc-with-sidebar"><div class="sidebar-nav"><ol>
<li class="section-title"><a href="search/EVChargingTariffElement-class.html#constructors">Constructors</a></li>
<li><a href="search/EVChargingTariffElement/EVChargingTariffElement.html">EVChargingTariffElement</a></li>
<li class="section-title">
<a href="search/EVChargingTariffElement-class.html#instance-properties">Properties</a>
</li>
<li><a href="search/EVChargingTariffElement/components.html">components</a></li>
<li><a href="search/EVChargingTariffElement/condition.html">condition</a></li>
<li><a href="search/EVChargingTariffElement/hashCode.html">hashCode</a></li>
<li class="inherited"><a href="search/EVChargingTariffElement/runtimeType.html">runtimeType</a></li>
<li class="section-title inherited"><a href="search/EVChargingTariffElement-class.html#instance-methods">Methods</a></li>
<li class="inherited"><a href="search/EVChargingTariffElement/noSuchMethod.html">noSuchMethod</a></li>
<li class="inherited"><a href="search/EVChargingTariffElement/toString.html">toString</a></li>
<li class="section-title"><a href="search/EVChargingTariffElement-class.html#operators">Operators</a></li>
<li><a href="search/EVChargingTariffElement/operator_equals.html">operator ==</a></li>
</ol></div><div class="doc-content">
<div id="overlay-under-drawer"></div>
<header id="title">
menu
<ol class="breadcrumbs gt-separated dark hidden-xs">
<li>/sdk-for-flutter-explore</li>
<li>/sdk-for-flutter-explore-search-search-library</li>
<li class="self-crumb">EVChargingTariffElement class</li>
</ol>
<div class="self-name">EVChargingTariffElement</div>
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
<div class="main-content" data-above-sidebar="search/search-library-sidebar.html" data-below-sidebar="search/EVChargingTariffElement-class-sidebar.html" id="dartdoc-main-content">
<div>
<h1>EVChargingTariffElement class</h1></div>
<section class="desc markdown">
<p>Represents a tariff element, which defines how pricing is applied.</p>
<p>The associated condition assists the client in selecting the appropriate element for a charging session.
<strong>Note:</strong> This is a beta release of this feature, so there could be a few bugs and unexpected behaviors.
Related APIs may change for new releases without a deprecation process.</p>
</section>
<section class="summary offset-anchor" id="constructors">
<h2>Constructors</h2>
<dl class="constructor-summary-list">
<dt class="callable" id="EVChargingTariffElement">
/sdk-for-flutter-explore-search-evchargingtariffelement-evchargingtariffelement()
</dt>
<dd>
</dd>
</dl>
</section>
<section class="summary offset-anchor" id="instance-properties">
<h2>Properties</h2>
<dl class="properties">
<dt class="property" id="components">
/sdk-for-flutter-explore-search-evchargingtariffelement-components
↔ List&lt;<wbr/>/sdk-for-flutter-explore-search-evchargingtariffpricecomponent-class&gt;
</dt>
<dd>
  List of price components that describe the tariff.
Each of the components should have a different /sdk-for-flutter-explore-search-evchargingtariffdimension.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property" id="condition">
/sdk-for-flutter-explore-search-evchargingtariffelement-condition
↔ /sdk-for-flutter-explore-search-evchargingtariffelementcondition-class?
</dt>
<dd>
  Condition that the charging session needs to meet to apply the tariff element. An element without any
condition is typically present for charging sessions that do not meet any of the conditions.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property" id="hashCode">
/sdk-for-flutter-explore-search-evchargingtariffelement-hashcode
→ int
</dt>
<dd>
  The hash code for this object.
  <div class="features">no setter</div>
</dd>
<dt class="property inherited" id="runtimeType">
/sdk-for-flutter-explore-search-evchargingtariffelement-runtimetype
→ Type
</dt>
<dd class="inherited">
  A representation of the runtime type of the object.
  <div class="features">no setterinherited</div>
</dd>
</dl>
</section>
<section class="summary offset-anchor inherited" id="instance-methods">
<h2>Methods</h2>
<dl class="callables">
<dt class="callable inherited" id="noSuchMethod">
/sdk-for-flutter-explore-search-evchargingtariffelement-nosuchmethod(<wbr/>Invocation invocation)
    → dynamic

</dt>
<dd class="inherited">
  Invoked when a nonexistent method or property is accessed.
  <div class="features">inherited</div>
</dd>
<dt class="callable inherited" id="toString">
/sdk-for-flutter-explore-search-evchargingtariffelement-tostring(<wbr/>)
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
/sdk-for-flutter-explore-search-evchargingtariffelement-operator-equals(<wbr/>Object other)
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
<li>/sdk-for-flutter-explore</li>
<li>/sdk-for-flutter-explore-search-search-library</li>
<li class="self-crumb">EVChargingTariffElement class</li>
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
`
}</HTMLBlock>
