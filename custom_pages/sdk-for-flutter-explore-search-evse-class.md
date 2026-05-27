---
title: "Constructors"
slug: "sdk-for-flutter-explore-search-evse-class"
---

<HTMLBlock>
<div class="sdk-for-flutter">
<!-- Evse-class.html -->
<div class="doc-with-sidebar"><div class="sidebar-nav"><ol>
<li class="section-title"><a href="search/Evse-class.html#constructors">Constructors</a></li>
<li><a href="search/Evse/Evse.html">Evse</a></li>
<li class="section-title">
<a href="search/Evse-class.html#instance-properties">Properties</a>
</li>
<li><a href="search/Evse/connectors.html">connectors</a></li>
<li><a href="search/Evse/cpoEvseEmi3Id.html">cpoEvseEmi3Id</a></li>
<li><a href="search/Evse/cpoId.html">cpoId</a></li>
<li><a href="search/Evse/hashCode.html">hashCode</a></li>
<li><a href="search/Evse/id.html">id</a></li>
<li><a href="search/Evse/lastUpdated.html">lastUpdated</a></li>
<li class="inherited"><a href="search/Evse/runtimeType.html">runtimeType</a></li>
<li><a href="search/Evse/status.html">status</a></li>
<li class="section-title inherited"><a href="search/Evse-class.html#instance-methods">Methods</a></li>
<li class="inherited"><a href="search/Evse/noSuchMethod.html">noSuchMethod</a></li>
<li class="inherited"><a href="search/Evse/toString.html">toString</a></li>
<li class="section-title"><a href="search/Evse-class.html#operators">Operators</a></li>
<li><a href="search/Evse/operator_equals.html">operator ==</a></li>
</ol></div><div class="doc-content">
<div id="overlay-under-drawer"></div>
<header id="title">
menu
<ol class="breadcrumbs gt-separated dark hidden-xs">
<li><a href="../index.html">/sdk-for-flutter-explore</a></li>
<li><a href="../search/search-library.html">/sdk-for-flutter-explore-search-search-library</a></li>
<li class="self-crumb">Evse class</li>
</ol>
<div class="self-name">Evse</div>
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
<div class="main-content" data-above-sidebar="search/search-library-sidebar.html" data-below-sidebar="search/Evse-class-sidebar.html" id="dartdoc-main-content">
<div>
<h1>Evse class</h1></div>
<section class="desc markdown">
<p>Charge Point Operator (CPO) ID uses the Electric Vehicle Supply Equipment ID (EVSE ID) for an exact identification of the charging infrastructure and charging point.</p>
</section>
<section class="summary offset-anchor" id="constructors">
<h2>Constructors</h2>
<dl class="constructor-summary-list">
<dt class="callable" id="Evse">
<a href="../search/Evse/Evse.html">/sdk-for-flutter-explore-search-evse-evse</a>()
</dt>
<dd>
</dd>
</dl>
</section>
<section class="summary offset-anchor" id="instance-properties">
<h2>Properties</h2>
<dl class="properties">
<dt class="property" id="connectors">
<a href="../search/Evse/connectors.html">/sdk-for-flutter-explore-search-evse-connectors</a>
↔ List&lt;<wbr/><a href="../search/EVSEConnector-class.html">/sdk-for-flutter-explore-search-evseconnector-class</a>&gt;
</dt>
<dd>
  List of connectors of this EVSE.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property" id="cpoEvseEmi3Id">
<a href="../search/Evse/cpoEvseEmi3Id.html">/sdk-for-flutter-explore-search-evse-cpoevseemi3id</a>
↔ String?
</dt>
<dd>
  Identifier in Emi3 format of the EVSE within the Charge Point Operator (CPO) platform.
This id is not always present.
Example of ID format: <code>DE*ICT*E0001897</code>.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property" id="cpoId">
<a href="../search/Evse/cpoId.html">/sdk-for-flutter-explore-search-evse-cpoid</a>
↔ String?
</dt>
<dd>
  The unique ID of an EVSE in the system of the CPO.
This ID is unique in the system of the CPO but not necessarily globally unique.
The format will differ between different CPOs.
This ID is always provided.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property" id="hashCode">
<a href="../search/Evse/hashCode.html">/sdk-for-flutter-explore-search-evse-hashcode</a>
→ int
</dt>
<dd>
  The hash code for this object.
  <div class="features">no setter</div>
</dd>
<dt class="property" id="id">
<a href="../search/Evse/id.html">/sdk-for-flutter-explore-search-evse-id</a>
↔ String?
</dt>
<dd>
  HERE ID of the EVSE.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property" id="lastUpdated">
<a href="../search/Evse/lastUpdated.html">/sdk-for-flutter-explore-search-evse-lastupdated</a>
↔ DateTime?
</dt>
<dd>
  Last update of the dynamic connector availability information.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property inherited" id="runtimeType">
<a href="../search/Evse/runtimeType.html">/sdk-for-flutter-explore-search-evse-runtimetype</a>
→ Type
</dt>
<dd class="inherited">
  A representation of the runtime type of the object.
  <div class="features">no setterinherited</div>
</dd>
<dt class="property" id="status">
<a href="../search/Evse/status.html">/sdk-for-flutter-explore-search-evse-status</a>
↔ <a href="../search/EVSEStatus.html">/sdk-for-flutter-explore-search-evsestatus</a>?
</dt>
<dd>
  EVSE status.
  <div class="features">getter/setter pair</div>
</dd>
</dl>
</section>
<section class="summary offset-anchor inherited" id="instance-methods">
<h2>Methods</h2>
<dl class="callables">
<dt class="callable inherited" id="noSuchMethod">
<a href="../search/Evse/noSuchMethod.html">/sdk-for-flutter-explore-search-evse-nosuchmethod</a>(<wbr/>Invocation invocation)
    → dynamic

</dt>
<dd class="inherited">
  Invoked when a nonexistent method or property is accessed.
  <div class="features">inherited</div>
</dd>
<dt class="callable inherited" id="toString">
<a href="../search/Evse/toString.html">/sdk-for-flutter-explore-search-evse-tostring</a>(<wbr/>)
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
<a href="../search/Evse/operator_equals.html">/sdk-for-flutter-explore-search-evse-operator-equals</a>(<wbr/>Object other)
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
<li class="self-crumb">Evse class</li>
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
