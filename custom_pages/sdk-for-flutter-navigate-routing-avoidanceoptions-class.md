---
title: "Untitled"
slug: "sdk-for-flutter-navigate-routing-avoidanceoptions-class"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- AvoidanceOptions-class.html -->

<div id="overlay-under-drawer"></div>
<header id="title">
menu
<ol class="breadcrumbs gt-separated dark hidden-xs">
<li>/sdk-for-flutter-navigate</li>
<li>/sdk-for-flutter-navigate-routing-routing-library</li>
<li class="self-crumb">AvoidanceOptions class</li>
</ol>
<div class="self-name">AvoidanceOptions</div>
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
<div class="main-content" data-above-sidebar="routing/routing-library-sidebar.html" data-below-sidebar="routing/AvoidanceOptions-class-sidebar.html" id="dartdoc-main-content">
<div>
<h1>AvoidanceOptions class</h1></div>
<section class="desc markdown">
<p>The options to specify restrictions for route calculations.</p>
</section>
<section class="summary offset-anchor" id="constructors">
<h2>Constructors</h2>
<dl class="constructor-summary-list">
<dt class="callable" id="AvoidanceOptions">
/sdk-for-flutter-navigate-routing-avoidanceoptions-avoidanceoptions()
</dt>
<dd>
</dd>
</dl>
</section>
<section class="summary offset-anchor" id="instance-properties">
<h2>Properties</h2>
<dl class="properties">
<dt class="property" id="avoidBoundingBoxAreasOptions">
/sdk-for-flutter-navigate-routing-avoidanceoptions-avoidboundingboxareasoptions
↔ List&lt;<wbr/>/sdk-for-flutter-navigate-routing-avoidboundingboxareaoptions-class&gt;
</dt>
<dd>
  List of rectangular shapes which routes must not cross and additional options for this area.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property" id="avoidCorridorAreasOptions">
/sdk-for-flutter-navigate-routing-avoidanceoptions-avoidcorridorareasoptions
↔ List&lt;<wbr/>/sdk-for-flutter-navigate-routing-avoidcorridorareaoptions-class&gt;
</dt>
<dd>
  List of corridor shapes which routes must not cross and additional options for this area.
<strong>Note:</strong> Currently, the maximum count of corridors is limited to 20.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property" id="avoidedTruckRoadTypes">
/sdk-for-flutter-navigate-routing-avoidanceoptions-avoidedtruckroadtypes
↔ List&lt;<wbr/>/sdk-for-flutter-navigate-transport-truckroadtype&gt;
</dt>
<dd>
  Specifies a list of avoided truck road types for vehicle.
Refer to /sdk-for-flutter-navigate-transport-truckroadtype for the available options.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property" id="avoidPolygonAreasOptions">
/sdk-for-flutter-navigate-routing-avoidanceoptions-avoidpolygonareasoptions
↔ List&lt;<wbr/>/sdk-for-flutter-navigate-routing-avoidpolygonareaoptions-class&gt;
</dt>
<dd>
  List of polygon shapes which routes must not cross and additional options for this area.
<strong>Note:</strong> Currently, the maximum count of polygons is limited to 20.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property" id="countries">
/sdk-for-flutter-navigate-routing-avoidanceoptions-countries
↔ List&lt;<wbr/>/sdk-for-flutter-navigate-core-countrycode&gt;
</dt>
<dd>
  Countries that the route must avoid. Strictly enforced.
Violations are reported as /sdk-for-flutter-navigate-routing-sectionnoticecode.
<strong>Note:</strong> This avoidance option is not supported in <code>IsolineOptions</code> for isoline calculation.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property" id="exceptZoneIds">
/sdk-for-flutter-navigate-routing-avoidanceoptions-exceptzoneids
↔ List&lt;<wbr/>String&gt;
</dt>
<dd>
  Exception to <code>AvoidanceOptions.zone_categories</code>, which can be specified by list of zone identifiers.
e.g. the format of ID is like <code>here:cm:envzone:2</code>.
Information about the various routing zones originates from the respective catalogs of platform.here.com.
For example, more information on zone IDs for Environmental Zones is available under "https://platform.here.com/data/hrn:here:data::olp-here:rib-2/environmental-zones/overview".
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property" id="hashCode">
/sdk-for-flutter-navigate-routing-avoidanceoptions-hashcode
→ int
</dt>
<dd>
  The hash code for this object.
  <div class="features">no setter</div>
</dd>
<dt class="property" id="roadFeatures">
/sdk-for-flutter-navigate-routing-avoidanceoptions-roadfeatures
↔ List&lt;<wbr/>/sdk-for-flutter-navigate-routing-roadfeatures&gt;
</dt>
<dd>
  Features which routes should avoid. Best effort only (not enforced).
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property inherited" id="runtimeType">
/sdk-for-flutter-navigate-routing-avoidanceoptions-runtimetype
→ Type
</dt>
<dd class="inherited">
  A representation of the runtime type of the object.
  <div class="features">no setterinherited</div>
</dd>
<dt class="property" id="segments">
/sdk-for-flutter-navigate-routing-avoidanceoptions-segments
↔ List&lt;<wbr/>/sdk-for-flutter-navigate-routing-segmentreference-class&gt;
</dt>
<dd>
  Segments that routes will avoid going through.
Violations are reported as /sdk-for-flutter-navigate-routing-sectionnoticecode.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property" id="zoneCategories">
/sdk-for-flutter-navigate-routing-avoidanceoptions-zonecategories
↔ List&lt;<wbr/>/sdk-for-flutter-navigate-routing-zonecategory&gt;
</dt>
<dd>
  Zone categories which routes must not cross. Strictly enforced.
Violations are reported as /sdk-for-flutter-navigate-routing-sectionnoticecode.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property" id="zoneIds">
/sdk-for-flutter-navigate-routing-avoidanceoptions-zoneids
↔ List&lt;<wbr/>String&gt;
</dt>
<dd>
  List containing identifiers of zones that routes should avoid going through.
e.g. the format of ID is like <code>here:cm:envzone:2</code>.
Information about the various routing zones originates from the respective catalogs of platform.here.com.
For example, more information on zone IDs for Environmental Zones is available under "https://platform.here.com/data/hrn:here:data::olp-here:rib-2/environmental-zones/overview".
  <div class="features">getter/setter pair</div>
</dd>
</dl>
</section>
<section class="summary offset-anchor inherited" id="instance-methods">
<h2>Methods</h2>
<dl class="callables">
<dt class="callable inherited" id="noSuchMethod">
/sdk-for-flutter-navigate-routing-avoidanceoptions-nosuchmethod(<wbr/>Invocation invocation)
    → dynamic

</dt>
<dd class="inherited">
  Invoked when a nonexistent method or property is accessed.
  <div class="features">inherited</div>
</dd>
<dt class="callable inherited" id="toString">
/sdk-for-flutter-navigate-routing-avoidanceoptions-tostring(<wbr/>)
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
/sdk-for-flutter-navigate-routing-avoidanceoptions-operator-equals(<wbr/>Object other)
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
<li class="self-crumb">AvoidanceOptions class</li>
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
