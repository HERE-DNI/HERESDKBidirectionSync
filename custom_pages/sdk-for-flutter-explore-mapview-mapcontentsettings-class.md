---
title: "Constructors"
slug: "sdk-for-flutter-explore-mapview-mapcontentsettings-class"
---

<HTMLBlock>
<div class="sdk-for-flutter">
<!-- MapContentSettings-class.html -->
<div class="doc-with-sidebar"><div class="sidebar-nav"><ol>
<li class="section-title"><a href="mapview/MapContentSettings-class.html#constructors">Constructors</a></li>
<li><a href="mapview/MapContentSettings/MapContentSettings.html">MapContentSettings</a></li>
<li class="section-title inherited">
<a href="mapview/MapContentSettings-class.html#instance-properties">Properties</a>
</li>
<li class="inherited"><a href="mapview/MapContentSettings/hashCode.html">hashCode</a></li>
<li class="inherited"><a href="mapview/MapContentSettings/runtimeType.html">runtimeType</a></li>
<li class="section-title inherited"><a href="mapview/MapContentSettings-class.html#instance-methods">Methods</a></li>
<li class="inherited"><a href="mapview/MapContentSettings/noSuchMethod.html">noSuchMethod</a></li>
<li class="inherited"><a href="mapview/MapContentSettings/toString.html">toString</a></li>
<li class="section-title inherited"><a href="mapview/MapContentSettings-class.html#operators">Operators</a></li>
<li class="inherited"><a href="mapview/MapContentSettings/operator_equals.html">operator ==</a></li>
<li class="section-title"><a href="mapview/MapContentSettings-class.html#static-methods">Static methods</a></li>
<li><a href="mapview/MapContentSettings/filterTrafficIncidents.html">filterTrafficIncidents</a></li>
<li><a href="mapview/MapContentSettings/resetTrafficIncidentFilter.html">resetTrafficIncidentFilter</a></li>
<li><a href="mapview/MapContentSettings/resetTrafficRefreshPeriod.html">resetTrafficRefreshPeriod</a></li>
<li><a href="mapview/MapContentSettings/setTrafficRefreshPeriod.html">setTrafficRefreshPeriod</a></li>
</ol></div><div class="doc-content">
<div id="overlay-under-drawer"></div>
<header id="title">
menu
<ol class="breadcrumbs gt-separated dark hidden-xs">
<li><a href="../index.html">/sdk-for-flutter-explore</a></li>
<li><a href="../mapview/mapview-library.html">/sdk-for-flutter-explore-mapview-mapview-library</a></li>
<li class="self-crumb">MapContentSettings class</li>
</ol>
<div class="self-name">MapContentSettings</div>
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
<div class="main-content" data-above-sidebar="mapview/mapview-library-sidebar.html" data-below-sidebar="mapview/MapContentSettings-class-sidebar.html" id="dartdoc-main-content">
<div>
<h1>MapContentSettings class abstract</h1></div>
<section class="desc markdown">
<p>Provides settings regarding map data which are applied globally to all map views.</p>
<p>The settings
can already be changed before a map view instance is created.</p>
</section>
<section class="summary offset-anchor" id="constructors">
<h2>Constructors</h2>
<dl class="constructor-summary-list">
<dt class="callable" id="MapContentSettings">
<a href="../mapview/MapContentSettings/MapContentSettings.html">/sdk-for-flutter-explore-mapview-mapcontentsettings-mapcontentsettings</a>()
</dt>
<dd>
</dd>
</dl>
</section>
<section class="summary offset-anchor inherited" id="instance-properties">
<h2>Properties</h2>
<dl class="properties">
<dt class="property inherited" id="hashCode">
<a href="../mapview/MapContentSettings/hashCode.html">/sdk-for-flutter-explore-mapview-mapcontentsettings-hashcode</a>
→ int
</dt>
<dd class="inherited">
  The hash code for this object.
  <div class="features">no setterinherited</div>
