---
title: "Untitled"
slug: "sdk-for-flutter-navigate-routing-violatedrestriction-class"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- ViolatedRestriction-class.html -->

<div id="overlay-under-drawer"></div>
<header id="title">
menu
<ol class="breadcrumbs gt-separated dark hidden-xs">
<li>/sdk-for-flutter-navigate</li>
<li>/sdk-for-flutter-navigate-routing-routing-library</li>
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
/sdk-for-flutter-navigate-routing-violatedrestriction-violatedrestriction(String cause, bool timeDependent)
</dt>
<dd>
</dd>
</dl>
</section>
<section class="summary offset-anchor" id="instance-properties">
<h2>Properties</h2>
<dl class="properties">
<dt class="property" id="cause">
/sdk-for-flutter-navigate-routing-violatedrestriction-cause
↔ String
</dt>
<dd>
  Cause of the notice. Human readable description of the notice, for example "Route violates vehicle restriction". It will be EN-US text only.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property" id="details">
/sdk-for-flutter-navigate-routing-violatedrestriction-details
↔ /sdk-for-flutter-navigate-routing-violatedrestrictiondetails-class?
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
/sdk-for-flutter-navigate-routing-violatedrestriction-hashcode
→ int
</dt>
<dd>
  The hash code for this object.
  <div class="features">no setter</div>
</dd>
<dt class="property inherited" id="runtimeType">
/sdk-for-flutter-navigate-routing-violatedrestriction-runtimetype
→ Type
</dt>
<dd class="inherited">
  A representation of the runtime type of the object.
  <div class="features">no setterinherited</div>
</dd>
<dt class="property" id="timeDependent">
/sdk-for-flutter-navigate-routing-violatedrestriction-timedependent
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
/sdk-for-flutter-navigate-routing-violatedrestriction-nosuchmethod(<wbr/>Invocation invocation)
    → dynamic

</dt>
<dd class="inherited">
  Invoked when a nonexistent method or property is accessed.
  <div class="features">inherited</div>
</dd>
<dt class="callable inherited" id="toString">
/sdk-for-flutter-navigate-routing-violatedrestriction-tostring(<wbr/>)
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
/sdk-for-flutter-navigate-routing-violatedrestriction-operator-equals(<wbr/>Object other)
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
<li>/sdk-for-flutter-navigate-routing-routing-library</li>
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



</div>
`
}</HTMLBlock>
