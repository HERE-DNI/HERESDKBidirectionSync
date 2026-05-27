---
title: "Constructors"
slug: "sdk-for-flutter-explore-routing-maneuver-class"
---

<HTMLBlock>
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
<li><a href="../index.html">/sdk-for-flutter-explore</a></li>
<li><a href="../routing/routing-library.html">/sdk-for-flutter-explore-routing-routing-library</a></li>
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
numbers and signpost direction) is stored in <a href="../routing/Maneuver/roadTexts.html">/sdk-for-flutter-explore-routing-maneuver-roadtexts</a> and <a href="../routing/Maneuver/nextRoadTexts.html">/sdk-for-flutter-explore-routing-maneuver-nextroadtexts</a> attributes.
As for the motorway exit information, it can be obtained from <a href="../routing/Maneuver/exitSignTexts.html">/sdk-for-flutter-explore-routing-maneuver-exitsigntexts</a> attribute.</p>
</section>
<section class="summary offset-anchor" id="constructors">
<h2>Constructors</h2>
<dl class="constructor-summary-list">
<dt class="callable" id="Maneuver">
<a href="../routing/Maneuver/Maneuver.html">/sdk-for-flutter-explore-routing-maneuver-maneuver</a>()
</dt>
<dd>
</dd>
</dl>
</section>
<section class="summary offset-anchor" id="instance-properties">
<h2>Properties</h2>
<dl class="properties">
<dt class="property" id="action">
<a href="../routing/Maneuver/action.html">/sdk-for-flutter-explore-routing-maneuver-action</a>
→ <a href="../routing/ManeuverAction.html">/sdk-for-flutter-explore-routing-maneuveraction</a>
</dt>
<dd>
  Indicates the maneuver action.
Gets the maneuver action.
  <div class="features">no setter</div>
</dd>
<dt class="property" id="coordinates">
<a href="../routing/Maneuver/coordinates.html">/sdk-for-flutter-explore-routing-maneuver-coordinates</a>
→ <a href="../core/GeoCoordinates-class.html">/sdk-for-flutter-explore-core-geocoordinates-class</a>
</dt>
<dd>
  Geographic coordinates where the maneuver is located.
Gets the geographic coordinates where the maneuver is located.
  <div class="features">no setter</div>
</dd>
<dt class="property" id="countryCode">
<a href="../routing/Maneuver/countryCode.html">/sdk-for-flutter-explore-routing-maneuver-countrycode</a>
→ String?
</dt>
<dd>
  The country code of the maneuver position. The value is <code>null</code> when no data is available.
Gets the country code of the maneuver position. The value is <code>null</code> when no data is available.
  <div class="features">no setter</div>
</dd>
<dt class="property" id="duration">
<a href="../routing/Maneuver/duration.html">/sdk-for-flutter-explore-routing-maneuver-duration</a>
→ Duration
</dt>
<dd>
  The estimated time in seconds needed to perform the maneuver.
Gets the estimated time in seconds needed to perform the maneuver.
  <div class="features">no setter</div>
</dd>
<dt class="property" id="exitSignTexts">
<a href="../routing/Maneuver/exitSignTexts.html">/sdk-for-flutter-explore-routing-maneuver-exitsigntexts</a>
→ <a href="../core/LocalizedTexts-class.html">/sdk-for-flutter-explore-core-localizedtexts-class</a>
</dt>
<dd>
  The textual attributes of the exit sign. These might contain exit number(s) and/or name(s).
These attributes are only available for the Navigate license.
Otherwise, the attributes are always empty.
Gets the textual attributes of the exit sign. These might contain exit number(s) and/or name(s).
  <div class="features">no setter</div>
</dd>
<dt class="property inherited" id="hashCode">
<a href="../routing/Maneuver/hashCode.html">/sdk-for-flutter-explore-routing-maneuver-hashcode</a>
→ int
</dt>
<dd class="inherited">
  The hash code for this object.
  <div class="features">no setterinherited</div>
</dd>
<dt class="property" id="intersectionNames">
<a href="../routing/Maneuver/intersectionNames.html">/sdk-for-flutter-explore-routing-maneuver-intersectionnames</a>
→ <a href="../core/LocalizedTexts-class.html">/sdk-for-flutter-explore-core-localizedtexts-class</a>
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
<a href="../routing/Maneuver/lengthInMeters.html">/sdk-for-flutter-explore-routing-maneuver-lengthinmeters</a>
→ int
</dt>
<dd>
  The length of the maneuver in meters.
Gets the length of the maneuver in meters.
  <div class="features">no setter</div>
</dd>
<dt class="property" id="nextRoadTexts">
<a href="../routing/Maneuver/nextRoadTexts.html">/sdk-for-flutter-explore-routing-maneuver-nextroadtexts</a>
→ <a href="../routing/RoadTexts-class.html">/sdk-for-flutter-explore-routing-roadtexts-class</a>
</dt>
<dd>
  The textual attributes of the next road containing the corresponding road name(s) and road number(s) after the maneuver point.
These attributes are only available for the Navigate license.
Otherwise, the attributes are always empty.
Gets the textual attributes of the next road containing the corresponding road name(s) and road number(s) after the maneuver point.
  <div class="features">no setter</div>
</dd>
<dt class="property" id="offset">
<a href="../routing/Maneuver/offset.html">/sdk-for-flutter-explore-routing-maneuver-offset</a>
→ int
</dt>
<dd>
  Index over <a href="../routing/Section/geometry.html">/sdk-for-flutter-explore-routing-section-geometry</a> where the maneuver is located.