</dd>
<dt class="property inherited" id="runtimeType">
<a href="../mapview/MapContentSettings/runtimeType.html">/sdk-for-flutter-explore-mapview-mapcontentsettings-runtimetype</a>
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
<a href="../mapview/MapContentSettings/noSuchMethod.html">/sdk-for-flutter-explore-mapview-mapcontentsettings-nosuchmethod</a>(<wbr/>Invocation invocation)
    → dynamic

</dt>
<dd class="inherited">
  Invoked when a nonexistent method or property is accessed.
  <div class="features">inherited</div>
</dd>
<dt class="callable inherited" id="toString">
<a href="../mapview/MapContentSettings/toString.html">/sdk-for-flutter-explore-mapview-mapcontentsettings-tostring</a>(<wbr/>)
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
<a href="../mapview/MapContentSettings/operator_equals.html">/sdk-for-flutter-explore-mapview-mapcontentsettings-operator-equals</a>(<wbr/>Object other)
    → bool

</dt>
<dd class="inherited">
  The equality operator.
  <div class="features">inherited</div>
</dd>
</dl>
</section>
<section class="summary offset-anchor" id="static-methods">
<h2>Static Methods</h2>
<dl class="callables">
<dt class="callable" id="filterTrafficIncidents">
<a href="../mapview/MapContentSettings/filterTrafficIncidents.html">/sdk-for-flutter-explore-mapview-mapcontentsettings-filtertrafficincidents</a>(<wbr/>List&lt;<wbr/><a href="../traffic/TrafficIncidentType.html">/sdk-for-flutter-explore-traffic-trafficincidenttype</a>&gt; trafficIncidents)
    → void

</dt>
<dd>
  Filters the displayed traffic incidents so that only the ones applicable to the specified
criteria are shown when general display of traffic incidents is enabled.
  

</dd>
<dt class="callable" id="resetTrafficIncidentFilter">
<a href="../mapview/MapContentSettings/resetTrafficIncidentFilter.html">/sdk-for-flutter-explore-mapview-mapcontentsettings-resettrafficincidentfilter</a>(<wbr/>)
    → void

</dt>
<dd>
  Removes all filters regarding Traffic Incidents so that all incidents will be displayed,
when the display of Traffic Incidents is enabled using <a href="../mapview/MapScene/enableFeatures.html">/sdk-for-flutter-explore-mapview-mapscene-enablefeatures</a> with
<a href="../mapview/MapFeatures/trafficIncidents.html">/sdk-for-flutter-explore-mapview-mapfeatures-trafficincidents</a>.
  

</dd>
<dt class="callable" id="resetTrafficRefreshPeriod">
<a href="../mapview/MapContentSettings/resetTrafficRefreshPeriod.html">/sdk-for-flutter-explore-mapview-mapcontentsettings-resettrafficrefreshperiod</a>(<wbr/>)
    → void

</dt>
<dd>
  Resets the traffic data (both flow and incidents) refresh period so the default traffic information
validity time and the refresh period derived from the refresh period of the traffic server is used.
  

</dd>
<dt class="callable" id="setTrafficRefreshPeriod">
<a href="../mapview/MapContentSettings/setTrafficRefreshPeriod.html">/sdk-for-flutter-explore-mapview-mapcontentsettings-settrafficrefreshperiod</a>(<wbr/>Duration value)
    → void

</dt>
<dd>
  Sets the traffic data refresh period for both <a href="../mapview/MapFeatures/trafficFlow.html">/sdk-for-flutter-explore-mapview-mapfeatures-trafficflow</a> and
<a href="../mapview/MapFeatures/trafficIncidents.html">/sdk-for-flutter-explore-mapview-mapfeatures-trafficincidents</a>.
  

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
<li><a href="../mapview/mapview-library.html">/sdk-for-flutter-explore-mapview-mapview-library</a></li>
<li class="self-crumb">MapContentSettings class</li>
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
</div></div>
</div>
</HTMLBlock>
