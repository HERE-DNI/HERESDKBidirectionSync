---
title: "TrafficMergeWarningListener constructor"
slug: "sdk-for-flutter-navigate-navigation-trafficmergewarninglistener-trafficmergewarninglistener"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- TrafficMergeWarningListener.html -->
<div class="doc-with-sidebar"><div class="doc-content">
<div id="overlay-under-drawer"></div>
<header id="title">
menu
<ol class="breadcrumbs gt-separated dark hidden-xs">
<li>/sdk-for-flutter-navigate</li>
<li>/sdk-for-flutter-navigate-navigation-navigation-library</li>
<li>/sdk-for-flutter-navigate-navigation-trafficmergewarninglistener-class</li>
<li class="self-crumb">TrafficMergeWarningListener factory constructor</li>
</ol>
<div class="self-name">TrafficMergeWarningListener</div>
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
<div class="main-content" data-above-sidebar="navigation/TrafficMergeWarningListener-class-sidebar.html" data-below-sidebar="" id="dartdoc-main-content">
<div>
<h1>TrafficMergeWarningListener constructor</h1></div>
<section class="multi-line-signature">
TrafficMergeWarningListener(<wbr/><ol class="parameter-list single-line"> <li>void onTrafficMergeWarningUpdatedLambda(<ol class="parameter-list single-line"> <li>/sdk-for-flutter-navigate-navigation-trafficmergewarning-class</li>
</ol>)</li>
</ol>)
    </section>
<section class="desc markdown">
<p>This abstract class
should be implemented in order to receive traffic merge warnings.</p>
<p><strong>Note:</strong> The traffic merge warner is a point warner, which means that for a traffic merge there will <em>always</em> be
2 warnings emitted, with the <code>TrafficMergeWarning.distance_type</code> set to <code>DistanceType.AHEAD</code> and <code>DistanceType.PASSED</code>
which is given when the location of the traffic merge is reached.
A <code>TrafficMergeWarning</code> will not be given until the previous warning of that type has been passed.
For example, a route with <code>TrafficMergeWarning</code> 120 meters and <code>TrafficMergeWarning</code> 160 meters ahead,
the first <code>TrafficMergeWarning.distance_to_traffic_merge_in_meters</code> is 120 meters
and the next <code>TrafficMergeWarning.distance_to_traffic_merge_in_meters</code> is then 40 meters,
since that is the distance between the first and second warnings.</p>
</section>
<section class="summary source-code" id="source">
<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">factory TrafficMergeWarningListener(
  void Function(TrafficMergeWarning) onTrafficMergeWarningUpdatedLambda,

) =&gt; TrafficMergeWarningListener$Lambdas(
  onTrafficMergeWarningUpdatedLambda,

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
<li>/sdk-for-flutter-navigate</li>
<li>/sdk-for-flutter-navigate-navigation-navigation-library</li>
<li>/sdk-for-flutter-navigate-navigation-trafficmergewarninglistener-class</li>
<li class="self-crumb">TrafficMergeWarningListener factory constructor</li>
</ol>
<h5>TrafficMergeWarningListener class</h5>
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
