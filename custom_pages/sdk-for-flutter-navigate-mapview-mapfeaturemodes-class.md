---
title: "Untitled"
slug: "sdk-for-flutter-navigate-mapview-mapfeaturemodes-class"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- MapFeatureModes-class.html -->

<div id="overlay-under-drawer"></div>
<header id="title">
menu
<ol class="breadcrumbs gt-separated dark hidden-xs">
<li>/sdk-for-flutter-navigate</li>
<li>/sdk-for-flutter-navigate-mapview-mapview-library</li>
<li class="self-crumb">MapFeatureModes class</li>
</ol>
<div class="self-name">MapFeatureModes</div>
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
<div class="main-content" data-above-sidebar="mapview/mapview-library-sidebar.html" data-below-sidebar="mapview/MapFeatureModes-class-sidebar.html" id="dartdoc-main-content">
<div>
<h1>MapFeatureModes class</h1></div>
<section class="desc markdown">
<p>Holds constants for map feature modes, to be used with /sdk-for-flutter-navigate-mapview-mapscene-enablefeatures.</p>
<p>Use /sdk-for-flutter-navigate-mapview-mapfeaturemodes-defaultmode to enable a feature with its default mode.</p>
<p>Note: The default mode is defined by the currently loaded map scene configuration and
may vary per /sdk-for-flutter-navigate-mapview-mapscheme. The currently active features and modes can be inspected
using /sdk-for-flutter-navigate-mapview-mapscene-getactivefeatures after the scene is loaded.</p>
<p>See /sdk-for-flutter-navigate-mapview-mapfeatures-class for constants representing the feature names.</p>
</section>
<section class="summary offset-anchor" id="constructors">
<h2>Constructors</h2>
<dl class="constructor-summary-list">
<dt class="callable" id="MapFeatureModes">
/sdk-for-flutter-navigate-mapview-mapfeaturemodes-mapfeaturemodes()
</dt>
<dd>
</dd>
</dl>
</section>
<section class="summary offset-anchor inherited" id="instance-properties">
<h2>Properties</h2>
<dl class="properties">
<dt class="property inherited" id="hashCode">
/sdk-for-flutter-navigate-mapview-mapfeaturemodes-hashcode
→ int
</dt>
<dd class="inherited">
  The hash code for this object.
  <div class="features">no setterinherited</div>
</dd>
<dt class="property inherited" id="runtimeType">
/sdk-for-flutter-navigate-mapview-mapfeaturemodes-runtimetype
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
/sdk-for-flutter-navigate-mapview-mapfeaturemodes-nosuchmethod(<wbr/>Invocation invocation)
    → dynamic

</dt>
<dd class="inherited">
  Invoked when a nonexistent method or property is accessed.
  <div class="features">inherited</div>
</dd>
<dt class="callable inherited" id="toString">
/sdk-for-flutter-navigate-mapview-mapfeaturemodes-tostring(<wbr/>)
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
/sdk-for-flutter-navigate-mapview-mapfeaturemodes-operator-equals(<wbr/>Object other)
    → bool

</dt>
<dd class="inherited">
  The equality operator.
  <div class="features">inherited</div>
</dd>
</dl>
</section>
<section class="summary offset-anchor" id="static-properties">
<h2>Static Properties</h2>
<dl class="properties">
<dt class="property" id="ambientOcclusionAll">
/sdk-for-flutter-navigate-mapview-mapfeaturemodes-ambientocclusionall
→ String
</dt>
<dd>
  Ambient occlusion effect is shown for extruded buildings and landmarks.
  <div class="features">final</div>
</dd>
<dt class="property" id="buildingFootprintsAll">
/sdk-for-flutter-navigate-mapview-mapfeaturemodes-buildingfootprintsall
→ String
</dt>
<dd>
  All building footprints are shown.
  <div class="features">final</div>
</dd>
<dt class="property" id="congestionZonesAll">
/sdk-for-flutter-navigate-mapview-mapfeaturemodes-congestionzonesall
→ String
</dt>
<dd>
  All congestion zones are shown.
  <div class="features">final</div>
</dd>
<dt class="property" id="contoursAll">
/sdk-for-flutter-navigate-mapview-mapfeaturemodes-contoursall
→ String
</dt>
<dd>
  Contour lines indicating representing elevation changes are shown.
  <div class="features">final</div>
</dd>
<dt class="property" id="defaultMode">
/sdk-for-flutter-navigate-mapview-mapfeaturemodes-defaultmode
→ String
</dt>
<dd>
  Enables the default mode of a map feature. Can be used with any map feature.
  <div class="features">final</div>
</dd>
<dt class="property" id="environmentalZonesAll">
/sdk-for-flutter-navigate-mapview-mapfeaturemodes-environmentalzonesall
→ String
</dt>
<dd>
  All environmental zones are shown.
  <div class="features">final</div>
</dd>
<dt class="property" id="extrudedBuildingsAll">
/sdk-for-flutter-navigate-mapview-mapfeaturemodes-extrudedbuildingsall
→ String
</dt>
<dd>
  All extruded buildings are shown.
  <div class="features">final</div>
</dd>
<dt class="property" id="landmarksGrayscale">
/sdk-for-flutter-navigate-mapview-mapfeaturemodes-landmarksgrayscale
→ String
</dt>
<dd>
  3D landmarks are textured with grayscale filter.
  <div class="features">final</div>
</dd>
<dt class="property" id="landmarksTextured">
/sdk-for-flutter-navigate-mapview-mapfeaturemodes-landmarkstextured
→ String
</dt>
<dd>
  3D landmarks are textured.
  <div class="features">final</div>