Gets the index over <a href="../routing/Section/geometry.html">/sdk-for-flutter-explore-routing-section-geometry</a> where the maneuver is located.
  <div class="features">no setter</div>
</dd>
<dt class="property" id="roadTexts">
<a href="../routing/Maneuver/roadTexts.html">/sdk-for-flutter-explore-routing-maneuver-roadtexts</a>
→ <a href="../routing/RoadTexts-class.html">/sdk-for-flutter-explore-routing-roadtexts-class</a>
</dt>
<dd>
  The textual attributes of the current road containing road names, road numbers and signpost direction (towards) information.
<strong>Note:</strong> These attributes are only available for the Navigate license.
Otherwise, the attributes are always empty.
Gets the textual attributes of the current road containing road names, road numbers and signpost direction (towards) information.
  <div class="features">no setter</div>
</dd>
<dt class="property" id="roundaboutAngleInDegrees">
<a href="../routing/Maneuver/roundaboutAngleInDegrees.html">/sdk-for-flutter-explore-routing-maneuver-roundaboutangleindegrees</a>
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
<a href="../routing/Maneuver/runtimeType.html">/sdk-for-flutter-explore-routing-maneuver-runtimetype</a>
→ Type
</dt>
<dd class="inherited">
  A representation of the runtime type of the object.
  <div class="features">no setterinherited</div>
</dd>
<dt class="property" id="sectionIndex">
<a href="../routing/Maneuver/sectionIndex.html">/sdk-for-flutter-explore-routing-maneuver-sectionindex</a>
→ int
</dt>
<dd>
  Index over <a href="../routing/Route/sections.html">/sdk-for-flutter-explore-routing-route-sections</a> indicating the section to which the maneuver belongs to.
Gets the index over <a href="../routing/Route/sections.html">/sdk-for-flutter-explore-routing-route-sections</a> indicating the section to which the maneuver belongs to.
  <div class="features">no setter</div>
</dd>
<dt class="property" id="signpost">
<a href="../routing/Maneuver/signpost.html">/sdk-for-flutter-explore-routing-maneuver-signpost</a>
→ <a href="../routing/Signpost-class.html">/sdk-for-flutter-explore-routing-signpost-class</a>?
</dt>
<dd>
  Gets the <a href="../routing/Signpost-class.html">/sdk-for-flutter-explore-routing-signpost-class</a> object.
Gets <a href="../routing/Signpost-class.html">/sdk-for-flutter-explore-routing-signpost-class</a> object.
  <div class="features">no setter</div>
</dd>
<dt class="property" id="spanIndex">
<a href="../routing/Maneuver/spanIndex.html">/sdk-for-flutter-explore-routing-maneuver-spanindex</a>
→ int
</dt>
<dd>
  Index over <a href="../routing/Section/spans.html">/sdk-for-flutter-explore-routing-section-spans</a> indicating the first span after the maneuver point.
<strong>Note:</strong> The span index for the last maneuvers (those maneuvers with maneuver action set to
<a href="../routing/ManeuverAction.html">/sdk-for-flutter-explore-routing-maneuveraction</a>) cannot be used, since these maneuvers are placed after the last span of the route and
the span index for them would be greater than the span list size.
Gets the index over <a href="../routing/Section/spans.html">/sdk-for-flutter-explore-routing-section-spans</a> indicating the first span after the maneuver point.
  <div class="features">no setter</div>
</dd>
<dt class="property" id="text">
<a href="../routing/Maneuver/text.html">/sdk-for-flutter-explore-routing-maneuver-text</a>
→ String
</dt>
<dd>
  The maneuver instruction. The text is formatted and localized as specified via
<a href="../routing/RouteTextOptions-class.html">/sdk-for-flutter-explore-routing-routetextoptions-class</a>.
<strong>Note for users of the Navigate license:</strong> This text is meant to be displayed in a preview context, whereas real-time <code>EventTextListener</code> texts are meant to be used
for spoken voice announcements during a trip.
Gets the maneuver instruction. The text is formatted and localized as specified via
<a href="../routing/RouteTextOptions-class.html">/sdk-for-flutter-explore-routing-routetextoptions-class</a>.
  <div class="features">no setter</div>
</dd>
<dt class="property" id="turnAngleInDegrees">
<a href="../routing/Maneuver/turnAngleInDegrees.html">/sdk-for-flutter-explore-routing-maneuver-turnangleindegrees</a>
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
<a href="../routing/Maneuver/noSuchMethod.html">/sdk-for-flutter-explore-routing-maneuver-nosuchmethod</a>(<wbr/>Invocation invocation)
    → dynamic

</dt>
<dd class="inherited">
  Invoked when a nonexistent method or property is accessed.
  <div class="features">inherited</div>
</dd>
<dt class="callable inherited" id="toString">
<a href="../routing/Maneuver/toString.html">/sdk-for-flutter-explore-routing-maneuver-tostring</a>(<wbr/>)
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
<a href="../routing/Maneuver/operator_equals.html">/sdk-for-flutter-explore-routing-maneuver-operator-equals</a>(<wbr/>Object other)
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
<li><a href="../index.html">/sdk-for-flutter-explore</a></li>
<li><a href="../routing/routing-library.html">/sdk-for-flutter-explore-routing-routing-library</a></li>
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
</HTMLBlock>
