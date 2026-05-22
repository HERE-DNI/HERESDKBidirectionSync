---
title: "Untitled"
slug: "sdk-for-flutter-navigate-navigation-railwaycrossingwarninglistener-class"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- RailwayCrossingWarningListener-class.html -->

<div id="overlay-under-drawer"></div>
<header id="title">
menu
<ol class="breadcrumbs gt-separated dark hidden-xs">
<li>/sdk-for-flutter-navigate</li>
<li>/sdk-for-flutter-navigate-navigation-navigation-library</li>
<li class="self-crumb">RailwayCrossingWarningListener class</li>
</ol>
<div class="self-name">RailwayCrossingWarningListener</div>
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
<div class="main-content" data-above-sidebar="navigation/navigation-library-sidebar.html" data-below-sidebar="navigation/RailwayCrossingWarningListener-class-sidebar.html" id="dartdoc-main-content">
<div>
<h1>RailwayCrossingWarningListener class abstract</h1></div>
<section class="desc markdown">
<p>This abstract class
should be implemented in order to receive railway crossing warnings.</p>
<p><strong>Note:</strong> The railway crossing warner can be either a zone warner or a point warner, depending
on whether the railroad crossing warning is given for a railroad crossing zone or just a point. This
means that for a railway crossing there will can be either 2 or 3 warnings emitted. In case the railroad
crossing is a zone warner then 3 warnings will be emitted with the <code>RailwayCrossingWarning.distance_type</code> set to <code>DistanceType.AHEAD</code>,
<code>DistanceType.REACHED</code> and lastly <code>DistanceType.PASSED</code> when the end of the railway crossing is passed. In
case the railroad crossing is a point warner then 2 warnings will be emitted with the <code>RailwayCrossingWarning.distance_type</code>
set to <code>DistanceType.AHEAD</code> and <code>DistanceType.PASSED</code> when the end of the railway crossing is passed.</p>
</section>
<section class="summary offset-anchor" id="constructors">
<h2>Constructors</h2>
<dl class="constructor-summary-list">
<dt class="callable" id="RailwayCrossingWarningListener">
/sdk-for-flutter-navigate-navigation-railwaycrossingwarninglistener-railwaycrossingwarninglistener(void onRailwayCrossingWarningUpdatedLambda(/sdk-for-flutter-navigate-navigation-railwaycrossingwarning-class))
</dt>
<dd>
          This abstract class
should be implemented in order to receive railway crossing warnings.
            <div class="constructor-modifier features">factory</div>
</dd>
</dl>
</section>
<section class="summary offset-anchor inherited" id="instance-properties">
<h2>Properties</h2>
<dl class="properties">
<dt class="property inherited" id="hashCode">
/sdk-for-flutter-navigate-navigation-railwaycrossingwarninglistener-hashcode
→ int
</dt>
<dd class="inherited">
  The hash code for this object.
  <div class="features">no setterinherited</div>
</dd>
<dt class="property inherited" id="runtimeType">
/sdk-for-flutter-navigate-navigation-railwaycrossingwarninglistener-runtimetype
→ Type
</dt>
<dd class="inherited">
  A representation of the runtime type of the object.
  <div class="features">no setterinherited</div>
</dd>
</dl>
</section>
<section class="summary offset-anchor" id="instance-methods">
<h2>Methods</h2>
<dl class="callables">
<dt class="callable inherited" id="noSuchMethod">
/sdk-for-flutter-navigate-navigation-railwaycrossingwarninglistener-nosuchmethod(<wbr/>Invocation invocation)
    → dynamic

</dt>
<dd class="inherited">
  Invoked when a nonexistent method or property is accessed.
  <div class="features">inherited</div>
</dd>
<dt class="callable" id="onRailwayCrossingWarningUpdated">
/sdk-for-flutter-navigate-navigation-railwaycrossingwarninglistener-onrailwaycrossingwarningupdated(<wbr/>/sdk-for-flutter-navigate-navigation-railwaycrossingwarning-class railwayCrossingWarning)
    → void

</dt>
<dd>
  Called whenever a new railway crossing warning is available.
  

</dd>
<dt class="callable inherited" id="toString">
/sdk-for-flutter-navigate-navigation-railwaycrossingwarninglistener-tostring(<wbr/>)
    → String

</dt>
<dd class="inherited">
  A string representation of this object.
  <div class="features">inherited</div>
</dd>
</dl>
</section>
<section class="summary offset-anchor inherited" id="operators">
<h2>Operators</h2>
<dl class="callables">
<dt class="callable inherited" id="operator ==">
/sdk-for-flutter-navigate-navigation-railwaycrossingwarninglistener-operator-equals(<wbr/>Object other)
    → bool

</dt>
<dd class="inherited">
  The equality operator.
  <div class="features">inherited</div>
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
<li class="self-crumb">RailwayCrossingWarningListener class</li>
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



</div>
`
}</HTMLBlock>
