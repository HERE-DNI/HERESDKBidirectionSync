---
title: "Constructors"
slug: "sdk-for-flutter-explore-search-daterange-class"
---

<HTMLBlock>
<div class="sdk-for-flutter">
<!-- DateRange-class.html -->
<div class="doc-with-sidebar"><div class="sidebar-nav"><ol>
<li class="section-title"><a href="search/DateRange-class.html#constructors">Constructors</a></li>
<li><a href="search/DateRange/DateRange.html">DateRange</a></li>
<li class="section-title">
<a href="search/DateRange-class.html#instance-properties">Properties</a>
</li>
<li><a href="search/DateRange/from.html">from</a></li>
<li><a href="search/DateRange/hashCode.html">hashCode</a></li>
<li class="inherited"><a href="search/DateRange/runtimeType.html">runtimeType</a></li>
<li><a href="search/DateRange/to.html">to</a></li>
<li class="section-title inherited"><a href="search/DateRange-class.html#instance-methods">Methods</a></li>
<li class="inherited"><a href="search/DateRange/noSuchMethod.html">noSuchMethod</a></li>
<li class="inherited"><a href="search/DateRange/toString.html">toString</a></li>
<li class="section-title"><a href="search/DateRange-class.html#operators">Operators</a></li>
<li><a href="search/DateRange/operator_equals.html">operator ==</a></li>
</ol></div><div class="doc-content">
<div id="overlay-under-drawer"></div>
<header id="title">
menu
<ol class="breadcrumbs gt-separated dark hidden-xs">
<li><a href="../index.html">/sdk-for-flutter-explore</a></li>
<li><a href="../search/search-library.html">/sdk-for-flutter-explore-search-search-library</a></li>
<li class="self-crumb">DateRange class</li>
</ol>
<div class="self-name">DateRange</div>
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
<div class="main-content" data-above-sidebar="search/search-library-sidebar.html" data-below-sidebar="search/DateRange-class-sidebar.html" id="dartdoc-main-content">
<div>
<h1>DateRange class</h1></div>
<section class="desc markdown">
<p>Represents the date range when the tariff element is valid.</p>
<p>This is typically used to indicate
seasonal tariffs or to announce an update to the tariff in advance. It may also be used to
indicate spot prices, together with time period.
<strong>Note:</strong> This is a beta release of this feature, so there could be a few bugs and unexpected behaviors.
Related APIs may change for new releases without a deprecation process.</p>
</section>
<section class="summary offset-anchor" id="constructors">
<h2>Constructors</h2>
<dl class="constructor-summary-list">
<dt class="callable" id="DateRange">
<a href="../search/DateRange/DateRange.html">/sdk-for-flutter-explore-search-daterange-daterange</a>()
</dt>
<dd>
</dd>
</dl>
</section>
<section class="summary offset-anchor" id="instance-properties">
<h2>Properties</h2>
<dl class="properties">
<dt class="property" id="from">
<a href="../search/DateRange/from.html">/sdk-for-flutter-explore-search-daterange-from</a>
↔ DateTime?
</dt>
<dd>
  First date when the element is valid.
If absent the element becomes valid as soon as other conditions allow.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property" id="hashCode">
<a href="../search/DateRange/hashCode.html">/sdk-for-flutter-explore-search-daterange-hashcode</a>
→ int
</dt>
<dd>
  The hash code for this object.
  <div class="features">no setter</div>
</dd>
<dt class="property inherited" id="runtimeType">
<a href="../search/DateRange/runtimeType.html">/sdk-for-flutter-explore-search-daterange-runtimetype</a>
→ Type
</dt>
<dd class="inherited">
  A representation of the runtime type of the object.
  <div class="features">no setterinherited</div>
</dd>
<dt class="property" id="to">
<a href="../search/DateRange/to.html">/sdk-for-flutter-explore-search-daterange-to</a>
↔ DateTime?
</dt>
<dd>
  First date when the element is no longer valid, exclusive and later than <a href="../search/DateRange/from.html">/sdk-for-flutter-explore-search-daterange-from</a>.
If absent the element is valid until some other element takes over.
  <div class="features">getter/setter pair</div>
</dd>
</dl>
</section>
<section class="summary offset-anchor inherited" id="instance-methods">
<h2>Methods</h2>
<dl class="callables">
<dt class="callable inherited" id="noSuchMethod">
<a href="../search/DateRange/noSuchMethod.html">/sdk-for-flutter-explore-search-daterange-nosuchmethod</a>(<wbr/>Invocation invocation)
    → dynamic

</dt>
<dd class="inherited">
  Invoked when a nonexistent method or property is accessed.
  <div class="features">inherited</div>
</dd>
<dt class="callable inherited" id="toString">
<a href="../search/DateRange/toString.html">/sdk-for-flutter-explore-search-daterange-tostring</a>(<wbr/>)
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
<a href="../search/DateRange/operator_equals.html">/sdk-for-flutter-explore-search-daterange-operator-equals</a>(<wbr/>Object other)
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
<li class="self-crumb">DateRange class</li>
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
