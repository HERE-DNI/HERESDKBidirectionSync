---
title: "IndoorManeuver class abstract"
slug: "sdk-for-flutter-explore-routing-indoormaneuver-class"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- IndoorManeuver-class.html -->
<div class="doc-with-sidebar"><div class="sidebar-nav"><ol>
<li class="section-title"><a href="routing/IndoorManeuver-class.html#constructors">Constructors</a></li>
<li><a href="routing/IndoorManeuver/IndoorManeuver.html">IndoorManeuver</a></li>
<li class="section-title">
<a href="routing/IndoorManeuver-class.html#instance-properties">Properties</a>
</li>
<li><a href="routing/IndoorManeuver/action.html">action</a></li>
<li><a href="routing/IndoorManeuver/coordinate.html">coordinate</a></li>
<li><a href="routing/IndoorManeuver/duration.html">duration</a></li>
<li class="inherited"><a href="routing/IndoorManeuver/hashCode.html">hashCode</a></li>
<li><a href="routing/IndoorManeuver/indoorLevelChangeData.html">indoorLevelChangeData</a></li>
<li><a href="routing/IndoorManeuver/indoorSpaceData.html">indoorSpaceData</a></li>
<li><a href="routing/IndoorManeuver/lengthInMeters.html">lengthInMeters</a></li>
<li><a href="routing/IndoorManeuver/levelZIndex.html">levelZIndex</a></li>
<li><a href="routing/IndoorManeuver/offset.html">offset</a></li>
<li class="inherited"><a href="routing/IndoorManeuver/runtimeType.html">runtimeType</a></li>
<li><a href="routing/IndoorManeuver/sectionIndex.html">sectionIndex</a></li>
<li class="section-title inherited"><a href="routing/IndoorManeuver-class.html#instance-methods">Methods</a></li>
<li class="inherited"><a href="routing/IndoorManeuver/noSuchMethod.html">noSuchMethod</a></li>
<li class="inherited"><a href="routing/IndoorManeuver/toString.html">toString</a></li>
<li class="section-title inherited"><a href="routing/IndoorManeuver-class.html#operators">Operators</a></li>
<li class="inherited"><a href="routing/IndoorManeuver/operator_equals.html">operator ==</a></li>
</ol></div><div class="doc-content">
<div id="overlay-under-drawer"></div>
<header id="title">
menu
<ol class="breadcrumbs gt-separated dark hidden-xs">
<li>/sdk-for-flutter-explore</li>
<li>/sdk-for-flutter-explore-routing-routing-library</li>
<li class="self-crumb">IndoorManeuver class</li>
</ol>
<div class="self-name">IndoorManeuver</div>
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
<div class="main-content" data-above-sidebar="routing/routing-library-sidebar.html" data-below-sidebar="routing/IndoorManeuver-class-sidebar.html" id="dartdoc-main-content">
<div>
<h1>IndoorManeuver class abstract</h1></div>
<section class="desc markdown">
<p>Represents a maneuver within an indoor section.</p>
</section>
<section class="summary offset-anchor" id="constructors">
<h2>Constructors</h2>
<dl class="constructor-summary-list">
<dt class="callable" id="IndoorManeuver">
/sdk-for-flutter-explore-routing-indoormaneuver-indoormaneuver()
</dt>
<dd>
</dd>
</dl>
</section>
<section class="summary offset-anchor" id="instance-properties">
<h2>Properties</h2>
<dl class="properties">
<dt class="property" id="action">
/sdk-for-flutter-explore-routing-indoormaneuver-action
→ /sdk-for-flutter-explore-routing-indoormaneuveractions?
</dt>
<dd>
  The action type of this maneuver.
Gets the action type of this maneuver.
  <div class="features">no setter</div>
</dd>
<dt class="property" id="coordinate">
/sdk-for-flutter-explore-routing-indoormaneuver-coordinate
→ /sdk-for-flutter-explore-core-geocoordinates-class
</dt>
<dd>
  The geographic coordinates of this maneuver.
