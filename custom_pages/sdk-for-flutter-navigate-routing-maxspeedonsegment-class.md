---
title: "Untitled"
slug: "sdk-for-flutter-navigate-routing-maxspeedonsegment-class"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- MaxSpeedOnSegment-class.html -->

<div id="overlay-under-drawer"></div>
<header id="title">
menu
<ol class="breadcrumbs gt-separated dark hidden-xs">
<li>/sdk-for-flutter-navigate</li>
<li>/sdk-for-flutter-navigate-routing-routing-library</li>
<li class="self-crumb">MaxSpeedOnSegment class</li>
</ol>
<div class="self-name">MaxSpeedOnSegment</div>
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
<div class="main-content" data-above-sidebar="routing/routing-library-sidebar.html" data-below-sidebar="routing/MaxSpeedOnSegment-class-sidebar.html" id="dartdoc-main-content">
<div>
<h1>MaxSpeedOnSegment class</h1></div>
<section class="desc markdown">
<p>New base speed for a segment.</p>
<p>Affects route calculation and the ETA. Cannot increase base speed on segment.</p>
<p><strong>Note:</strong> This option can only be used with the <code>RoutingEngine</code>. The <code>OfflineRoutingEngine</code> is not supported and the option will be ignored. Note that the <code>OfflineRoutingEngine</code> is only available for the Navigate license.</p>
</section>
<section class="summary offset-anchor" id="constructors">
<h2>Constructors</h2>
<dl class="constructor-summary-list">
<dt class="callable" id="MaxSpeedOnSegment">
/sdk-for-flutter-navigate-routing-maxspeedonsegment-maxspeedonsegment(/sdk-for-flutter-navigate-routing-segmentreference-class segment, double baseSpeedInMetersPerSecond)
</dt>
<dd>
          Creates a new instance.
        </dd>
</dl>
</section>
<section class="summary offset-anchor" id="instance-properties">
<h2>Properties</h2>
<dl class="properties">
<dt class="property" id="baseSpeedInMetersPerSecond">
/sdk-for-flutter-navigate-routing-maxspeedonsegment-basespeedinmeterspersecond
↔ double
</dt>
<dd>
  New maximum value in m/s of baseSpeed on segment.  The provided value must be in the range [1.0, 70.0].
Cannot increase base speed on segment. If the value is greater than the default base speed, then such penalty will have no effect.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property" id="hashCode">
/sdk-for-flutter-navigate-routing-maxspeedonsegment-hashcode
→ int
</dt>
<dd>
  The hash code for this object.
  <div class="features">no setter</div>
</dd>
<dt class="property inherited" id="runtimeType">
/sdk-for-flutter-navigate-routing-maxspeedonsegment-runtimetype
→ Type
</dt>
<dd class="inherited">
  A representation of the runtime type of the object.
  <div class="features">no setterinherited</div>
</dd>
<dt class="property" id="segment">
/sdk-for-flutter-navigate-routing-maxspeedonsegment-segment
↔ /sdk-for-flutter-navigate-routing-segmentreference-class
</dt>
<dd>
  A segment for which the new base speed is specified. Only the <code>segmendId</code> and <code>travelDirection</code>
parameters are used, other parameters are ignored. Setting a <code>segmendId</code> is mandatory.
  <div class="features">getter/setter pair</div>
</dd>
</dl>
</section>
<section class="summary offset-anchor inherited" id="instance-methods">
<h2>Methods</h2>
<dl class="callables">
<dt class="callable inherited" id="noSuchMethod">
/sdk-for-flutter-navigate-routing-maxspeedonsegment-nosuchmethod(<wbr/>Invocation invocation)
    → dynamic

</dt>
<dd class="inherited">
  Invoked when a nonexistent method or property is accessed.
  <div class="features">inherited</div>
</dd>
<dt class="callable inherited" id="toString">
/sdk-for-flutter-navigate-routing-maxspeedonsegment-tostring(<wbr/>)
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
/sdk-for-flutter-navigate-routing-maxspeedonsegment-operator-equals(<wbr/>Object other)
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
<li class="self-crumb">MaxSpeedOnSegment class</li>
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
