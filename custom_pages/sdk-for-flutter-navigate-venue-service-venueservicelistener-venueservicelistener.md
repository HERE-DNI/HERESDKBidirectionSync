---
title: "VenueServiceListener constructor"
slug: "sdk-for-flutter-navigate-venue-service-venueservicelistener-venueservicelistener"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- VenueServiceListener.html -->
<div class="doc-with-sidebar"><div class="doc-content">
<div id="overlay-under-drawer"></div>
<header id="title">
menu
<ol class="breadcrumbs gt-separated dark hidden-xs">
<li>/sdk-for-flutter-navigate</li>
<li>/sdk-for-flutter-navigate-venue-service-venue-service-library</li>
<li>/sdk-for-flutter-navigate-venue-service-venueservicelistener-class</li>
<li class="self-crumb">VenueServiceListener factory constructor</li>
</ol>
<div class="self-name">VenueServiceListener</div>
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
<div class="main-content" data-above-sidebar="venue.service/VenueServiceListener-class-sidebar.html" data-below-sidebar="" id="dartdoc-main-content">
<div>
<h1>VenueServiceListener constructor</h1></div>
<section class="multi-line-signature">
VenueServiceListener(<wbr/><ol class="parameter-list single-line"> <li>void onInitializationCompletedLambda(<ol class="parameter-list single-line"> <li>/sdk-for-flutter-navigate-venue-service-venueserviceinitstatus</li>
</ol>), </li>
<li>void onVenueServiceStoppedLambda()</li>
</ol>)
    </section>
<section class="desc markdown">
<p>The abstract class for listeners for
lifecycle events in /sdk-for-flutter-navigate-venue-service-venueservice-class.</p>
</section>
<section class="summary source-code" id="source">
<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">factory VenueServiceListener(
  void Function(VenueServiceInitStatus) onInitializationCompletedLambda,
  void Function() onVenueServiceStoppedLambda,

) =&gt; VenueServiceListener$Lambdas(
  onInitializationCompletedLambda,
  onVenueServiceStoppedLambda,

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
<li>/sdk-for-flutter-navigate-venue-service-venue-service-library</li>
<li>/sdk-for-flutter-navigate-venue-service-venueservicelistener-class</li>
<li class="self-crumb">VenueServiceListener factory constructor</li>
</ol>
<h5>VenueServiceListener class</h5>
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
