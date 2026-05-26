---
title: "Maneuver class abstract"
slug: "sdk-for-flutter-explore-routing-maneuver-class"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- Maneuver-class.html -->
<div class="doc-with-sidebar"><div class="sidebar-nav"><ol>
<li class="section-title"><a href="routing/Maneuver-class.html#constructors">Constructors</a></li>
<li><a href="routing/Maneuver/Maneuver.html">Maneuver</a></li>
<li class="section-title">
<a href="routing/Maneuver-class.html#instance-properties">Properties</a>
</li>
<li><a href="routing/Maneuver/action.html">action</a></li>
<li><a href="routing/Maneuver/coordinates.html">coordinates</a></li>
<li><a href="routing/Maneuver/countryCode.html">countryCode</a></li>
<li><a href="routing/Maneuver/duration.html">duration</a></li>
<li><a href="routing/Maneuver/exitSignTexts.html">exitSignTexts</a></li>
<li class="inherited"><a href="routing/Maneuver/hashCode.html">hashCode</a></li>
<li><a href="routing/Maneuver/intersectionNames.html">intersectionNames</a></li>
<li><a href="routing/Maneuver/lengthInMeters.html">lengthInMeters</a></li>
<li><a href="routing/Maneuver/nextRoadTexts.html">nextRoadTexts</a></li>
<li><a href="routing/Maneuver/offset.html">offset</a></li>
<li><a href="routing/Maneuver/roadTexts.html">roadTexts</a></li>
<li><a href="routing/Maneuver/roundaboutAngleInDegrees.html">roundaboutAngleInDegrees</a></li>
<li class="inherited"><a href="routing/Maneuver/runtimeType.html">runtimeType</a></li>
<li><a href="routing/Maneuver/sectionIndex.html">sectionIndex</a></li>
<li><a href="routing/Maneuver/signpost.html">signpost</a></li>
<li><a href="routing/Maneuver/spanIndex.html">spanIndex</a></li>
<li><a href="routing/Maneuver/text.html">text</a></li>
<li><a href="routing/Maneuver/turnAngleInDegrees.html">turnAngleInDegrees</a></li>
<li class="section-title inherited"><a href="routing/Maneuver-class.html#instance-methods">Methods</a></li>
<li class="inherited"><a href="routing/Maneuver/noSuchMethod.html">noSuchMethod</a></li>
<li class="inherited"><a href="routing/Maneuver/toString.html">toString</a></li>
<li class="section-title inherited"><a href="routing/Maneuver-class.html#operators">Operators</a></li>
<li class="inherited"><a href="routing/Maneuver/operator_equals.html">operator ==</a></li>
</ol></div><div class="doc-content">
<div id="overlay-under-drawer"></div>
<header id="title">
menu
<ol class="breadcrumbs gt-separated dark hidden-xs">
<li>/sdk-for-flutter-explore</li>
<li>/sdk-for-flutter-explore-routing-routing-library</li>
<li class="self-crumb">Maneuver class</li>
</ol>
<div class="self-name">Maneuver</div>
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
<div class="main-content" data-above-sidebar="routing/routing-library-sidebar.html" data-below-sidebar="routing/Maneuver-class-sidebar.html" id="dartdoc-main-content">
<div>
<h1>Maneuver class abstract</h1></div>
<section class="desc markdown">
<p>This class provides all the information for a maneuver.</p>
<p>The directional information (e.g. road names, road
numbers and signpost direction) is stored in /sdk-for-flutter-explore-routing-maneuver-roadtexts and /sdk-for-flutter-explore-routing-maneuver-nextroadtexts attributes.
As for the motorway exit information, it can be obtained from /sdk-for-flutter-explore-routing-maneuver-exitsigntexts attribute.</p>
</section>
<section class="summary offset-anchor" id="constructors">
<h2>Constructors</h2>
<dl class="constructor-summary-list">
<dt class="callable" id="Maneuver">
/sdk-for-flutter-explore-routing-maneuver-maneuver()
</dt>
<dd>
</dd>
</dl>
</section>
<section class="summary offset-anchor" id="instance-properties">
<h2>Properties</h2>
<dl class="properties">
<dt class="property" id="action">
/sdk-for-flutter-explore-routing-maneuver-action
→ /sdk-for-flutter-explore-routing-maneuveraction
</dt>
<dd>
  Indicates the maneuver action.
Gets the maneuver action.
  <div class="features">no setter</div>
