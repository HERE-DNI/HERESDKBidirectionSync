---
title: "LaneDecreaseWarning class"
slug: "sdk-for-flutter-navigate-warner-lanedecreasewarning-class"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- LaneDecreaseWarning-class.html -->
<div class="doc-with-sidebar"><div class="sidebar-nav"><ol>
<li class="section-title"><a href="warner/LaneDecreaseWarning-class.html#constructors">Constructors</a></li>
<li><a href="warner/LaneDecreaseWarning/LaneDecreaseWarning.html">LaneDecreaseWarning</a></li>
<li class="section-title">
<a href="warner/LaneDecreaseWarning-class.html#instance-properties">Properties</a>
</li>
<li><a href="warner/LaneDecreaseWarning/distanceInMeters.html">distanceInMeters</a></li>
<li><a href="warner/LaneDecreaseWarning/distanceType.html">distanceType</a></li>
<li><a href="warner/LaneDecreaseWarning/hashCode.html">hashCode</a></li>
<li><a href="warner/LaneDecreaseWarning/id.html">id</a></li>
<li><a href="warner/LaneDecreaseWarning/lanesDecreasedFromLeft.html">lanesDecreasedFromLeft</a></li>
<li><a href="warner/LaneDecreaseWarning/lanesDecreasedFromRight.html">lanesDecreasedFromRight</a></li>
<li><a href="warner/LaneDecreaseWarning/newLaneNumber.html">newLaneNumber</a></li>
<li><a href="warner/LaneDecreaseWarning/previousLaneNumber.html">previousLaneNumber</a></li>
<li class="inherited"><a href="warner/LaneDecreaseWarning/runtimeType.html">runtimeType</a></li>
<li class="section-title inherited"><a href="warner/LaneDecreaseWarning-class.html#instance-methods">Methods</a></li>
<li class="inherited"><a href="warner/LaneDecreaseWarning/noSuchMethod.html">noSuchMethod</a></li>
<li class="inherited"><a href="warner/LaneDecreaseWarning/toString.html">toString</a></li>
<li class="section-title"><a href="warner/LaneDecreaseWarning-class.html#operators">Operators</a></li>
<li><a href="warner/LaneDecreaseWarning/operator_equals.html">operator ==</a></li>
</ol></div><div class="doc-content">
<div id="overlay-under-drawer"></div>
<header id="title">
menu
<ol class="breadcrumbs gt-separated dark hidden-xs">
<li>/sdk-for-flutter-navigate</li>
<li>/sdk-for-flutter-navigate-warner-warner-library</li>
<li class="self-crumb">LaneDecreaseWarning class</li>
</ol>
<div class="self-name">LaneDecreaseWarning</div>
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
<div class="main-content" data-above-sidebar="warner/warner-library-sidebar.html" data-below-sidebar="warner/LaneDecreaseWarning-class-sidebar.html" id="dartdoc-main-content">
<div>
<h1>LaneDecreaseWarning class</h1></div>
<section class="desc markdown">
<p>Represents a lane decrease warning that notifies about upcoming reductions in the number of available lanes.</p>
<p>Lane decrease warnings are generated when the road ahead has fewer lanes
than the previous road segment provided by <code>sdk.electronic_horizon.ElectronicHorizonEngine</code>,
requiring drivers to merge or change lanes.
Lane decrease is provided only on highways and motorways. It will not be provided for junctions,
when maneuver is given for the lane decrease situation or when the /sdk-for-flutter-navigate-navigation-trafficmergewarning-class
is provided. Special lanes (e.g. Bus lane, HOV) will only be included to the lane decrease warning generation
if the according options are set in /sdk-for-flutter-navigate-transport-transportspecification-class.</p>
<p><strong>Note:</strong> This is a beta release of this feature, so there could be a few bugs and unexpected
behaviors. Related APIs may change for new releases without a deprecation process.</p>
</section>
<section class="summary offset-anchor" id="constructors">
<h2>Constructors</h2>
<dl class="constructor-summary-list">
<dt class="callable" id="LaneDecreaseWarning">
/sdk-for-flutter-navigate-warner-lanedecreasewarning-lanedecreasewarning(double distanceInMeters, /sdk-for-flutter-navigate-navigation-distancetype distanceType)
</dt>
<dd>
</dd>
</dl>
</section>
<section class="summary offset-anchor" id="instance-properties">
<h2>Properties</h2>
<dl class="properties">
<dt class="property" id="distanceInMeters">
/sdk-for-flutter-navigate-warner-lanedecreasewarning-distanceinmeters
↔ double
</dt>
<dd>
  The distance from the current location to the Lane decrease event.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property" id="distanceType">
/sdk-for-flutter-navigate-warner-lanedecreasewarning-distancetype
↔ /sdk-for-flutter-navigate-navigation-distancetype
</dt>
<dd>
  Indicates if the specified event is ahead of the vehicle or has just passed by. If it is
ahead, then /sdk-for-flutter-navigate-warner-lanedecreasewarning-distanceinmeters is greater than 0.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property" id="hashCode">
/sdk-for-flutter-navigate-warner-lanedecreasewarning-hashcode
→ int
</dt>
<dd>
  The hash code for this object.
  <div class="features">no setter</div>
</dd>
<dt class="property" id="id">
/sdk-for-flutter-navigate-warner-lanedecreasewarning-id
↔ int
</dt>
<dd>
  Unique identifier for this lane decrease warning instance.
Each warning type (truck restrictions, speed warnings, etc.) maintains its own independent ID namespace.
Use this ID to track, update, or dismiss individual warning instances of this type.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property" id="lanesDecreasedFromLeft">
/sdk-for-flutter-navigate-warner-lanedecreasewarning-lanesdecreasedfromleft
↔ int?
</dt>
<dd>
  Number of lanes decreased on the left side of the road,
<code>null</code> if the left-side change is unknown or not applicable.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property" id="lanesDecreasedFromRight">
/sdk-for-flutter-navigate-warner-lanedecreasewarning-lanesdecreasedfromright
↔ int?
</dt>
<dd>
  Number of lanes decreased on the right side of the road,
<code>null</code> if the right-side change is unknown or not applicable.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property" id="newLaneNumber">
/sdk-for-flutter-navigate-warner-lanedecreasewarning-newlanenumber
↔ int
</dt>
<dd>
  Number of lanes after the lane decrease event.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property" id="previousLaneNumber">
/sdk-for-flutter-navigate-warner-lanedecreasewarning-previouslanenumber
↔ int
</dt>
<dd>
  Number of lanes before the lane decrease event.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property inherited" id="runtimeType">
/sdk-for-flutter-navigate-warner-lanedecreasewarning-runtimetype
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
/sdk-for-flutter-navigate-warner-lanedecreasewarning-nosuchmethod(<wbr/>Invocation invocation)
    → dynamic

</dt>
<dd class="inherited">
  Invoked when a nonexistent method or property is accessed.
  <div class="features">inherited</div>
</dd>
<dt class="callable inherited" id="toString">
/sdk-for-flutter-navigate-warner-lanedecreasewarning-tostring(<wbr/>)
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
/sdk-for-flutter-navigate-warner-lanedecreasewarning-operator-equals(<wbr/>Object other)
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
<li>/sdk-for-flutter-navigate-warner-warner-library</li>
<li class="self-crumb">LaneDecreaseWarning class</li>
</ol>
<h5>warner library</h5>
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
