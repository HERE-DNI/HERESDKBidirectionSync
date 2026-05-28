---
title: "match abstract method"
slug: "sdk-for-flutter-navigate-mapmatcher-mapmatcher-match"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- match.html -->
<div class="doc-with-sidebar"><div class="doc-content">
<div id="overlay-under-drawer"></div>
<header id="title">
menu
<ol class="breadcrumbs gt-separated dark hidden-xs">
<li>/sdk-for-flutter-navigate</li>
<li>/sdk-for-flutter-navigate-mapmatcher-mapmatcher-library</li>
<li>/sdk-for-flutter-navigate-mapmatcher-mapmatcher-class</li>
<li class="self-crumb">match abstract method</li>
</ol>
<div class="self-name">match</div>
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
<div class="main-content" data-above-sidebar="mapmatcher/MapMatcher-class-sidebar.html" data-below-sidebar="" id="dartdoc-main-content">
<div>
<h1>match abstract method</h1></div>
<section class="multi-line-signature">
/sdk-for-flutter-navigate-navigation-mapmatchedlocation-class?
match(<wbr/><ol class="parameter-list single-line"> <li>/sdk-for-flutter-navigate-core-location-class location</li>
</ol>)

      

    </section>
<section class="desc markdown">
<p>This method computes the map-matched location for the provided input location.</p>
<p>Currently, matching is performed within a 50-meter radius of the provided location. If no road network is found
within that radius, <code>null</code> is returned.</p>
<p>It's required to set <code>time</code> field for each <code>Location</code> object for the <code>MapMatcher</code> to work properly. In case no time is provided,
<code>null</code> is returned and an error message is logged. It is used to calculate the distance in time between
consecutive matches. Together with <code>speed</code>, this allows to calculate how likely a match is consistent with a previous match.
To improve matching accuracy, it is recommended to provide <code>bearing</code> and <code>speed</code> parameters for each <code>Location</code> object.</p>
<ul>
<li><code>location</code> The input location.</li>
</ul>
<p>Returns /sdk-for-flutter-navigate-navigation-mapmatchedlocation-class. map-matched location or <code>null</code> if the location could not be matched to a road network.</p>
</section>
<section class="summary source-code" id="source">
<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">MapMatchedLocation? match(Location location);</code></pre>
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
<li>/sdk-for-flutter-navigate-mapmatcher-mapmatcher-library</li>
<li>/sdk-for-flutter-navigate-mapmatcher-mapmatcher-class</li>
<li class="self-crumb">match abstract method</li>
</ol>
<h5>MapMatcher class</h5>
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
