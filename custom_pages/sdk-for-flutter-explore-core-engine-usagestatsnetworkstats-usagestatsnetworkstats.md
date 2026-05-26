---
title: "UsageStatsNetworkStats constructor"
slug: "sdk-for-flutter-explore-core-engine-usagestatsnetworkstats-usagestatsnetworkstats"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- UsageStatsNetworkStats.html -->
<div class="doc-with-sidebar"><div class="doc-content">
<div id="overlay-under-drawer"></div>
<header id="title">
menu
<ol class="breadcrumbs gt-separated dark hidden-xs">
<li>/sdk-for-flutter-explore</li>
<li>/sdk-for-flutter-explore-core-engine-core-engine-library</li>
<li>/sdk-for-flutter-explore-core-engine-usagestatsnetworkstats-class</li>
<li class="self-crumb">UsageStatsNetworkStats constructor</li>
</ol>
<div class="self-name">UsageStatsNetworkStats</div>
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
<div class="main-content" data-above-sidebar="core.engine/UsageStatsNetworkStats-class-sidebar.html" data-below-sidebar="" id="dartdoc-main-content">
<div>
<h1>UsageStatsNetworkStats constructor</h1></div>
<section class="multi-line-signature">
UsageStatsNetworkStats(<wbr/><ol class="parameter-list"> <li>int sentBytes, </li>
<li>int receivedBytes, </li>
<li>String methodCall, </li>
<li>int requestCounter, </li>
</ol>)
    </section>
<section class="desc markdown">
<p>Creates a new instance.</p>
<ul>
<li><code>sentBytes</code> Number of bytes sent over the network.</li>
<li><code>receivedBytes</code> Number of bytes received from the network.</li>
<li><code>methodCall</code> Name or description of the method being called.</li>
<li><code>requestCounter</code> Amount of calls for particular family of methodCall.
methodCall in this case is considered as base request,
additional query params are ignored, all calculated as one request.
e.g. <a href="https://search.hereapi.com/someparams">https://search.hereapi.com/someparams</a> and <a href="https://search.hereapi.com/someparams2">https://search.hereapi.com/someparams2</a>
will be considered as 1 methodCall, and requestCounter is 2.</li>
</ul>
</section>
<section class="summary source-code" id="source">
<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">UsageStatsNetworkStats(this.sentBytes, this.receivedBytes, this.methodCall, this.requestCounter);</code></pre>
</section>
</div>
<div class="sidebar sidebar-offcanvas-left" id="dartdoc-sidebar-left">
<header class="hidden-l" id="header-search-sidebar">
<form class="search-sidebar" role="search">
<input autocomplete="off" class="form-control typeahead" disabled="" id="search-sidebar" placeholder="Loading search..." type="text"/>
</form>
</header>
<ol class="breadcrumbs gt-separated dark hidden-l" id="sidebar-nav">
<li>/sdk-for-flutter-explore</li>
<li>/sdk-for-flutter-explore-core-engine-core-engine-library</li>
<li>/sdk-for-flutter-explore-core-engine-usagestatsnetworkstats-class</li>
<li class="self-crumb">UsageStatsNetworkStats constructor</li>
</ol>
<h5>UsageStatsNetworkStats class</h5>
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
