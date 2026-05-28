---
title: "VenueListener constructor"
slug: "sdk-for-flutter-navigate-venue-service-venuelistener-venuelistener"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- VenueListener.html -->
<div class="doc-with-sidebar"><div class="doc-content">
<div id="overlay-under-drawer"></div>
<header id="title">
menu
<ol class="breadcrumbs gt-separated dark hidden-xs">
<li>/sdk-for-flutter-navigate</li>
<li>/sdk-for-flutter-navigate-venue-service-venue-service-library</li>
<li>/sdk-for-flutter-navigate-venue-service-venuelistener-class</li>
<li class="self-crumb">VenueListener factory constructor</li>
</ol>
<div class="self-name">VenueListener</div>
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
<div class="main-content" data-above-sidebar="venue.service/VenueListener-class-sidebar.html" data-below-sidebar="" id="dartdoc-main-content">
<div>
<h1>VenueListener constructor</h1></div>
<section class="multi-line-signature">
VenueListener(<wbr/><ol class="parameter-list single-line"> <li>void onGetVenueCompletedLambda(<ol class="parameter-list"> <li>int, </li>
<li>/sdk-for-flutter-navigate-venue-data-venuemodel-class?, </li>
<li>bool, </li>
<li>/sdk-for-flutter-navigate-venue-style-venuestyle-class?, </li>
</ol>)</li>
</ol>)
    </section>
<section class="desc markdown">
<p>The abstract class for listeners for
venue loading events in /sdk-for-flutter-navigate-venue-service-venueservice-class.</p>
</section>
<section class="summary source-code" id="source">
<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">factory VenueListener(
  void Function(int, VenueModel?, bool, VenueStyle?) onGetVenueCompletedLambda,

) =&gt; VenueListener$Lambdas(
  onGetVenueCompletedLambda,

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
<li>/sdk-for-flutter-navigate-venue-service-venuelistener-class</li>
<li class="self-crumb">VenueListener factory constructor</li>
</ol>
<h5>VenueListener class</h5>
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
