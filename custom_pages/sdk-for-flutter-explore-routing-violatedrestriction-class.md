---
title: "Constructors"
slug: "sdk-for-flutter-explore-routing-violatedrestriction-class"
---

<HTMLBlock>
<div class="sdk-for-flutter">
<!-- ViolatedRestriction-class.html -->
<div class="doc-with-sidebar"><div class="sidebar-nav"><ol>
<li class="section-title"><a href="routing/ViolatedRestriction-class.html#constructors">Constructors</a></li>
<li><a href="routing/ViolatedRestriction/ViolatedRestriction.html">ViolatedRestriction</a></li>
<li class="section-title">
<a href="routing/ViolatedRestriction-class.html#instance-properties">Properties</a>
</li>
<li><a href="routing/ViolatedRestriction/cause.html">cause</a></li>
<li><a href="routing/ViolatedRestriction/details.html">details</a></li>
<li><a href="routing/ViolatedRestriction/hashCode.html">hashCode</a></li>
<li class="inherited"><a href="routing/ViolatedRestriction/runtimeType.html">runtimeType</a></li>
<li><a href="routing/ViolatedRestriction/timeDependent.html">timeDependent</a></li>
<li class="section-title inherited"><a href="routing/ViolatedRestriction-class.html#instance-methods">Methods</a></li>
<li class="inherited"><a href="routing/ViolatedRestriction/noSuchMethod.html">noSuchMethod</a></li>
<li class="inherited"><a href="routing/ViolatedRestriction/toString.html">toString</a></li>
<li class="section-title"><a href="routing/ViolatedRestriction-class.html#operators">Operators</a></li>
<li><a href="routing/ViolatedRestriction/operator_equals.html">operator ==</a></li>
</ol></div><div class="doc-content">
<div id="overlay-under-drawer"></div>
<header id="title">
menu
<ol class="breadcrumbs gt-separated dark hidden-xs">
<li><a href="../index.html">/sdk-for-flutter-explore</a></li>
<li><a href="../routing/routing-library.html">/sdk-for-flutter-explore-routing-routing-library</a></li>
<li class="self-crumb">ViolatedRestriction class</li>
</ol>
<div class="self-name">ViolatedRestriction</div>
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
<div class="main-content" data-above-sidebar="routing/routing-library-sidebar.html" data-below-sidebar="routing/ViolatedRestriction-class-sidebar.html" id="dartdoc-main-content">
<div>
<h1>ViolatedRestriction class</h1></div>
<section class="desc markdown">
<p><code>ViolatedRestriction</code> contains all the violated restriction details for the planned trip.</p>
</section>
<section class="summary offset-anchor" id="constructors">
<h2>Constructors</h2>
<dl class="constructor-summary-list">
<dt class="callable" id="ViolatedRestriction">
<a href="../routing/ViolatedRestriction/ViolatedRestriction.html">/sdk-for-flutter-explore-routing-violatedrestriction-violatedrestriction</a>(String cause, bool timeDependent)
</dt>
<dd>
</dd>
</dl>
</section>
<section class="summary offset-anchor" id="instance-properties">
<h2>Properties</h2>
<dl class="properties">
<dt class="property" id="cause">
<a href="../routing/ViolatedRestriction/cause.html">/sdk-for-flutter-explore-routing-violatedrestriction-cause</a>
↔ String
</dt>
<dd>
  Cause of the notice. Human readable description of the notice, for example "Route violates vehicle restriction". It will be EN-US text only.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property" id="details">
<a href="../routing/ViolatedRestriction/details.html">/sdk-for-flutter-explore-routing-violatedrestriction-details</a>
↔ <a href="../routing/ViolatedRestrictionDetails-class.html">/sdk-for-flutter-explore-routing-violatedrestrictiondetails-class</a>?
</dt>
<dd>
  The detailed information of restriction depending on the specific violation.
For time dependent restriction or transport mode restriction, this property will be null.
For vehicle restriction, the corresponding member will be set, for example, if the vehicle violates the maximum
allowed gross weight for a specific route, the max_gross_weight_in_kilograms will be set with the maximum allowed
gross weight for this route.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property" id="hashCode">
<a href="../routing/ViolatedRestriction/hashCode.html">/sdk-for-flutter-explore-routing-violatedrestriction-hashcode</a>
→ int
</dt>
<dd>
  The hash code for this object.
  <div class="features">no setter</div>
</dd>
<dt class="property inherited" id="runtimeType">
<a href="../routing/ViolatedRestriction/runtimeType.html">/sdk-for-flutter-explore-routing-violatedrestriction-runtimetype</a>
→ Type
</dt>
<dd class="inherited">
  A representation of the runtime type of the object.
  <div class="features">no setterinherited</div>
</dd>
<dt class="property" id="timeDependent">
<a href="../routing/ViolatedRestriction/timeDependent.html">/sdk-for-flutter-explore-routing-violatedrestriction-timedependent</a>
↔ bool
</dt>
<dd>
  Indicates that restriction depends on time.
  <div class="features">getter/setter pair</div>
</dd>
</dl>
</section>
<section class="summary offset-anchor inherited" id="instance-methods">
<h2>Methods</h2>
<dl class="callables">
<dt class="callable inherited" id="noSuchMethod">
<a href="../routing/ViolatedRestriction/noSuchMethod.html">/sdk-for-flutter-explore-routing-violatedrestriction-nosuchmethod</a>(<wbr/>Invocation invocation)
    → dynamic

</dt>
<dd class="inherited">
  Invoked when a nonexistent method or property is accessed.
  <div class="features">inherited</div>
</dd>
<dt class="callable inherited" id="toString">
<a href="../routing/ViolatedRestriction/toString.html">/sdk-for-flutter-explore-routing-violatedrestriction-tostring</a>(<wbr/>)
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
<a href="../routing/ViolatedRestriction/operator_equals.html">/sdk-for-flutter-explore-routing-violatedrestriction-operator-equals</a>(<wbr/>Object other)
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
<li class="self-crumb">ViolatedRestriction class</li>
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
