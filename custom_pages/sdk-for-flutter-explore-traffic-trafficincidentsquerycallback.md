---
title: "Implementation"
slug: "sdk-for-flutter-explore-traffic-trafficincidentsquerycallback"
---

<HTMLBlock>
<div class="sdk-for-flutter">
<!-- TrafficIncidentsQueryCallback.html -->
<div class="doc-with-sidebar"><div class="doc-content">
<div id="overlay-under-drawer"></div>
<header id="title">
menu
<ol class="breadcrumbs gt-separated dark hidden-xs">
<li><a href="../index.html">/sdk-for-flutter-explore</a></li>
<li><a href="../traffic/traffic-library.html">/sdk-for-flutter-explore-traffic-traffic-library</a></li>
<li class="self-crumb">TrafficIncidentsQueryCallback typedef</li>
</ol>
<div class="self-name">TrafficIncidentsQueryCallback</div>
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
<div class="main-content" data-above-sidebar="traffic/traffic-library-sidebar.html" data-below-sidebar="" id="dartdoc-main-content">
<div>
<h1>TrafficIncidentsQueryCallback typedef</h1></div>
<section class="multi-line-signature">
TrafficIncidentsQueryCallback =
     void Function(<a href="../traffic/TrafficQueryError.html">/sdk-for-flutter-explore-traffic-trafficqueryerror</a>? queryError, List&lt;<wbr/><a href="../traffic/TrafficIncident-class.html">/sdk-for-flutter-explore-traffic-trafficincident-class</a>&gt;? result)
</section>
<section class="desc markdown">
<p>Callback passed to <a href="../traffic/TrafficEngine/queryForIncidentsInCorridor.html">/sdk-for-flutter-explore-traffic-trafficengine-queryforincidentsincorridor</a>.</p>
<p>The method will be called on the main thread when a search call has been completed.
The first argument is the error in the case of the failure. It is <code>null</code> for an operation that succeeds.
The second argument is the list of incidents in the case of the success. It is <code>null</code> in case of an error.</p>
<ul>
<li>
<p><code>queryError</code> The error in the case of the failure. It is <code>null</code> for an operation that succeeds.</p>
</li>
<li>
<p><code>result</code> The list of incidents in the case of the success. It is <code>null</code> in case of an error.</p>
</li>
</ul>
</section>
<section class="summary source-code" id="source">
<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">typedef TrafficIncidentsQueryCallback = void Function(TrafficQueryError? queryError, List&lt;TrafficIncident&gt;? result);</code></pre>
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
<li class="self-crumb">TrafficIncidentsQueryCallback typedef</li>
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
