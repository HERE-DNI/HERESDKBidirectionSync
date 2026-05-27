---
title: "Constructors"
slug: "sdk-for-flutter-explore-traffic-trafficincidentsqueryoptions-class"
---

<HTMLBlock>
<div class="sdk-for-flutter">
<!-- TrafficIncidentsQueryOptions-class.html -->
<div class="doc-with-sidebar"><div class="sidebar-nav"><ol>
<li class="section-title"><a href="traffic/TrafficIncidentsQueryOptions-class.html#constructors">Constructors</a></li>
<li><a href="traffic/TrafficIncidentsQueryOptions/TrafficIncidentsQueryOptions.html">TrafficIncidentsQueryOptions</a></li>
<li class="section-title">
<a href="traffic/TrafficIncidentsQueryOptions-class.html#instance-properties">Properties</a>
</li>
<li><a href="traffic/TrafficIncidentsQueryOptions/earliestStartTime.html">earliestStartTime</a></li>
<li><a href="traffic/TrafficIncidentsQueryOptions/hashCode.html">hashCode</a></li>
<li><a href="traffic/TrafficIncidentsQueryOptions/impactFilter.html">impactFilter</a></li>
<li><a href="traffic/TrafficIncidentsQueryOptions/languageCode.html">languageCode</a></li>
<li><a href="traffic/TrafficIncidentsQueryOptions/latestEndTime.html">latestEndTime</a></li>
<li class="inherited"><a href="traffic/TrafficIncidentsQueryOptions/runtimeType.html">runtimeType</a></li>
<li><a href="traffic/TrafficIncidentsQueryOptions/typeFilter.html">typeFilter</a></li>
<li class="section-title inherited"><a href="traffic/TrafficIncidentsQueryOptions-class.html#instance-methods">Methods</a></li>
<li class="inherited"><a href="traffic/TrafficIncidentsQueryOptions/noSuchMethod.html">noSuchMethod</a></li>
<li class="inherited"><a href="traffic/TrafficIncidentsQueryOptions/toString.html">toString</a></li>
<li class="section-title"><a href="traffic/TrafficIncidentsQueryOptions-class.html#operators">Operators</a></li>
<li><a href="traffic/TrafficIncidentsQueryOptions/operator_equals.html">operator ==</a></li>
</ol></div><div class="doc-content">
<div id="overlay-under-drawer"></div>
<header id="title">
menu
<ol class="breadcrumbs gt-separated dark hidden-xs">
<li><a href="../index.html">/sdk-for-flutter-explore</a></li>
<li><a href="../traffic/traffic-library.html">/sdk-for-flutter-explore-traffic-traffic-library</a></li>
<li class="self-crumb">TrafficIncidentsQueryOptions class</li>
</ol>
<div class="self-name">TrafficIncidentsQueryOptions</div>
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
<div class="main-content" data-above-sidebar="traffic/traffic-library-sidebar.html" data-below-sidebar="traffic/TrafficIncidentsQueryOptions-class-sidebar.html" id="dartdoc-main-content">
<div>
<h1>TrafficIncidentsQueryOptions class</h1></div>
<section class="desc markdown">
<p>The options to specify how incidents should be queried.</p>
</section>
<section class="summary offset-anchor" id="constructors">
<h2>Constructors</h2>
<dl class="constructor-summary-list">
<dt class="callable" id="TrafficIncidentsQueryOptions">
<a href="../traffic/TrafficIncidentsQueryOptions/TrafficIncidentsQueryOptions.html">/sdk-for-flutter-explore-traffic-trafficincidentsqueryoptions-trafficincidentsqueryoptions</a>()
</dt>
<dd>
          Creates a new instance with default values.
        </dd>
</dl>
</section>
<section class="summary offset-anchor" id="instance-properties">
<h2>Properties</h2>
<dl class="properties">
<dt class="property" id="earliestStartTime">
<a href="../traffic/TrafficIncidentsQueryOptions/earliestStartTime.html">/sdk-for-flutter-explore-traffic-trafficincidentsqueryoptions-earlieststarttime</a>
↔ DateTime?
</dt>
<dd>
  The earliest start time of incidents to be queried.
