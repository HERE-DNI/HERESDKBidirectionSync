---
title: "Constructors"
slug: "sdk-for-flutter-explore-routing-avoidanceoptions-class"
---

<HTMLBlock>
<div class="sdk-for-flutter">
<!-- AvoidanceOptions-class.html -->
<div class="doc-with-sidebar"><div class="sidebar-nav"><ol>
<li class="section-title"><a href="routing/AvoidanceOptions-class.html#constructors">Constructors</a></li>
<li><a href="routing/AvoidanceOptions/AvoidanceOptions.html">AvoidanceOptions</a></li>
<li class="section-title">
<a href="routing/AvoidanceOptions-class.html#instance-properties">Properties</a>
</li>
<li><a href="routing/AvoidanceOptions/avoidBoundingBoxAreasOptions.html">avoidBoundingBoxAreasOptions</a></li>
<li><a href="routing/AvoidanceOptions/avoidCorridorAreasOptions.html">avoidCorridorAreasOptions</a></li>
<li><a href="routing/AvoidanceOptions/avoidedTruckRoadTypes.html">avoidedTruckRoadTypes</a></li>
<li><a href="routing/AvoidanceOptions/avoidPolygonAreasOptions.html">avoidPolygonAreasOptions</a></li>
<li><a href="routing/AvoidanceOptions/countries.html">countries</a></li>
<li><a href="routing/AvoidanceOptions/exceptZoneIds.html">exceptZoneIds</a></li>
<li><a href="routing/AvoidanceOptions/hashCode.html">hashCode</a></li>
<li><a href="routing/AvoidanceOptions/roadFeatures.html">roadFeatures</a></li>
<li class="inherited"><a href="routing/AvoidanceOptions/runtimeType.html">runtimeType</a></li>
<li><a href="routing/AvoidanceOptions/segments.html">segments</a></li>
<li><a href="routing/AvoidanceOptions/zoneCategories.html">zoneCategories</a></li>
<li><a href="routing/AvoidanceOptions/zoneIds.html">zoneIds</a></li>
<li class="section-title inherited"><a href="routing/AvoidanceOptions-class.html#instance-methods">Methods</a></li>
<li class="inherited"><a href="routing/AvoidanceOptions/noSuchMethod.html">noSuchMethod</a></li>
<li class="inherited"><a href="routing/AvoidanceOptions/toString.html">toString</a></li>
<li class="section-title"><a href="routing/AvoidanceOptions-class.html#operators">Operators</a></li>
<li><a href="routing/AvoidanceOptions/operator_equals.html">operator ==</a></li>
</ol></div><div class="doc-content">
<div id="overlay-under-drawer"></div>
<header id="title">
menu
<ol class="breadcrumbs gt-separated dark hidden-xs">
<li><a href="../index.html">/sdk-for-flutter-explore</a></li>
<li><a href="../routing/routing-library.html">/sdk-for-flutter-explore-routing-routing-library</a></li>
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
<a href="../routing/AvoidanceOptions/AvoidanceOptions.html">/sdk-for-flutter-explore-routing-avoidanceoptions-avoidanceoptions</a>()
</dt>
<dd>
</dd>
</dl>
</section>
<section class="summary offset-anchor" id="instance-properties">
<h2>Properties</h2>
<dl class="properties">
<dt class="property" id="avoidBoundingBoxAreasOptions">
<a href="../routing/AvoidanceOptions/avoidBoundingBoxAreasOptions.html">/sdk-for-flutter-explore-routing-avoidanceoptions-avoidboundingboxareasoptions</a>
↔ List&lt;<wbr/><a href="../routing/AvoidBoundingBoxAreaOptions-class.html">/sdk-for-flutter-explore-routing-avoidboundingboxareaoptions-class</a>&gt;
</dt>
<dd>
  List of rectangular shapes which routes must not cross and additional options for this area.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property" id="avoidCorridorAreasOptions">
<a href="../routing/AvoidanceOptions/avoidCorridorAreasOptions.html">/sdk-for-flutter-explore-routing-avoidanceoptions-avoidcorridorareasoptions</a>
↔ List&lt;<wbr/><a href="../routing/AvoidCorridorAreaOptions-class.html">/sdk-for-flutter-explore-routing-avoidcorridorareaoptions-class</a>&gt;
</dt>
<dd>
  List of corridor shapes which routes must not cross and additional options for this area.
<strong>Note:</strong> Currently, the maximum count of corridors is limited to 20.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property" id="avoidedTruckRoadTypes">
<a href="../routing/AvoidanceOptions/avoidedTruckRoadTypes.html">/sdk-for-flutter-explore-routing-avoidanceoptions-avoidedtruckroadtypes</a>
↔ List&lt;<wbr/><a href="../transport/TruckRoadType.html">/sdk-for-flutter-explore-transport-truckroadtype</a>&gt;
</dt>
<dd>
  Specifies a list of avoided truck road types for vehicle.
