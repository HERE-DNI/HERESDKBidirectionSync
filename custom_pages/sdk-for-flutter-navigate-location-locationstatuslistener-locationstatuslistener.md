---
title: "LocationStatusListener constructor"
slug: "sdk-for-flutter-navigate-location-locationstatuslistener-locationstatuslistener"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- LocationStatusListener.html -->
<div class="doc-with-sidebar"><div class="doc-content">
<div id="overlay-under-drawer"></div>
<header id="title">
menu
<ol class="breadcrumbs gt-separated dark hidden-xs">
<li>/sdk-for-flutter-navigate</li>
<li>/sdk-for-flutter-navigate-location-location-library</li>
<li>/sdk-for-flutter-navigate-location-locationstatuslistener-class</li>
<li class="self-crumb">LocationStatusListener factory constructor</li>
</ol>
<div class="self-name">LocationStatusListener</div>
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
<div class="main-content" data-above-sidebar="location/LocationStatusListener-class-sidebar.html" data-below-sidebar="" id="dartdoc-main-content">
<div>
<h1>LocationStatusListener constructor</h1></div>
<section class="multi-line-signature">
LocationStatusListener(<wbr/><ol class="parameter-list single-line"> <li>void onStatusChangedLambda(<ol class="parameter-list single-line"> <li>/sdk-for-flutter-navigate-location-locationenginestatus</li>
</ol>), </li>
<li>void onFeaturesNotAvailableLambda(<ol class="parameter-list single-line"> <li>List&lt;<wbr/>/sdk-for-flutter-navigate-location-locationfeature&gt;</li>
</ol>)</li>
</ol>)
    </section>
<section class="desc markdown">
<p>Abstract class for listening the
LocationEngine status updates.</p>
</section>
<section class="summary source-code" id="source">
<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">factory LocationStatusListener(
  void Function(LocationEngineStatus) onStatusChangedLambda,
  void Function(List&lt;LocationFeature&gt;) onFeaturesNotAvailableLambda,

) =&gt; LocationStatusListener$Lambdas(
  onStatusChangedLambda,
  onFeaturesNotAvailableLambda,

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
<li>/sdk-for-flutter-navigate-location-location-library</li>
<li>/sdk-for-flutter-navigate-location-locationstatuslistener-class</li>
<li class="self-crumb">LocationStatusListener factory constructor</li>
</ol>
<h5>LocationStatusListener class</h5>
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
