---
title: "RoadSign class"
slug: "sdk-for-flutter-navigate-navigation-roadsign-class"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- RoadSign-class.html -->
<div class="doc-with-sidebar"><div class="sidebar-nav"><ol>
<li class="section-title"><a href="navigation/RoadSign-class.html#constructors">Constructors</a></li>
<li><a href="navigation/RoadSign/RoadSign.html">RoadSign</a></li>
<li class="section-title">
<a href="navigation/RoadSign-class.html#instance-properties">Properties</a>
</li>
<li><a href="navigation/RoadSign/generalWarningType.html">generalWarningType</a></li>
<li><a href="navigation/RoadSign/hashCode.html">hashCode</a></li>
<li><a href="navigation/RoadSign/isPrioritySign.html">isPrioritySign</a></li>
<li><a href="navigation/RoadSign/localizedDuration.html">localizedDuration</a></li>
<li><a href="navigation/RoadSign/localizedPreWarning.html">localizedPreWarning</a></li>
<li><a href="navigation/RoadSign/localizedSignValue.html">localizedSignValue</a></li>
<li><a href="navigation/RoadSign/localizedValidityTime.html">localizedValidityTime</a></li>
<li><a href="navigation/RoadSign/offsetInMeters.html">offsetInMeters</a></li>
<li><a href="navigation/RoadSign/roadSignCategory.html">roadSignCategory</a></li>
<li><a href="navigation/RoadSign/roadSignType.html">roadSignType</a></li>
<li class="inherited"><a href="navigation/RoadSign/runtimeType.html">runtimeType</a></li>
<li><a href="navigation/RoadSign/travelDirection.html">travelDirection</a></li>
<li><a href="navigation/RoadSign/vehicleTypes.html">vehicleTypes</a></li>
<li><a href="navigation/RoadSign/weatherType.html">weatherType</a></li>
<li class="section-title inherited"><a href="navigation/RoadSign-class.html#instance-methods">Methods</a></li>
<li class="inherited"><a href="navigation/RoadSign/noSuchMethod.html">noSuchMethod</a></li>
<li class="inherited"><a href="navigation/RoadSign/toString.html">toString</a></li>
<li class="section-title"><a href="navigation/RoadSign-class.html#operators">Operators</a></li>
<li><a href="navigation/RoadSign/operator_equals.html">operator ==</a></li>
</ol></div><div class="doc-content">
<div id="overlay-under-drawer"></div>
<header id="title">
menu
<ol class="breadcrumbs gt-separated dark hidden-xs">
<li>/sdk-for-flutter-navigate</li>
<li>/sdk-for-flutter-navigate-navigation-navigation-library</li>
<li class="self-crumb">RoadSign class</li>
</ol>
<div class="self-name">RoadSign</div>
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
<div class="main-content" data-above-sidebar="navigation/navigation-library-sidebar.html" data-below-sidebar="navigation/RoadSign-class-sidebar.html" id="dartdoc-main-content">
<div>
<h1>RoadSign class</h1></div>
<section class="desc markdown">
<p>Describes a road sign.</p>
<p><strong>Note:</strong> This is a beta release of this feature, so there could be a few bugs and unexpected behaviors.
Related APIs may change for new releases without a deprecation process.</p>
</section>
<section class="summary offset-anchor" id="constructors">
<h2>Constructors</h2>
<dl class="constructor-summary-list">
<dt class="callable" id="RoadSign">
/sdk-for-flutter-navigate-navigation-roadsign-roadsign(int offsetInMeters, /sdk-for-flutter-navigate-routing-traveldirection travelDirection, /sdk-for-flutter-navigate-navigation-roadsigntype roadSignType, /sdk-for-flutter-navigate-navigation-roadsigncategory roadSignCategory, bool isPrioritySign, /sdk-for-flutter-navigate-navigation-generalwarningroadsigntype generalWarningType, List&lt;<wbr/>/sdk-for-flutter-navigate-navigation-roadsignvehicletype&gt; vehicleTypes, /sdk-for-flutter-navigate-navigation-weathertype weatherType)
</dt>
<dd>
</dd>
</dl>
</section>
<section class="summary offset-anchor" id="instance-properties">
<h2>Properties</h2>
<dl class="properties">
<dt class="property" id="generalWarningType">
/sdk-for-flutter-navigate-navigation-roadsign-generalwarningtype
↔ /sdk-for-flutter-navigate-navigation-generalwarningroadsigntype
</dt>
<dd>
  Specifies the general warning to which the road sign belongs.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property" id="hashCode">