</dd>
<dt class="property" id="landmarksTextureless">
/sdk-for-flutter-navigate-mapview-mapfeaturemodes-landmarkstextureless
→ String
</dt>
<dd>
  3D landmarks have solid color.
  <div class="features">final</div>
</dd>
<dt class="property" id="lowSpeedZonesAll">
/sdk-for-flutter-navigate-mapview-mapfeaturemodes-lowspeedzonesall
→ String
</dt>
<dd>
  All low speed zones are shown.
  <div class="features">final</div>
</dd>
<dt class="property" id="publicTransitAll">
/sdk-for-flutter-navigate-mapview-mapfeaturemodes-publictransitall
→ String
</dt>
<dd>
  Line geometry for all available public transit systems is shown; including subway, tram, train,
monorail, ferry and more.
  <div class="features">final</div>
</dd>
<dt class="property" id="publicTransitAsia">
/sdk-for-flutter-navigate-mapview-mapfeaturemodes-publictransitasia
→ String
</dt>
<dd>
  Line geometry for selected public transit systems is shown: subway lines in Japan.
Only available when Japan map is used.
  <div class="features">final</div>
</dd>
<dt class="property" id="roadExitLabelsAll">
/sdk-for-flutter-navigate-mapview-mapfeaturemodes-roadexitlabelsall
→ String
</dt>
<dd>
  Road exit labels are shown with numbers and names, if available.
  <div class="features">final</div>
</dd>
<dt class="property" id="roadExitLabelsNumbersOnly">
/sdk-for-flutter-navigate-mapview-mapfeaturemodes-roadexitlabelsnumbersonly
→ String
</dt>
<dd>
  Road exit labels are shown with numbers, if available.
  <div class="features">final</div>
</dd>
<dt class="property" id="safetyCamerasAll">
/sdk-for-flutter-navigate-mapview-mapfeaturemodes-safetycamerasall
→ String
</dt>
<dd>
  All types of safety cameras are shown. Includes speed, red light, red light + speed,
bus lane, distance and speed section cameras.
  <div class="features">final</div>
</dd>
<dt class="property" id="shadowsAll">
/sdk-for-flutter-navigate-mapview-mapfeaturemodes-shadowsall
→ String
</dt>
<dd>
  Shadows are shown for extruded buildings and landmarks.
  <div class="features">final</div>
</dd>
<dt class="property" id="terrain3d">
/sdk-for-flutter-navigate-mapview-mapfeaturemodes-terrain3d
→ String
</dt>
<dd>
  Topography-shading is shown on 3d terrain.
  <div class="features">final</div>
</dd>
<dt class="property" id="terrainHillshade">
/sdk-for-flutter-navigate-mapview-mapfeaturemodes-terrainhillshade
→ String
</dt>
<dd>
  Topography-shading is shown.
  <div class="features">final</div>
</dd>
<dt class="property" id="trafficFlowJapanWithoutFreeFlow">
/sdk-for-flutter-navigate-mapview-mapfeaturemodes-trafficflowjapanwithoutfreeflow
→ String
</dt>
<dd>
  Only available when Japan map is used.
  <div class="features">final</div>
</dd>
<dt class="property" id="trafficFlowWithFreeFlow">
/sdk-for-flutter-navigate-mapview-mapfeaturemodes-trafficflowwithfreeflow
→ String
</dt>
<dd>
  Traffic flow shows green lines when there is no traffic congestion.
  <div class="features">final</div>
</dd>
<dt class="property" id="trafficFlowWithoutFreeFlow">
/sdk-for-flutter-navigate-mapview-mapfeaturemodes-trafficflowwithoutfreeflow
→ String
</dt>
<dd>
  Traffic flow does not show green lines when there is no traffic congestion.
  <div class="features">final</div>
</dd>
<dt class="property" id="trafficIncidentsAll">
/sdk-for-flutter-navigate-mapview-mapfeaturemodes-trafficincidentsall
→ String
</dt>
<dd>
  All available traffic incidents are shown.
  <div class="features">final</div>
</dd>
<dt class="property" id="trafficLightsAll">
/sdk-for-flutter-navigate-mapview-mapfeaturemodes-trafficlightsall
→ String
</dt>
<dd>
  All available traffic lights are shown.
  <div class="features">final</div>
</dd>
<dt class="property" id="truckPreferredRoadsAll">
/sdk-for-flutter-navigate-mapview-mapfeaturemodes-truckpreferredroadsall
→ String
</dt>
<dd>
  Display truck preferred roads
  <div class="features">final</div>
</dd>
<dt class="property" id="vehicleRestrictionsActive">
/sdk-for-flutter-navigate-mapview-mapfeaturemodes-vehiclerestrictionsactive
→ String
</dt>
<dd>
  Inactive time-based restrictions are not shown.
  <div class="features">final</div>
</dd>
<dt class="property" id="vehicleRestrictionsActiveAndInactive">
/sdk-for-flutter-navigate-mapview-mapfeaturemodes-vehiclerestrictionsactiveandinactive
→ String
</dt>
<dd>
  Both active and inactive time-based restrictions are shown.
  <div class="features">final</div>
</dd>
<dt class="property" id="vehicleRestrictionsActiveAndInactiveDifferentiated">
/sdk-for-flutter-navigate-mapview-mapfeaturemodes-vehiclerestrictionsactiveandinactivedifferentiated
→ String
</dt>
<dd>
  Both active and inactive restrictions are shown, but inactive time-based restrictions are
shown as faded.
  <div class="features">final</div>
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
<li>/sdk-for-flutter-navigate-mapview-mapview-library</li>
<li class="self-crumb">MapFeatureModes class</li>
</ol>
<h5>mapview library</h5>
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
