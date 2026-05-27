---
title: "Constructors"
slug: "sdk-for-flutter-explore-search-evsearchoptions-class"
---

<HTMLBlock>
<div class="sdk-for-flutter">
<!-- EVSearchOptions-class.html -->
<div class="doc-with-sidebar"><div class="sidebar-nav"><ol>
<li class="section-title"><a href="search/EVSearchOptions-class.html#constructors">Constructors</a></li>
<li><a href="search/EVSearchOptions/EVSearchOptions.html">EVSearchOptions</a></li>
<li class="section-title">
<a href="search/EVSearchOptions-class.html#instance-properties">Properties</a>
</li>
<li><a href="search/EVSearchOptions/additionalFeatures.html">additionalFeatures</a></li>
<li><a href="search/EVSearchOptions/hashCode.html">hashCode</a></li>
<li><a href="search/EVSearchOptions/requestedTariffs.html">requestedTariffs</a></li>
<li class="inherited"><a href="search/EVSearchOptions/runtimeType.html">runtimeType</a></li>
<li class="section-title inherited"><a href="search/EVSearchOptions-class.html#instance-methods">Methods</a></li>
<li class="inherited"><a href="search/EVSearchOptions/noSuchMethod.html">noSuchMethod</a></li>
<li class="inherited"><a href="search/EVSearchOptions/toString.html">toString</a></li>
<li class="section-title"><a href="search/EVSearchOptions-class.html#operators">Operators</a></li>
<li><a href="search/EVSearchOptions/operator_equals.html">operator ==</a></li>
</ol></div><div class="doc-content">
<div id="overlay-under-drawer"></div>
<header id="title">
menu
<ol class="breadcrumbs gt-separated dark hidden-xs">
<li><a href="../index.html">/sdk-for-flutter-explore</a></li>
<li><a href="../search/search-library.html">/sdk-for-flutter-explore-search-search-library</a></li>
<li class="self-crumb">EVSearchOptions class</li>
</ol>
<div class="self-name">EVSearchOptions</div>
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
<div class="main-content" data-above-sidebar="search/search-library-sidebar.html" data-below-sidebar="search/EVSearchOptions-class-sidebar.html" id="dartdoc-main-content">
<div>
<h1>EVSearchOptions class</h1></div>
<section class="desc markdown">
<p>Encapsulates additional options that control the behavior of <code>EVSearchEngine</code>.</p>
<p><strong>Note:</strong> This is a beta release of this feature, so there could be a few bugs and unexpected behaviors.
Related APIs may change for new releases without a deprecation process.</p>
</section>
<section class="summary offset-anchor" id="constructors">
<h2>Constructors</h2>
<dl class="constructor-summary-list">
<dt class="callable" id="EVSearchOptions">
<a href="../search/EVSearchOptions/EVSearchOptions.html">/sdk-for-flutter-explore-search-evsearchoptions-evsearchoptions</a>()
</dt>
<dd>
</dd>
</dl>
</section>
<section class="summary offset-anchor" id="instance-properties">
<h2>Properties</h2>
<dl class="properties">
<dt class="property" id="additionalFeatures">
<a href="../search/EVSearchOptions/additionalFeatures.html">/sdk-for-flutter-explore-search-evsearchoptions-additionalfeatures</a>
↔ List&lt;<wbr/><a href="../search/EVChargingLocationFeature.html">/sdk-for-flutter-explore-search-evcharginglocationfeature</a>&gt;
</dt>
<dd>
  List of additional optional features to be returned in <a href="../search/EVChargingLocation-class.html">/sdk-for-flutter-explore-search-evcharginglocation-class</a>.
If empty, only minimal set of the required features will be returned.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property" id="hashCode">
<a href="../search/EVSearchOptions/hashCode.html">/sdk-for-flutter-explore-search-evsearchoptions-hashcode</a>
→ int
</dt>
<dd>
  The hash code for this object.
  <div class="features">no setter</div>
</dd>
<dt class="property" id="requestedTariffs">
<a href="../search/EVSearchOptions/requestedTariffs.html">/sdk-for-flutter-explore-search-evsearchoptions-requestedtariffs</a>
↔ List&lt;<wbr/><a href="../search/EVChargingTariffRequest-class.html">/sdk-for-flutter-explore-search-evchargingtariffrequest-class</a>&gt;
</dt>
<dd>
  List of tariff search options.
This parameter is effective only if the <a href="../search/EVSearchOptions/additionalFeatures.html">/sdk-for-flutter-explore-search-evsearchoptions-additionalfeatures</a> contains <a href="../search/EVChargingLocationFeature.html">/sdk-for-flutter-explore-search-evcharginglocationfeature</a>.
If empty, the response contains only ad-hoc tariffs, if available.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property inherited" id="runtimeType">
<a href="../search/EVSearchOptions/runtimeType.html">/sdk-for-flutter-explore-search-evsearchoptions-runtimetype</a>
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
<a href="../search/EVSearchOptions/noSuchMethod.html">/sdk-for-flutter-explore-search-evsearchoptions-nosuchmethod</a>(<wbr/>Invocation invocation)
    → dynamic

</dt>
<dd class="inherited">
  Invoked when a nonexistent method or property is accessed.
  <div class="features">inherited</div>
</dd>
<dt class="callable inherited" id="toString">
<a href="../search/EVSearchOptions/toString.html">/sdk-for-flutter-explore-search-evsearchoptions-tostring</a>(<wbr/>)
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
<a href="../search/EVSearchOptions/operator_equals.html">/sdk-for-flutter-explore-search-evsearchoptions-operator-equals</a>(<wbr/>Object other)
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
<li class="self-crumb">EVSearchOptions class</li>
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
