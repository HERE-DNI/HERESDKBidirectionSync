---
title: "Untitled"
slug: "sdk-for-flutter-explore-traffic-trafficflowbase-trafficflowbase"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- TrafficFlowBase.html -->

<div id="overlay-under-drawer"></div>
<header id="title">
menu
<ol class="breadcrumbs gt-separated dark hidden-xs">
<li>/sdk-for-flutter-explore</li>
<li>/sdk-for-flutter-explore-traffic-traffic-library</li>
<li>/sdk-for-flutter-explore-traffic-trafficflowbase-class</li>
<li class="self-crumb">TrafficFlowBase factory constructor</li>
</ol>
<div class="self-name">TrafficFlowBase</div>
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
<div class="main-content" data-above-sidebar="traffic/TrafficFlowBase-class-sidebar.html" data-below-sidebar="" id="dartdoc-main-content">
<div>
<h1>TrafficFlowBase constructor</h1></div>
<section class="multi-line-signature">
TrafficFlowBase(<wbr/><ol class="parameter-list single-line"> <li>double freeFlowSpeedInMetersPerSecondGetLambda(), </li>
<li>double jamFactorGetLambda()</li>
</ol>)
    </section>
<section class="desc markdown">
<p>This interface provides details about a traffic flow.<br/>
For additional information about fields, refer to <a href="https://www.here.com/docs/bundle/traffic-api-v7-api-reference/page/index.html#tag/Real-Time-Traffic">Traffic API v7 API Reference: Traffic API v7</a>.</p>
<p>Note: This is a beta release of this feature, so there could be a few bugs and unexpected behaviors.
Related APIs may change for new releases without a deprecation process.</p>
</section>
<section class="summary source-code" id="source">
<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">factory TrafficFlowBase(
  double Function() freeFlowSpeedInMetersPerSecondGetLambda,
  double Function() jamFactorGetLambda
) =&gt; TrafficFlowBase$Lambdas(
  freeFlowSpeedInMetersPerSecondGetLambda,
  jamFactorGetLambda
);</code></pre>
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
<li>/sdk-for-flutter-explore-traffic-traffic-library</li>
<li>/sdk-for-flutter-explore-traffic-trafficflowbase-class</li>
<li class="self-crumb">TrafficFlowBase factory constructor</li>
</ol>
<h5>TrafficFlowBase class</h5>
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
