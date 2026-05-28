---
title: "VenueLifecycleListener constructor"
slug: "sdk-for-flutter-navigate-venue-control-venuelifecyclelistener-venuelifecyclelistener"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- VenueLifecycleListener.html -->
<div class="doc-with-sidebar"><div class="doc-content">
<div id="overlay-under-drawer"></div>
<header id="title">
menu
<ol class="breadcrumbs gt-separated dark hidden-xs">
<li>/sdk-for-flutter-navigate</li>
<li>/sdk-for-flutter-navigate-venue-control-venue-control-library</li>
<li>/sdk-for-flutter-navigate-venue-control-venuelifecyclelistener-class</li>
<li class="self-crumb">VenueLifecycleListener factory constructor</li>
</ol>
<div class="self-name">VenueLifecycleListener</div>
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
<div class="main-content" data-above-sidebar="venue.control/VenueLifecycleListener-class-sidebar.html" data-below-sidebar="" id="dartdoc-main-content">
<div>
<h1>VenueLifecycleListener constructor</h1></div>
<section class="multi-line-signature">
VenueLifecycleListener(<wbr/><ol class="parameter-list single-line"> <li>void onVenueAddedLambda(<ol class="parameter-list single-line"> <li>/sdk-for-flutter-navigate-venue-control-venue-class</li>
</ol>), </li>
<li>void onVenueRemovedLambda(<ol class="parameter-list single-line"> <li>int</li>
</ol>)</li>
</ol>)
    </section>
<section class="desc markdown">
<p>The abstract class for  for
the /sdk-for-flutter-navigate-venue-control-venue-class lifecycle events.</p>
<p>Use the /sdk-for-flutter-navigate-venue-control-venuemap-class
to add and remove the /sdk-for-flutter-navigate-venue-control-venuelifecyclelistener-class.</p>
</section>
<section class="summary source-code" id="source">
<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">factory VenueLifecycleListener(
  void Function(Venue) onVenueAddedLambda,
  void Function(int) onVenueRemovedLambda,

) =&gt; VenueLifecycleListener$Lambdas(
  onVenueAddedLambda,
  onVenueRemovedLambda,

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
<li>/sdk-for-flutter-navigate-venue-control-venue-control-library</li>
<li>/sdk-for-flutter-navigate-venue-control-venuelifecyclelistener-class</li>
<li class="self-crumb">VenueLifecycleListener factory constructor</li>
</ol>
<h5>VenueLifecycleListener class</h5>
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