Gets the geographic coordinates of this maneuver.
  <div class="features">no setter</div>
</dd>
<dt class="property" id="duration">
/sdk-for-flutter-explore-routing-indoormaneuver-duration
→ Duration
</dt>
<dd>
  The duration to complete this maneuver.
Gets the duration to complete this maneuver.
  <div class="features">no setter</div>
</dd>
<dt class="property inherited" id="hashCode">
/sdk-for-flutter-explore-routing-indoormaneuver-hashcode
→ int
</dt>
<dd class="inherited">
  The hash code for this object.
  <div class="features">no setterinherited</div>
</dd>
<dt class="property" id="indoorLevelChangeData">
/sdk-for-flutter-explore-routing-indoormaneuver-indoorlevelchangedata
→ /sdk-for-flutter-explore-routing-indoorlevelchangedata-class?
</dt>
<dd>
  The level change data for this maneuver. This will be not null if the IndoorManeuverAction is LEVEL_CHANGE_ACTION.
Gets the level change data for this maneuver. This will be not null if the IndoorManeuverAction is LEVEL_CHANGE_ACTION.
  <div class="features">no setter</div>
</dd>
<dt class="property" id="indoorSpaceData">
/sdk-for-flutter-explore-routing-indoormaneuver-indoorspacedata
→ /sdk-for-flutter-explore-routing-indoorspacedata-class?
</dt>
<dd>
  The indoor space data for this maneuver. This will be not null if the IndoorManeuverAction is ENTER_ACTION or LEAVE_ACTION.
Gets the indoor space data for this maneuver. This will be not null if the IndoorManeuverAction is ENTER_ACTION or LEAVE_ACTION.
  <div class="features">no setter</div>
</dd>
<dt class="property" id="lengthInMeters">
/sdk-for-flutter-explore-routing-indoormaneuver-lengthinmeters
→ double
</dt>
<dd>
  The length of this maneuver in meters.
Gets the length of this maneuver in meters.
  <div class="features">no setter</div>
</dd>
<dt class="property" id="levelZIndex">
/sdk-for-flutter-explore-routing-indoormaneuver-levelzindex
→ int
</dt>
<dd>
  The vertical level index of this maneuver.
Gets the vertical level index of this maneuver.
  <div class="features">no setter</div>
</dd>
<dt class="property" id="offset">
/sdk-for-flutter-explore-routing-indoormaneuver-offset
→ int
</dt>
<dd>
  The offset of this maneuver from the start of the section.
Gets the offset of this maneuver from the start of the section.
  <div class="features">no setter</div>
</dd>
<dt class="property inherited" id="runtimeType">
/sdk-for-flutter-explore-routing-indoormaneuver-runtimetype
→ Type
</dt>
<dd class="inherited">
  A representation of the runtime type of the object.
  <div class="features">no setterinherited</div>
</dd>
<dt class="property" id="sectionIndex">
/sdk-for-flutter-explore-routing-indoormaneuver-sectionindex
→ int
</dt>
<dd>
  The section index this maneuver belongs to.
Gets the section index this maneuver belongs to.
  <div class="features">no setter</div>
</dd>
</dl>
</section>
<section class="summary offset-anchor inherited" id="instance-methods">
<h2>Methods</h2>
<dl class="callables">
<dt class="callable inherited" id="noSuchMethod">
/sdk-for-flutter-explore-routing-indoormaneuver-nosuchmethod(<wbr/>Invocation invocation)
    → dynamic

</dt>
<dd class="inherited">
  Invoked when a nonexistent method or property is accessed.
  <div class="features">inherited</div>
</dd>
<dt class="callable inherited" id="toString">
/sdk-for-flutter-explore-routing-indoormaneuver-tostring(<wbr/>)
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
/sdk-for-flutter-explore-routing-indoormaneuver-operator-equals(<wbr/>Object other)
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
<li>/sdk-for-flutter-explore</li>
<li>/sdk-for-flutter-explore-routing-routing-library</li>
<li class="self-crumb">IndoorManeuver class</li>
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
`
}</HTMLBlock>
