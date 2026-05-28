---
title: "setTrafficRefreshPeriod static method"
slug: "sdk-for-flutter-navigate-mapview-mapcontentsettings-settrafficrefreshperiod"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- setTrafficRefreshPeriod.html -->
<div class="doc-with-sidebar"><div class="doc-content">
<div id="overlay-under-drawer"></div>
<header id="title">
menu
<ol class="breadcrumbs gt-separated dark hidden-xs">
<li>/sdk-for-flutter-navigate</li>
<li>/sdk-for-flutter-navigate-mapview-mapview-library</li>
<li>/sdk-for-flutter-navigate-mapview-mapcontentsettings-class</li>
<li class="self-crumb">setTrafficRefreshPeriod static method</li>
</ol>
<div class="self-name">setTrafficRefreshPeriod</div>
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
<h1>setTrafficRefreshPeriod static method</h1></div>
<section class="multi-line-signature">
void
setTrafficRefreshPeriod(<wbr/><ol class="parameter-list single-line"> <li>Duration value</li>
</ol>)

      

    </section>
<section class="desc markdown">
<p>Sets the traffic data refresh period for both /sdk-for-flutter-navigate-mapview-mapfeatures-trafficflow and
/sdk-for-flutter-navigate-mapview-mapfeatures-trafficincidents.</p>
<p>By default, the traffic information
validity time and the refresh period is derived from the refresh period of HERE's traffic server.
The period set by this function will override the server's default setting for
upcoming traffic data requests.
Defaults to 60 seconds.</p>
<ul>
<li><code>value</code> Traffic data refresh period in seconds. Valid range is [60, 300] seconds.
The shortest refresh period that can be set is 60 seconds. This means that the traffic
data shown on a map view will be refreshed every minute.
The longest refresh period that can be set is 300 seconds. This means that the traffic
data shown on the current map view will be refreshed every 5 minutes
if the viewport does not change.
Note that when a viewport change occurs, new traffic data may be requested
regardless of the set refresh period. For example, during turn-by-turn navigation,
frequent viewport changes can result in missing traffic data, causing new requests
to be made more often.</li>
</ul>
<p>Throws /sdk-for-flutter-navigate-mapview-mapcontentsettingstrafficrefreshperiodexceptionexception-class. /sdk-for-flutter-navigate-mapview-mapcontentsettingstrafficrefreshperiodexceptionexception-class indicates what went wrong.</p>
</section>
<section class="summary source-code" id="source">
<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">static void setTrafficRefreshPeriod(Duration value) =&gt; $prototype.setTrafficRefreshPeriod(value);</code></pre>
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
<li>/sdk-for-flutter-navigate-mapview-mapcontentsettings-class</li>
<li class="self-crumb">setTrafficRefreshPeriod static method</li>
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
`
}</HTMLBlock>
