---
title: "ManeuverViewLaneAssistance class"
slug: "sdk-for-flutter-navigate-navigation-maneuverviewlaneassistance-class"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- ManeuverViewLaneAssistance-class.html -->
<div class="doc-with-sidebar"><div class="sidebar-nav"><ol>
<li class="section-title"><a href="navigation/ManeuverViewLaneAssistance-class.html#constructors">Constructors</a></li>
<li><a href="navigation/ManeuverViewLaneAssistance/ManeuverViewLaneAssistance.html">ManeuverViewLaneAssistance</a></li>
<li class="section-title">
<a href="navigation/ManeuverViewLaneAssistance-class.html#instance-properties">Properties</a>
</li>
<li><a href="navigation/ManeuverViewLaneAssistance/hashCode.html">hashCode</a></li>
<li><a href="navigation/ManeuverViewLaneAssistance/lanesForNextManeuver.html">lanesForNextManeuver</a></li>
<li><a href="navigation/ManeuverViewLaneAssistance/lanesForNextNextManeuver.html">lanesForNextNextManeuver</a></li>
<li class="inherited"><a href="navigation/ManeuverViewLaneAssistance/runtimeType.html">runtimeType</a></li>
<li class="section-title inherited"><a href="navigation/ManeuverViewLaneAssistance-class.html#instance-methods">Methods</a></li>
<li class="inherited"><a href="navigation/ManeuverViewLaneAssistance/noSuchMethod.html">noSuchMethod</a></li>
<li class="inherited"><a href="navigation/ManeuverViewLaneAssistance/toString.html">toString</a></li>
<li class="section-title"><a href="navigation/ManeuverViewLaneAssistance-class.html#operators">Operators</a></li>
<li><a href="navigation/ManeuverViewLaneAssistance/operator_equals.html">operator ==</a></li>
</ol></div><div class="doc-content">
<div id="overlay-under-drawer"></div>
<header id="title">
menu
<ol class="breadcrumbs gt-separated dark hidden-xs">
<li>/sdk-for-flutter-navigate</li>
<li>/sdk-for-flutter-navigate-navigation-navigation-library</li>
<li class="self-crumb">ManeuverViewLaneAssistance class</li>
</ol>
<div class="self-name">ManeuverViewLaneAssistance</div>
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
<div class="main-content" data-above-sidebar="navigation/navigation-library-sidebar.html" data-below-sidebar="navigation/ManeuverViewLaneAssistance-class-sidebar.html" id="dartdoc-main-content">
<div>
<h1>ManeuverViewLaneAssistance class</h1></div>
<section class="desc markdown">
<p>A class that provides lane assistance information for the next maneuver(s).</p>
<p>During turn-by-turn navigation lane assistance can help a driver to choose the recommended lanes
in order to complete the upcoming maneuvers.
The notifications are synchronized with the /sdk-for-flutter-navigate-navigation-eventtextlistener-class.
/sdk-for-flutter-navigate-navigation-eventtextlistener-class has 4 notification types for each maneuver:
Range, Reminder, Distance and Action.
Only the maneuver notification of type Distance will also notify a ManeuverViewLaneAssistance object
(e.g. "After 400 meters, turn right onto Invalidenstraße").
The notification will not be sent when other types of maneuver notification are given.
The notification will not be sent when no lane data is available.
During tracking mode, no notifications are delivered.
This ManeuverViewLaneAssistance information is valid until the next maneuver is reached.</p>
</section>
<section class="summary offset-anchor" id="constructors">
<h2>Constructors</h2>
<dl class="constructor-summary-list">
<dt class="callable" id="ManeuverViewLaneAssistance">
/sdk-for-flutter-navigate-navigation-maneuverviewlaneassistance-maneuverviewlaneassistance(List&lt;<wbr/>/sdk-for-flutter-navigate-navigation-lane-class&gt; lanesForNextManeuver, List&lt;<wbr/>/sdk-for-flutter-navigate-navigation-lane-class&gt; lanesForNextNextManeuver)
</dt>
<dd>
          Creates a new instance.
        </dd>
</dl>
</section>
<section class="summary offset-anchor" id="instance-properties">
<h2>Properties</h2>
<dl class="properties">
<dt class="property" id="hashCode">
/sdk-for-flutter-navigate-navigation-maneuverviewlaneassistance-hashcode
→ int
</dt>
<dd>
  The hash code for this object.
  <div class="features">no setter</div>
</dd>
<dt class="property" id="lanesForNextManeuver">
/sdk-for-flutter-navigate-navigation-maneuverviewlaneassistance-lanesfornextmaneuver
↔ List&lt;<wbr/>/sdk-for-flutter-navigate-navigation-lane-class&gt;
</dt>
<dd>
  A list of lanes on the current road that leads to the upcoming maneuver.
The lanes are sorted from left to right: The lane at index 0 represents the leftmost lane and
the last index represents the rightmost lane.
This is valid for both right-hand and left-hand driving countries.
Contraflow lanes are not included in the list.
The list is guaranteed to be non-empty.
/sdk-for-flutter-navigate-navigation-roadattributes-isrightdrivingside indicates if this is a left-hand driving country or not.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property" id="lanesForNextNextManeuver">
/sdk-for-flutter-navigate-navigation-maneuverviewlaneassistance-lanesfornextnextmaneuver
↔ List&lt;<wbr/>/sdk-for-flutter-navigate-navigation-lane-class&gt;
</dt>
<dd>
  A list of lanes on the road that leads to the maneuver after the upcoming maneuver.
The lanes are sorted from left to right: The lane at index 0 represents the leftmost lane and
the last index represents the rightmost lane.
This is valid for both right-hand and left-hand driving countries.
Contraflow lanes are not included in the list.
/sdk-for-flutter-navigate-navigation-roadattributes-isrightdrivingside indicates if this is a left-hand driving country or not.
By default, this list is empty. It will be filled when the next two maneuvers are too
close to each other, or when the next two maneuvers are roundabout maneuvers.
Note: This notification is delivered at the same time as the /sdk-for-flutter-navigate-navigation-maneuverviewlaneassistance-lanesfornextmaneuver.
There is no separate maneuver notification on the second maneuver when two maneuvers are
are too close to each other.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property inherited" id="runtimeType">
/sdk-for-flutter-navigate-navigation-maneuverviewlaneassistance-runtimetype
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
/sdk-for-flutter-navigate-navigation-maneuverviewlaneassistance-nosuchmethod(<wbr/>Invocation invocation)
    → dynamic

</dt>
<dd class="inherited">
  Invoked when a nonexistent method or property is accessed.
  <div class="features">inherited</div>
</dd>
<dt class="callable inherited" id="toString">
/sdk-for-flutter-navigate-navigation-maneuverviewlaneassistance-tostring(<wbr/>)
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
/sdk-for-flutter-navigate-navigation-maneuverviewlaneassistance-operator-equals(<wbr/>Object other)
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
<li class="self-crumb">ManeuverViewLaneAssistance class</li>
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
