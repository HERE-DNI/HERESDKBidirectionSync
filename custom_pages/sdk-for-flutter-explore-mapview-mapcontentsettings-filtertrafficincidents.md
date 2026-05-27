---
title: "Implementation"
slug: "sdk-for-flutter-explore-mapview-mapcontentsettings-filtertrafficincidents"
---

<HTMLBlock>
<div class="sdk-for-flutter">
<!-- filterTrafficIncidents.html -->
<div class="doc-with-sidebar"><div class="doc-content">
<div id="overlay-under-drawer"></div>
<header id="title">
menu
<ol class="breadcrumbs gt-separated dark hidden-xs">
<li><a href="../../index.html">/sdk-for-flutter-explore</a></li>
<li><a href="../../mapview/mapview-library.html">/sdk-for-flutter-explore-mapview-mapview-library</a></li>
<li><a href="../../mapview/MapContentSettings-class.html">/sdk-for-flutter-explore-mapview-mapcontentsettings-class</a></li>
<li class="self-crumb">filterTrafficIncidents static method</li>
</ol>
<div class="self-name">filterTrafficIncidents</div>
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
<div class="main-content" data-above-sidebar="mapview/MapContentSettings-class-sidebar.html" data-below-sidebar="" id="dartdoc-main-content">
<div>
<h1>filterTrafficIncidents static method</h1></div>
<section class="multi-line-signature">
void
filterTrafficIncidents(<wbr/><ol class="parameter-list single-line"> <li>List&lt;<wbr/><a href="../../traffic/TrafficIncidentType.html">/sdk-for-flutter-explore-traffic-trafficincidenttype</a>&gt; trafficIncidents</li>
</ol>)

      

    </section>
<section class="desc markdown">
<p>Filters the displayed traffic incidents so that only the ones applicable to the specified
criteria are shown when general display of traffic incidents is enabled.</p>
<p>The display of traffic incidents can be enabled using <a href="../../mapview/MapScene/enableFeatures.html">/sdk-for-flutter-explore-mapview-mapscene-enablefeatures</a> with
<a href="../../mapview/MapFeatures/trafficIncidents.html">/sdk-for-flutter-explore-mapview-mapfeatures-trafficincidents</a>.</p>
<ul>
<li><code>trafficIncidents</code> The traffic incidents to filter for, so that only applicable incidents are displayed.
When the list is empty, then all traffic incidents will be displayed.
If the <code>MapContentSettings.filterTrafficIncidents.trafficIncidents</code> contains <a href="../../traffic/TrafficIncidentType.html">/sdk-for-flutter-explore-traffic-trafficincidenttype</a>, then the
traffic filter will be applied ignoring this element.</li>
</ul>
</section>
<section class="summary source-code" id="source">
<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">static void filterTrafficIncidents(List&lt;TrafficIncidentType&gt; trafficIncidents) =&gt; $prototype.filterTrafficIncidents(trafficIncidents);</code></pre>
</section>
</div>
<div class="sidebar sidebar-offcanvas-left" id="dartdoc-sidebar-left">
<header class="hidden-l" id="header-search-sidebar">
<form class="search-sidebar" role="search">
<input autocomplete="off" class="form-control typeahead" disabled="" id="search-sidebar" placeholder="Loading search..." type="text"/>
</form>
</header>
<ol class="breadcrumbs gt-separated dark hidden-l" id="sidebar-nav">
<li><a href="../../index.html">/sdk-for-flutter-explore</a></li>
<li><a href="../../mapview/mapview-library.html">/sdk-for-flutter-explore-mapview-mapview-library</a></li>
<li><a href="../../mapview/MapContentSettings-class.html">/sdk-for-flutter-explore-mapview-mapcontentsettings-class</a></li>
<li class="self-crumb">filterTrafficIncidents static method</li>
</ol>
<h5>MapContentSettings class</h5>
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
