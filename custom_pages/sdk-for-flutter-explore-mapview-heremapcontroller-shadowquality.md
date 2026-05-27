---
title: "Implementation"
slug: "sdk-for-flutter-explore-mapview-heremapcontroller-shadowquality"
---

<HTMLBlock>
<div class="sdk-for-flutter">
<!-- shadowQuality.html -->
<div class="doc-with-sidebar"><div class="doc-content">
<div id="overlay-under-drawer"></div>
<header id="title">
menu
<ol class="breadcrumbs gt-separated dark hidden-xs">
<li><a href="../../index.html">/sdk-for-flutter-explore</a></li>
<li><a href="../../mapview/mapview-library.html">/sdk-for-flutter-explore-mapview-mapview-library</a></li>
<li><a href="../../mapview/HereMapController-class.html">/sdk-for-flutter-explore-mapview-heremapcontroller-class</a></li>
<li class="self-crumb">shadowQuality property</li>
</ol>
<div class="self-name">shadowQuality</div>
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
<div class="main-content" data-above-sidebar="mapview/HereMapController-class-sidebar.html" data-below-sidebar="" id="dartdoc-main-content">
<div>
<h1>shadowQuality property</h1></div>
<section id="getter">
<section class="multi-line-signature">
<a href="../../mapview/ShadowQuality.html">/sdk-for-flutter-explore-mapview-shadowquality</a>
shadowQuality
</section>
<section class="desc markdown">
<p>The current shadow quality.
Default shadow quality is <a href="../../mapview/ShadowQuality.html">/sdk-for-flutter-explore-mapview-shadowquality</a>.
Note: This feature is in beta state and thus there can be bugs and unexpected behavior.</p>
</section>
<section class="summary source-code" id="source">
<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">static ShadowQuality get shadowQuality =&gt; $prototype.shadowQuality;</code></pre>
</section>
</section>
<section id="setter">
<section class="multi-line-signature">
void
shadowQuality=(<wbr/><a href="../../mapview/ShadowQuality.html">/sdk-for-flutter-explore-mapview-shadowquality</a> shadowQuality)
</section>
<section class="desc markdown">
<p>Sets the desired shadow quality for all instances of HereMap to <code>shadowQuality</code>.
The quality controls the size of the shadow maps and the cascade count.
Default shadow quality is <a href="../../mapview/ShadowQuality.html">/sdk-for-flutter-explore-mapview-shadowquality</a>.
HereMaps can request to render shadows by feature.
Enabling shadows has a performance impact and should be considered only for devices with
sufficient performance.
Note: This feature is in beta state and thus there can be bugs and unexpected behavior.</p>
</section>
<section class="summary source-code" id="source">
<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">static void set shadowQuality(ShadowQuality shadowQuality) {
  $prototype.shadowQuality = shadowQuality;
}</code></pre>
</section>
</section>
</div>
<div class="sidebar sidebar-offcanvas-left" id="dartdoc-sidebar-left">
<header class="hidden-l" id="header-search-sidebar">
<form class="search-sidebar" role="search">
<input autocomplete="off" class="form-control typeahead" disabled="" id="search-sidebar" placeholder="Loading search..." type="text"/>
</form>
</header>
<ol class="breadcrumbs gt-separated dark hidden-l" id="sidebar-nav">
<li><a href="../../index.html">/sdk-for-flutter-explore</a></li>
<li><a href="../../mapview/mapview-library.html">/sdk-for-flutter-explore-mapview-mapview-library</a></li>
<li><a href="../../mapview/HereMapController-class.html">/sdk-for-flutter-explore-mapview-heremapcontroller-class</a></li>
<li class="self-crumb">shadowQuality property</li>
</ol>
<h5>HereMapController class</h5>
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
