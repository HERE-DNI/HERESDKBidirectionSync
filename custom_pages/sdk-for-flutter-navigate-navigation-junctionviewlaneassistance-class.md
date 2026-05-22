---
title: "Untitled"
slug: "sdk-for-flutter-navigate-navigation-junctionviewlaneassistance-class"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- JunctionViewLaneAssistance-class.html -->

<div id="overlay-under-drawer"></div>
<header id="title">
menu
<ol class="breadcrumbs gt-separated dark hidden-xs">
<li>/sdk-for-flutter-navigate</li>
<li>/sdk-for-flutter-navigate-navigation-navigation-library</li>
<li class="self-crumb">JunctionViewLaneAssistance class</li>
</ol>
<div class="self-name">JunctionViewLaneAssistance</div>
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
<div class="main-content" data-above-sidebar="navigation/navigation-library-sidebar.html" data-below-sidebar="navigation/JunctionViewLaneAssistance-class-sidebar.html" id="dartdoc-main-content">
<div>
<h1>JunctionViewLaneAssistance class</h1></div>
<section class="desc markdown">
<p>A class that provides lane assistance information for the next complex junction
in order to keep following the route.</p>
<p>It is recommended to indicate /sdk-for-flutter-navigate-navigation-junctionviewlaneassistance-class
and /sdk-for-flutter-navigate-navigation-maneuverviewlaneassistance-class separately or to indicate only /sdk-for-flutter-navigate-navigation-maneuverviewlaneassistance-class information -
/sdk-for-flutter-navigate-navigation-junctionviewlaneassistance-class will recommend all lanes that allow to pass the upcoming complex junction, regardless
if they will lead to the next maneuver or not.
If the location of a maneuver lies on an upcoming complex junction, the recommended lanes will be
the same as the ones from /sdk-for-flutter-navigate-navigation-maneuverviewlaneassistance-class.</p>
<p>A junction is recognized as complex only if:</p>
<ul>
<li>it is at least a bifurcation;</li>
<li>it has at least two lanes whose directions do not follow the current route.
In opposition to /sdk-for-flutter-navigate-navigation-maneuverviewlaneassistance-class, notifications are also forwarded when there is
no maneuver action occurring at the next complex junction.
Therefore, /sdk-for-flutter-navigate-navigation-junctionviewlaneassistance-class can be disjointed from maneuvers. If lane assistance should be used to
associate it with upcoming maneuvers, consider to use /sdk-for-flutter-navigate-navigation-maneuverviewlaneassistance-class instead.
Note that /sdk-for-flutter-navigate-navigation-maneuverviewlaneassistance-class notifications are synchronized with maneuver events,
whereas /sdk-for-flutter-navigate-navigation-junctionviewlaneassistance-class events are not strictly synchronized with maneuver events.</li>
</ul>
</section>
<section class="summary offset-anchor" id="constructors">
<h2>Constructors</h2>
<dl class="constructor-summary-list">
<dt class="callable" id="JunctionViewLaneAssistance">
/sdk-for-flutter-navigate-navigation-junctionviewlaneassistance-junctionviewlaneassistance(List&lt;<wbr/>/sdk-for-flutter-navigate-navigation-lane-class&gt; lanesForNextJunction, double distanceToJunctionInMeters)
</dt>
<dd>
          Creates a new instance.
        </dd>
</dl>
</section>
<section class="summary offset-anchor" id="instance-properties">
<h2>Properties</h2>
<dl class="properties">
<dt class="property" id="distanceToJunctionInMeters">
/sdk-for-flutter-navigate-navigation-junctionviewlaneassistance-distancetojunctioninmeters
↔ double
</dt>
<dd>
  Distance to the next complex junction in meters.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property" id="hashCode">
/sdk-for-flutter-navigate-navigation-junctionviewlaneassistance-hashcode
→ int
</dt>
<dd>
  The hash code for this object.
  <div class="features">no setter</div>
</dd>
<dt class="property" id="lanesForNextJunction">
/sdk-for-flutter-navigate-navigation-junctionviewlaneassistance-lanesfornextjunction
↔ List&lt;<wbr/>/sdk-for-flutter-navigate-navigation-lane-class&gt;
</dt>
<dd>
  A list of lanes on the next complex junction.
The lanes are sorted from left to right: The lane at index 0 represents the leftmost lane and
the last index represents the rightmost lane. This is valid for right-hand and left-hand driving
countries. An empty list means that the complex junction has been passed and that the lane information is not
valid anymore. Exactly one event with a non-empty list is delivered before reaching a complex junction and
one event with an empty list afterwards.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property inherited" id="runtimeType">
/sdk-for-flutter-navigate-navigation-junctionviewlaneassistance-runtimetype
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
/sdk-for-flutter-navigate-navigation-junctionviewlaneassistance-nosuchmethod(<wbr/>Invocation invocation)
    → dynamic

</dt>
<dd class="inherited">
  Invoked when a nonexistent method or property is accessed.
  <div class="features">inherited</div>
</dd>
<dt class="callable inherited" id="toString">
/sdk-for-flutter-navigate-navigation-junctionviewlaneassistance-tostring(<wbr/>)
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
/sdk-for-flutter-navigate-navigation-junctionviewlaneassistance-operator-equals(<wbr/>Object other)
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
<li class="self-crumb">JunctionViewLaneAssistance class</li>
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
