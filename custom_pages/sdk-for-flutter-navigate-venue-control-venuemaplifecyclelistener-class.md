---
title: "VenueMapLifecycleListener class abstract"
slug: "sdk-for-flutter-navigate-venue-control-venuemaplifecyclelistener-class"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- VenueMapLifecycleListener-class.html -->
<div class="doc-with-sidebar"><div class="sidebar-nav"><ol>
<li class="section-title"><a href="venue.control/VenueMapLifecycleListener-class.html#constructors">Constructors</a></li>
<li><a href="venue.control/VenueMapLifecycleListener/VenueMapLifecycleListener.html">VenueMapLifecycleListener</a></li>
<li class="section-title inherited">
<a href="venue.control/VenueMapLifecycleListener-class.html#instance-properties">Properties</a>
</li>
<li class="inherited"><a href="venue.control/VenueMapLifecycleListener/hashCode.html">hashCode</a></li>
<li class="inherited"><a href="venue.control/VenueMapLifecycleListener/runtimeType.html">runtimeType</a></li>
<li class="section-title"><a href="venue.control/VenueMapLifecycleListener-class.html#instance-methods">Methods</a></li>
<li class="inherited"><a href="venue.control/VenueMapLifecycleListener/noSuchMethod.html">noSuchMethod</a></li>
<li><a href="venue.control/VenueMapLifecycleListener/onVenueAdded.html">onVenueAdded</a></li>
<li><a href="venue.control/VenueMapLifecycleListener/onVenueRemoved.html">onVenueRemoved</a></li>
<li class="inherited"><a href="venue.control/VenueMapLifecycleListener/toString.html">toString</a></li>
<li class="section-title inherited"><a href="venue.control/VenueMapLifecycleListener-class.html#operators">Operators</a></li>
<li class="inherited"><a href="venue.control/VenueMapLifecycleListener/operator_equals.html">operator ==</a></li>
</ol></div><div class="doc-content">
<div id="overlay-under-drawer"></div>
<header id="title">
menu
<ol class="breadcrumbs gt-separated dark hidden-xs">
<li>/sdk-for-flutter-navigate</li>
<li>/sdk-for-flutter-navigate-venue-control-venue-control-library</li>
<li class="self-crumb">VenueMapLifecycleListener class</li>
</ol>
<div class="self-name">VenueMapLifecycleListener</div>
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
<div class="main-content" data-above-sidebar="venue.control/venue.control-library-sidebar.html" data-below-sidebar="venue.control/VenueMapLifecycleListener-class-sidebar.html" id="dartdoc-main-content">
<div>
<h1>VenueMapLifecycleListener class abstract</h1></div>
<section class="desc markdown">
<p>The abstract class for  for
the /sdk-for-flutter-navigate-venue-control-venue-class lifecycle events.</p>
<p>Use the /sdk-for-flutter-navigate-venue-control-venuemap-class
to add and remove the /sdk-for-flutter-navigate-venue-control-venuemaplifecyclelistener-class.</p>
</section>
<section class="summary offset-anchor" id="constructors">
<h2>Constructors</h2>
<dl class="constructor-summary-list">
<dt class="callable" id="VenueMapLifecycleListener">
/sdk-for-flutter-navigate-venue-control-venuemaplifecyclelistener-venuemaplifecyclelistener(void onVenueAddedLambda(/sdk-for-flutter-navigate-venue-control-venue-class), void onVenueRemovedLambda(String))
</dt>
<dd>
          The abstract class for  for
the /sdk-for-flutter-navigate-venue-control-venue-class lifecycle events.
            <div class="constructor-modifier features">factory</div>
</dd>
</dl>
</section>
<section class="summary offset-anchor inherited" id="instance-properties">
<h2>Properties</h2>
<dl class="properties">
<dt class="property inherited" id="hashCode">
/sdk-for-flutter-navigate-venue-control-venuemaplifecyclelistener-hashcode
→ int
</dt>
<dd class="inherited">
  The hash code for this object.
  <div class="features">no setterinherited</div>
</dd>
<dt class="property inherited" id="runtimeType">
/sdk-for-flutter-navigate-venue-control-venuemaplifecyclelistener-runtimetype
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
/sdk-for-flutter-navigate-venue-control-venuemaplifecyclelistener-nosuchmethod(<wbr/>Invocation invocation)
    → dynamic

</dt>
<dd class="inherited">
  Invoked when a nonexistent method or property is accessed.
  <div class="features">inherited</div>
</dd>
<dt class="callable" id="onVenueAdded">
/sdk-for-flutter-navigate-venue-control-venuemaplifecyclelistener-onvenueadded(<wbr/>/sdk-for-flutter-navigate-venue-control-venue-class venue)
    → void

</dt>
<dd>
  Indicates that a /sdk-for-flutter-navigate-venue-control-venue-class was added to the /sdk-for-flutter-navigate-venue-control-venuemap-class.
  

</dd>
<dt class="callable" id="onVenueRemoved">
/sdk-for-flutter-navigate-venue-control-venuemaplifecyclelistener-onvenueremoved(<wbr/>String venueIdentifier)
    → void

</dt>
<dd>
  Indicates that a /sdk-for-flutter-navigate-venue-control-venue-class was removed from the /sdk-for-flutter-navigate-venue-control-venuemap-class.
  

</dd>
<dt class="callable inherited" id="toString">
/sdk-for-flutter-navigate-venue-control-venuemaplifecyclelistener-tostring(<wbr/>)
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
/sdk-for-flutter-navigate-venue-control-venuemaplifecyclelistener-operator-equals(<wbr/>Object other)
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
<li>/sdk-for-flutter-navigate-venue-control-venue-control-library</li>
<li class="self-crumb">VenueMapLifecycleListener class</li>
</ol>
<h5>venue.control library</h5>
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