</dd>
<dt class="property" id="coordinates">
/sdk-for-flutter-explore-routing-maneuver-coordinates
→ /sdk-for-flutter-explore-core-geocoordinates-class
</dt>
<dd>
  Geographic coordinates where the maneuver is located.
Gets the geographic coordinates where the maneuver is located.
  <div class="features">no setter</div>
</dd>
<dt class="property" id="countryCode">
/sdk-for-flutter-explore-routing-maneuver-countrycode
→ String?
</dt>
<dd>
  The country code of the maneuver position. The value is <code>null</code> when no data is available.
Gets the country code of the maneuver position. The value is <code>null</code> when no data is available.
  <div class="features">no setter</div>
</dd>
<dt class="property" id="duration">
/sdk-for-flutter-explore-routing-maneuver-duration
→ Duration
</dt>
<dd>
  The estimated time in seconds needed to perform the maneuver.
Gets the estimated time in seconds needed to perform the maneuver.
  <div class="features">no setter</div>
</dd>
<dt class="property" id="exitSignTexts">
/sdk-for-flutter-explore-routing-maneuver-exitsigntexts
→ /sdk-for-flutter-explore-core-localizedtexts-class
</dt>
<dd>
  The textual attributes of the exit sign. These might contain exit number(s) and/or name(s).
These attributes are only available for the Navigate license.
Otherwise, the attributes are always empty.
Gets the textual attributes of the exit sign. These might contain exit number(s) and/or name(s).
  <div class="features">no setter</div>
</dd>
<dt class="property inherited" id="hashCode">
/sdk-for-flutter-explore-routing-maneuver-hashcode
→ int
</dt>
<dd class="inherited">
  The hash code for this object.
  <div class="features">no setterinherited</div>
</dd>
<dt class="property" id="intersectionNames">
/sdk-for-flutter-explore-routing-maneuver-intersectionnames
→ /sdk-for-flutter-explore-core-localizedtexts-class
</dt>
<dd>
  The textual attributes of the intersection.
These attributes are only available for the Navigate license.
Otherwise, the attributes are always empty.
<strong>Note:</strong> Routes calculated with OfflineRoutingEngine are not supported.
Gets the textual attributes of the intersection.
  <div class="features">no setter</div>
</dd>
<dt class="property" id="lengthInMeters">
/sdk-for-flutter-explore-routing-maneuver-lengthinmeters
→ int
</dt>
<dd>
  The length of the maneuver in meters.
Gets the length of the maneuver in meters.
  <div class="features">no setter</div>
</dd>
<dt class="property" id="nextRoadTexts">
/sdk-for-flutter-explore-routing-maneuver-nextroadtexts
→ /sdk-for-flutter-explore-routing-roadtexts-class
</dt>
<dd>
  The textual attributes of the next road containing the corresponding road name(s) and road number(s) after the maneuver point.
These attributes are only available for the Navigate license.
Otherwise, the attributes are always empty.
Gets the textual attributes of the next road containing the corresponding road name(s) and road number(s) after the maneuver point.
  <div class="features">no setter</div>
</dd>
<dt class="property" id="offset">
/sdk-for-flutter-explore-routing-maneuver-offset
→ int
</dt>
<dd>
  Index over /sdk-for-flutter-explore-routing-section-geometry where the maneuver is located.
Gets the index over /sdk-for-flutter-explore-routing-section-geometry where the maneuver is located.
  <div class="features">no setter</div>
</dd>
<dt class="property" id="roadTexts">
/sdk-for-flutter-explore-routing-maneuver-roadtexts
→ /sdk-for-flutter-explore-routing-roadtexts-class
</dt>
<dd>
  The textual attributes of the current road containing road names, road numbers and signpost direction (towards) information.
<strong>Note:</strong> These attributes are only available for the Navigate license.
Otherwise, the attributes are always empty.
Gets the textual attributes of the current road containing road names, road numbers and signpost direction (towards) information.
  <div class="features">no setter</div>
</dd>
<dt class="property" id="roundaboutAngleInDegrees">
/sdk-for-flutter-explore-routing-maneuver-roundaboutangleindegrees
→ double?
</dt>
<dd>
  The angle is estimated between the incoming and outgoing route parts before entering the actual roundabout.
