---
title: "RoadSignWarning class"
slug: "sdk-for-flutter-navigate-navigation-roadsignwarning-class"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- RoadSignWarning-class.html -->
<div class="doc-with-sidebar"><div class="sidebar-nav"><ol>
<li class="section-title"><a href="navigation/RoadSignWarning-class.html#constructors">Constructors</a></li>
<li><a href="navigation/RoadSignWarning/RoadSignWarning.html">RoadSignWarning</a></li>
<li class="section-title">
<a href="navigation/RoadSignWarning-class.html#instance-properties">Properties</a>
</li>
<li><a href="navigation/RoadSignWarning/category.html">category</a></li>
<li><a href="navigation/RoadSignWarning/distanceToRoadSignInMeters.html">distanceToRoadSignInMeters</a></li>
<li><a href="navigation/RoadSignWarning/distanceType.html">distanceType</a></li>
<li><a href="navigation/RoadSignWarning/duration.html">duration</a></li>
<li><a href="navigation/RoadSignWarning/generalWarningType.html">generalWarningType</a></li>
<li><a href="navigation/RoadSignWarning/hashCode.html">hashCode</a></li>
<li><a href="navigation/RoadSignWarning/id.html">id</a></li>
<li><a href="navigation/RoadSignWarning/isPrioritySign.html">isPrioritySign</a></li>
<li><a href="navigation/RoadSignWarning/preWarning.html">preWarning</a></li>
<li><a href="navigation/RoadSignWarning/roadSignSegment.html">roadSignSegment</a></li>
<li class="inherited"><a href="navigation/RoadSignWarning/runtimeType.html">runtimeType</a></li>
<li><a href="navigation/RoadSignWarning/signValue.html">signValue</a></li>
<li><a href="navigation/RoadSignWarning/type.html">type</a></li>
<li><a href="navigation/RoadSignWarning/validityTime.html">validityTime</a></li>
<li><a href="navigation/RoadSignWarning/vehicleTypes.html">vehicleTypes</a></li>
<li><a href="navigation/RoadSignWarning/weatherType.html">weatherType</a></li>
<li class="section-title inherited"><a href="navigation/RoadSignWarning-class.html#instance-methods">Methods</a></li>
<li class="inherited"><a href="navigation/RoadSignWarning/noSuchMethod.html">noSuchMethod</a></li>
<li class="inherited"><a href="navigation/RoadSignWarning/toString.html">toString</a></li>
<li class="section-title"><a href="navigation/RoadSignWarning-class.html#operators">Operators</a></li>
<li><a href="navigation/RoadSignWarning/operator_equals.html">operator ==</a></li>
</ol></div><div class="doc-content">
<div id="overlay-under-drawer"></div>
<header id="title">
menu
<ol class="breadcrumbs gt-separated dark hidden-xs">
<li>/sdk-for-flutter-navigate</li>
<li>/sdk-for-flutter-navigate-navigation-navigation-library</li>
<li class="self-crumb">RoadSignWarning class</li>
</ol>
<div class="self-name">RoadSignWarning</div>
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
<div class="main-content" data-above-sidebar="navigation/navigation-library-sidebar.html" data-below-sidebar="navigation/RoadSignWarning-class-sidebar.html" id="dartdoc-main-content">
<div>
<h1>RoadSignWarning class</h1></div>
<section class="desc markdown">
<p>A road sign.</p>
<p>The main field describing the sign is <code>RoadSignWarning.type</code>. Some road types are standardized, others can be country specific.
A valid road sign contains known <code>RoadSignWarning.type</code> or <code>RoadSignWarning.category</code>.
Use <code>RoadSignWarningListener</code> to get notifications with current road signs.</p>
</section>
<section class="summary offset-anchor" id="constructors">
<h2>Constructors</h2>
<dl class="constructor-summary-list">
<dt class="callable" id="RoadSignWarning">
/sdk-for-flutter-navigate-navigation-roadsignwarning-roadsignwarning(double distanceToRoadSignInMeters, /sdk-for-flutter-navigate-navigation-roadsigntype type, /sdk-for-flutter-navigate-navigation-roadsigncategory category, /sdk-for-flutter-navigate-navigation-generalwarningroadsigntype generalWarningType, bool isPrioritySign, List&lt;<wbr/>/sdk-for-flutter-navigate-navigation-roadsignvehicletype&gt; vehicleTypes, /sdk-for-flutter-navigate-navigation-weathertype weatherType, /sdk-for-flutter-navigate-routing-segmentreference-class roadSignSegment, /sdk-for-flutter-navigate-navigation-distancetype distanceType)
</dt>
<dd>
</dd>
</dl>
</section>
<section class="summary offset-anchor" id="instance-properties">
<h2>Properties</h2>
<dl class="properties">
<dt class="property" id="category">
/sdk-for-flutter-navigate-navigation-roadsignwarning-category
↔ /sdk-for-flutter-navigate-navigation-roadsigncategory
</dt>
<dd>
  The main category to which the road sign belongs.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property" id="distanceToRoadSignInMeters">
/sdk-for-flutter-navigate-navigation-roadsignwarning-distancetoroadsigninmeters
↔ double
</dt>
<dd>
  Distance to the road sign in meters.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property" id="distanceType">
/sdk-for-flutter-navigate-navigation-roadsignwarning-distancetype
↔ /sdk-for-flutter-navigate-navigation-distancetype
</dt>
<dd>
  The distance type for the warning, e.g. a warning for a new road sign ahead or a warning for