Refer to <a href="../transport/TruckRoadType.html">/sdk-for-flutter-explore-transport-truckroadtype</a> for the available options.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property" id="avoidPolygonAreasOptions">
<a href="../routing/AvoidanceOptions/avoidPolygonAreasOptions.html">/sdk-for-flutter-explore-routing-avoidanceoptions-avoidpolygonareasoptions</a>
↔ List&lt;<wbr/><a href="../routing/AvoidPolygonAreaOptions-class.html">/sdk-for-flutter-explore-routing-avoidpolygonareaoptions-class</a>&gt;
</dt>
<dd>
  List of polygon shapes which routes must not cross and additional options for this area.
<strong>Note:</strong> Currently, the maximum count of polygons is limited to 20.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property" id="countries">
<a href="../routing/AvoidanceOptions/countries.html">/sdk-for-flutter-explore-routing-avoidanceoptions-countries</a>
↔ List&lt;<wbr/><a href="../core/CountryCode.html">/sdk-for-flutter-explore-core-countrycode</a>&gt;
</dt>
<dd>
  Countries that the route must avoid. Strictly enforced.
Violations are reported as <a href="../routing/SectionNoticeCode.html">/sdk-for-flutter-explore-routing-sectionnoticecode</a>.
<strong>Note:</strong> This avoidance option is not supported in <code>IsolineOptions</code> for isoline calculation.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property" id="exceptZoneIds">
<a href="../routing/AvoidanceOptions/exceptZoneIds.html">/sdk-for-flutter-explore-routing-avoidanceoptions-exceptzoneids</a>
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
<a href="../routing/AvoidanceOptions/hashCode.html">/sdk-for-flutter-explore-routing-avoidanceoptions-hashcode</a>
→ int
</dt>
<dd>
  The hash code for this object.
  <div class="features">no setter</div>
</dd>
<dt class="property" id="roadFeatures">
<a href="../routing/AvoidanceOptions/roadFeatures.html">/sdk-for-flutter-explore-routing-avoidanceoptions-roadfeatures</a>
↔ List&lt;<wbr/><a href="../routing/RoadFeatures.html">/sdk-for-flutter-explore-routing-roadfeatures</a>&gt;
</dt>
<dd>
  Features which routes should avoid. Best effort only (not enforced).
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property inherited" id="runtimeType">
<a href="../routing/AvoidanceOptions/runtimeType.html">/sdk-for-flutter-explore-routing-avoidanceoptions-runtimetype</a>
→ Type
</dt>
<dd class="inherited">
  A representation of the runtime type of the object.
  <div class="features">no setterinherited</div>
</dd>
<dt class="property" id="segments">
<a href="../routing/AvoidanceOptions/segments.html">/sdk-for-flutter-explore-routing-avoidanceoptions-segments</a>
↔ List&lt;<wbr/><a href="../routing/SegmentReference-class.html">/sdk-for-flutter-explore-routing-segmentreference-class</a>&gt;
</dt>
<dd>
  Segments that routes will avoid going through.
Violations are reported as <a href="../routing/SectionNoticeCode.html">/sdk-for-flutter-explore-routing-sectionnoticecode</a>.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property" id="zoneCategories">
<a href="../routing/AvoidanceOptions/zoneCategories.html">/sdk-for-flutter-explore-routing-avoidanceoptions-zonecategories</a>
↔ List&lt;<wbr/><a href="../routing/ZoneCategory.html">/sdk-for-flutter-explore-routing-zonecategory</a>&gt;
</dt>
<dd>
  Zone categories which routes must not cross. Strictly enforced.
Violations are reported as <a href="../routing/SectionNoticeCode.html">/sdk-for-flutter-explore-routing-sectionnoticecode</a>.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property" id="zoneIds">
<a href="../routing/AvoidanceOptions/zoneIds.html">/sdk-for-flutter-explore-routing-avoidanceoptions-zoneids</a>
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
<a href="../routing/AvoidanceOptions/noSuchMethod.html">/sdk-for-flutter-explore-routing-avoidanceoptions-nosuchmethod</a>(<wbr/>Invocation invocation)
    → dynamic

</dt>
<dd class="inherited">
  Invoked when a nonexistent method or property is accessed.
  <div class="features">inherited</div>
</dd>
<dt class="callable inherited" id="toString">
<a href="../routing/AvoidanceOptions/toString.html">/sdk-for-flutter-explore-routing-avoidanceoptions-tostring</a>(<wbr/>)
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
<a href="../routing/AvoidanceOptions/operator_equals.html">/sdk-for-flutter-explore-routing-avoidanceoptions-operator-equals</a>(<wbr/>Object other)
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
<li><a href="../index.html">/sdk-for-flutter-explore</a></li>
<li><a href="../routing/routing-library.html">/sdk-for-flutter-explore-routing-routing-library</a></li>
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
</div></div>
</div>
</HTMLBlock>