If the value is null filtering by the earliest start time is not applied.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property" id="hashCode">
<a href="../traffic/TrafficIncidentsQueryOptions/hashCode.html">/sdk-for-flutter-explore-traffic-trafficincidentsqueryoptions-hashcode</a>
→ int
</dt>
<dd>
  The hash code for this object.
  <div class="features">no setter</div>
</dd>
<dt class="property" id="impactFilter">
<a href="../traffic/TrafficIncidentsQueryOptions/impactFilter.html">/sdk-for-flutter-explore-traffic-trafficincidentsqueryoptions-impactfilter</a>
↔ List&lt;<wbr/><a href="../traffic/TrafficIncidentImpact.html">/sdk-for-flutter-explore-traffic-trafficincidentimpact</a>&gt;
</dt>
<dd>
  The list of incident impacts to be queried. If the list is empty, all incident impacts will be queried.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property" id="languageCode">
<a href="../traffic/TrafficIncidentsQueryOptions/languageCode.html">/sdk-for-flutter-explore-traffic-trafficincidentsqueryoptions-languagecode</a>
↔ <a href="../core/LanguageCode.html">/sdk-for-flutter-explore-core-languagecode</a>?
</dt>
<dd>
  The language code of the query.
It's the expected language of fields <a href="../traffic/TrafficIncidentBase/description.html">/sdk-for-flutter-explore-traffic-trafficincidentbase-description</a> and <a href="../traffic/TrafficIncident/summary.html">/sdk-for-flutter-explore-traffic-trafficincident-summary</a> in the relevant response.
However, the language code doesn't impact on <a href="../traffic/TrafficLocation/description.html">/sdk-for-flutter-explore-traffic-trafficlocation-description</a>.
If the language code is null or not supported then response fields are expected in the original language of the country that the incident belongs to.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property" id="latestEndTime">
<a href="../traffic/TrafficIncidentsQueryOptions/latestEndTime.html">/sdk-for-flutter-explore-traffic-trafficincidentsqueryoptions-latestendtime</a>
↔ DateTime?
</dt>
<dd>
  The latest end time of incidents to be queried.
If the value is null filtering by the latest end time is not applied.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property inherited" id="runtimeType">
<a href="../traffic/TrafficIncidentsQueryOptions/runtimeType.html">/sdk-for-flutter-explore-traffic-trafficincidentsqueryoptions-runtimetype</a>
→ Type
</dt>
<dd class="inherited">
  A representation of the runtime type of the object.
  <div class="features">no setterinherited</div>
</dd>
<dt class="property" id="typeFilter">
<a href="../traffic/TrafficIncidentsQueryOptions/typeFilter.html">/sdk-for-flutter-explore-traffic-trafficincidentsqueryoptions-typefilter</a>
↔ List&lt;<wbr/><a href="../traffic/TrafficIncidentType.html">/sdk-for-flutter-explore-traffic-trafficincidenttype</a>&gt;
</dt>
<dd>
  The list of incident types to be queried. If the list is empty, all types will be queried.
  <div class="features">getter/setter pair</div>
</dd>
</dl>
</section>
<section class="summary offset-anchor inherited" id="instance-methods">
<h2>Methods</h2>
<dl class="callables">
<dt class="callable inherited" id="noSuchMethod">
<a href="../traffic/TrafficIncidentsQueryOptions/noSuchMethod.html">/sdk-for-flutter-explore-traffic-trafficincidentsqueryoptions-nosuchmethod</a>(<wbr/>Invocation invocation)
    → dynamic

</dt>
<dd class="inherited">
  Invoked when a nonexistent method or property is accessed.
  <div class="features">inherited</div>
</dd>
<dt class="callable inherited" id="toString">
<a href="../traffic/TrafficIncidentsQueryOptions/toString.html">/sdk-for-flutter-explore-traffic-trafficincidentsqueryoptions-tostring</a>(<wbr/>)
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
<a href="../traffic/TrafficIncidentsQueryOptions/operator_equals.html">/sdk-for-flutter-explore-traffic-trafficincidentsqueryoptions-operator-equals</a>(<wbr/>Object other)
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
<li><a href="../traffic/traffic-library.html">/sdk-for-flutter-explore-traffic-traffic-library</a></li>
<li class="self-crumb">TrafficIncidentsQueryOptions class</li>
</ol>
<h5>traffic library</h5>
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