This is done to provide a better orientation for drivers. For better results, the incoming and outcoming route
parts can be around 50 meters in length. In addition, these parts lie usually around 30 meters away from
the actual roundabout. Therefore, the resulting arc does not necessarily represent the exact curved path a
vehicle has to follow within a roundabout from the point of entry to the point of exit. Instead, it reflects
the route path before and after the roundabout to highlight the directional change along the route. The angle can have a value from -360.0 to 360.0, and it is positive
in right-hand side driving country, and negative in left-hand side countries.
Note that the value is available for both the enter roundabout actions and the exit roundabout
actions. Both maneuvers have the same value. When the incoming or outgoing route parts are curvy or when the
roundabout itself is not representing a perfect circle, then the accuracy of the angle may be
compromised.
<strong>Note:</strong> These attributes are only available for the Navigate license.
The angle is estimated between the incoming and outgoing route parts before entering the actual roundabout.
  <div class="features">no setter</div>
</dd>
<dt class="property inherited" id="runtimeType">
/sdk-for-flutter-explore-routing-maneuver-runtimetype
→ Type
</dt>
<dd class="inherited">
  A representation of the runtime type of the object.
  <div class="features">no setterinherited</div>
</dd>
<dt class="property" id="sectionIndex">
/sdk-for-flutter-explore-routing-maneuver-sectionindex
→ int
</dt>
<dd>
  Index over /sdk-for-flutter-explore-routing-route-sections indicating the section to which the maneuver belongs to.
Gets the index over /sdk-for-flutter-explore-routing-route-sections indicating the section to which the maneuver belongs to.
  <div class="features">no setter</div>
</dd>
<dt class="property" id="signpost">
/sdk-for-flutter-explore-routing-maneuver-signpost
→ /sdk-for-flutter-explore-routing-signpost-class?
</dt>
<dd>
  Gets the /sdk-for-flutter-explore-routing-signpost-class object.
Gets /sdk-for-flutter-explore-routing-signpost-class object.
  <div class="features">no setter</div>
</dd>
<dt class="property" id="spanIndex">
/sdk-for-flutter-explore-routing-maneuver-spanindex
→ int
</dt>
<dd>
  Index over /sdk-for-flutter-explore-routing-section-spans indicating the first span after the maneuver point.
<strong>Note:</strong> The span index for the last maneuvers (those maneuvers with maneuver action set to
/sdk-for-flutter-explore-routing-maneuveraction) cannot be used, since these maneuvers are placed after the last span of the route and
the span index for them would be greater than the span list size.
Gets the index over /sdk-for-flutter-explore-routing-section-spans indicating the first span after the maneuver point.
  <div class="features">no setter</div>
</dd>
<dt class="property" id="text">
/sdk-for-flutter-explore-routing-maneuver-text
→ String
</dt>
<dd>
  The maneuver instruction. The text is formatted and localized as specified via
/sdk-for-flutter-explore-routing-routetextoptions-class.
<strong>Note for users of the Navigate license:</strong> This text is meant to be displayed in a preview context, whereas real-time <code>EventTextListener</code> texts are meant to be used
for spoken voice announcements during a trip.
Gets the maneuver instruction. The text is formatted and localized as specified via
/sdk-for-flutter-explore-routing-routetextoptions-class.
  <div class="features">no setter</div>
</dd>
<dt class="property" id="turnAngleInDegrees">
/sdk-for-flutter-explore-routing-maneuver-turnangleindegrees
→ double?
</dt>
<dd>
  The angle of the turn component of the maneuver.
The angle increases clockwise and small values are used for going straight, i.e. a positive number
means there is a right turn and a negative number is a left turn.
Some maneuvers like Depart, Arrive and Roundabout pass doesn't have a well defined angle, so the value
is omitted.
<strong>Note:</strong> These attributes are only available for the Navigate license.
Gets the angle of the turn component of the maneuver. The value is in degrees and from -180 to 180.
  <div class="features">no setter</div>
</dd>
</dl>
</section>
<section class="summary offset-anchor inherited" id="instance-methods">
<h2>Methods</h2>
<dl class="callables">
<dt class="callable inherited" id="noSuchMethod">
/sdk-for-flutter-explore-routing-maneuver-nosuchmethod(<wbr/>Invocation invocation)
    → dynamic

</dt>
<dd class="inherited">
  Invoked when a nonexistent method or property is accessed.
  <div class="features">inherited</div>
</dd>
<dt class="callable inherited" id="toString">
/sdk-for-flutter-explore-routing-maneuver-tostring(<wbr/>)
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
/sdk-for-flutter-explore-routing-maneuver-operator-equals(<wbr/>Object other)
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
<li class="self-crumb">Maneuver class</li>
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