passing a road sign. Since the road sign warning is given relative to a single position on
the route, /sdk-for-flutter-navigate-navigation-distancetype will never be given for this warning.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property" id="duration">
/sdk-for-flutter-navigate-navigation-roadsignwarning-duration
↔ /sdk-for-flutter-navigate-core-localizedtext-class?
</dt>
<dd>
  Optional length information during which the warning is applicable.
Usually, this information is shown on a separate shield below the main shield.
For example, a sign may warn on playing children for a length of 100 m, starting from
the location of the warning sign.
The length information (most likely with units) is given as printed on the local road sign.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property" id="generalWarningType">
/sdk-for-flutter-navigate-navigation-roadsignwarning-generalwarningtype
↔ /sdk-for-flutter-navigate-navigation-generalwarningroadsigntype
</dt>
<dd>
  Specifies the general warning to which the road sign belongs.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property" id="hashCode">
/sdk-for-flutter-navigate-navigation-roadsignwarning-hashcode
→ int
</dt>
<dd>
  The hash code for this object.
  <div class="features">no setter</div>
</dd>
<dt class="property" id="id">
/sdk-for-flutter-navigate-navigation-roadsignwarning-id
↔ int
</dt>
<dd>
  Unique identifier for this specific road sign warning instance.
Each warning type (truck restrictions, speed warnings, etc.) maintains its own independent ID namespace.
Use this ID to track, update, or dismiss individual warning instances of this type.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property" id="isPrioritySign">
/sdk-for-flutter-navigate-navigation-roadsignwarning-isprioritysign
↔ bool
</dt>
<dd>
  Flag indicating if the road sign is a priority sign.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property" id="preWarning">
/sdk-for-flutter-navigate-navigation-roadsignwarning-prewarning
↔ /sdk-for-flutter-navigate-core-localizedtext-class?
</dt>
<dd>
  Optional pre-warning in terms of distance, of the upcoming warning or regulation.
The pre-warning information is given as printed on the local road sign.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property" id="roadSignSegment">
/sdk-for-flutter-navigate-navigation-roadsignwarning-roadsignsegment
↔ /sdk-for-flutter-navigate-routing-segmentreference-class
</dt>
<dd>
  The reference to the segment where the road sign is located. It can be used to identify the
location of the road sign.
It allows to compare the road sign location with the <code>MapMatchedLocation.segment_reference</code>
provided by the <code>NavigableLocationListener</code> or with the /sdk-for-flutter-navigate-routing-span-segmentreference
available in the Route's Span.
By combining it with the geometry of the segment, that can be loaded using
/sdk-for-flutter-navigate-mapdata-segmentdataloader-class, it is possible to identify the road sign's coordinates.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property inherited" id="runtimeType">
/sdk-for-flutter-navigate-navigation-roadsignwarning-runtimetype
→ Type
</dt>
<dd class="inherited">
  A representation of the runtime type of the object.
  <div class="features">no setterinherited</div>
</dd>
<dt class="property" id="signValue">
/sdk-for-flutter-navigate-navigation-roadsignwarning-signvalue
↔ /sdk-for-flutter-navigate-core-localizedtext-class?
</dt>
<dd>
  Optional value visible on the main sign related to specific road sign types, as it is printed on the local road sign.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property" id="type">
/sdk-for-flutter-navigate-navigation-roadsignwarning-type
↔ /sdk-for-flutter-navigate-navigation-roadsigntype
</dt>
<dd>
  Type of the road sign.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property" id="validityTime">
/sdk-for-flutter-navigate-navigation-roadsignwarning-validitytime
↔ /sdk-for-flutter-navigate-core-localizedtext-class?
</dt>
<dd>
  Optional text visible on the supplemental sign indicating specific
time(s) at which the road sign is applicable.
The time information is given as printed on the local road sign.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property" id="vehicleTypes">
/sdk-for-flutter-navigate-navigation-roadsignwarning-vehicletypes
↔ List&lt;<wbr/>/sdk-for-flutter-navigate-navigation-roadsignvehicletype&gt;
</dt>
<dd>
  Specifies a list of vehicle types for which the road sign is applicable.
The list will be empty when the road sign is applicable for all vehicles including cars.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property" id="weatherType">
/sdk-for-flutter-navigate-navigation-roadsignwarning-weathertype
↔ /sdk-for-flutter-navigate-navigation-weathertype
</dt>
<dd>
  Specifies the weather type for which the sign is applicable. If weather type is <code>WeatherType.UNKNOWN</code>, the sign is actual for all weather types.
  <div class="features">getter/setter pair</div>
</dd>
</dl>
</section>
<section class="summary offset-anchor inherited" id="instance-methods">
<h2>Methods</h2>
<dl class="callables">
<dt class="callable inherited" id="noSuchMethod">
/sdk-for-flutter-navigate-navigation-roadsignwarning-nosuchmethod(<wbr/>Invocation invocation)
    → dynamic

</dt>
<dd class="inherited">
  Invoked when a nonexistent method or property is accessed.
  <div class="features">inherited</div>
</dd>
<dt class="callable inherited" id="toString">
/sdk-for-flutter-navigate-navigation-roadsignwarning-tostring(<wbr/>)
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
/sdk-for-flutter-navigate-navigation-roadsignwarning-operator-equals(<wbr/>Object other)
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
<li class="self-crumb">RoadSignWarning class</li>
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
