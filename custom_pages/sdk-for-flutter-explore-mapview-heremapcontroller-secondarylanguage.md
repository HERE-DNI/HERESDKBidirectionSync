---
title: "Implementation"
slug: "sdk-for-flutter-explore-mapview-heremapcontroller-secondarylanguage"
---

<HTMLBlock>
<div class="sdk-for-flutter">
<!-- secondaryLanguage.html -->
<div class="doc-with-sidebar"><div class="doc-content">
<div id="overlay-under-drawer"></div>
<header id="title">
menu
<ol class="breadcrumbs gt-separated dark hidden-xs">
<li><a href="../../index.html">/sdk-for-flutter-explore</a></li>
<li><a href="../../mapview/mapview-library.html">/sdk-for-flutter-explore-mapview-mapview-library</a></li>
<li><a href="../../mapview/HereMapController-class.html">/sdk-for-flutter-explore-mapview-heremapcontroller-class</a></li>
<li class="self-crumb">secondaryLanguage property</li>
</ol>
<div class="self-name">secondaryLanguage</div>
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
<h1>secondaryLanguage property</h1></div>
<section id="getter">
<section class="multi-line-signature">
<a href="../../core/LanguageCode.html">/sdk-for-flutter-explore-core-languagecode</a>?
secondaryLanguage
</section>
<section class="desc markdown">
<p>The code of desired secondary map display language.
Note: This feature is in beta state and thus there can be bugs and unexpected behavior.</p>
</section>
<section class="summary source-code" id="source">
<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">static LanguageCode? get secondaryLanguage =&gt; $prototype.secondaryLanguage;</code></pre>
</section>
</section>
<section id="setter">
<section class="multi-line-signature">
void
secondaryLanguage=(<wbr/><a href="../../core/LanguageCode.html">/sdk-for-flutter-explore-core-languagecode</a>? languageCode)
</section>
<section class="desc markdown">
<p>Sets the desired secondary map display language for all instances of
MapView to <code>languageCode</code>. Applying a language change causes map to be
redrawn. If the specified language is not supported, local language of the
region will be used. If null, no secondary map language will be used which
is the default behaviour.
Note: This feature is in beta state and thus there can be bugs and unexpected behavior.</p>
</section>
<section class="summary source-code" id="source">
<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">static void set secondaryLanguage(LanguageCode? languageCode) {
  $prototype.secondaryLanguage = languageCode;
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
<li class="self-crumb">secondaryLanguage property</li>
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
