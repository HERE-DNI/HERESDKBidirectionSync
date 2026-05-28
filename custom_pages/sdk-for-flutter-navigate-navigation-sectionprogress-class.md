---
title: "SectionProgress class"
slug: "sdk-for-flutter-navigate-navigation-sectionprogress-class"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- SectionProgress-class.html -->
<div class="doc-with-sidebar"><div class="sidebar-nav"><ol>
<li class="section-title"><a href="navigation/SectionProgress-class.html#constructors">Constructors</a></li>
<li><a href="navigation/SectionProgress/SectionProgress.html">SectionProgress</a></li>
<li class="section-title">
<a href="navigation/SectionProgress-class.html#instance-properties">Properties</a>
</li>
<li><a href="navigation/SectionProgress/hashCode.html">hashCode</a></li>
<li><a href="navigation/SectionProgress/remainingDistanceInMeters.html">remainingDistanceInMeters</a></li>
<li><a href="navigation/SectionProgress/remainingDuration.html">remainingDuration</a></li>
<li class="inherited"><a href="navigation/SectionProgress/runtimeType.html">runtimeType</a></li>
<li><a href="navigation/SectionProgress/trafficDelay.html">trafficDelay</a></li>
<li class="section-title inherited"><a href="navigation/SectionProgress-class.html#instance-methods">Methods</a></li>
<li class="inherited"><a href="navigation/SectionProgress/noSuchMethod.html">noSuchMethod</a></li>
<li class="inherited"><a href="navigation/SectionProgress/toString.html">toString</a></li>
<li class="section-title"><a href="navigation/SectionProgress-class.html#operators">Operators</a></li>
<li><a href="navigation/SectionProgress/operator_equals.html">operator ==</a></li>
</ol></div><div class="doc-content">
<div id="overlay-under-drawer"></div>
<header id="title">
menu
<ol class="breadcrumbs gt-separated dark hidden-xs">
<li>/sdk-for-flutter-navigate</li>
<li>/sdk-for-flutter-navigate-navigation-navigation-library</li>
<li class="self-crumb">SectionProgress class</li>
</ol>
<div class="self-name">SectionProgress</div>
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
<div class="main-content" data-above-sidebar="navigation/navigation-library-sidebar.html" data-below-sidebar="navigation/SectionProgress-class-sidebar.html" id="dartdoc-main-content">
<div>
<h1>SectionProgress class</h1></div>
<section class="desc markdown">
<p>Indicates a user's progress along a /sdk-for-flutter-navigate-routing-section-class.</p>
</section>
<section class="summary offset-anchor" id="constructors">
<h2>Constructors</h2>
<dl class="constructor-summary-list">
<dt class="callable" id="SectionProgress">
/sdk-for-flutter-navigate-navigation-sectionprogress-sectionprogress()
</dt>
<dd>
</dd>
</dl>
</section>
<section class="summary offset-anchor" id="instance-properties">
<h2>Properties</h2>
<dl class="properties">
<dt class="property" id="hashCode">
/sdk-for-flutter-navigate-navigation-sectionprogress-hashcode
→ int
</dt>
<dd>
  The hash code for this object.
  <div class="features">no setter</div>
</dd>
<dt class="property" id="remainingDistanceInMeters">
/sdk-for-flutter-navigate-navigation-sectionprogress-remainingdistanceinmeters
↔ int
</dt>
<dd>
  The distance in meters from current location until the end of the /sdk-for-flutter-navigate-routing-section-class.
Note that the value is accumulated per section, and that the last section contains the overall
distance to the destination.
Defaults to 0.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property" id="remainingDuration">
/sdk-for-flutter-navigate-navigation-sectionprogress-remainingduration
↔ Duration
</dt>
<dd>
  The estimated time in seconds from current location until the end of the /sdk-for-flutter-navigate-routing-section-class
is reached, including traffic delays if available.
Note that the value is accumulated per section, and that the last section contains the overall
duration until the destination is reached.
Defaults to 0 seconds.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property inherited" id="runtimeType">
/sdk-for-flutter-navigate-navigation-sectionprogress-runtimetype
→ Type
</dt>
<dd class="inherited">
  A representation of the runtime type of the object.
  <div class="features">no setterinherited</div>
</dd>
<dt class="property" id="trafficDelay">
/sdk-for-flutter-navigate-navigation-sectionprogress-trafficdelay
↔ Duration
</dt>
<dd>
  The estimated traffic delay in seconds from current location until the end of the
/sdk-for-flutter-navigate-routing-section-class is reached.
Note that the value is accumulated per section, and that the last section contains the overall
traffic delay until the destination is reached. The delay might be a negative value:
Negative values indicate that the part of this section can be traversed faster than usual.
Note that this is based on a delay value received at the moment of route calculation.
Defaults to 0 seconds.
  <div class="features">getter/setter pair</div>
</dd>
</dl>
</section>
<section class="summary offset-anchor inherited" id="instance-methods">
<h2>Methods</h2>
<dl class="callables">
<dt class="callable inherited" id="noSuchMethod">
/sdk-for-flutter-navigate-navigation-sectionprogress-nosuchmethod(<wbr/>Invocation invocation)
    → dynamic

</dt>
<dd class="inherited">
  Invoked when a nonexistent method or property is accessed.
  <div class="features">inherited</div>
</dd>
<dt class="callable inherited" id="toString">
/sdk-for-flutter-navigate-navigation-sectionprogress-tostring(<wbr/>)
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
/sdk-for-flutter-navigate-navigation-sectionprogress-operator-equals(<wbr/>Object other)
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
<li>/sdk-for-flutter-navigate-navigation-navigation-library</li>
<li class="self-crumb">SectionProgress class</li>
</ol>
<h5>navigation library</h5>
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
