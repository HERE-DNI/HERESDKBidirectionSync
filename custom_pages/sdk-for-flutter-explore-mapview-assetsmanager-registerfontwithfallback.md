---
title: "Implementation"
slug: "sdk-for-flutter-explore-mapview-assetsmanager-registerfontwithfallback"
---

<HTMLBlock>
<div class="sdk-for-flutter">
<!-- registerFontWithFallback.html -->
<div class="doc-with-sidebar"><div class="doc-content">
<div id="overlay-under-drawer"></div>
<header id="title">
menu
<ol class="breadcrumbs gt-separated dark hidden-xs">
<li><a href="../../index.html">/sdk-for-flutter-explore</a></li>
<li><a href="../../mapview/mapview-library.html">/sdk-for-flutter-explore-mapview-mapview-library</a></li>
<li><a href="../../mapview/AssetsManager-class.html">/sdk-for-flutter-explore-mapview-assetsmanager-class</a></li>
<li class="self-crumb">registerFontWithFallback abstract method</li>
</ol>
<div class="self-name">registerFontWithFallback</div>
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
<div class="main-content" data-above-sidebar="mapview/AssetsManager-class-sidebar.html" data-below-sidebar="" id="dartdoc-main-content">
<div>
<h1>registerFontWithFallback abstract method</h1></div>
<section class="multi-line-signature">
void
registerFontWithFallback(<wbr/><ol class="parameter-list single-line"> <li>String fontName, </li>
<li>String fontPath, </li>
<li>List&lt;<wbr/>String&gt; fallbackFontFilePaths</li>
</ol>)

      

    </section>
<section class="desc markdown">
<p>Registers a font set under a font name.</p>
<p>After registration, the font name can be used in</p>
<ul>
<li>the SVG <code>text</code> tag as <code>font-family</code> attribute parameter when creating a <a href="../../mapview/MapImage-class.html">/sdk-for-flutter-explore-mapview-mapimage-class</a> with <code>ImageFormat.SVG</code>.</li>
<li><a href="../../mapview/MapMarkerTextStyle-class.html">/sdk-for-flutter-explore-mapview-mapmarkertextstyle-class</a></li>
</ul>
<p>Repeated registration with the same font name is ignored.</p>
<ul>
<li>
<p><code>fontName</code> A font name.</p>
</li>
<li>
<p><code>fontPath</code> A font file path. TTF, OTF and WOFF formats are supported.</p>
</li>
</ul>
<p>Can be an asset file path or an absolute file path.</p>
<ul>
<li><code>fallbackFontFilePaths</code> Additional font files are intended to be used if main font
does not contain required character symbol and shall be sorted starting from most useful.</li>
</ul>
</section>
<section class="summary source-code" id="source">
<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">void registerFontWithFallback(String fontName, String fontPath, List&lt;String&gt; fallbackFontFilePaths);</code></pre>
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
<li><a href="../../mapview/AssetsManager-class.html">/sdk-for-flutter-explore-mapview-assetsmanager-class</a></li>
<li class="self-crumb">registerFontWithFallback abstract method</li>
</ol>
<h5>AssetsManager class</h5>
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
