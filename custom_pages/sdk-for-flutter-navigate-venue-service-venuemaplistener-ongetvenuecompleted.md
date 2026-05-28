---
title: "onGetVenueCompleted abstract method"
slug: "sdk-for-flutter-navigate-venue-service-venuemaplistener-ongetvenuecompleted"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- onGetVenueCompleted.html -->
<div class="doc-with-sidebar"><div class="doc-content">
<div id="overlay-under-drawer"></div>
<header id="title">
menu
<ol class="breadcrumbs gt-separated dark hidden-xs">
<li>/sdk-for-flutter-navigate</li>
<li>/sdk-for-flutter-navigate-venue-service-venue-service-library</li>
<li>/sdk-for-flutter-navigate-venue-service-venuemaplistener-class</li>
<li class="self-crumb">onGetVenueCompleted abstract method</li>
</ol>
<div class="self-name">onGetVenueCompleted</div>
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
<div class="main-content" data-above-sidebar="venue.service/VenueMapListener-class-sidebar.html" data-below-sidebar="" id="dartdoc-main-content">
<div>
<h1>onGetVenueCompleted abstract method</h1></div>
<section class="multi-line-signature">
void
onGetVenueCompleted(<wbr/><ol class="parameter-list"> <li>String venueIdentifier, </li>
<li>/sdk-for-flutter-navigate-venue-data-venuemodel-class? venueModel, </li>
<li>bool online, </li>
<li>/sdk-for-flutter-navigate-venue-style-venuestyle-class? venueStyle, </li>
</ol>)

      

    </section>
<section class="desc markdown">
<p>Called when loading of a venue or its retrieval from the cache is completed.</p>
<ul>
<li>
<p><code>venueIdentifier</code> The id of the venue.</p>
</li>
<li>
<p><code>venueModel</code> The venue model.</p>
</li>
<li>
<p><code>online</code> <code>True</code> if a new venue was loaded from the server and <code>false</code> otherwise.</p>
</li>
<li>
<p><code>venueStyle</code> The style associated with the venue.</p>
</li>
</ul>
</section>
<section class="summary source-code" id="source">
<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">void onGetVenueCompleted(String venueIdentifier, VenueModel? venueModel, bool online, VenueStyle? venueStyle);</code></pre>
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
<li>/sdk-for-flutter-navigate-venue-service-venuemaplistener-class</li>
<li class="self-crumb">onGetVenueCompleted abstract method</li>
</ol>
<h5>VenueMapListener class</h5>
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