/sdk-for-flutter-navigate-navigation-roadsign-hashcode
→ int
</dt>
<dd>
  The hash code for this object.
  <div class="features">no setter</div>
</dd>
<dt class="property" id="isPrioritySign">
/sdk-for-flutter-navigate-navigation-roadsign-isprioritysign
↔ bool
</dt>
<dd>
  Flag indicating if the road sign is a priority sign.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property" id="localizedDuration">
/sdk-for-flutter-navigate-navigation-roadsign-localizedduration
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
<dt class="property" id="localizedPreWarning">
/sdk-for-flutter-navigate-navigation-roadsign-localizedprewarning
↔ /sdk-for-flutter-navigate-core-localizedtext-class?
</dt>
<dd>
  Optional pre-warning in terms of distance, of the upcoming warning or regulation.
The pre-warning information is given as printed on the local road sign.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property" id="localizedSignValue">
/sdk-for-flutter-navigate-navigation-roadsign-localizedsignvalue
↔ /sdk-for-flutter-navigate-core-localizedtext-class?
</dt>
<dd>
  Optional value visible on the main sign related to specific road sign types, as it is printed on the local road sign.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property" id="localizedValidityTime">
/sdk-for-flutter-navigate-navigation-roadsign-localizedvaliditytime
↔ /sdk-for-flutter-navigate-core-localizedtext-class?
</dt>
<dd>
  Optional text visible on the supplemental sign indicating specific
time(s) at which the road sign is applicable.
The time information is given as printed on the local road sign.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property" id="offsetInMeters">
/sdk-for-flutter-navigate-navigation-roadsign-offsetinmeters
↔ int
</dt>
<dd>
  The offset in meters from the beginning of the segment to the location of the road sign
in positive direction.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property" id="roadSignCategory">
/sdk-for-flutter-navigate-navigation-roadsign-roadsigncategory
↔ /sdk-for-flutter-navigate-navigation-roadsigncategory
</dt>
<dd>
  The main category to which the road sign belongs.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property" id="roadSignType">
/sdk-for-flutter-navigate-navigation-roadsign-roadsigntype
↔ /sdk-for-flutter-navigate-navigation-roadsigntype
</dt>
<dd>
  Type of the road sign.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property inherited" id="runtimeType">
/sdk-for-flutter-navigate-navigation-roadsign-runtimetype
→ Type
</dt>
<dd class="inherited">
  A representation of the runtime type of the object.
  <div class="features">no setterinherited</div>
</dd>
<dt class="property" id="travelDirection">
/sdk-for-flutter-navigate-navigation-roadsign-traveldirection
↔ /sdk-for-flutter-navigate-routing-traveldirection
</dt>
<dd>
  Segment direction which the road sign is applied.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property" id="vehicleTypes">
/sdk-for-flutter-navigate-navigation-roadsign-vehicletypes
↔ List&lt;<wbr/>/sdk-for-flutter-navigate-navigation-roadsignvehicletype&gt;
</dt>
<dd>
  Specifies a list of vehicle types for which the road sign is applicable.
The list will be empty when the road sign is applicable for all vehicles including cars.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property" id="weatherType">
/sdk-for-flutter-navigate-navigation-roadsign-weathertype
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
/sdk-for-flutter-navigate-navigation-roadsign-nosuchmethod(<wbr/>Invocation invocation)
    → dynamic

</dt>
<dd class="inherited">
  Invoked when a nonexistent method or property is accessed.
  <div class="features">inherited</div>
</dd>
<dt class="callable inherited" id="toString">
/sdk-for-flutter-navigate-navigation-roadsign-tostring(<wbr/>)
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
/sdk-for-flutter-navigate-navigation-roadsign-operator-equals(<wbr/>Object other)
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
<li class="self-crumb">RoadSign class</li>
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
